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
    def __init__(self, last_name, first_name, email, phone_number):
        self._last_name = str(last_name)
        self._first_name = str(first_name)
        self._email = str(email)
        self._phone_number = 5555555555
        if type(phone_number) is int:
            if phone_number > 999999999 and phone_number < 10000000000:
                # This means it's a 10-digit number
                self._phone_number = phone_number
        else:
            print("\nError: phone number must be 9-digit integer value.  Setting to 5555555555.")

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def set_last_name(self, new_last_name):
        self._last_name = str(new_last_name)

    def set_first_name(self, new_first_name):
        self._first_name = str(new_first_name)

    def set_email(self, new_email):
        self._email = str(new_email)

    def set_phone_number(self, new_phone_number):
        if type(new_phone_number) is int:
            if new_phone_number > 999999999 and new_phone_number < 10000000000:
                # This means it's a 10-digit number
                self._new_phone_number = new_phone_number
        else:
            print("\nError: phone number must be 9-digit integer value.  No change made.")
