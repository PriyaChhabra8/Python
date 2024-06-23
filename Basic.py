
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

#example of for loop

numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

#example of while loop
count  = 0
while count < 5:
    print(count)
    count +=1


#Write a program that checks if a number is even or odd using if-else.

num = int(input('Enter an integer number: '))

if num % 2 == 0:
    print('Number is even.')
else:
    print('Number is odd.')

#Use a for loop to iterate through a list and print each item.

numbers1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in numbers1:
    print(num)

#Functions are blocks of reusable code that perform a specific task. They help in organizing code and making it more modular:

#def: Keyword to define a function.
#return: Statement to return a value from a function.

# Example of a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!

def rect_area(length, width):
    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    length (float or int): Length of the rectangle.
    width (float or int): Width of the rectangle.

    Returns:
    float or int: Area of the rectangle, calculated as length * width.
    """
    area = length * width
    return area

#Modify the function to return both the area and perimeter of the rectangle.

def rect_area(length, width):
    """
    Calculate the area of a rectangle given its length and width.

    Parameters:
    length (float or int): Length of the rectangle.
    width (float or int): Width of the rectangle.

    Returns:
    float or int: Area of the rectangle, calculated as length * width.
    """
    area = length * width
    perimeter = 2*(length+width)
    return area, perimeter


