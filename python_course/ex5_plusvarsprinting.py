# -*- coding: utf-8 -*-

# Program name:Example to show how to use print formatters and use variables
# Programmer: Anartz Muxika
# Modify: 2016/09/10

my_name = 'Anartz'
my_age = 30
my_height = 1.85 #metres
my_weight = 71 #kgs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print '=========================================================================='
print 'EXERCISE 5: Example to show how to use print formatters and use variables'
print '=========================================================================='
print 'Let\'s talk about %s' % my_name
print 'He\'s %r metres tall.' % my_height
print 'He\'s %d kgs heavy.' % my_weight
print 'Actually that\'s not too heavy.'
print 'He\'s got %s eyes and %s hair.' % (my_eyes, my_hair)
print 'His teeth are usually %s depending on the coffee.' % my_teeth
#this line is trickly, try to get in exactly right
print 'If I add %d, %r, and %d I get %d.' % (
    my_age, my_height, my_weight, my_age + my_height+my_weight)