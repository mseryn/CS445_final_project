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
from Delectable import customer
from Delectable import menu

import datetime
from datetime import *

class Order():

    _all_orders = []
    _all_customers = []
    _order_id_counter = 0

    def __init__(self, initialized_customer, 
            initialized_billing_address, 
            initialized_delivery_address,
            initialized_menu, 
            order_date = datetime.today(), 
            delivery_date = (datetime.today() + timedelta(1)), 
            items = [], 
            instructions = ""):

        self._menu = initialized_menu
        self._surcharge = self._menu.get_surcharge()

        # Dealing with order ID
        self._order_id = self._order_id_counter
        Order._order_id_counter += 1

        self._delivery_status = "open"

        # Type-confirming customer
        if isinstance(initialized_customer, customer.Customer):
            self._customer = initialized_customer

        # Type-confirming dates
        if type(order_date) is datetime:
            self._order_date = order_date
        else:
            self._order_date = datetime.now()
        if type(delivery_date) is datetime:
            self._delivery_date = delivery_date
        else:
            self._delivery_date = datetime.today() + timedelta(1)

        # Items passed in as (item_id, serving_size) tuples
        # Items are then stored as (item, serving_size) tuples
        self._items = []
        self._total_item_cost = 0
        for item_id, quantity in items:
            new_item = self._menu.get_item_by_id(item_id)
            if new_item is not None:
                new_item_servings = quantity
                if new_item:
                    if new_item_servings >= new_item.get_min_serving():
                        self._items.append((new_item, new_item_servings))
                        self._total_item_cost += new_item.get_price_per_person() * new_item_servings
                    else:
                        print("Error: too few servings ordered for item %i" %(new_item.get_item_id()))

        # Setting address strings
        self._billing_address = initialized_billing_address
        self._delivery_address = initialized_delivery_address
        self._surcharge = menu.Menu().get_surcharge()
        self._instructions = instructions

        self._all_customers.append(self._customer)
        self._all_orders.append(self)

    @staticmethod
    def get_all_orders():
        return Order._all_orders

    @staticmethod
    def get_order_by_id(order_id):
        for order in Order._all_orders:
            if order.get_order_id() == order_id:
                return order

    @staticmethod
    def get_all_customers():
        return Order._all_customers

    def get_order_id(self):
        return self._order_id

    def get_customer_id(self):
        return self._customer.get_customer_id()

    def get_customer(self):
        return self._customer

    def get_delivery_status(self):
        return self._delivery_status

    def set_delivery_status(self, new_status):
        if ((new_status.lower() == "open") 
        or (new_status.lower() == 'delivered')
        or (new_status.lower() == "cancelled")):
            self._delivery_status = new_status.lower()
        else:
            print("\nError: delivery status must be set to either 'open', 'delivered', or 'cancelled'.  Status unchanged.")

    def get_order_date(self):
        return self._order_date

    def set_order_date(self, new_date):
        if type(new_date) is datetime:
            self._order_date = new_date

    def get_delivery_date(self):
        return self._delivery_date

    def set_delivery_date(self, new_date):
        if type(new_date) is datetime.datetime:
            self._order_date = new_date

    def get_surcharge(self):
        return self._surcharge

    def get_surcharge_considering_day(self):
        # To determine if surcharge applies:
        # weekday() applied to a datetime object returns the day of week
        # where Monday = 0 and Sunday = 6.
        # Surcharges apply only on weekends, IE when return value is 5 or 6.
        if self._delivery_date.weekday() > 4:
            return self._surcharge
        else:
            return 0

    def get_total_cost(self):
        """
        Returns cost of all order elements - items and surcharge
        """
        return self._total_item_cost + self.get_surcharge_considering_day()

    def get_total_item_cost(self):
        """
        Returns cost of all items
        """
        return self._total_item_cost

    def get_items(self):
        return self._items

    def add_item(self, item_tuple):
        """
        Takes tuple of form (item_id, serving_size)
        Stores in form (item, serving_size)
        """
        new_item = self._menu.get_item_by_id(item_tuple[0])
        new_item_servings = item_tuple[1]
        if new_item:
            if new_item_servings >= new_item.get_min_serving():
                self._items.append((new_item, new_item_servings))
                self._total_item_cost += new_item.get_price_per_person() * new_item_servings
            else:
                print("Error: too few servings ordered for item %i" %(new_item.get_item_id()))

    def remove_item(self, item_id):
        """
        Takes item_id, removes from list of items in order
        """
        for item_tuple in self._items:
            if item_tuple[0] == item_id:
                self._items.remove(item_tuple)

    def get_instructions(self):
        return self._instructions

    def set_instructions(self, new_instructions):
        self._instructions = new_instructions

    def get_delivery_address(self):
        return self._delivery_address

    def get_billing_address(self):
        return self._billing_address

    def get_order_details_in_dict(self):
        """
        Returns a dict containing the following information concerning an order:
            id, surcharge, status, order_date, delivery_date, delivery_address,
            note, ordered_by, and order_detail
        ordered_by is a dict containing the following information concerning a
        customer:
            name, email, and phone
        order_detail is a dict containing the following information concerning
        items in an order:
            id (item), name, count (number of servings ordered)
        """
        order_item = {}
        order_item['id'] = self._order_id
        order_item['amount'] = self._total_item_cost
        order_item['surcharge'] = self.get_surcharge_considering_day()
        order_item['status'] = self._delivery_status
        order_item['order_date'] = self._order_date.strftime("%Y%m%d")
        order_item['delivery_date'] = self._delivery_date.strftime("%Y%m%d")
        name_string = self._customer.get_first_name() + " " + self._customer.get_last_name()
        order_item['ordered_by'] = {"name" : name_string,
                                    "email": self._customer.get_email(),
                                    "phone": self._customer.get_phone_number(), 
                                    }
        order_item['delivery_address'] = self._delivery_address
        order_item['note'] = self._instructions
        order_item['order_detail'] = []
        for individual_item, serving_size in self._items:
            order_item['order_detail'].append({"id"   : individual_item.get_item_id(),
                                               "name" : individual_item.get_name(),
                                               "count": serving_size,
                                               })
        return order_item

