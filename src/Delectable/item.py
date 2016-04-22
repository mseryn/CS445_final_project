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

import datetime

class Item():
    _item_id_counter = 0

    def __init__(self, name = "default item", price = 0.0, min_serving = 1, category = []):
        self._create_date = datetime.datetime.now()
        self._last_modified_date = datetime.datetime.now()

        self._item_id =self. _item_id_counter
        Item._item_id_counter += 1

        self._name = name
        self._category = category

        if price >= 0:
            self._price = price
        else:
            print("Error: item price must be at least $0. Setting item price to $0.")
            self._price = 0.0

        if min_serving > 0:
            if min_serving % 1 == 0:
                self._min_serving = min_serving
            else:
                self._min_serving = 1 + int(min_serving)
        else:
            print("Error: minimum number of servings for an item must be greater than 0. Setting minimum serving size to 1.")
            self._min_serving = 1

    def get_item_id(self):
        return self._item_id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name
        self.set_last_modified_date()

    def get_price_per_person(self):
        return self._price

    def set_price_per_person(self, new_price):
        if new_price >= 0:
            self._price = new_price
            self.set_last_modified_date()
        else:
            print("Error: item price must be at least $0.")

    def get_min_serving(self):
        return self._min_serving

    def set_min_serving(self, new_min_serving):
        if new_min_serving > 0:
            if new_min_serving % 1 == 0:
                self._min_serving = new_min_serving
            else:
                self._min_serving = 1 + int(new_min_serving)
            self.set_last_modified_date()
        else:
            print("Error: minimum number of servings for an item must be greater than 0.")

    def get_category(self):
        return self._category

    def add_category(self, new_category):
        self._category.append(str(new_category))
        self.set_last_modified_date()

    def remove_category(self, category_to_remove):
        self._category.remove(category_to_remove)
        self.set_last_modified_date()

    def set_last_modified_date(self):
        self._last_modified_date = datetime.datetime.now()

    def get_last_modified_date(self):
        return self._last_modified_date

    def get_creation_date(self):
        return self._creation_date
