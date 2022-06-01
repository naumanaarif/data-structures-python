import random


class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data) -> None:
        # If already exists
        if data == self.data:
            return
        
        # Add to the left
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        # Add to the right
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
    
    def inorder_traversal(self) -> list:
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
        if not self.left:
            return self.data

        cursor = self.left
        while cursor:
            if not cursor.left:
                return cursor.data
            cursor = cursor.left

    def max(self):
        if not self.right:
            return self.data

        cursor = self.right
        while cursor:
            if not cursor.right:
                return cursor.data
            cursor = cursor.right

    def total(self) -> int:
        return sum(self.inorder_traversal())

    ...


def build_tree(seq):
    root = BSTNode(seq[0])

    for element in seq[1:]:
        root.add_child(element)

    return root


if __name__ == '__main__':
    numbers = [random.randint(1, 5) for _ in range(5)]
    print(numbers)
    tree = build_tree(numbers)
    # inorder_result = tree.inorder_traversal()
    print(tree.inorder_traversal())
    # print(tree.search(7))
    print("MIN:", tree.min())
    print("MAX:", tree.max())
    print("SUM:", tree.total())
