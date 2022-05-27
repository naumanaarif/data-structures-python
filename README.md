# Data Structures

Implementing Data Structures in Python

## Table of Contents

* Linked Lists
* Hash Tables
* Stacks
* Queues (in progress)

# Linked Lists

A linked list is a linear data structure that includes a series of connected *nodes*, where each node stores the data and the address of the next node.

## Creating a LinkedList object

To create a LinkedList, do this:

    linkedlist = LinkedList()

<!-- ---- -->

## Methods

The following methods can be used on LinkedList objects.

| Method | Description |
| ------ | ----------- |
| `append()` | Adds an element at the end of the LinkedList |
| `clear()` | Removes all the elements from a LinkedList |
| `insert()` | Adds an element at the specified position |
| `pop()` | Removes an element at the specified position |
| `remove()` | Removes the first item with the specified value |

<!-- ---- -->

## Support for Built-in Python Functions

A LinkedList object supports the following built-in Python functions.
* `print()`
* `len()`
* `str()`

Moreover, each LinkedList object is **iterable** which means you can iterate over it using a `for` loop.  
For example,

    for item in linkedlist:
    print(item)
