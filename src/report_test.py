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

# Testing Report

import report

# Testing get all reports

def test_report_get_all_reports():
    comparison = {801: ("Orders to deliver today", report.undelivered.daily_today),
                  802: ("Orders to deliver tomorrow", report.undelivered.daily_tomorrow),
                  803: ("Revenue report", report.delivered.revenue),
                  804: ("Orders delivery report", report.delivered.deliveries) }

    test_report = report.Report()
    assert((test_report.get_report == comparison), "get all reports in report not functioning correctly")


