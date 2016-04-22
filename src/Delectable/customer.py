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

class Customer():
    _customer_id_counter = 0
    _all_customers = []

    def __init__(self, last_name, first_name, email, phone_number):
        self._last_name = str(last_name)
        self._first_name = str(first_name)
        self._email = str(email)
        self._phone_number = 5555555555
        self._phone_number = phone_number

        self._customer_id = -1
        for customer in Customer._all_customers:
            if self == customer:
                self._customer_id = customer.get_id()
        if self._customer_id == -1:
            self._customer_id = self._customer_id_counter
            Customer._customer_id_counter += 1
            self._all_customers.append(self)

    @staticmethod
    def get_all_customers():
        return Customer._all_customers

    def get_customer_id(self):
        return self._customer_id

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, new_last_name):
        self._last_name = str(new_last_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, new_first_name):
        self._first_name = str(new_first_name)

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = str(new_email)

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, new_phone_number):
        self._new_phone_number = new_phone_number

    def __eq__(self, other_customer):
        if ((self._last_name == other_customer.get_last_name())
        and (self._first_name == other_customer.get_last_name())
        and (self._email == other_customer.get_email())
        and (self._phone_number == other_customer.get_phone_number())):
            return True
        else:
            return False
