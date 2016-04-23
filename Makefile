default: all
all: 

test:
	python3 src/Table_Lamp.py

unit_test:
	py.test src/unit_tests/lightbulb_test.py
	py.test src/unit_tests/button_test.py
	py.test src/unit_tests/single_push_button_test.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} \; &> /dev/null
