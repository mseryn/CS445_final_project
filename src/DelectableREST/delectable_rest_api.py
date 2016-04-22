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

import flask
import datetime

class DelectableREST():
    def __init__(self):
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
        self.app.add_url_rule('/delectable/order?date=<string:datestring>', 
                'get_orders_by_day_json_dict', self.get_orders_by_day_json_dict, 
                methods = ['GET'])
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
        self.app.add_url_rule('/delectable/customer?key=<string:query>', 
                'get_customer_by_key_json_dict', self.get_customer_by_key_json_dict, 
                methods = ['GET'])
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
        menu_item = {}
        all_menu_dicts = []
        items = self._menu.get_items()

        for individual_item in items:
            menu_item['id'] = individual_item.get_item_id()
            menu_item['name'] = individual_item.get_name()
            menu_item['price_per_person'] = individual_item.get_price_per_person()
            menu_item['minimum_order'] = individual_item.get_min_serving()
            menu_item['categories'] = [{'name' : category} 
                    for category in individual_item.get_category()]
            all_menu_dicts.append(menu_item)
            menu_item = {}
        return flask.jsonify(all_menu_dicts) , 200

    def get_menu_item_json_dict(self, menu_id):
        menu_item = {}
        individual_item = self._menu.get_item_by_id(menu_id)
        if not individual_item:
            print("Error: menu item not found")
            return None, 404

        menu_item['id'] = individual_item.get_item_id()
        menu_item['name'] = individual_item.get_name()
        menu_item['price_per_person'] = individual_item.get_price_per_person()
        menu_item['minimum_order'] = individual_item.get_min_serving()
        menu_item['categories'] = [{'name' : category} for category in individual_item.get_category()]
        menu_item['create_date'] = individual_item.get_creation_date().strftime("%Y%m%d")
        menu_item['last_modified_date'] = individual_item.get_last_modified_date().strftime("Y%m%d")
        return flask.jsonify(menu_item) , 200

    # ***
    # *  REST commands for Order
    # ***

    def get_orders_json_dict(self):
        order_item = {}
        all_order_dicts = []
        order = Delectable.order.Order() 
        orders = order.get_all_orders()

        for individual_order in orders:
            order_item['id'] = individual_order.get_order_id()
            order_item['order_date'] = individual_order.get_order_date().strftime("%Y%m%d")
            order_item['delivery_date'] = individual_order.get_delivery_date().strftime("%Y%m%d")
            order_item['amount'] = individual_order.get_total_cost()
            order_item['surcharge'] = individual_order.get_surcharge_considering_day()
            order_item['status'] = individual_order.get_status()
            order_item['ordered_by'] = individual_order.get_customer().get_email()

            all_order_dicts.append(order_item)
            order_item = {}
        return flask.jsonify(all_order_dicts) , 200

    def get_orders_by_day_json_dict(self, datestring):
        orders_for_date = []
        order_item = {}
        order = Delectable.order.Order() 
        orders = order.get_all_orders()

        parsed_year = int(datestring[0:4])
        parsed_month = int(datestring[4:6])
        parsed_day = int(datestring[6:8])
        try:
            parsed_date = datetime.datetime(year = parsed_year, month = parsed_month, day = parsed_day)
        except:
            print("Error: year, month, date provided not acceptable.  Defaulting to today's date.")
            parsed_date = datetime.datetime.now()

        for individual_order in orders:
            if individual_order.get_delivery_date().date() == parsed_date.date():
                order_item['id'] = individual_order.get_order_id()
                order_item['order_date'] = individual_order.get_order_date().strftime("%Y%m%d")
                order_item['delivery_date'] = individual_order.get_delivery_date().strftime("%Y%m%d")
                order_item['amount'] = individual_order.get_total_cost()
                order_item['surcharge'] = individual_order.get_surcharge_considering_day()
                order_item['status'] = individual_order.get_status()
                order_item['ordered_by'] = individual_order.get_customer().get_email()
                orders_for_date.append(order_item)
        return flask.jsonify(orders_for_date) , 200

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
            # Also check for all components of orders? Not sure how.
            print("Error: not all components for order present.  Aborting.")
        else:
            # getting the date:
            parsed_date = string_to_date(flask.request.json['delivery_date'])

            # getting address
            address_string = flask.request.json['delivery_address']
            
            # getting personal information
            customer_dict = flas.request.json['personal_info']
            customer_name = customer_dict['name']
            customer_last_name = customer_name.split()[1:]
            customer_first_name = customer_name.split()[0]
            customer_email = customer_dict['email']
            customer_phone = customer_dict['phone']
            parsed_customer = customer.Customer(customer_last_name, 
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
            order = Delectable.order.Order(parsed_customer, address_string, 
                    address_string, delivery_date = parsed_date, 
                    items = item_input_list,  instructions = note_string)

            # returning formatted dict with cancelation URL
            order_cancel_url = "/order/cancel/" + str(order.get_order_id())
            return flask.jsonify({'id'         : order.get_order_id, 
                                  'cancel_url' : order_cancel_url}) , 201

    def get_order_by_id_json_dict(self, order_id):
        order_item = {}
        order = Delectable.order.Order() 
        orders = order.get_all_orders()
        order_found = False

        for individual_order in orders:
            if individual_order.get_order_id() == order_id:
                order_found = True
                order_item['id'] = individual_order.get_order_id()
                order_item['amount'] = individual_order.get_total_cost()
                order_item['surcharge'] = individual_order.get_surcharge_considering_day()
                order_item['status'] = individual_order.get_status()
                order_item['order_date'] = individual_order.get_order_date().strftime("%Y%m%d")
                order_item['delivery_date'] = individual_order.get_delivery_date().strftime("%Y%m%d")
                order_customer = individual_order.get_customer()
                order_item['ordered_by'] = {"name": (order_customer.get_first_name() 
                                                    + order_customer.get_last_name()),
                                            "email": order_customer.get_email(),
                                            "phone": order_customer.get_phone_number() }
                order_item['delivery_address'] = individual_order.get_delivery_address()
                order_item['note'] = individual_order.get_instructions()
                items = individual_order.get_items()
                order_item['order_detail'] = []
                for item in items:
                    order_item['order_detail'].append({"id": item.get_item_id(),
                                                       "name": item.get_name(),
                                                       "count": item.get_serving_size() })
        if order_found:
            return flask.jsonify(order_item) , 200
        else:
            print("Error: order not found")
            return None, 404
    
    def post_order_cancel_json_dict(self, order_id):
        order = Delectable.order.Order() 
        orders = order.get_all_orders()
        order_found = False
        for individual_order in orders:
            if individual_order.get_order_id() == order_id:
                order_found = True
                individual_order.set_delivery_status(order_id, "cancelled")
        if order_found:
            return
        else:
            print("Error: order not found")
            return None, 202


    # ***
    # *  REST commands for Customer
    # ***

    def get_customers_json_dict(self):
        customer = Delectable.customer.Customer()
        customers = customer.get_all_customers()
        customer_item ={}
        customer_dict_list = []

        for individual_customer in customers:
            customer_item['id'] = individual_customer.get_customer_id()
            customer_item['name'] = (individual_customer.get_first_name() + 
                                    individual_customer.get_last_name())
            customer_item['email'] = individual_customer.get_email()
            customer_item['phone'] = individual_customer.get_phone_number()
            customer_dict_list.append(customer_item)
            customer_item ={}
        return flask.jsonify(customer_dict_list) , 200

    def get_customer_by_key_json_dict(self, query):
        customer = Delectable.customer.Customer()
        customers = customer.get_all_customers()
        customer_item ={}
        customer_dict_list = []

        for individual_customer in customers:
            if customer_key_match(individual_customer, query):
                customer_item['id'] = individual_customer.get_customer_id()
                customer_item['name'] = (individual_customer.get_first_name() + 
                                        individual_customer.get_last_name())
                customer_item['email'] = individual_customer.get_email()
                customer_item['phone'] = individual_customer.get_phone_number()
                customer_dict_list.append(customer_item)
                customer_item ={}
        return flask.jsonify(customer_dict_list) , 200

    def get_customer_by_id_json_dict(self, customer_id):
        customer = Delectable.customer.Customer()
        order = Delectable.order.Order()
        customers = customer.get_all_customers()
        orders = order.get_all_orders()
        customer_item ={}
        order_item = {}
        customer_orders = []
        customer_found = False

        for individual_customer in customers:
            if individual_customer.get_customer_id() == customer_id:
                customer_found = True
                customer_item['id'] = individual_customer.get_customer_id()
                customer_item['name'] = (individual_customer.get_first_name() + 
                                        individual_customer.get_last_name())
                customer_item['email'] = individual_customer.get_email()
                customer_item['phone'] = individual_customer.get_phone_number()
                for individual_order in orders:
                    if individual_order.get_customer_id() == customer_item["id"]:
                        order_item["id"] = individual_order.get_order_id()
                        order_item["order_date"] = \
                            individual_order.get_order_date().strftime("%Y%m%d")
                        order_item["delivery_date"] = \
                            individual_order.get_delivery_date().strftime("%Y%m%d")
                        order_item["amount"] = individual_order.get_total_item_cost()
                        order_item["surcharge"] = individual_order.get_surcharge_considering_day()
                        order_item["status"] = individual_order.get_status()
                        customer_orders.append(order_item)
                        order_item = {}
                customer_item['orders'] = customer_orders
        if customer_found:
            return flask.jsonify(customer_item) , 200
        else:
            print("Error: customer not found")
            return None, 404

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
        return flask.jsonify(reports_list) , 200

    def get_report_in_range_json_dict(self, report_id):
        if not flask.request.json:
            # Not an expressly specified return - okay? QUESTION
            print("Error: report id required")
            return None, 400
        else:
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
                return None, 404
        start_date = flask.request.args.get('start_date', datetime.datetime.min)
        end_date = flask.request.args.get('end_date', datetime.datetime.max)
        individual_report = desired_report_tuple[1](start_date, end_date)
        return flask.jsonify(individual_report.get_report_contents())
            

    # ***
    # *  REST commands for an admin
    # ***

    def put_item_on_menu_json_dict():
        # Ensuring all necessary fields are filled:
        if (not flask.request.json 
        or not 'name' in flask.request.json
        or not 'price_per_person' in flask.request.json
        or not 'minimum_order' in flask.request.json
        or not 'categories' in flask.request.json):
            # Also check for all components of categories? Not sure how.
            print("Error: not all components for item PUT are present.  Aborting.")
            return None, 400
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

            return flask.jsonify({'id': item.get_item_id()}) , 201

    def post_item_price_json_dict(self):
        if (not flask.request.json
        or not 'id' in flask.request.json
        or not 'price_per_person' in flask.request.json):
            print("Error: not all components for item price change are present.  Aborting.")
            return None, 400
        else:
            item_to_modify = self._menu.get_item_by_id(flask.request.json['id'])
            item_to_modify.set_price_per_person(flask.request.json['price_per_person'])
            return None, 204
        # may need empty string instead of None

    def get_menu_surcharge_json_dict(self):
        return flask.jsonify({'surcharge': self._menu.get_surcharge()}) , 200

    def post_menu_surcharge_json_dict(self):
        if not flask.request.json:
            print("Error: missing content")
            return None, 204
        elif not 'surcharge' in flask.request.json:
            print("Error: not all components for surcharge POST are present.  Aborting.")
            return None, 400
        elif not type(flask.request.json['surcharge']) is float:
            print("Error: surcharge must be float value")
            return None, 400
        else:
            self._menu.set_surcharge(float(flask.request.json['surcharge']))
            return

    def post_order_delivered_json_dict(self, order_id):
        order = Delectable.order.Order()
        orders = order.get_all_orders()
        
        if not order_id:
            print("Error: missing arguments")
            return None, 204
        else:
            if not type(order_id) is int:
                print("Error: order id must be an integer value")
                return None, 404
            else:
                for individual_order in orders:
                    if individual_order.get_order_id() == order_id:
                        individual_order.set_delivery_status("delivered")
                        return
            return None, 404

    # ***
    # *  Helper Routines for JSON Class
    # ***

    def customer_key_match(self, customer, key_raw):
        key = str(key_raw)
        name = customer.get_first_name() + customer.get_last_name()
        if key == name:
            return True
        if key == str(customer.get_customer_id()):
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
