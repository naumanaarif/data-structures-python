from collections import deque


class Stack:
    """A linear data structure that follows the Last In First Out rule"""

    def __init__(self) -> None:
        self.container = deque()

    def push(self, value) -> None:
        """Adds an element at the top of the Stack"""
        self.container.append(value)

    def pop(self) -> any:
        """Removes the last added (topmost) element from the Stack"""
        return self.container.pop()

    def peek(self) -> any:
        """Returns an element from the top of the Stack"""
        return self.container[-1]

    def is_empty(self) -> bool:
        """Returns True if the Stack is empty, else returns False"""
        return not len(self.container)

    def size(self) -> int:
        """Returns the size (no. of items) of the Stack"""
        return len(self.container)

    def __str__(self) -> str:
        return str(self.container)


if __name__ == '__main__':
    stack = Stack()
