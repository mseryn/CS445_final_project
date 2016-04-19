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

# Unit tests for Customer

import address
import customer

# Testing last_name

def test_customer_initialize_last_name():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_last_name() == "test Last Name"), "default last name in customer not correctly set")

def test_customer_set_last_name():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_last_name("new Last Name")
    assert((test_customer.get_last_name() == "new Last Name"), "set last name in customer not correctly set")

# Testing first_name

def test_customer_initialize_first_name():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_first_name() == "test First Name"), "default first name in customer not correctly set")
    
def test_customer_set_first_name():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_first_name("new First Name")
    assert((test_customer.get_last_name() == "new First Name"), "set first name in customer not correctly set")

# Testing email

def test_customer_initialize_email():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_email() == "test email address"), "default email customer not correctly set")

def test_customer_initialize_email():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_email("new email address")
    assert((test_customer.get_email() == "new email address"), "set email customer not correctly set")

# Testing phone number

def test_customer_initialize_phone_number():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_phone_number() == 123456789), "default phone number in customer not correctly set")

def test_customer_set_phone_number():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_phone_number(5555555555)
    assert((test_customer.get_phone_number() == 5555555555), "set phone number in customer not correctly set")

def test_customer_set_phone_number_invalid_string():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_phone_number("invalid string")
    assert((test_customer.get_phone_number() == 123456789), "set phone number in customer allowed for invalid value")

def test_customer_set_phone_number_invalid_too_short():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_phone_number(555)
    assert((test_customer.get_phone_number() == 123456789), "set phone number in customer allowed for invalid value")

def test_customer_set_phone_number_invalid_float():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    test_customer.set_phone_number(555.5)
    assert((test_customer.get_phone_number() == 123456789), "set phone number in customer allowed for invalid value")
