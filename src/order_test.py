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

import order
import item
import customer
import address
import datetime
from datetime import *

# Testing order_id
def test_order_id():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_order_id() == 0), "first order ID not correctly set")

def test_order_id_incriment():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_order_id() == 1), "incrimented order ID not correctly set")

# Testing order_date

def test_order_default_order_date():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_order_date() == datetime.now()), "default order date in order not correctly set to today's date")

def test_order_default_order_date_invalid():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, order_date = 15 )
    assert((test_order.get_order_date() == None), "initialized order date in order allowed for invalid date")

# Testing delivery_date

def test_order_default_delivery_date():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_delivery_date() == (datetime.now() + timedelta(1))), "default delivery date in order not correctly set to tomorrow's date")

def test_order_default_order_date_invalid():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, delivery_date = 15)
    assert((test_order.get_delivery_date() == None), "initialized delivery date in order allowed for invalid date")

# Testing items

def test_order_default_items():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_items() == []), "default items in order not correctly set")

def test_order_initialized_items():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)

    test_item = item.Item()
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, items = [test_item])
    assert((test_order.get_items() == [test_item]), "initialized items in order not correctly set")

def test_order_initialized_items_invalid():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, items = [15])
    assert((test_order.get_items() == []), "initialized items in order allowed invalid value")

def test_order_add_item():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_item = item.Item()
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.add_item(test_item)
    assert((test_order.get_items() == [test_item]), "added item in order not correctly set")

def test_order_add_item_invalid():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.add_item(15)
    assert((test_order.get_items() == []), "added item in order allowed invalid value")

def test_order_remove_item_to_empty():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    test_item = item.Item()

    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.add_item(test_item)
    test_order.remove_item(test_item)
    assert((test_order.get_items() == []), "removing all items from order not correctly removed")

def test_order_remove_item():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_item_1 = item.Item(name = "default item 1")
    test_item_2 = item.Item(name = "default item 2")
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.add_item(test_item_1)
    test_order.add_item(test_item_2)
    test_order.remove_item(test_item_1)
    assert((test_order.get_items() == [test_item_2]), "removed item in order not correctly removed")

# Testing surcharge

def test_order_default_surcharge():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_surcharge() == 0), "default surcharge in order not correctly set")

def test_order_initialized_surcharge():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, surcharge = 15.25)
    assert((test_order.get_surcharge() == 15.25), "initialized surcharge in order not correctly set")

def test_order_set_surcharge():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.set_surcharge(15.25)
    assert((test_order.get_surcharge() == 15.25), "set surcharge in order not correctly set")

def test_order_should_surcahrge_apply():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    if datetime.today().weekday() > 4:
        assert((test_order.should_surcharge_apply() == True), "should_surcharge_apply in order returned false for a weekend - this is incorrect")
    else:
        assert((test_order.should_surcharge_apply() == False), "should_surcharge_apply in order returned true for a weekday - this is incorrect")

# Testing instructions

def test_order_default_instructions():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    assert((test_order.get_instructions == ""), "default instructions in order not correctly set")

def test_order_initialized_instructions():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing, instructions = "test instructions")
    assert((test_order.get_instructions == "test instructions"), "initialized instructions in order not correctly set")

def test_order_set_instructions():
    test_customer = customer.Customer("default last", "default first", "default email", 123456789)
    test_address_delivery = address.Address("default street 1", "default city 1", "default state 1", 12345)
    test_address_billing = address.Address("default street 2", "default city 2", "default state 2", 67890)
    
    test_order = order.Order(test_customer, test_address_delivery, test_address_billing)
    test_order.set_instructions("test instructions")
    assert((test_order.get_instructions == "test instructions"), "set instructions in order not correctly set")
