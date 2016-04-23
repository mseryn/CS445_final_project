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

from Delectable import item

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

    def get_items(self):
        return self._items

    def get_item_by_id(self, item_id):
        for individual_item in self._items:
            if individual_item.get_item_id() == item_id:
                return individual_item
        return None

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

    def add_item(self, new_item):
        # ensure new_item is an Item
        if isinstance(new_item, item.Item):
            self._items.append(new_item)

    def remove_item_by_id(self, item_id):
        for item in self._items:
            if item.get_item_id() == item_id:
                self._items.remove(item)

    def get_surcharge(self):
        return self._surcharge

    def set_surcharge(self, new_charge):
        if (type(new_charge) is int) or (type(new_charge) is float):
            if new_charge >= 0:
                self._surcharge = new_charge
        else:
            print("\nError: Surcharge must be a positive number. Surcharge not changed.")

    def get_menu_item_contents_in_dict(self, individual_item):
        menu_item = {}
        if individual_item in self._items:
            return individual_item.get_item_contents_in_dict()
        return menu_item

    def get_menu_contents_in_dict(self):
        menu_dict = {'surcharge': self._surcharge,
                     'items'    : [],
                    }
        for each_item in self._items:
            menu_dict['items'].append(self.get_menu_item_contents_in_dict(each_item))
        return menu_dict
        
