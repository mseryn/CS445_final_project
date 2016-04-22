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

class Address():
    def __init__(self, street, city, state, zipcode):
        self._street = street
        self._city = city
        self._state = state
        if type(zipcode) is int:
            self._zipcode = zipcode

    def get_street(self):
        return self._street

    def get_city(self):
        return self._city

    def get_state(self):
        return self._state

    def get_zipcode(self):
        return self._zipcode
