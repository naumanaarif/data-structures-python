class Node:
    """Represents a node of the Singly Linked List"""

    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    """A Singly Linked List data structure"""

    def __init__(self) -> None:
        self.head = None

    def insert(self, data: any, at: int = None) -> None:
        """Insert an element at the beginning of a LinkedList"""
        # If index is provided
        if at:
            index = at

            if index < 0 or index >= len(self):
                raise IndexError("LinkedList index out of range")
            
            elif index == 0:
                node = Node(data, self.head)
                self.head = node
                return
            
            else:
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

    def push(self, data: any) -> None:
        """Push an element at the end of a LinkedList"""
        if not self.head:
            self.head = Node(data)
            return
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
        cursor.next = Node(data)

    def remove(self, index: int, value=None) -> None:
        """Removes a Node at the given index from a LinkedList object"""
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

    @classmethod
    def to_LinkedList(cls, seq: list):
        llist = LinkedList()
        for data in seq:
            llist.push(data)
        return llist


if __name__ == "__main__":
    llist = LinkedList()
    print(llist)
    llist.insert(1)
    llist.insert(2)
    llist.push(0)
    llist.insert([3, 4, 5])
    print(llist)
    print(len(llist))
    llist.insert("Abdullah", at=3)
    print(llist)
    llist.insert("Umar", at=2)
    print(llist)
    llist.push("Ali")
    print(llist)
