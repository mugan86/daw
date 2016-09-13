# -*- coding: utf-8 -*-
"""
Relational operators

http://pythonya.appspot.com/detalleconcepto?deta=Operadores%20relacionales

==  equal
!=  not equal
<   less-than
>   greather-than
<=  less-than-equal
>=  greater-than-equal

"""

import random

number1 = random.randint(1,10)
number2 = random.randint(1,10)

print('N1: %d / N2 %d' % (number1,number2))

equals = number1 == number2

print 'Values equals: ', equals

not_equals = number1 != number2

print 'Values NOT equals: ', not_equals

less_than_equal = number1 <= number2

print 'N1 Less than equal respect N2: ', less_than_equal

less_than = number1 < number2

print 'N1 Less than respect N2: ', less_than

greater_than_equal = number1 >= number2

print 'N1 greater than equal respect N2: ', greater_than_equal

greater_than = number1 > number2

print 'N1 Greater than respect N2: ', greater_than
