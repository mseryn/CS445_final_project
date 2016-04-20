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

class Revenue(Delivered):

    def __init__(self, start_date, end_date):
        super(self, start_date, end_date)

    def get_report_contents(self):
        total_revenue
        for individual_order in self._orders_for_dates:
            total_revenue += individual_order.get_total_cost()
        return total_revenue
