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
from Delectable import order

import datetime

class Deliveries(report.Report):
    def __init__(self, start_date, end_date):
        self._start_date = start_date
        self._end_date = end_date

        # Getting all orders in the date range
        self._all_orders = [individual_order for individual_order in order.Order.get_all_orders()
                  if (individual_order.get_delivery_date().date() <= end_date.date()) 
                      and (individual_order.get_delivery_date().date() >= start_date.date())]

    def get_report_contents(self):
        delivered_dict = {}
        delivered_orders = []
        for individual_order in self._all_orders:
            if individual_order.get_delivery_status() == "delivered":
                delivered_orders.append(individual_order.get_order_details_in_dict())

        delivered_dict['id'] = 804 
        delivered_dict['name'] = "Orders delivery report"
        delivered_dict['orders'] = delivered_orders
        return delivered_dict

report.Report._reports[804] = ("Orders delivery report", Deliveries)
