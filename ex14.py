# -*- coding: utf-8 -*-
from sys import argv
# argv 和 raw_input 的区别 如果是参数是在用户执行命令时就要输入，那就是argv，
# 如果是在脚本运行过程中需要用户输入，那就使用raw_input()
# prompt: 该脚本的执行方法是 python ex14.py 王超美
script, user_name =  argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few quetions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "WHere do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alrigth, so you said %r about liking me.
You live in %r. not sure where that is.
And you have a %r computer. Nice.
""" % (likes ,lives, computer)