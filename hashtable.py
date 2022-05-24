from linkedlist import LinkedList


class HashTable():
    """Implements a Hash Table data structure"""

    def __init__(self, max=100) -> None:
        self.MAX = max
        self.arr = [LinkedList() for _ in range(self.MAX)]

if __name__ == '__main__':
    table = HashTable(10)
    for llist in table.arr:
        print(llist)
