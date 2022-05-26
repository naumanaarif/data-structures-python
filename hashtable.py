from linkedlist import LinkedList


class HashTable():
    """A Hash Table data structure that uses
    separate chaining method to prevent collision"""

    def __init__(self, max=100) -> None:
        self.MAX = max
        self.llist = [LinkedList() for _ in range(self.MAX)]

    def hash(self, key: int | str) -> int:
        """Returns a hashed value for a given key"""
        if type(key) != str:
            key = str(key)
        
        h = i = 0
        for char in key:
            h += ord(char) * i
            i += 1
        return h % self.MAX

    def get(self, key: int | str) -> any:
        """Returns the value of the specified key
        
        Raises KeyError if key is not found in the HashTable"""
        key = key if type(key) == str else str(key)
        return self[key]

    def pop(self, key: str):
        ...

    def keys(self) -> list:
        """Returns a list containing all the keys in the HashTable"""
        keys = [item[0] for llist in self.llist for item in llist]
        return keys

    def values(self) -> list:
        """Returns a list containing all the values in the HashTable"""
        values = [item[1] for llist in self.llist for item in llist]
        return values

    def items(self) -> list:
        """Returns a list of tuples, each tuple containing a key, value pair"""
        items = [item for llist in self.llist for item in llist]
        return items

    def __getitem__(self, key: int | str) -> any:
        key = key if type(key) == str else str(key)
        i = self.hash(key)

        if key not in self.keys():
            raise KeyError("key not found in the HashTable")

        for item in self.llist[i]:
            if item[0] == key:
                return item[1]

    def __setitem__(self, key: int | str, value) -> None:
        key = key if type(key) == str else str(key)
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

    def __str__(self) -> str:
        table_str = ""
        for row in table.llist:
            table_str += str(row) + "\n"
        return table_str.rstrip("\n")

    def __repr__(self) -> str:
        return f"HashTable({self.MAX})"

    def __len__(self):
        return self.MAX


if __name__ == '__main__':
    table = HashTable(10)

    for i in range(20):
        # key = f"key{i}"
        table[f"key{i}"] = i

    print(table)
