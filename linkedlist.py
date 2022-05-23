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
        """Insert element(s) at the beginning of a LinkedList

        Supported Datatypes: int, float, bool, str, list, tuple, set"""
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

        # If data is iterable
        if type(data) in [list, tuple, set]:
            for item in data:
                node = Node(item, self.head)
                self.head = node
            return

        # If data is not iterable
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
        """Removes the Node at the specified position.
        
        If no index is specified, it removes the last Node from the LinkedList.
        """
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
        """Removes the first Node from the list whose value is equal to 'value'.
        
        Raises ValueError if the value is not present or the LinkedList is empty."""
        # If LinkedList is empty
        if not len(self):
            raise ValueError("cannot remove from an empty LinkedList")

        # If a single item is present in LinkedList
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
        """Print a LinkedList object."""
        if not self.head:
            return "[ > ]"

        cursor = self.head
        ll_str = "[ "
        while cursor:
            ll_str += str(cursor.data) + " > "
            cursor = cursor.next
        return ll_str + "]"

# TODO: Add support for iteration

    def __iter__(self):
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

    @classmethod
    def to_LinkedList(cls, seq: list):
        llist = LinkedList()
        for data in seq:
            llist.push(data)
        return llist


if __name__ == "__main__":
    llist = LinkedList()
    print(llist)
    for i in range(1, 11):
        llist.append(i)
    print(llist)
