Lesson 2: Python Data Structures

Topic 4: Lists
Explanation:
Lists are ordered collections that can contain elements of different data types. They are mutable, meaning you can change their contents:

Indexing: Accessing elements in a list using indices.
Slicing: Extracting sublists from a list.

number = [1,2,3,4,5,6,7,8,9,10]
fruits = ['Mango','Apple','Banana','Strawberry']
#Accessing the elements
print(number[1])
#slicing
print(fruits[1:3])

#Create a list of your favorite movies and print the first and last elements.

movies = ['black swan',' Despicable me','Rachel getting married','Inception','Minions']
print(movies[0])
print(movies[-1])

#Use slicing to print the second and third elements of the list.
print(movies[2:4])

Tips:

Lists can be nested (a list inside another list).
Use list methods like append(), insert(), remove(), and pop() to modify lists.

Topic 5: Tuples and Dictionaries
Explanation:

Tuples: Immutable sequences, similar to lists but cannot be changed after creation.
Dictionaries: Unordered collections of key-value pairs. Keys must be unique within a dictionary.

#tuples
lock = (1,8,9,10)

#dictonary 
emp = {'name':'pRIYA', age : 27, 'Number': 888888888, postcode: 110001}

#Create a tuple representing the dimensions of a box (length, width, height) and print its elements.
box = (1,2,3)
print(box)

#Create a dictionary for a person with name, age, and city, and print their age.
person = {'name': 'alice', 'age': 18, 'city':'nyc'}
print(person['age'])

Tips:

Tuples are faster than lists and can be used as keys in dictionaries.
Dictionaries are versatile and efficient for data retrieval based on keys.

Topic 6: Sets and Set Operations
Explanation:
Sets are unordered collections of unique elements. They support mathematical set operations:

Union: Combines elements from two sets.
Intersection: Finds common elements between two sets.
Difference: Finds elements present in one set but not in another.

# Example of sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Set operations
print(a.union(b))       # Output: {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # Output: {3, 4}
print(a.difference(b))  # Output: {1, 2}

#Create two sets of numbers and perform union, intersection, and difference operations.

c = {2,4,6,8}
d= {1,3,5,7}