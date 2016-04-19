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

import item

class Menu():
    
    def __init__(self, items = [], surcharge = 0):
        self._items = []
        for item_individual in items:
            if isinstance(item_individual, item.Item):
                self._items.append(item_individual)

        if type(surcharge) is int:
            if surcharge >= 0:
                self._surcharge = surcharge
        else:
            print("\nError: surcharge must be positive number.  Setting surcharge to $0.")
            self._surcharge = 0

    def set_surcharge(self, new_charge):
        if type(new_charge) is int:
            if new_charge >= 0:
                self._surcharge = new_charge
        else:
            print("\nError: Surcharge must be a positive number. Surcharge not changed.")

    def get_surcharge(self):
        return self._surcharge

    def add_item(self, new_item):
        # ensure new_item is an Item
        if isinstance(new_item, item.Item):
            self._items.append(new_item)

    def remove_item_by_name(self, item_name):
        """
        Removes all items corresponding to the given name.
        """
        for item in self._items:
            if item.get_name() == item_name:
                self._items.remove(item)

    def get_items(self):
        return self._items

    def get_items_filter(self, desired_categories):
        """
        Takes a list of categories in the form of strings. Input must be a list.
        """
        sorted_items = []
        if desired_categories:
            for item in self._items:
                for category in item.get_category():
                    for desired_category in desired_categories:
                        if category == desired_category:
                            sorted_items.append(item)
            return sorted_items
        else:
            return self._items
