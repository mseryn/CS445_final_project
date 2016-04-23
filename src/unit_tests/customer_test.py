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

from Delectable import customer

# Testing customer_id

def test_customer_id():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_customer_id() == 0), "first customer ID not correctly set")

def test_customer_id_incrimented():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", 123456789)
    assert((test_customer.get_customer_id() == 1), "incrimented customer ID not correctly set")

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
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", "123456789")
    assert((test_customer.get_phone_number() == "123456789"), "default phone number in customer not correctly set")

def test_customer_set_phone_number():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", "123456789")
    test_customer.set_phone_number("5555555555")
    assert((test_customer.get_phone_number() == "5555555555"), "set phone number in customer not correctly set")

# Testing customer equality

def test_customer_equality():
    test_customer_1 = customer.Customer("test Last Name", "test First Name", "test email address", "123456789")
    test_customer_2 = customer.Customer("test Last Name", "test First Name", "test email address", "123456789")
    assert((test_customer_1 == test_customer_2), "customer equality not functioning")

# Testing customer dict output format

def test_customer_details_dict():
    test_customer = customer.Customer("test Last Name", "test First Name", "test email address", "123456789")
    expected = {'id'    : test_customer.get_customer_id(),
                'name'  : "test Last Name",
                'email' : "test email address",
                'phone' : "123456789",
                }
    assert((test_customer.get_customer_details_dict() == expected), "customer details dictionary not correctly formatted")

