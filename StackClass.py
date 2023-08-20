#add comments LIFO
#Think how to add/apply is_FULL??
#add comments LIFO
#Think how to add/apply is_FULL??
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):  # to check if stack has items
        return len(self.items) == 0

    def push(self, item):  #push to add at the top
        self.items.append(item)

    def pop(self):  #pop to remove from end to return not deleted
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")
        #raise mean erroe exaptin this in method diff from try and exept

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self):
        return len(self.items)


   