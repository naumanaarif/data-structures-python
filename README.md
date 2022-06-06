# Implementing Data Structures & Algorithms in Python

**Table of Contents**

- [Implementing Data Structures in Python](#implementing-data-structures-in-python)
- [Linked Lists](#linked-lists)
  - [Implementation](#implementation)
  - [Creating a LinkedList object](#creating-a-linkedlist-object)
  - [LinkedList Methods](#linkedlist-methods)
  - [Support for Built-in Python Functions](#support-for-built-in-python-functions)
- [Hash Tables](#hash-tables)
  - [Creating a HashTable object](#creating-a-hashtable-object)
- [Stacks](#stacks)
- [Queues](#queues)

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

To create an empty LinkedList object, do this:
```python
>>> a = LinkedList()
>>> a
[ > ]
```

We can also create a LinkedList from an iterable object such as list, tuple, set, etc.  
Example
```python
>>> a = LinkedList.linkedlist(["h", "e", "l", "l", "o"])
>>> a
[ h > e > l > l > o ]
```

## LinkedList Methods

The following methods can be used on LinkedList objects.

| Method     | Description                                              |
| ---------- | -------------------------------------------------------- |
| `insert()` | Adds an element at the specified position                |
| `pop()`    | Removes an element at the specified position             |
| `append()` | Adds an element at the end of the LinkedList             |
| `remove()` | Removes the first item with the specified value          |
| `clear()`  | Removes all the elements from a LinkedList               |
| `extend()` | Appends all the elements of a sequence to the LinkedList |

The `LinkedList` class also have a **classmethod**
* `linkedlist()` - Converts an iterable object into a `LinkedList` while preserving the order of items.  

Usage:
```python
>>> a = LinkedList.linkedlist([0, 1, 2, 3])
>>> a
[ 0 > 1 > 2 > 3 ]
```

## Support for Built-in Python Functions

A `LinkedList` object supports the following built-in Python functions.
* `print()`
* `str()`
* `len()`
* `iter()`
* `next()`

Therefore, `LinkedList` objects are **iterable** which means you can iterate over them using a `for` loop.  
e.g.
```python
>>> for item in linkedlist:
>>>    print(item)
```

`LinkedList` objects also support indexing using square bracket notation (just like a `list`).  
e.g.
```python 
>>> linkedlist[i] = "hello"
>>> print(linkedlist)
[ hello ]
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
