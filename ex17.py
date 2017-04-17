# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too,how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()
print "The input file is %d  bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue,CRTL-C to abort."
raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)
open(to_file, 'w').write(indata)
print "Altigth, all done."

# 使用了 in_file = open(from_file).read() 就可以不用在最后关闭文件
# out_file.close()
# in_file.close()