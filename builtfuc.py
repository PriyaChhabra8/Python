Topic 11: Built-in Functions
Explanation:
Python provides a set of built-in functions for common tasks:

len(): Calculate the length of a sequence (list, tuple, string).
range(): Generate a sequence of numbers.
zip(): Combine multiple iterables element-wise.
enumerate(): Iterate over an iterable and return index-value pairs.

# Example of built-in functions
# Using len()
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

# Using range()
for num in range(1, 5):
    print(num)  # Output: 1, 2, 3, 4

# Using zip()
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")  # Output: Alice is 30 years old., ...

# Using enumerate()
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")  # Output: Index 0: apple, Index 1: banana, ...

Exercise:

Use zip() to combine two lists (names and ages) and print each pair.
Iterate over a list using enumerate() and print the index and element.
Tips:

Built-in functions save time and effort by providing ready-to-use solutions for common tasks.
Explore more built-in functions in Python's documentation to expand your toolkit.

