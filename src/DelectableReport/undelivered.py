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

from . import report
import Delectable.order

import datetime

class Undelivered(report.Report):
    def __init__(self, date):
        if type(date) == datetime:
            _self.start_date = date

    def get_report_contents(self):
        orders_for_date = []
        orders = order.Order.get_all_orders()
        for individual_order in orders:
            if individual_order.get_status() == "open":
                if individual_order.get_delivery_date().date() == self._start_date.date():
                    orders_for_date.append(individual_order)
        return orders_for_date
