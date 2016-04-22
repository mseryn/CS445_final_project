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
from . import undelivered

import datetime

class DailyTomorrow(undelivered.Undelivered):
    def __init__(self):
        super(self, (datetime.today() + datetime.timedelta(1)))

report.Report._reports[802] = ("Orders to deliver tomorrow", DailyTomorrow)
