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
        
        # Insert at the given position
        if at:
            index = at
            if index < 0 or index >= len(self):
                raise IndexError("LinkedList index out of range")
            elif index == 0:
                node = Node(data, next=self.head)
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
        
        # Insert at the beginning
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

    def extend(self, seq: list | tuple | set) -> None:
        """Appends all elements of a sequence to a LinkedList"""
        for item in seq:
            self.append(item)

    def pop(self, index: int = None) -> any:
        """Removes an element at the specified position.
        
        If no index is specified, the last element is removed."""

        if not self.head:
            return

        if index:
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
                    data = cursor.next.data
                    cursor.next = cursor.next.next
                    return data
                cursor = cursor.next
                count += 1

        # Remove the last element
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data

        cursor = self.head
        while cursor.next:
            if not cursor.next.next:
                data = cursor.next.data
                cursor.next = None
                return data
            cursor = cursor.next

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
        return self

    def __setitem__(self, index: int, value: any) -> None:
        index = index if index > 0 else len(self) + index

        if index < 0 or index >= len(self):
            raise IndexError("linked list assignment index out of range")

        self.insert(value, at=index)

    def __getitem__(self, index: int | slice):
        # Get value at the index
        if isinstance(index, int):
            index = index if index >= 0 else len(self) + index

            if index >= len(self):
                raise IndexError("index out of range")

            for idx, item in enumerate(self):
                if idx == index:
                    return item
        # Get a slice
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            sliced_llist = LinkedList.linkedlist([self[i] for i in range(start, stop, step)])
            return sliced_llist
        else:
            raise TypeError("index must be an int or slice")

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
        """Represents a LinkedList object as a string."""
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
    def linkedlist(cls, iterable=None):
        """Creates a LinkedList from an iterable object. e.g. `LinkedList.linkedlist([1, 2, 3])`
        
        Returns an empty LinkedList if no argument is passed."""
        llist = cls()

        if iterable:
            for data in iterable[::-1]:
                llist.insert(data)

        return llist


if __name__ == "__main__":
    a = LinkedList.linkedlist([1,2,3])
    print(a)
    print(a[0], a[1], a[2])
    print(a[-1], a[-2], a[-3])
