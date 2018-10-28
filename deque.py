#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:05:10 2018

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

class Deque:
    """Deque class using python list data type"""
    def __init__(self):
        self.head = None
        self.num = 0
        
    def is_empty(self):
        """Check if the stack has element in it or not"""
        return self.num == 0
    
    def add_front(self, item):
        """Adds a new item to the front of the deque
        
        it needs the item and returns nothing"""
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(temp)
        self.num += 1
        
    def add_rear(self, item):
        """Adds a new item to the rear of the deque
        
        it needs the item and returns nothing"""
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        else:
            temp.set_next(current)
            self.head = temp
        self.num += 1
        
    def remove_front(self):
        """Removes the front item from the deque 
        
        it needs no parameters and returns the item; the deque is modified """
        current = self.head
        temp = None
        previous = None
        if self.is_empty():
            raise IndexError("Remove element from an empty deque!")
        else:
            for i in range(self.size() - 1):
                previous = current
                current = current.get_next()
            if previous is None:
                temp = self.head.get_data()
                current = ''
                self.head = None
            else:
                previous.set_next(None)
                temp = current.get_data()
        self.num -= 1
        return temp

    def remove_rear(self):
        """Removes the rear item from the deque 
        
        it needs no parameters and returns the item; the deque is modified """
        current = self.head
        previous = None
        if self.is_empty():
            raise IndexError("Remove element from an empty deque!")
        else:
            self.head = current.get_next()
            previous = current.get_data()
            self.num -= 1
        #print(previous)
        return previous

    def size(self):
        """returns the number of items in the deque

        it needs no parameters and returns an integer"""
        return self.num
    
    def print(self):  # this method is just for check use
        """Print the elements in deque"""
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)
        
        
# test
def palchecker(aString):
    """
    Test `Queue` class by running the **palindrome checker**
    """
    chardeque = Deque()

    for ch in aString:
        chardeque.add_rear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        #chardeque.print()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

# check if all methods work
d = Deque()
d.add_front(1)
d.add_rear(2)
d.add_rear(3)
d.print()

d.remove_front()
d.print()

d.remove_rear()
d.print()

d.add_front(1)
d.add_front(2)
d.add_front(3)
d.add_front(4)
d.add_front(5)
d.add_front(10)
d.print()
for i in range(0,6):
    d.remove_rear()
    d.print()
    
i = len([frozenset([1]),frozenset([])])
i+=1
i

