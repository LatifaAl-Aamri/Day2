"""
Write a Python function that takes a string as input and checks whether
the string is a palindrome or not. A palindrome is a word, phrase,
number, or sequence that reads the same backward as forward.

Your task is to implement the is_palindrome function that checks
whether the given string is a palindrome or not. The function should
return True if the string is a palindrome, and False otherwise.
"""

#from QueueClass import Queue
def is_palindrome(input_string):
    #Remove any non-alphanumeric characters and convert to lower
    cleaned_string = ''
    for char in input_string:
        if char.isalnum():
            cleaned_string = cleaned_string+char.lower()
            
    #Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]
#Test cases
print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man, a plan, a canal, Panama"))   # True


"""
def is_palindrome(input_string):
    cleaned_string = "".join(filter(str.isalnum, input_string)).lower()
    return cleaned_string == cleaned_string[::-1]

# Test cases
print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man, a plan, a canal, Panama"))   # True
"""


