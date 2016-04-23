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

# Unit tests for Menu()

from Delectable import menu
from Delectable import item

# Testing items

def test_menu_default_items():
    test_menu = menu.Menu()
    assert((test_menu.get_items() == []), "default items in menu not correctly set")

def test_menu_initialized_items():
    test_item = item.Item()
    test_menu = menu.Menu(items = [test_item])
    assert((test_menu.get_items() == [test_item]), "initialized items in menu not correctly set")

def test_menu_initialized_items_invalid():
    test_menu = menu.Menu(items = [15])
    assert((test_menu.get_items() == []), "initialized items in menu allowed for invalid value")

def test_menu_add_item():
    test_item = item.Item()
    test_menu = menu.Menu()
    test_menu.add_item(test_item)
    assert((test_menu.get_items() == [test_item]), "added item in menu not correctly set")

def test_menu_add_item_invalid():
    test_menu = menu.Menu()
    test_menu.add_item(15)
    assert((test_menu.get_items() == []), "add item in menu allowed for invalid value")

def test_menu_remove_item_to_empty():
    test_item = item.Item()
    test_menu = menu.Menu()
    test_menu.add_item(test_item)
    test_menu.remove_item_by_id(test_item.get_name())
    assert((test_menu.get_items() == []), "removing items to empty list in menu not correctly functioning")

def test_menu_remove_item():
    test_item_1 = item.Item(name = "default item 1")
    test_item_2 = item.Item(name = "default item 2")
    test_menu = menu.Menu()
    test_menu.add_item(test_item_1)
    test_menu.add_item(test_item_2)
    test_menu.remove_item_by_id(test_item_1.get_item_id())
    assert((test_menu.get_items() == [test_item_2]), "remove item in menu not correctly functioning")

def test_menu_remove_item_not_there():
    test_item = item.Item()
    test_menu = menu.Menu(items = [test_item])
    test_menu.remove_item_by_id("test item not existant")
    assert((test_menu.get_items() == [test_item]), "removing item by name not in list in menu not functioning")

# Testing item filter

def test_menu_item_filter_none_given():
    test_item = item.Item()
    test_menu = menu.Menu(items = [test_item])
    assert((test_menu.get_items_filter([]) == [test_item]), "filtering with empty list in menu returned incorrect values")

def test_menu_one_category_filter():
    test_item_1 = item.Item(category = ["test category 1"])
    test_item_2 = item.Item(category = ["test category 2"])
    test_menu = menu.Menu(items = [test_item_1, test_item_2])
    assert((test_menu.get_items_filter(["test category 1"]) == [test_item_1]), "filtering with single parameter in menu returned incorrect values")

def test_menu_multiple_category_filter():
    test_item_1 = item.Item(category = ["test category 1"])
    test_item_2 = item.Item(category = ["test category 2"])
    test_menu = menu.Menu(items = [test_item_1, test_item_2])
    assert((test_menu.get_items_filter(["test category 1", "test category 2"]) == [test_item_1, test_item_2]), "filtering with single parameter in menu returned incorrect values")

# Testing surcharge

def test_menu_default_surcharge():
    test_menu = menu.Menu()
    assert((test_menu.get_surcharge() == 0), "default surcharge value in menu not correctly set")

def test_menu_initialized_surcharge():
    test_menu = menu.Menu(surcharge = 15.25)
    assert((test_menu.get_surcharge() == 15.25), "initialized surcharge value in menu not correctly set")

def test_menu_initialized_surcharge_invalid():
    test_menu = menu.Menu(surcharge = -15.25)
    assert((test_menu.get_surcharge() == 0), "initialized surcharge value in menu allowed for invalid value")

def test_menu_initialized_surcharge_invalid_string():
    test_menu = menu.Menu(surcharge = "test invalid string")
    assert((test_menu.get_surcharge() == 0), "initialized surcharge value in menu allowed for invalid value")

def test_menu_set_surcharge():
    test_menu = menu.Menu()
    test_menu.set_surcharge(15.25)
    assert((test_menu.get_surcharge() == 15.25), "set surcharge value in menu not correctly set")

def test_menu_set_surcharge_invalid():
    test_menu = menu.Menu()
    test_menu.set_surcharge(-15.25)
    assert((test_menu.get_surcharge() == 0), "set surcharge value in menu allowed for invalid value")

def test_menu_set_surcharge_invalid_string():
    test_menu = menu.Menu()
    test_menu.set_surcharge("test invalid string")
    assert((test_menu.get_surcharge() == 0), "set surcharge value in menu allowed for invalid value")
