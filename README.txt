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


Dependencies: 
    Python 3
    pip3....... Python package manager
    Flask...... Python web framework
    pytest..... For running unit tests
    curl....... For running sample uses


General Instructions:

To install dependencies:
> ./setup.sh 

To run unit test suite:
> make unit_test

To run a local version of the API:
> make live
NOTE: This will consume a terminal, but it will also give valuable information
      as the service is interacted with.

API Instructions:
The file curl_example_commands.txt in examples/ has a list of example API
commands that can be executed via curl, a terminal web service.

While the service is live, in separate terminal, the following commands will
execute various sample API calls:

To add an item to the menu:
> make example_add_itemA_to_menu
> make example_add_itemB_to_menu

To get menu:
> make example_get_menu

To get an item from menu:
> make example_get_menu_item_0
> make example_get_menu_item_1

To modify the price of an item on the menu:
> make example_modify_price_item_0

To get surcharge:
> make example_get_surcharge

To modify surcharge:
> make example_modify_surcharge

To get an order:
> make example_get_all_orders
> make example_get_order_0
> make example_get_order_1
> make example_get_order_by_date

To set an order's status to "delivered":
> make example_set_order_0_status_to_delivered
> make example_set_order_1_status_to_delivered

To cancel an order:
> make example_cancel_order_0

To get a report:
> make example_reports_list
> make example_revenue_report
> make example_report_deliveries_today
> make example_report_deliveries_tomorrow

To get a customer:
> make example_get_all_customers
> make example_get_customer_0
> make example_get_customer_1
> make example_get_customer_by_name



Additional Information:

memo_final_project_mdooley1.pdf contains statistics and required commentary.

Please note - a build is not necessary in Python.

To pull Melanie Dooley's assignment repository:
(NOTE: requires permission, repository is private)
> sudo apt-get install git
> git clone http://github.com/mseryn/CS445_Object_Oriented_Design.git



This code is licensed under the GNU V.3 General Use license.
See 'LICENSE' for full details.
