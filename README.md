# Data Structures

Data structure is a storage that is used to store and organize data. It is a way of arranging data on a computer so that it can be accessed and updated efficiently.

## Table of Contents

* [Linked Lists](https://github.com/naumanaarif/data-structures-python#linked-lists)
* [Hash Tables](https://github.com/naumanaarif/data-structures-python#hash-tables)
* [Stacks](https://github.com/naumanaarif/data-structures-python#stacks)
* [Queues](https://github.com/naumanaarif/data-structures-python#queues) (in progress)

---

# Linked Lists

A linked list is a linear data structure that includes a series of connected *nodes*, where each node stores the data and the address of the next node.

## Implementation

First, create a class that represents a `Node` of a linked list.
```python
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
```

Then create another class that represents a `LinkedList`.
```python
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.n = 0
    ...
```

## Creating a LinkedList object

To create a LinkedList object, do this:
```python
linkedlist = LinkedList()
```

## Methods

The following methods can be used on LinkedList objects.

| Method        | Description                                                |
| ------        | -----------                                                |
| `append()`    | Adds an element at the end of the LinkedList               |
| `clear()`     | Removes all the elements from a LinkedList                 |
| `insert()`    | Adds an element at the specified position                  |
| `pop()`       | Removes an element at the specified position               |
| `remove()`    | Removes the first item with the specified value            |
| `convert()`   | A classmethod that converts a sequence to a `LinkedList` |

## Support for Built-in Python Functions

A `LinkedList` object supports the following built-in Python functions.
* `print()`
* `str()`
* `len()`
* `iter()`
* `next()`

Moreover, `LinkedList` objects are **iterable** which means you can iterate over it using a `for` loop.  
e.g.
```python
for item in linkedlist:
    print(item)
```

`LinkedList` objects also support indexing using square bracket notation (just like a `list`).  
e.g.
```python 
linkedlist[i] = "hello"
print(linkedlist[i])
```

You can also add two `LinkedList` objects together using the '`+`' operator.  
e.g.
```python 
result = a + b  # where 'a' and 'b' are LinkedList objects
```

---

# Hash Tables

The Hash table data structure stores elements in key-value pairs where  
* **key** - unique integer that is used for indexing the values  
* **value** - data that are associated with keys

## Creating a HashTable object

You can create a HashTable object like this
```python
table = HashTable()
```

# Stacks

# Queues
