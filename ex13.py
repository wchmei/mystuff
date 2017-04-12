# -*- coding: utf-8 -*-
"""
此处只是简单的使用argv 和 raw_imput,后面再深入学习
"""
from sys import argv

script, first, second, third, fouth = argv


print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fouth variable is:", fouth

enter_something = raw_input("Plz enter first variable:")
print "wcm: %s" % enter_something 