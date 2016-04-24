default: all
all: 

live:
	cd src/
	PYTHONPATH=src/. ./src/DelectableREST/delectablerest.py 

unit_test:
	py.test src/unit_tests/customer_test.py
	py.test src/unit_tests/delectable_rest_api_test.py
	py.test src/unit_tests/item_test.py
	py.test src/unit_tests/menu_test.py
	py.test src/unit_tests/order_test.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} \; &> /dev/null


example_add_itemA_to_menu:
	curl -i -H "Content-Type: application/json" -X PUT -d '{"name": "Lasagna", "price_per_person": 2.49, "minimum_order": 6, "categories": [{"name": "organic"}, {"name": "vegetarian"}]}' http://localhost:5000/delectable/admin/menu

example_add_itemB_to_menu:
	curl -i -H "Content-Type: application/json" -X PUT -d '{"name": "Salad", "price_per_person": 5.5, "minimum_order": 3, "categories": [{"name": "vegetarian"}]}' http://localhost:5000/delectable/admin/menu
	
example_get_menu:
	curl -i http://localhost:5000/delectable/menu

example_get_menu_item_0:
	curl -i http://localhost:5000/delectable/menu/0

example_get_menu_item_1:
	curl -i http://localhost:5000/delectable/menu/1

example_add_orderA:
	curl -i -H "Content-Type: application/json" -X PUT -d '{"delivery_date": "20160301", "delivery_address": "10 West 31st ST, Chicago IL 60616","personal_info": {"name": "Virgil B","email": "virgil@example.com","phone": "312-456-7890"},"note": "Room SB-214","order_detail": [{"id": 1,"count": 8}, {"id": 0,"count": 7}]}' http://localhost:5000/delectable/order

example_add_orderB:
	curl -i -H "Content-Type: application/json" -X PUT -d '{"delivery_date": "20160423", "delivery_address": "3501 S State St, Chicago IL 60616","personal_info": {"name": "Sample Student","email": "student@hawk.iit.edu","phone": "111-222-3456"},"note": "Please call ahead, the doors will be locked","order_detail": [{"id": 1,"count": 10}, {"id": 0,"count": 15}]}' http://localhost:5000/delectable/order

example_get_all_orders:
	http://localhost:5000/delectable/order

example_get_order_0:
	curl -i http://localhost:5000/delectable/order/0

example_get_order_1:
	curl -i http://localhost:5000/delectable/order/1

example_get_order_by_date:
	curl -i http://localhost:5000/delectable/order?date=20160423

example_cancel_order_0:
	curl -i -X POST -d '{"id": 0}' -H "Content-Type: application/json" http://localhost:5000/delectable/order/cancel/0

example_get_all_customers:
	curl -i http://localhost:5000/delectable/customer

example_get_customer_0:
	curl -i http://localhost:5000/delectable/customer/0

example_get_customer_1:
	curl -i http://localhost:5000/delectable/customer/1

example_get_customer_by_name:
	curl -i -X GET -d '{"key": "Student"}' http://localhost:5000/delectable/customer -H "Content-Type: application/json"

example_reports_list:
	curl -i http://localhost:5000/delectable/report

example_revenue_report:
	curl -i http://localhost:5000/delectable/report/803

example_report_deliveries_today:
	curl -i http://localhost:5000/delectable/report/801

example_report_deliveries_tomorrow:
	curl -i http://localhost:5000/delectable/report/802

example_modify_price_item_0:
	curl -i -X POST -d '{"id": 0, "price_per_person": 3.99}' http://localhost:5000/delectable/admin/menu/0  -H "Content-Type: application/json"

example_get_surcharge:
	curl -i http://localhost:5000/delectable/admin/surcharge

example_modify_surcharge:
	curl -i -X POST -d '{"surcharge": 15.25}' http://localhost:5000/delectable/admin/surcharge  -H "Content-Type: application/json"

example_set_order_0_status_to_delivered:
	curl -i -X POST -d '{"id": 0}' http://localhost:5000/delectable/admin/delivery/0  -H "Content-Type: application/json"

example_set_order_1_status_to_delivered:
	curl -i -X POST -d '{"id": 1}' http://localhost:5000/delectable/admin/delivery/1  -H "Content-Type: application/json"
