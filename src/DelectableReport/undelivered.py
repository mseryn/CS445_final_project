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
    def __init__(self, start_date, end_date):
        self._start_date = start_date

    def get_report_contents(self):
        orders_for_date = []
        orders = Delectable.order.Order.get_all_orders()
        for individual_order in orders:
            if individual_order.get_delivery_status() == "open":
                if individual_order.get_delivery_date().date() == self._start_date.date():
                    orders_for_date.append(individual_order.get_order_details_in_dict())
        
        return {'orders': orders_for_date}
