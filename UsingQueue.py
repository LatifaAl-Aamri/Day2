from QueueClass import Queue
lane = Queue()
print(lane.is_empty())  # Output: True

lane.enqueue("A")
lane.enqueue("B")
lane.enqueue("C")

print(lane.peek())  # Output: 1
print(lane.size())  # Output: 3

print("bye bye: ", lane.dequeue())  # Output: 1
print("next in line:", lane.peek())
print("waiting:", lane.size()) 

print(lane.dequeue())  # Output: 2

print(lane.is_empty())  # Output: False