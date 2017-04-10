# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()
#注意在python3中 取消了raw_input
print "How tall are you?",
heigth = raw_input()
print "How much do you weigth?",
weigth = raw_input()

print "So, you're %s old,%r tall and %r heavy."% (age, heigth, weigth)