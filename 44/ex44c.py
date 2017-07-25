class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEAFORE PARENT altered()"
        super(Child, self).altered()#super 访问Parent的类
        print "CHILD, ALTER PARNET altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()