# -*- coding: utf-8 -*-
print "How old are you?",
age = raw_input()
#注意在python3中 取消了raw_input
print "How tall are you?",
heigth = raw_input()
print "How much do you weigth?",
weigth = raw_input()
# 如果输入的是中文，那么就得将 %r 替换为 %s 就可以打印出中文
print "So, you're %s old,%r tall and %r heavy."% (age, heigth, weigth)