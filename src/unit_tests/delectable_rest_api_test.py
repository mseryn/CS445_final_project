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

import datetime
import flask


def setup():
    api = delectablerest.DelectableREST().test_client()
    return api

def test_get_menu():
    """
    GET /menu
        Returns an array of all menu items in the menu.
        
        HTTP response code: 200 (OK).
        
        Resource URL:
            /menu
        Parameters:
            None
    """
    api = setup()
    result = api.get('/delectable/menu')
    print(result)
    assert(result.status_code == 200), "GET menu failed"

def test_get_menu_item():
    """
    GET /menu/{mid}
        Returns a detailed description of the menu item identified by {mid}.
        
        HTTP response code: 200 (OK), 404 (Not Found) if {mid} not found or invalid.
        
        Resource URL
            /menu/{mid}
        Parameters
            None.
    """

def test_get_order():
    """
    GET /order
        Returns an array of all orders.
        
        HTTP response code: 200 (OK).
        
        Resource URL
            /order
        Parameters
            None.
    """
    pass

def test_get_order_with_daterange():
    """
    GET /order?date=YYYYMMDD
        Returns an array of all orders that need to be delivered on YYYYMMDD.
        
        HTTP response code: 200 (OK).
        
        Resource URL
            /order?date=YYYYMMDD
        Parameters
            None.
    """
    pass

def test_put_order():
    """
    PUT /order
        Creates an order and returns the ID of that order {oid}.
        
        HTTP response codes: 201 (Created), 'Location' header with link to /order/{oid}. 
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
    pass

def test_get_order():
    """
    GET /order/{oid}
        Returns the detail for the order identified by {oid}.
        
        HTTP response code: 200 (OK) or 404 (Not Found) if the order {oid} doesn't exist.
        
        Resource URL
            /order/{oid}
        Parameters
            None.
    """
    pass

def test_post_order_cancellation():
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
    pass

def test_get_customer():
    """
    GET /customer
        Returns an array of all customers that have placed an order in the system.
        HTTP response code: 200 (OK).
        Resource URL
            /customer
        Parameters
            None.
    """
    pass

def test_get_customer_by_query():
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
    pass

def test_get_customer_by_id():
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
    pass

def test_get_report():
    """
    GET /report
        Returns an array of report IDs with their corresponding names.
        
        HTTP response code: 200 (OK).
        
        Resource URL
            /report
        Parameters
            None.
    """
    pass

def test_get_report_daterange():
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
    pass

def test_put_item_on_menu():
    """
    PUT /admin/menu
        Creates a new menu item entry in the menu.
        
        HTTP response codes: 201 (Created), 'Location' header with link to 
        /menu/account/{mid} where {mid} is the newly assigned ID for the menu item.
        
        Resource URL
            /admin/menu
        Parameters
            name             (required): the name of the menu item.
            price_per_person (required): the price of this menu item per person.
            minimum_order    (required): minimum number of orders of this menu item.
            categories       (required): an array of categories the menu item belongs 
                                         to, e.g. "organic", "vegan", etc.
    """
    pass

def test_post_price_on_menu():
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
    pass

def test_get_surcharge():
    """
    GET /admin/surcharge
        Returns an the current value of the surcharge.

        HTTP response code: 200 (OK).

        Resource URL
            /menu
        Parameters
            None.
    """
    pass

def test_post_surcharge():
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
    pass

def test_post_order_delivery():
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
    pass

if __name__ == "__main__":
    test_get_menu()
