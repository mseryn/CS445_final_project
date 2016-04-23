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


class Report():
    _reports = {}

    def __init__(self):
        pass

    def get_report(self, report_id, start_date = None, end_date = None):
        # This takes the second argument from the tuple corresponding
        # to the ID in the report dictionary, stored as a constant in the
        # class, and makes an instance from the described subclass.
        # It then constructs the desired subclass using the date range
        # if present.
        if report_id in _reports:
            desired_report_class = self._reports[report_id][1]()
            if start_date and end_date:
                desired_report = desired_report_class(start_date, end_date)
                return desired_report.get_report_contents()
            else:
                desired_report = desired_report_class()
                return desired_report.get_report_contents()
        else:
            print("\nError: No such report ID")

    def get_all_reports(self):
        return Report._reports

from . import daily_today, daily_tomorrow, revenue, deliveries
