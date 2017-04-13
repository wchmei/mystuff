# -*- coding: utf-8 -*-
from sys import argv
# 传入文件名
script, filename = argv

print "We're goning to erase %r." % filename
print "If you don't want that, hit CRTL-C."
print "If you want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print ("Truncating the file.Goodbye!")
# 获取文件到size个字节，默认是截取到文件指针当前位置
target.truncate()

print "Now I'm goning to ask you for thress lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()