class Node:
    """Represents a Node of a Singly Linked List"""

    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    """Represents a Singly Linked List data structure"""

    def __init__(self) -> None:
        self.head = None
        self.n = 0

    def insert(self, data: any, at: int = None) -> None:
        """Adds an element at the specified position

        If no position is specified, the element is added at the beginning.
        """
        
        # If index is provided
        if at:
            index = at
            if index < 0 or index >= len(self):
                raise IndexError("LinkedList index out of range")
            elif index == 0:
                node = Node(data, self.head)
                self.head = node
                return
            count = 0

            cursor = self.head
            while cursor:
                if count == index - 1:
                    node = Node(data, next=cursor.next)
                    cursor.next = node
                    break

                cursor = cursor.next
                count += 1
            return
        
        node = Node(data, self.head)
        self.head = node

    def append(self, data: any) -> None:
        """Adds an element at the end of the LinkedList"""

        if not self.head:
            self.head = Node(data)
            return
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = Node(data)

    def pop(self, index: int = None) -> None:
        """Removes an element at the specified position.
        
        If no index is specified, the last element is removed."""

        # If index is out of range
        if index < 0 or index >= len(self):
            raise IndexError("LinkedList index out of range")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        cursor = self.head
        while cursor:
            if count == index - 1:
                cursor.next = cursor.next.next
                break
            cursor = cursor.next
            count += 1

    def remove(self, value: any) -> None:
        """Removes the first item with the specified value.
        
        Raises ValueError if the value is not found or the LinkedList is empty."""
        
        # If LinkedList is empty
        if not len(self):
            raise ValueError("cannot remove from an empty LinkedList")

        # If only one item is present in the LinkedList
        if len(self) == 1 and self.head.data == value:
            self.head = None
            return

        # If the LinkedList has more than one elements
        index = 0
        cursor = self.head
        while cursor.next:
            # If value is found at the beginning
            if cursor.data == value:
                self.head = cursor.next
                return

            if cursor.next.data == value:
                # If value is at the end
                if index == len(self) - 1:
                    self.pop(index)
                    return
                # If value is somewhere in between
                cursor.next = cursor.next.next
                return

            cursor = cursor.next
            index += 1

        # If value not found in the LinkedList
        raise ValueError("value not found in the LinkedList")

    def clear(self) -> None:
        """Removes all the elements from a LinkedList"""
        if not self.head:
            return

        self.head = None

    def __setitem__(self, index: int, value: any) -> None:
        if index < 0 or index >= len(self):
            raise IndexError("index out of range")

        self.insert(value, at=index)

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("index out of range")

        count = 0
        cursor = self.head
        for _ in range(index + 1):
            if index == count:
                return cursor.data

            cursor = cursor.next
            count += 1

    def __len__(self) -> int:
        """Returns the length (number of items) of a LinkedList object"""
        len = 0

        if not self.head:
            return len

        cursor = self.head
        while cursor.next:
            cursor = cursor.next
            len += 1
        return len + 1

    def __str__(self) -> None:
        """Prints a LinkedList object."""
        if not self.head:
            return "[ > ]"

        cursor = self.head
        ll_str = "[ "
        while cursor:
            ll_str += str(cursor.data) + " > "
            cursor = cursor.next
        return ll_str.rstrip("> ") + " ]"

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n == len(self):
            self.n = 0
            raise StopIteration
        
        if not self.n:
            self.n += 1
            return self.head.data

        cursor = self.head
        for _ in range(self.n):
            cursor = cursor.next
        self.n += 1
        return cursor.data

    def __add__(self, other):
        x, y = self, other
        llist = LinkedList()
        for a in x:
            llist.append(a)
        for a in y:
            llist.append(a)
        return llist

    @classmethod
    def convert(cls, seq: list | tuple | set):
        """Converts a sequence (list, tuple or set) into a LinkedList"""
        llist = LinkedList()
        for data in seq:
            llist.insert(data)
        return llist


if __name__ == "__main__":
    llist = LinkedList.convert([1, 2, 3, 4, 5])
    print(llist)
    llist.clear()
    print(llist)
