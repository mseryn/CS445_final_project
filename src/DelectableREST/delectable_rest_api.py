#!/usr/bin/python3

###
#   Written by Melanie Cornelius (nee Dooley)
#  
#   for final project in: 
#   CS 445: Object Oriented Design Programming
#   Section 02, Spring 2016
#   Illinois Institute of Technology
#  
#   student email: mdooley1@hawk.iit.edu
#   github username: mseryn
###

import Delectable
import DelectableReport

import flask
import json
import datetime
from pprint import pprint


class DelectableREST():
    def __init__(self):
        self._response_header = {"Content-Type": "application/json"}

        self.app = flask.Flask(__name__)
        self._menu = Delectable.menu.Menu()        
        
        # Menu calls:
        self.app.add_url_rule('/delectable/menu', 'get_menu_json_dict', 
                self.get_menu_json_dict, methods = ['GET'])
        self.app.add_url_rule('/delectable/menu/<int:menu_id>', 
                'get_menu_item_json_dict', self.get_menu_item_json_dict, 
                methods = ['GET'])
        # Order calls:
        self.app.add_url_rule('/delectable/order', 'get_orders_json_dict', 
                self.get_orders_json_dict, methods = ['GET'])
        self.app.add_url_rule('/delectable/order', 'put_order_json_dict', 
                self.put_order_json_dict, methods = ['PUT'])
        self.app.add_url_rule('/delectable/order/<int:order_id>', 
                'get_order_by_id_json_dict', self.get_order_by_id_json_dict, 
                methods = ['GET'])
        self.app.add_url_rule('/delectable/order/cancel/<int:order_id>', 
                'post_order_cancel_json_dict', self.post_order_cancel_json_dict, 
                methods = ['POST'])
        # Customer calls:
        self.app.add_url_rule('/delectable/customer', 'get_customers_json_dict', 
                self.get_customers_json_dict, methods = ['GET'])
        self.app.add_url_rule('/delectable/customer/<int:customer_id>', 
                'get_customer_by_id_json_dict', self.get_customer_by_id_json_dict, 
                methods = ['GET'])
        # Report calls:
        self.app.add_url_rule('/delectable/report', 'get_report_json_dict', 
                self.get_report_json_dict, methods = ['GET'])
        self.app.add_url_rule('/delectable/report/<int:report_id>', 
                'get_report_in_range_json_dict', self.get_report_in_range_json_dict, 
                methods = ['GET'])
        # admin calls:
        self.app.add_url_rule('/delectable/admin/menu', 'put_item_on_menu_json_dict',
                self.put_item_on_menu_json_dict, methods = ['PUT'])
        self.app.add_url_rule('/delectable/admin/menu/<int:menu_id>', 
                'post_item_price_json_dict', self.post_item_price_json_dict,
                methods = ['POST'])
        self.app.add_url_rule('/delectable/admin/surcharge', 'get_menu_surcharge_json_dict',
                self.get_menu_surcharge_json_dict, methods = ['GET'])
        self.app.add_url_rule('/delectable/admin/surcharge', 'post_menu_surcharge_json_dict',
                self.post_menu_surcharge_json_dict, methods = ['POST'])
        self.app.add_url_rule('/delectable/admin/delivery/<int:order_id>',
                'post_order_delivered_json_dict', self.post_order_delivered_json_dict,
                methods = ['POST'])
        
    def run(self):
        self.app.run(debug = True)

    # ***
    # *  REST commands for Menu
    # ***

    def get_menu_json_dict(self):
        all_menu_dicts = []
        items = self._menu.get_items()

        if items:
            for individual_item in items:
                all_menu_dicts.append(self._menu.get_menu_item_contents_in_dict(individual_item))
        if all_menu_dicts:
            return json.dumps(all_menu_dicts), 200, self._response_header
        else:
            # no menu items to return
            return "", 200
            #return "", 200, self._response_header

    def get_menu_item_json_dict(self, menu_id):
        individual_item = self._menu.get_item_by_id(menu_id)
        if individual_item:
            menu_item = self._menu.get_menu_item_contents_in_dict(individual_item)
            return json.dumps(menu_item) , 200, self._response_header
        else:
            return "", 404, self._response_handler

    # ***
    # *  REST commands for Order
    # ***

    def get_orders_json_dict(self):
        all_order_dicts = []
        order = Delectable.order.Order 
        if "date" in flask.request.args:
            request_date = self.string_to_date(flask.request.args["date"])
            orders = [iorder for iorder in order.get_all_orders() 
                      if iorder.get_delivery_date().date() == request_date.date() 
                       and iorder.get_delivery_status() == "open"]
        else:
            orders = order.get_all_orders()

        for individual_order in orders:
            order_item = individual_order.get_order_details_in_dict()
            order_item['ordered_by'] = individual_order.get_customer().get_email()
            del order_item['note']
            del order_item['delivery_address']
            del order_item['order_detail']
            all_order_dicts.append(order_item)
        return json.dumps(all_order_dicts) , 200, self._response_header

    def put_order_json_dict(self):
        # Ensuring all necessary fields are filled:
        if (not flask.request.json 
            or not 'delivery_date' in flask.request.json
            or not 'delivery_address' in flask.request.json 
            or not 'personal_info' in flask.request.json
            or not 'note' in flask.request.json
            or not 'order_detail' in flask.request.json
            or not 'name' in flask.request.json['personal_info']
            or not 'email' in flask.request.json['personal_info']
            or not 'phone' in flask.request.json['personal_info']):
            print("Error: not all components for order present.  Aborting.")

        else:
            # getting the date:
            parsed_date = self.string_to_date(flask.request.json['delivery_date'])

            # getting address
            address_string = flask.request.json['delivery_address']
            
            # getting personal information
            customer_dict = flask.request.json['personal_info']
            customer_name = customer_dict['name']
            customer_last_name = " ".join(customer_name.split()[1:])
            customer_first_name = customer_name.split()[0]
            customer_email = customer_dict['email']
            customer_phone = customer_dict['phone']
            parsed_customer = Delectable.customer.Customer(customer_last_name, 
                    customer_first_name, customer_email, customer_phone)
            
            # getting note
            note_string = flask.request.json['note']
            
            # getting order details
            item_input_list = []
            items_list = flask.request.json['order_detail']
            order_details = []
            for item_dict in items_list:
                item_input_list.append((item_dict["id"], item_dict["count"]))

            # making the order
            order = Delectable.order.Order(parsed_customer, self._menu, 
                    initialized_billing_address = address_string, 
                    initialized_delivery_address = address_string, 
                    delivery_date = parsed_date, items = item_input_list,  
                    instructions = note_string)

            # returning formatted dict with cancelation URL
            order_cancel_url = "/order/cancel/" + str(order.get_order_id())
            return json.dumps({'id'         : order.get_order_id(), 
                               'cancel_url' : order_cancel_url}) , 201,  \
                                    {"Content-Type": "application/json", \
                                    "Location": "/delectable/order/" + str(order.get_order_id())}

    def get_order_by_id_json_dict(self, order_id):
        order_item = {}
        order = Delectable.order.Order 
        orders = order.get_all_orders()
        order_found = False

        for individual_order in orders:
            if individual_order.get_order_id() == order_id:
                order_found = True
                order_item = individual_order.get_order_details_in_dict()
        if order_found:
            return json.dumps(order_item) , 200, self._response_header
        else:
            print("Error: order not found")
            return "", 404, self._response_header
    
    def post_order_cancel_json_dict(self, order_id):
        order = Delectable.order.Order 
        orders = order.get_all_orders()
        order_found = False
        for individual_order in orders:
            if individual_order.get_order_id() == order_id:
                order_found = True
                individual_order.set_delivery_status("cancelled")
        if order_found:
            return "", 204, {"Content-Type": "application/json", "Location": "/delectable/order/" + str(order_id)}
        else:
            print("Error: order not found")
            return "", 404, self._response_header


    # ***
    # *  REST commands for Customer
    # ***

    def get_customers_json_dict(self):
        customer = Delectable.customer.Customer
        customers = customer.get_all_customers()
        customer_dict_list = []

        if "key" in flask.request.args:
            customers = [icustomer for icustomer in customers
                         if self.customer_key_match(icustomer, flask.request.args["key"])]

        for individual_customer in customers:
            customer_dict_list.append(individual_customer.get_customer_details_dict())
        return json.dumps(customer_dict_list) , 200, self._response_header

    def get_customer_by_id_json_dict(self, customer_id):
        order = Delectable.order.Order
        orders = order.get_all_orders()
        customers = order.get_all_customers()

        customer_orders = []
        customer_found = False

        for individual_customer in customers:
            if individual_customer.get_customer_id() == customer_id:
                customer_found = True
                customer_item = individual_customer.get_customer_details_dict()
                for individual_order in orders:
                    if individual_order.get_customer_id() == customer_item["id"]:
                        order_item = individual_order.get_order_details_in_dict()
                        del order_item['ordered_by']
                        del order_item['note']
                        del order_item['delivery_address']
                        del order_item['order_detail']

                        customer_orders.append(order_item)
                customer_item['orders'] = customer_orders
        if customer_found:
            return json.dumps(customer_item) , 200, self._response_header
        else:
            print("Error: customer not found")
            return "", 404, self._response_header

    # ***
    # *  REST commands for Report
    # ***

    def get_report_json_dict(self):
        report = DelectableReport.report.Report()
        reports = report.get_all_reports()
        report_dict = {}
        reports_list = []
        for key in reports:
            report_dict['id'] = key
            report_dict['name'] = reports[key][0]
            reports_list.append(report_dict)
            report_dict = {}
        return json.dumps(reports_list) , 200, self._response_header

    def get_report_in_range_json_dict(self, report_id):
        # get report corresponding to report_id
        report = DelectableReport.report.Report()
        reports = report.get_all_reports()
        report_found = False
        for key in reports:
            if key == report_id:
                report_found = True
                desired_report_tuple = reports[key]
        if not report_found:
            print("Error: report not found")
            return "", 404, self._response_header
        start_date = self.string_to_date( \
                flask.request.args.get('start_date', datetime.datetime.min))
        end_date = self.string_to_date( \
                flask.request.args.get('end_date', datetime.datetime.max))
        individual_report = desired_report_tuple[1](start_date, end_date)
        return json.dumps(individual_report.get_report_contents())
            

    # ***
    # *  REST commands for an admin
    # ***

    def put_item_on_menu_json_dict(self):
        # Ensuring all necessary fields are filled:
        if (not flask.request.json 
            or not 'name' in flask.request.json
            or not 'price_per_person' in flask.request.json
            or not 'minimum_order' in flask.request.json
            or not 'categories' in flask.request.json):
            print("Error: not all components for item PUT are present.  Aborting.")
            return "", 400, self._response_header

        else:
            parsed_name = flask.request.json['name']
            parsed_price_per_person = float(flask.request.json['price_per_person'])
            parsed_minimum_serving = float(flask.request.json['minimum_order'])
            parsed_categories = []
            for category_dict in flask.request.json['categories']:
                parsed_categories.append(category_dict["name"])

            item = Delectable.item.Item(name = parsed_name, price = parsed_price_per_person,
                    min_serving = parsed_minimum_serving, category = parsed_categories)
            self._menu.add_item(item)

            return json.dumps({'id': item.get_item_id()}) , 201, {"Content-Type": "application/json",
                                    "Location": "/delectable/menu/" + str(item.get_item_id())}

    def post_item_price_json_dict(self, menu_id):
        if (not flask.request.json
            or not 'id' in flask.request.json
            or not 'price_per_person' in flask.request.json):
            print("Error: not all components for item price change are present.  Aborting.")
            return "", 400, self._response_header
        else:
            item_to_modify = self._menu.get_item_by_id(flask.request.json['id'])
            if item_to_modify:
                item_to_modify.set_price_per_person(flask.request.json['price_per_person'])
                return "", 204, self._response_header
            else:
                print("Error not found")
                return "", 404, self._response_header

    def get_menu_surcharge_json_dict(self):
        return json.dumps({'surcharge': self._menu.get_surcharge()}) , 200, self._response_header

    def post_menu_surcharge_json_dict(self):
        if not flask.request.json:
            print("Error: missing content")
            return "", 204, self._response_header
        elif not 'surcharge' in flask.request.json:
            print("Error: not all components for surcharge POST are present.  Aborting.")
            return "", 400, self._response_header
        else:
            self._menu.set_surcharge(float(flask.request.json['surcharge']))
            return "", 204, {"Content-Type": "application/json", "Location": "/delectable/surcharge/"}

    def post_order_delivered_json_dict(self, order_id):
        order = Delectable.order.Order
        orders = order.get_all_orders()
        
        if (not flask.request.json
            or not 'id' in flask.request.json):
            print("Error: missing arguments")
            return "", 204, self._response_header
        else:
            order_id = flask.request.json['id']
            if not type(order_id) is int:
                print("Error: order id must be an integer value")
                return "", 404, self._response_header
            else:
                for individual_order in orders:
                    if individual_order.get_order_id() == order_id:
                        individual_order.set_delivery_status("delivered")
                        return "", 204, {"Content-Type": "application/json", "Location": "/delectable/order/" + str(order_id)}
            return "", 404, self._response_header

    # ***
    # *  Helper Routines for JSON Class
    # ***

    def customer_key_match(self, customer, key_raw):
        key = str(key_raw)
        if key == customer.get_last_name():
            return True
        if key == customer.get_email():
            return True
        if key == customer.get_phone_number():
            return True
        return False

    def string_to_date(self, datestring):
        parsed_year = int(datestring[0:4])
        parsed_month = int(datestring[4:6])
        parsed_day = int(datestring[6:8])
        parsed_date = datetime.datetime(year = parsed_year, month = parsed_month, day = parsed_day)
        return parsed_date


if __name__ == "__main__":
    api = DelectableREST()
    api.run()
