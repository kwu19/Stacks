#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:06:45 2018

@author: kefei
"""

class Node:
    """Node for a singly-linked list"""
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
    def __repr__(self):
        return "Node({0})".format(self.data)
    
    def __str__(self):
        #return "<node: {0} next: {1}>".format(self.data, id(self.next) if self.next else None)
        neigh = id(self.next) if self.next else None  # ternary operator
        return f"<node: {self.data} ({id(self)}) next: {neigh}>"
    
class UnorderedList:
    def __init__(self):
        self.head = None
        self.num = 0
        
    def is_empty(self):
        return self.head == None
        
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
            
        return count
    
    def search(self, item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                
        return found
    
    def remove(self, item):
        """Removes node from the linked list having a particular value
        
        NOTE: Assumes value is already in the list!
        """
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

            
            
            
   
    def append(self, item):
        """Add an item to the end of the list
        
        Note: It is different from add()!
        add() is adding the item to the first position of the list"""
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(temp)
        self.num += 1
        
    def insert(self, pos, item):
        """Insert an item at a given position. 
        
        The second argument is the index of the element before which to insert, 
        so a.insert(0, x) inserts at the front of the list, 
        and a.insert(len(a), x) is equivalent to a.append(x)."""
        current = self.head
        if pos > self.length() + 1:
            raise IndexError("Index out of range!")
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        elif pos == 0:
            temp.set_next(current)
            self.head = temp
        elif pos != 0:
            for i in range(pos - 1):
                current = current.get_next()
            temp.set_next(current.get_next())
            current.set_next(temp)
        self.num += 1

    def get_index(self, item):
        """Get the index of the given item
        
        It needs the item, and returns the index of the item"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
                index += 1
        if not found:
            print("No item %d in the list!" %(item))
        else:
            return index

    def pop(self, index=-1):
        """Remove the item at the given position in the list
        
        If no index is given, a.pop() removes last item in the list
        It returns the item and the list is modified"""
        current = self.head
        temp = None
        previous = None
        if index > self.length() - 1:
            raise IndexError("Index out of range!")
        if self.is_empty():
            raise IndexError("Pop from an empty list!")
        if index == -1:  # check if the index is given
            index = self.length() - 1
        if index == 0:
            self.head = current.get_next()
            previous = current.get_data()
            temp = current.get_data()
        else:
            for i in range(index):
                previous = current
                current = current.get_next()
            if previous is None:
                temp = self.head.get_data()
                current = ''
                self.head = None
            else:
                previous.set_next(current.get_next())
                temp = current.get_data()
        #print(current)
        self.num -= 1
        return current
          
    
    def print(self):
        """Print the items in the list"""
        current = self.head   # copy the address of the head node into node
        while current != None:
            print(current.get_data())
            current = current.get_next()
        
# Test your class by:

# * Inserting some items.
# * Printing list items.
# * Removing some items, then printing again.
# * Insert a few more items print the list items.
# * Other tests of your own design.

from random import randrange

ul = UnorderedList()

for i in range(5):
    ul.add(randrange(0, 10))
    
ul.print()

ul.insert(0, 7)
ul.print()

ul.remove(9)
ul.print()

ul.insert(5, 6)
ul.insert(6, 7)
ul.insert(5, 10)
ul.print()

ul.append(100)
ul.print()



