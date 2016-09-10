# -*- coding: utf-8 -*-

# Program name: 'IF' conditionals
# Programmer: Anartz Muxika
# Modify: 2016/09/10


# Add age (int) value and name to check with if
age = 18
name = 'Anartz'   #my name

if (age < 18):
    print '%s a minor for having %d years' % (name, age)
else:
    print '%s is of legal age for having %d years' % (name, age)

#Exercise extra: Initialize first variable with random and other variable too and compare. Values between 1,100

import random #import to use random function

first = random.randint(1, 100)
print 'First value: ' , first
second = random.randint(1, 100)
print 'Second value: ' , second
if first == second:
    print 'Equal values!!'
else:
    print 'Not equals values :('

