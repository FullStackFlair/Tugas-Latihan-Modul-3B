class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Contoh penggunaan stack
stack = Stack()

stack.push("Aku")
stack.push("Anak")
stack.push("Indonesia")

print("Next : " + stack.peek())

stack.push("Raya")
print(stack.pop())
print("!")

count = 0
for item in reversed(stack.items):
    if item == "Aku":
        count += 1
        if count > 1:
            stack.pop()
    else:
        break

print(stack.pop())
print
