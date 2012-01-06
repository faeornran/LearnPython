# CSE 143, Winter 2010, Marty Stepp
#
# A basic testing program for SortedIntList objects.
# Expected output at bottom.

from sortedintlist import *

mylist = SortedIntList()
print(mylist)

mylist.append(42)
print(mylist)

mylist.append(11)
print(mylist)

mylist.append(68)
print(mylist)

mylist.append(-3)
print(mylist)

mylist.append(25)
print(mylist)

mylist.append(42)
mylist.append(42)
mylist.append(-3)
print(mylist)

mylist.set_unique(True)
print("")
print("After setting unique to true:")
print(mylist)



mylist2 = SortedIntList(True)
mylist2.append(42)
mylist2.append(17)
mylist2.append(42)
mylist2.append(42)
mylist2.append(17)
mylist2.append(-3)
print()
print("With constructor unique parameter set to true:")
print(mylist2)
print()
print("Testing max and min")
print("max: ", mylist2.max())
print("min: ", mylist2.min())

# Expected output:
# S:[]
# S:[42]
# S:[11, 42]
# S:[11, 42, 68]
# S:[-3, 11, 42, 68]
# S:[-3, 11, 25, 42, 68]
# S:[-3, -3, 11, 25, 42, 42, 42, 68]
# 
# After setting unique to true:
# S:[-3, 11, 25, 42, 68]U
# 
# With constructor unique parameter set to true:
# S:[-3, 17, 42]U

# Testing max and min
# max: 42
# min: -3
