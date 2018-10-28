#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:56:02 2018

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

class Stack:
    """Stack class using python list data type"""
    def __init__(self):
        self.head = None
        self.num = 0
        
    def is_empty(self):
        """Check if the stack has element in it or not"""
        return self.num == 0
    
    def push(self, item):
        """Add a new item to the top of the stack and returns nothing """
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(temp)
        self.num += 1

    def pop(self):
        """Removes the top item from the stack
    
        it needs no parameters, returns the item and the stack is modified"""
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

    def peek(self):
        """Returns the top item from the stack but does not remove it"""
        current = self.head
        if self.is_empty():
            raise IndexError("Peek from an empty stack!")
        else:
            for i in range(self.size() - 1):
                current = current.get_next()
            current = current.get_data()
        return current

    def size(self):
        """Returns the number of items on the stack"""
        return self.num
    
# Test
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))

s = Stack()
s.push(3)
s.push(4)
s.peek()

s.pop()

s.pop()
