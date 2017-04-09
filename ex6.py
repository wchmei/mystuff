# -*- coding: utf-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said:%r." % x
print "I also said:'%s' ." % y

hilarious = False
#使用 %r 的时候可以用例子里情况，在后面打印出来，测试将 %r 替换为 %s
joke_evaluation = "Isn't that joke so funny?! %r" 
#测试也是可行的
joke_evaluation1 = "Isn't that joke so funny?! %s"

print joke_evaluation % hilarious
print joke_evaluation1 % hilarious

w = "This is the left side of..."
e = "a string with a rigth side."

print w + e