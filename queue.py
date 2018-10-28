#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:03:30 2018

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

    
class Queue:
    """Queue class using python list data type"""
    def __init__(self):
        self.head = None
        self.num = 0

    def is_empty(self):
        """Check if the stack has element in it or not"""
        return self.num == 0
        
    def enqueue(self, item):
        """Add a new item to the rear of the queue
        
        it needs the item and returns nothing"""
        temp = Node(item)
        current = self.head
        if current is None:
            self.head = temp
        else:
            temp.set_next(current)
            self.head = temp
        self.num += 1
        
    def dequeue(self):
        """Removes the front item from the queue
        
        it needs no parameters, returns the item and the queue is modified"""
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
            
    def size(self):
        """Returns the number of items on the queue"""
        return self.num
    
    def print(self):  # this method is just for check use
        """Print the elements in queue"""
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)
        
# test
def hotPotato(namelist, num):
    """
    Test `Queue` class by running the **hot potato simulation**.
    """
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

        return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.print()

q.dequeue()
q.print()

q.dequeue()
q.print()