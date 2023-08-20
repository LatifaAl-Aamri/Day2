"""
Exercise: Reversing a String

Write a Python function that takes a string as input and returns the
string in reverse order. You should use the Stack class to implement the
solution.
"""
from StackClass import Stack
def reverse_string(input_string):
        stack = Stack()
        #Push each charactor of the input_string onto the stack
        for char in input_string :
            stack.push(char)
        recovered_string =""
        #Pop each character from the stack to construct the reversed string
        while not stack.is_empty():
            recovered_string += stack.pop()
        return recovered_string
        
#Test cases
print(reverse_string("hello")) #output: "olleh"
print(reverse_string("python"))  #output: "nohtyp"
print(reverse_string("racecar"))  #output: "racecar"
