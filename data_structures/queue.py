from linkedlist import LinkedList


class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def enqueue(self, data):
        self.queue.insert(data)

    def dequeue(self):
        self.queue.pop()

    def peek(self):
        if not self.queue.head:
            return
        return self.queue.head.data

    def is_empty(self):
        return not len(self.queue)

    def __str__(self):
        return str(self.queue)


if __name__ == '__main__':
    q = Queue()
    print(q)
