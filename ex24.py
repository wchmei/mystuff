# -*- coding: utf-8 -*-
print "Let's practice everything."
print 'You\'d need know \'bout escapes with \\ that do \n newlines and \t tabs'

pome = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
not comprehend passion from intution
and requires and explanation
\n\t\twhere there is none.
"""
print "----------"
print pome
print "----------"

five = 10 - 2 + 3 -6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting ponit of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

start_point = start_point  / 10

print "We can also do that this way:"
# 函数返回三个结果可以直接调用
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)