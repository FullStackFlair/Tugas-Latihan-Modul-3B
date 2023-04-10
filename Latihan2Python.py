class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Contoh penggunaan queue
queue = Queue()

queue.enqueue("Java")
queue.enqueue("DotNet")
queue.enqueue("PHP")
queue.enqueue("HTML")

print("remove : " + queue.dequeue())
print("element : " + queue.items[0])
print("poll : " + queue.dequeue())
print("peek : " + queue.items[0])
