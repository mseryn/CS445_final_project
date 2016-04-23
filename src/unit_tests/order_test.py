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

# Unit tests for Order()

from Delectable import order
from Delectable import item
from Delectable import customer
from Delectable import menu

import datetime
from datetime import *

# Testing all_orders

def test_order_get_all_orders():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(order.Order.get_all_orders() == [test_order]), "static method retrieval of all orders not correctly working"

def test_order_get_order_by_id():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(order.Order.get_order_by_id(test_order.get_order_id()) == test_order), "static method retrieval of order by ID not correctly working"

# Testing order_id

def test_order_id():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_order_id() == 2), "first order ID not correctly set"

# Testing all_customers

def test_order_get_all_customers():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(order.Order.get_all_customers() == [test_customer]), "static method retrieval of all customers not correctly working"

# Testing delivery_status

def test_order_delivery_status_at_creation():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_delivery_status() == 'open'), "delivery status not 'open' when order first created"

def test_order_delivery_status_set_delivered():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_order.set_delivery_status("delivered")
    assert(test_order.get_delivery_status() == 'delivered'), "set delivery status in object not functioning"

def test_order_delivery_status_set_cancelled():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_order.set_delivery_status("cancelled")
    assert(test_order.get_delivery_status() == 'cancelled'), "set delivery status in object not functioning"

def test_order_delivery_status_invalid():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_order.set_delivery_status("this")
    assert(test_order.get_delivery_status() == 'open'), "set delivery status in object allowed for invalid value"

# Testing order_date

def test_order_default_order_date():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_order_date().date() == datetime.now().date()), "default order date in order not correctly set to today's date"

def test_order_default_order_date_invalid():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu, order_date = 15 )
    assert(test_order.get_order_date().date() == datetime.now().date()), "initialized order date in order allowed for invalid date"

# Testing delivery_date

def test_order_default_delivery_date():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    tomorrow = datetime.now() + timedelta(1)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_delivery_date().date() == tomorrow.date()), "default delivery date in order not correctly set to tomorrow's date"

def test_order_default_order_date_invalid():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    tomorrow = datetime.now() + timedelta(1)
    test_order = order.Order(test_customer, test_menu, delivery_date = 15)
    assert(test_order.get_delivery_date().date() == tomorrow.date()), "initialized delivery date in order allowed for invalid date"

def test_order_set_delivery_date():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    tomorrow = datetime.now() + timedelta(1)
    test_order.set_delivery_date(tomorrow)
    assert(test_order.get_delivery_date().date() == tomorrow.date()), "default delivery date in order not correctly set to tomorrow's date"

# Testing items

def test_order_default_items():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_items() == []), "default items in order not correctly set"

def test_order_initialized_items():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_item = item.Item()
    test_menu.add_item(test_item)
    test_order = order.Order(test_customer, test_menu, items = [(test_item.get_item_id(), 15)])
    assert(test_order.get_items() == [(test_item, 15)]), "initialized items in order not correctly set"

def test_order_initialized_items_invalid():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu, items = [(15, 15)])
    assert(test_order.get_items() == []), "initialized items in order allowed invalid value"

def test_order_add_item():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_item = item.Item()
    test_menu.add_item(test_item)
    test_order.add_item((test_item.get_item_id(), 15))
    assert(test_order.get_items() == [(test_item, 15)]), "added item in order not correctly set"

def test_order_remove_item_to_empty():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_item = item.Item()
    test_menu.add_item(test_item)
    test_order.add_item((test_item.get_item_id(), 15))
    test_order.remove_item(test_item.get_item_id())
    assert(test_order.get_items() == []), "removing all items from order not correctly removed"

def test_order_remove_item():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_item_1 = item.Item(name = "default item 1")
    test_item_2 = item.Item(name = "default item 2")
    test_menu.add_item(test_item_1)
    test_menu.add_item(test_item_2)
    test_order.add_item((test_item_1.get_item_id(), 15))
    test_order.add_item((test_item_2.get_item_id(), 15))
    test_order.remove_item(test_item_1.get_item_id())
    assert(test_order.get_items() == [(test_item_2, 15)]), "removed item in order not correctly removed"

# Testing surcharge

def test_order_default_surcharge():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_surcharge() == 0), "default surcharge in order not correctly set"

def get_surcharge_considering_day():
    test_menu = menu.Menu()
    test_menu.set_surcharge(15.25)
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    today = datetime.now().weekday()
    if today > 4:
        assert(test_order.get_surcharge() == 15.25), "surcharge on a weekend not correctly applying to order"
    else:
        assert(test_order.get_surcharge() == 0), "surcharge on a weekday not correctly applying to order"

# Testing instructions

def test_order_default_instructions():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_instructions() == ""), "default instructions in order not correctly set"

def test_order_initialized_instructions():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu, instructions = "test instructions")
    assert(test_order.get_instructions() == "test instructions"), "initialized instructions in order not correctly set"

def test_order_set_instructions():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    test_order.set_instructions("test instructions")
    assert(test_order.get_instructions() == "test instructions"), "set instructions in order not correctly set"

# Testing customer

def test_order_get_customer_id():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_customer_id() == test_customer.get_customer_id()), "customer id retrieval fails in order"

def test_order_get_customer():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_customer() == test_customer), "customer retrieval fails in order"

# Testing billing_address

def test_order_billing_address():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_billing_address() == "default billing address"), "billing address in order fails"

# Testing delivery_address

def test_order_delivery_address():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu)
    assert(test_order.get_delivery_address() == "default delivery address"), "delivery address in order fails"

# Testing cost

def test_order_total_cost():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_item_1 = item.Item(price = 15.25)
    test_menu.add_item(test_item_1)
    test_order = order.Order(test_customer, test_menu, items = [(test_item_1.get_item_id(), 15)])
    assert(test_order.get_total_cost() == (15.25 * 15)), "total cost calculation in order fails"

def test_order_items_cost():
    test_menu = menu.Menu()
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_item_1 = item.Item(price = 15.25)
    test_menu.add_item(test_item_1)
    test_order = order.Order(test_customer, test_menu, items = [(test_item_1.get_item_id(), 15)])
    assert(test_order.get_total_item_cost() == (15.25 * 15)), "total item cost calculation in order fails"

# Testing order dict output

def test_order_formatted_dict_output():
    test_menu = menu.Menu()
    test_item = item.Item()
    test_menu.add_item(test_item)
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_order = order.Order(test_customer, test_menu, items = [(test_item, 16)])
    expected = {'id'              : test_order.get_order_id(),
                'amount'          : test_order.get_total_item_cost(),
                'surcharge'       : test_order.get_surcharge_considering_day(),
                'status'          : test_order.get_delivery_status(),
                'order_date'      : test_order.get_order_date().strftime("%Y%m%d"),
                'delivery_date'   : test_order.get_delivery_date().strftime("%Y%m%d"),
                'delivery_address': test_order.get_delivery_address(),
                'note'            : test_order.get_instructions(),
                'order_detail'    : [],
                }
    order_customer = customer.Customer.get_customer_by_id(test_order._customer)
    name_string = order_customer.get_first_name() + " " + order_customer.get_last_name()
    expected['ordered_by'] = {"name" : name_string, 
                              "email": order_customer.get_email(),
                              "phone": order_customer.get_phone_number(), 
                               }
    for individual_item, serving_size in test_order.get_items():
        expected['order_detail'].append({"id"   : individual_item.get_item_id(),
                                           "name" : individual_item.get_name(),
                                           "count": serving_size,
                                         })
    assert(test_order.get_order_details_in_dict() == expected), "dictionary output of order not correctly functioning"
