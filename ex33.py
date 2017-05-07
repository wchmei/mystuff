# -*- coding: utf-8 -*- 
'''
1. 尽量少用while循环，大部分时候for循环是更好的选择
2. 重复检查你的while语句，确定你测试的布尔表达式最终会变成False
3. 如果不确定，就是while循环的结尾打印出你要测试的值。看看它的变化
'''
i = 0 
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num