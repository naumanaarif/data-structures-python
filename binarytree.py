import random


class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, value) -> None:
        """Adds an element in a Binary Tree"""
        # If already exists
        if value == self.data:
            return
        
        # Add to the left
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = BSTNode(value)
        # Add to the right
        if value > self.data:
            if self.right:
                self.right.add(value)
            else:
                self.right = BSTNode(value)
    
    def remove(self, value):
        """Removes first element with the value from the Binary Tree"""
        if value < self.data:
            if self.left:
                self.left.remove(value)
        
        elif value > self.data:
            if self.right:
                self.right.remove(value)

        else:
            if not self.left and not self.right:
                return
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_value = self.right.min()
            self.data = min_value
            self.right = self.right.remove(min_value)
        
        return self

    def inorder_traversal(self) -> list:
        """Returns a sorted list of elements from Binary Tree"""
        elements = []

        # Traverse left
        if self.left:
            elements += self.left.inorder_traversal()
        # Base node
        elements.append(self.data)
        # Traverse right
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, data):
        """Search the value in a Binary Tree

        If found, returns True, else returns False"""
        if data == self.data:
            return True

        # Search the left half
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        # Search the right half
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    
    def min(self):
        """Returns the lowest value from a Binary Tree"""
        if not self.left:
            return self.data

        return self.left.min()

    def max(self):
        """Returns the highest value from a Binary Tree"""
        if not self.right:
            return self.data

        return self.right.max()

    def total(self) -> int:
        """Returns the sum of all the values in a Binary Tree"""
        return sum(self.inorder_traversal())

    ...


def build_tree(seq):
    root = BSTNode(seq[0])

    for element in seq[1:]:
        root.add(element)

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    
    tree = build_tree(numbers)
    print(tree.inorder_traversal())

    tree.remove(20)
    print(tree.inorder_traversal())

