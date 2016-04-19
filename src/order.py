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
import customer
import address

import datetime
from datetime import *

class Order():

    _id_counter = 0

    def __init__(self, initialized_customer, initialized_billing_address, initialized_delivery_address, 
            order_date = datetime.today(), 
            delivery_date = (datetime.today() + timedelta(1)), 
            items = [], surcharge = 0.0, instructions = ""):


        self._order_id = self._id_counter
        self._id_counter += 1

        if isinstance(initialized_customer, customer.Customer):
            self._customer = initialized_customer
        if isinstance(initialized_billing_address, address.Address):
            self._billing_address = initialized_billing_address
        if isinstance(initialized_delivery_address, address.Address):
            self._delivery_address = initialized_delivery_address

        if type(order_date) is datetime:
            self._order_date = order_date
        else:
            self._order_date = datetime.now()
        if type(delivery_date) is datetime:
            self._delivery_date = delivery_date
        else:
            self._delivery_date = datetime.today() + timedelta(1)

        self._items = []
        self._total_item_cost = 0
        for individual_item in items:
            if isinstance(individual_item, item.Item):
                self._items.append(individual_item)
                self._total_item_cost += individual_item.get_price() 

        self._surcharge = surcharge
        self._instructions = instructions
        self._total_item_cost = 0.0
            

    def get_order_id(self):
        return self._order_id

    def get_order_date(self):
        return self._order_date

    def get_delivery_date(self):
        return self._delivery_date

    def get_total_cost(self):
        return self._total_item_cost + self._surcharge

    def get_surcharge(self):
        return self._surcharge

    def get_total_item_cost(self):
        return self._total_item_cost

    def get_items(self):
        return self._items

    def get_instructions(self):
        return self._instructions

    def add_item(self, new_item):
        if isinstance(new_item, item.Item):
            self._items.append(new_item)

    def remove_item(self, item_to_remove):
        for item in self._items:
            if item == item_to_remove:
                self._items.remove(item_to_remove)

    def set_surcharge(self, new_surcharge):
        self._surcharge = new_surcharge

    def set_instructions(self, new_instructions):
        self._instructions = new_instructions

    def set_order_date(self, new_date):
        if type(new_date) is datetime:
            self._order_date = new_date

    def set_delivery_date(self, new_date):
        if type(new_date) is datetime.datetime:
            self._order_date = new_date

    def should_surcharge_apply(self):
        # weekday() applied to a datetime object returns the day of week
        # where Monday = 0 and Sunday = 6.
        # Surcharges apply only on weekends, IE when return value is 5 or 6.
        if self._delivery_date.weekday() > 4:
            return True
        else:
            return False
