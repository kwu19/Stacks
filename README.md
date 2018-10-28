# Stacks, Queues, Dequeue, List

## Implement a stack using linked lists.
Replace the use of the Python `list` data type with write your own `Node` class, which we used to build a singly linked-list.

## Implement a queue using linked lists.
Replace the use of the Python `list` data type with write your own `Node` class, which we used to build a singly linked-list.

## Implement a deques using linked lists.
Replace the use of the Python `list` data type with write your own `Node` class, which we used to build a singly linked-list.

## Implement additional operations for the `UnorderedList` ADT.

Implement all parts of the `UnorderedList` and `Node` classes as described
in the textbook. You will use the definition of `Node` to implement a
singly-linked list inside the `UnorderedList` class.

**UnorderedList**:
Use the methods given in the book (using the textbook source code is allowed):
    
 * `__init__(self, init_data)`
 * `add(self, item)`
 * `remove(self, item)`
 * `search(self, item)`
 * `is_empty(self)`
 * `length(self)` (*Slides have it named as "size", the book more aptly calls it "length"*)

Additional methods you need to write yourself:
 * `append(self, item)`
 * `insert(self, pos, item)`
 * `index(self, item)`
 * `pop(self)`
 * `pop(self, pos)`
 * `print(self)` (*Print the items in the list*)

**Node**: Use the methods given in the book (using the textbook source code is allowed):
 * `__init__(self, init_data)`
 * `get_data(self)`
 * `get_next(self)`
 * `set_data(self, new_data)`
 * `set_next(self, new_next)`
 * `__repr__(self)` (*Instances of this class should propery represent itself if evaluated (test this using* `repr()` *function)
