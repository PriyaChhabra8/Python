Topic 10: Lambda Functions and Functional Tools
Explanation:
Lambda functions are small anonymous functions defined with the lambda keyword:

lambda: Define a lambda function.
map(), filter(), reduce(): Higher-order functions for functional programming.

  # Example of lambda function
add_five = lambda x: x + 5
print(add_five(10))  # Output: 15

# Example of map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

Exercise:

Use filter() to filter out even numbers from a list.
Write a program using reduce() to find the maximum element in a list.
Tips:

Lambda functions are useful for short functions where def would be overkill.
Functional tools like map(), filter(), and reduce() promote functional programming paradigms.
