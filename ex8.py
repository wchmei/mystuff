# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "tow", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up rigth.",
	"But it didn't sing.",
	"So I said goodnight")