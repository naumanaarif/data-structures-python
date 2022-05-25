from linkedlist import LinkedList


class HashTable():
    """Implements a Hash Table data structure"""

    def __init__(self, max=100) -> None:
        self.MAX = max
        self.llist = [LinkedList() for _ in range(self.MAX)]

    def hash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key: int | str):
        ...

    def __setitem__(self, key: int | str, value):
        ...


if __name__ == '__main__':
    table = HashTable(10)

    table.add("AbuBakr", 123)
    table.add("Umar", 124)
    table.add("Umar", 127)
    table.add("Uthman", 125)
    table.add("Ali", 126)

    for row in table.llist:
        print(row)

    print(table)
