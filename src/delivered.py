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

import report
import order

import datetime

class Delivered(Report):
    def __init__(self, start_date, end_date):
        if (type(start_date) == datetime) and (if type(end_date) == datetime):
            self._start_date = start_date
            self._end_date = end_date
        self._number_delivered = 0

        self._orders_for_dates = []
        orders = order.Order.get_all_orders()

        for individual_order in orders:
            if individual_order.get_status() == "delivered":
                if (individual_order.get_delivery_date().date() <= end_date.date()) and (individual_order.get_delivery_date().date() >= start_date.date()):
                    self._orders_for_dates.append(individual_order)
                    self._number_delivered += 1

    def get_report_contents(self):
        return self._number_delivered
