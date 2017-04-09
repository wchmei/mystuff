# -*- coding: utf-8 -*-
'''
更多的变量和打印
'''
my_name = 'WCHM'
my_age = 30 # not a lie
my_heigth = 175 # CM
my_weigth = 65 # KG
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d CM tall."% my_heigth
print "He's %d KG heavy." %my_weigth
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky ,try to get it excatly right
print "if I add %d, %d, add %d I get %d." % (my_age, my_heigth, my_weigth, my_age + my_heigth + my_weigth)
# %r 就是一个非常有用的，它的含义是"不管什么都打印出来"