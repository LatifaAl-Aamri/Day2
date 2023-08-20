#add comments
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty, cannot dequeue an item.")

    def peek(self):  #peek  what is te first element
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty, cannot peek an item.")

    def size(self):
        return len(self.items)