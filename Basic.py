
# Variables are container to store the data values. Python has several built in data types.
# int for integer float for floatin pointng number str for string 
# list ordered collection of items, mutable(can be changed)
# tuple order collection of items, nonmutable (cannot be changed)
# dic collection of key value pair
#set undered collection on unqiue items

# examples
age = 30
height = 164.50
name = 'Alice'
numbers = [2,4,6,8]
person = { 'name' : 'Priya', 'age' : 27, 'location' : 'Delhi'} 

# Create variables of each data type and print their values.

num = 80  # int
temp = 42.2  # float
thought = 'Inhale calm exhale stress'  # string
location_code = [101, 102, 103, 104, 105, 108]  # list
cost_code = (4, 8, 9, 11)  # tuple (changed from list to tuple for immutability)
airline = {
    'Name': 'British Airways',
    'threeLetter_code': 125,  # Corrected key name to snake_case
    'twoLetter_code': 'BA',   # Corrected key name to camelCase
    'hub': 'London'
}  # dictionary (keys adjusted for Python naming conventions)

# Topic 2: Control Structures

"""
Control structures allow you to control the flow of your program:

if-elif-else: Conditional statements to execute different blocks of code based on conditions.
for: Loop through a sequence (like a list or tuple).
while: Loop until a condition is met.
"""

#example of if else
age = 18
if age >= 18:
    print('You are an adult')
else:
    print('You are minor')

#example 