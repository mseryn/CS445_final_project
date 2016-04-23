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

# Testing REST JSON-formatted API for Delectable

from DelectableREST import delectablerest
import Delectable

import datetime
import flask
import json
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.api = delectablerest.DelectableREST()
        self.app = self.api.app.test_client()
        self.app.testing = True
        self._response_header = {"Content-Type": "application/json"}

    def tearDown(self):
        Delectable.order.Order._all_orders = []
        Delectable.customer.Customer._all_customers = []

        Delectable.order.Order._order_id_counter = 0
        Delectable.customer.Customer._customer_id_counter = 0
        Delectable.item.Item._item_id_counter = 0

    def test_get_menu(self):
        """
        GET /menu
            Returns an array of all menu items in the menu.
            
            HTTP response code: 200 (OK).
            
            Resource URL:
                /menu
            Parameters:
                None
        """
        result = self.app.get('/delectable/menu')
        # assert response code where no data present
        assert(result.status_code == 200)
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                                      data = put_data,
                                      headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."

        result = self.app.get('/delectable/menu')
        # assert get response code
        assert(result.status_code == 200)

    def test_get_menu_item(self):
        """
        GET /menu/{mid}
            Returns a detailed description of the menu item identified by {mid}.
            
            HTTP response code: 200 (OK), 404 (Not Found) if {mid} not found or invalid.
            
            Resource URL
                /menu/{mid}
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."

        result = self.app.get('/delectable/menu/0')
        # assert get response code
        assert(result.status_code == 200), "GET menu item failed to return correct status"


    def test_get_orders(self):
        """
        GET /order
            Returns an array of all orders.
            
            HTTP response code: 200 (OK).
            
            Resource URL
                /order
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        result = self.app.get('/delectable/order',
                              headers = self._response_header)
        # assert response code
        assert(result.status_code == 200), "GET orders failed to return correct status"


    def test_get_order_with_daterange(self):
        """
        GET /order?date=YYYYMMDD
            Returns an array of all orders that need to be delivered on YYYYMMDD.
            
            HTTP response code: 200 (OK).
            
            Resource URL
                /order?date=YYYYMMDD
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        result = self.app.get('/delectable/order?date=20160423',
                              headers = self._response_header)
        # assert response code
        assert(result.status_code == 200), "GET order by daterange failed to return correct status"

    def test_put_order(self):
        """
        PUT /order
            Creates an order and returns the ID of that order {oid}.
            
            HTTP response codes: 201 (Created), 
            'Location' header with link to /order/{oid}. 
            The body of the response will contain the order id, and the URL needed to cancel the order.
            
            Resource URL
                /order
            Parameters
                delivery_date    (required): date when order needs to be delivered.
                delivery_address (required): address where order needs to be delivered.
                personal_info    (required): personal information for the person who places the order.
                note             (required): can be empty.
                order_detail     (required): a non-empty array of menu items.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.get('/delectable/menu/0')
        # assert get response code, invalid request
        assert(result.status_code == 404), "GET menu item failed to return correct status when request gave invalid menu id"
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."

        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"


    def test_get_order(self):
        """
        GET /order/{oid}
            Returns the detail for the order identified by {oid}.
            
            HTTP response code: 200 (OK) or 404 (Not Found) if the order {oid} doesn't exist.
            
            Resource URL
                /order/{oid}
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        result = self.app.get('/delectable/order/0',
                              headers = self._response_header)
        # assert response code
        assert(result.status_code == 200), "GET orders failed to return correct status"
        result = self.app.get('/delectable/order/1',
                              headers = self._response_header)
        # assert response code
        assert(result.status_code == 404), "GET orders failed to return correct status when given invalid order id"

    def test_post_order_cancellation(self):
        """
        POST /order/cancel/{oid}
            Cancels the order identified by {oid}.
            
            HTTP response codes: 204 (No Content), 'Location' header with link to 
            /order/{oid}. 
            The body of the response will be empty.
            
            Resource URL
                /order/cancel/{oid}
            Parameters
                id (required): the ID of the order being cancelled.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        post_data = """{'id': 0}"""
        result = self.app.post('/delectable/order/cancel/0',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code
        assert(result.status_code == 204), "POST order cancellation failed to return correct status"
        # assert post response header
        assert("/delectable/order/0" in str(result.headers)), "POST order cancellation failed to return correct headers"
                               

    def test_get_customer(self):
        """
        GET /customer
            Returns an array of all customers that have placed an order in the system.
            
            HTTP response code: 200 (OK).
            
            Resource URL
                /customer
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        result = self.app.get('/delectable/customer',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET customer failed to return correct status"

    def test_get_customer_by_query(self):
        """
        GET /customer?key=query_string
            Returns an array of all customers that have placed an order in the system and 
            match the query_string. An empty array will be returned if no customer matches 
            the query_string.
            
            HTTP response code: 200 (OK).
            
            Resource URL
                /customer
            Parameters
                key (optional): query string (aka keyword) used for search, if none specified, 
                                then everything matches.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        get_data = """{"key":"B"}"""
        result = self.app.get('/delectable/customer',
                              data = get_data,
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET customer by id failed to return correct status"

    def test_get_customer_by_id(self):
        """
        GET /customer/{cid}
            Returns details about customer identified by {cid}, including an array of all 
            orders by that customer.
            
            HTTP response code: 200 (OK) or 404 (Not Found) if customer {cid} doesn't exist.
            
            Resource URL
                /customer/{cid}
            Parameters
                None.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        result = self.app.get('/delectable/customer/0',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET customer by id failed to return correct status"
        result = self.app.get('/delectable/customer/1',
                              headers = self._response_header)
        # assert get response code - bad customer id
        assert(result.status_code == 404), "GET customer by id failed to return correct status when given invalid customer id"

    def test_get_report(self):
        """
        GET /report
            Returns an array of report IDs with their corresponding names.
            
            HTTP response code: 200 (OK).
            
            Resource URL
                /report
            Parameters
                None.
        """
        result = self.app.get('/delectable/report',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET reports failed to return correct status"

    def test_get_report_daterange(self):
        """
        GET /report/{rid}[?start_date=YYYYMMDD&end_date=YYYYMMDD]
            Returns the report identified by {rid}. If a start_date and end_date are 
            provided, then use those to narrow the result set.
            
            HTTP response code: 200 (OK) or 404 (Not Found) if {rid} is invalid.
            
            Resource URL
                /report/{rid}
            Parameters
                start_date (optional): the start date for the date range of the report.
                end_date   (optional): the end date for the date range of the report.
        """
        result = self.app.get('/delectable/report/801',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET report by id failed to return correct status"
        result = self.app.get('/delectable/report/802',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET report by id failed to return correct status"
        result = self.app.get('/delectable/report/803',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET report by id failed to return correct status"
        result = self.app.get('/delectable/report/804',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET report by id failed to return correct status"
        result = self.app.get('/delectable/report/1',
                              headers = self._response_header)
        # assert get response code - bad report id
        assert(result.status_code == 404), "GET report by id failed to return correct status with invalid report id"

    def test_put_item_on_menu(self):
        """
        PUT /admin/menu
            Creates a new menu item entry in the menu.
            
            HTTP response codes: 201 (Created), 
            'Location' header with link to /menu/account/{mid} 
            where {mid} is the newly assigned ID for the menu item.
            
            Resource URL
                /admin/menu
            Parameters
                name             (required): the name of the menu item.
                price_per_person (required): the price of this menu item per person.
                minimum_order    (required): minimum number of orders of this menu item.
                categories       (required): an array of categories the menu item belongs 
                                             to, e.g. "organic", "vegan", etc.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu', 
                              data = put_data, 
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."

    def test_post_price_on_menu(self):
        """
        POST /admin/menu/{mid}
            Modifies the price for the menu item identified by {mid}.

            HTTP response codes: 204 (No Content), 400 (Bad Request) if data is missing 
            from the request or is malformed. 
            'Location' header with link to /menu/{mid}. 
            The body of the response will be empty.
            
            Resource URL
                /admin/menu/{mid}
            Parameters
                id               (required): the ID of the menu item that's being changed.
                price_per_person (required): the price of this menu item per person.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu', 
                              data = put_data, 
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."

        post_data = """{"id": 0, "price_per_person": 3.99}"""
        result = self.app.post('/delectable/admin/menu/0',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code
        assert(result.status_code == 204), "POST menu item price failed to return correct status"
        # assert post respose header
        assert("/delectable/menu/0" in str(result.headers)), "POST menu item price failed to return correct location header"

    def test_get_surcharge(self):
        """
        GET /admin/surcharge
            Returns an the current value of the surcharge.

            HTTP response code: 200 (OK).

            Resource URL
                /menu
            Parameters
                None.
        """
        result = self.app.get('/delectable/admin/surcharge',
                              headers = self._response_header)
        # assert get response code
        assert(result.status_code == 200), "GET surcharge by admin failed to return correct status"

    def test_post_surcharge(self):
        """
        POST /admin/surcharge
            Modifies the surcharge amount.

            HTTP response codes: 204 (No Content), 400 (Bad Request) if data is 
            missing from the request or is malformed. 
            'Location' header with link to /admin/surcharge. 
            The body of the response will be empty.
            
            Resource URL
                /admin/surcharge
            Parameters
                surcharge (required): the new surcharge amount.
        """
        post_data = """{"surcharge": 15.25}"""
        result = self.app.post('/delectable/admin/surcharge',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code
        assert(result.status_code == 204), "POST surcharge by admin failed to return correct status"
        # assert post header
        assert("/delectable/admin/surcharge" in str(result.headers)), "POST surcharge by admin failed to return correct headers"
        post_data = """{}"""
        result = self.app.post('/delectable/admin/surcharge',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code - bad data
        assert(result.status_code == 400), "POST surcharge by admin failed to return correct status when handed bad data"
        


    def test_post_order_delivery(self):
        """
        POST /admin/delivery/{oid}
            Modifies the status of order {oid} to "delivered".

            HTTP response codes: 204 (No Content), 404 (Not Found) if {oid} not 
            found or invalid. 
            'Location' header with link to /order/{oid}. 
            The body of the response will be empty.

            Resource URL
                /admin/delivery/{oid}
            Parameters
                id (required): the id of the order being updated.
        """
        put_data = """{"name":"Lasagna","price_per_person": 2.49, "minimum_order":6, "categories":[{"name": "organic"},{"name": "vegetarian"}]}"""
        result = self.app.put('/delectable/admin/menu',
                               data = put_data,
                               headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT menu item failed to return correct status"
        # assert put respose header
        assert("/delectable/menu/0" in str(result.headers)), "PUT menu item failed to return correct location header"
        # assert put response data
        assert({"id": 0} == json.loads(result.data.decode("utf-8"))), "PUT menu item failed to return correct response data."
        put_data = """{"delivery_date": "20160423", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email":     "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}"""
        result = self.app.put('/delectable/order',
                              data = put_data,
                              headers = self._response_header)
        # assert put response code
        assert(result.status_code == 201), "PUT order failed to return correct status"
        # assert put response header
        assert("/delectable/order/0" in str(result.headers)), "PUT order failed to return correct location header"
        # assert put response data
        assert({"id": 0, "cancel_url": "/delectable/order/cancel/0"} == json.loads(result.data.decode("utf-8"))), "PUT order failed to return correct response data"

        post_data = """{"id": 0}"""
        result = self.app.post('/delectable/admin/delivery/0',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code
        assert(result.status_code == 204), "POST order status to delivery failed to return correct status"
        # assert post response header
        assert("/delectable/order/0" in str(result.headers)), "POST order status to delivery failed to return correct headers"
        post_data = """{"id": 1}"""
        result = self.app.post('/delectable/admin/delivery/1',
                               data = post_data,
                               headers = self._response_header)
        # assert post response code - given invalid order id
        assert(result.status_code == 404), "POST order status to delivery failed to return correct status when given invalid order id"


if __name__ == "__main__":
    TestAPI().test_get_menu()
