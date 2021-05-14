# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:02:35 2020

@author: Kwesi_Welbred
"""

"""
List is a collection of items of any kind(thus, it accepts any type of data).
The items are enclosed by square blacket and assgned to any variable name.
The elements in the list are accessed by indexing either by negative or positive index, depending the
element you want to access.

Programmers mostly use the negative indexing if they want to select a particular element
from the end of the list.

Follow the Tutorials as we begin. 
"""

myList = [2,5,6,'Kwesi','Yaw','Yaa','Agness']# declare the list
myList[0] # access the first item
myList[-1] # access the last but one item

#ask python to show you which built-in operational function can be perform on the list

dir(myList)
"""
The output

 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
"""
help(myList.sort)# Help on built-in function sort:
len(myList)#the length of the list




"""
slicing, the process of selecting a particular group of items in a particular range
use colon to slice 
eg myList[:]. this means select everything from the begining to the end.
eg2.
"""
myList[0 :-1]
myList[-3:-1]
myList[:-1]


"Loop through a List using for loop"
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

"""Check if Item Exists: "To determine if a specified item is present in a list use the in keyword:
Check if "apple" is present in the list:
"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


"""
There are several ways to join, or concatenate, two or more lists in Python
One of the easiest ways are by using the + operator.
"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

"""
Another way to join two lists are by appending all the items from list2 into list1, one by one:
Append list2 into list1 Or you can use the extend() method, which purpose is to add elements from one list to another list:
"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

"Use the extend() method to add list2 at the end of list1:"
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


"""
The list() Constructor
It is also possible to use the list() constructor to make a new list.
Example
Using the list() constructor to make a List: 

"""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
