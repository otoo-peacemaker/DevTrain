# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 04:10:20 2020

@author: Kwesi_Welbred
----------------------------------------------------------------------
String concatenation means add strings together.
Use the + character to add a variable to another variable:
"""

"Merge variable x with variable y into variable z:"
x = "Python is "
y = "awesome"
z =  x + y
print(z)

"To add a space between them, add a " ": "
a = "Hello"
b = "World"
c = a + " " + b
print(c)

"For numbers, the + character works as a mathematical operator:"
x = 5
y = 10
print(x + y)

"If you try to combine a string and a number, Python will give you an error: "
x = 5
y = "John"
print(x + y)