# CSE 143, Winter 2010, Marty Stepp
#
# An ArrayIntList stores a sequence of values.
# Basically it's just a useless wrapper around a list, but we are giving it to
# you as something to base your SortedIntList on.

class ArrayIntList:
    # Constructs a new list
    def __init__(self):
        self.elementData = []
    
    # called when user deletes an item from the list with 'del' keyword
    def __delitem__(self, index):
        del self.elementData[index]
    
    # called when user gets an item from the list with []
    def __getitem__(self, index):
        return self.elementData[index]
    
    # called when user loops over the elements of the list (for ... in)
    def __iter__(self):
        return self.elementData.__iter__()
    
    # called when user asks for the len() of the list
    def __len__(self):
        return len(self.elementData)
    
    # called when user prints the list or calls str() on it
    def __str__(self):
        return str(self.elementData)
    
    # adds an element to the end of the list
    def append(self, value):
        self.elementData.append(value)
    
    # removes the given element value from the list
    def remove(self, value):
        self.elementData.remove(value)
