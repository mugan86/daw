# -*- coding: utf-8 -*-

# Program name:Asign values in differents type variables and print to practice with differents variables
# Programmer: Anartz Muxika
# Modify: 2016/09/10

"""
Example to use in this program
numeric (integer) = cars, drivers, passengers
numeric (float) = space_in_car
numeric (complex) = complex_num
chars = driver_name
Boolean = ten_year_experience
"""

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
cardpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
complex_num = 35 + 5j
driver_name = 'Anartz'
ten_year_experience = True


print 'There are' , cars , 'cars available.'
print 'There are only' , drivers, 'drivers available.'
print 'There will be' , cars_not_driven, 'empty cars today.'
print 'We can transport' , cardpool_capacity, 'people today.'
print 'We have' , passengers, 'to carpool today'
print 'We need to put about' , average_passengers_per_car, 'in each car'
print 'Complex num: ' , complex_num
print 'Driver name: ' , driver_name
print 'Ten years experience: ' , ten_year_experience