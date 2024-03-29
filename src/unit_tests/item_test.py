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

# Unit tests for Item()

from Delectable import item

import datetime

# Testing name

def test_item_default_name():
    test_item = item.Item()
    assert(test_item.get_name() == 'default item'), "default name for item not correctly set"

def test_item_set_name():
    test_item = item.Item()
    test_item.set_name("new item name")
    assert(test_item.get_name() == 'new item name'), "set_name in item did not correctly set name"

# Testing price

def test_item_default_price():
    test_item = item.Item()
    assert(test_item.get_price_per_person() == 0), "default price for item not correctly set"

def test_item_set_price_per_person():
    test_item = item.Item()
    test_item.set_price_per_person(15.25)
    assert(test_item.get_price_per_person() == 15.25), "set_price in item did not correctly set price"

def test_item_set_price_invalid():
    test_item = item.Item()
    test_item.set_price_per_person(-15.25)
    assert(test_item.get_price_per_person() == 0.0), "set_price in item allowed for invalid amount"

def test_item_initialized_price_invalid():
    test_item = item.Item(price = -15.25)
    assert(test_item.get_price_per_person() == 0), "initialized price for item allowed for invalid amount"

# Testing minimum serving size

def test_item_default_serving_min():
    test_item = item.Item()
    assert(test_item.get_min_serving() == 1), "default minimum servings not correctly set"

def test_item_set_serving_min_as_int():
    test_item = item.Item()
    test_item.set_min_serving(15)
    assert(test_item.get_min_serving() == 15), "set_min_serving in item did not correctly set integer value"

def test_item_set_serving_min_as_float():
    test_item = item.Item()
    test_item.set_min_serving(15.5)
    assert(test_item.get_min_serving() == 16), "set_min_serving in item did not correctly set float value"

def test_item_set_serving_min_invalid():
    test_item = item.Item()
    test_item.set_min_serving(-15)
    assert(test_item.get_min_serving() == 1), "set_min_serving in item allowed for invalid amount"

def test_item_initialized_serving_min_invalid():
    test_item = item.Item(min_serving = -15)
    assert(test_item.get_min_serving() == 1), "setting min_serving in item creation allowed for invalid amount"

def test_item_initialized_serving_min_as_int():
    test_item = item.Item(min_serving = 15)
    assert(test_item.get_min_serving() == 15), "setting min_serving in item creation did not correctly set integer value"

def test_item_initialized_serving_min_as_float():
    test_item = item.Item(min_serving = 15.5)
    assert(test_item.get_min_serving() == 16), "setting min_serving in item creation did not correctly set float value"
    
# Testing categories

def test_item_default_category():
    test_item = item.Item()
    assert(test_item.get_category() == []), "default category for item not correctly set"

def test_item_add_category():
    test_item = item.Item()
    test_item.add_category("Test Category")
    assert(test_item.get_category() == ["Test Category"]), "set category in item not correctly set"

def test_item_remove_category():
    test_item = item.Item()
    test_item.add_category("Test Category 1")
    test_item.add_category("Test Category 2")
    test_item.remove_category("Test Category 1")
    assert(test_item.get_category() == ["Test Category", "Test Category 2"]), "remove category in item did not remove category"

# Testing last_modified_date

def test_item_initialized_last_modified_date():
    test_item = item.Item()
    assert(test_item.get_last_modified_date().date() == datetime.datetime.now().date()), "last_modified date not successfully set upon item creation"

# Testing creation_date

def test_item_initialized_creation_date():
    test_item = item.Item()
    assert(test_item.get_creation_date().date() == datetime.datetime.now().date()), "creation date not successfully set"

# Testing item information dictionary

def test_item_contents_in_dict():
    test_item = item.Item()
    expected = {'id'     : test_item.get_item_id(),
    'name'               : test_item.get_name(),
    'price_per_person'   : test_item.get_price_per_person(),
    'minimum_order'      : test_item.get_min_serving(),
    'categories'         : [{'name' : category} for category in test_item.get_category()],
    'create_date'        : test_item.get_creation_date().strftime("%Y%m%d"),
    'last_modified_date' : test_item.get_last_modified_date().strftime("%Y%m%d"),
    }
    assert(test_item.get_item_contents_in_dict() == expected), "item contents in dict form do not match expected"

