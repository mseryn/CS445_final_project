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

# Unit testing for Address()

from Delectable import address

# Testing street

def test_address_initialized_street():
    test_address = address.Address("test street string", "test city string", "state string", 12345)
    assert((test_address.get_street() == "test street string"), "initialized street in address not correctly set")

# Testing city

def test_address_initialized_city():
    test_address = address.Address("test street string", "test city string", "state string", 12345)
    assert((test_address.get_city() == "test city string"), "initialized city in address not correctly set")

# Testing state

def test_address_initialized_state():
    test_address = address.Address("test street string", "test city string", "state string", 12345)
    assert((test_address.get_state() == "test state string"), "initialized state in address not correctly set")

# Testing zipcode

def test_address_initialized_zipcode():
    test_address = address.Address("test street string", "test city string", "state string", 12345)
    assert((test_address.get_zipcode() == 12345), "initialized zipcode in address not correctly set")
