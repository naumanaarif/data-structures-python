from linkedlist import LinkedList


class HashTable():
    """A Hash Table data structure that uses
    separate chaining method to prevent collision"""

    def __init__(self, max=100) -> None:
        self.MAX = max
        self.llist = [LinkedList() for _ in range(self.MAX)]

    def hash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key: int | str):
        i = self.hash(key)

        for item in self.llist[i]:
            if item[0] == key:
                return item[1]

    def __setitem__(self, key: int | str, value) -> None:
        i = self.hash(key)
        found = False

        for idx, item in enumerate(self.llist[i]):
            # If key already exists in the table
            if item[0] == key:
                # Update the value
                self.llist[i].insert((key, value), at=idx)
                self.llist[i].remove(self.llist[i][idx+1])
                found = True
                break

        if not found:
            self.llist[i].insert((key, value))


if __name__ == '__main__':
    table = HashTable(20)

    for i in range(20):
        key = f"key{i}"
        table[key] = i

    for row in table.llist:
        print(row)
