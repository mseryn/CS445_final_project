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
from . import deliveries

class Revenue(deliveries.Deliveries):

    def __init__(self, start_date, end_date):
        super().__init__(start_date, end_date)

    def get_report_contents(self):
        # Parameters for revenue report
        revenue_report_dict = {'id'               : 803,
                               'name'             : 'Revenue report',
                               'orders_placed'    : 0, 
                               'orders_cancelled' : 0,
                               'orders_open'      : 0, 
                               'food_revenue'     : 0.0,
                               'surcharge_revenue': 0.0,
                               }

        for individual_order in self._all_orders:
            revenue_report_dict['orders_placed'] += 1
            status = individual_order.get_delivery_status()
            if status == "cancelled":
                revenue_report_dict['orders_cancelled'] += 1
            elif status == "open":
                revenue_report_dict['orders_open'] += 1
            elif status == "delivered":
                revenue_report_dict['food_revenue'] += individual_order.get_total_item_cost()
                revenue_report_dict['surcharge_revenue'] += \
                    individual_order.get_surcharge_considering_day()

        return revenue_report_dict


report.Report._reports[803] = ("Revenue report", Revenue)
