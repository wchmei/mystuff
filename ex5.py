# -*- coding: utf-8 -*-
'''
更多的变量和打印
'''
name = 'WCHM'
age = 30 # not a lie
heigth = 175 # CM
weigth = 65 # KG
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d CM tall."% heigth
print "He's %d KG heavy." %weigth
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky ,try to get it excatly right
print "if I add %d, %d, add %d I get %d." % (age, heigth, weigth, age + heigth + weigth)
# %r 就是一个非常有用的，它的含义是"不管什么都打印出来"