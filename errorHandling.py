Explanation:
Exceptions are runtime errors that occur during program execution:

try-except: Handle exceptions gracefully.
finally: Execute cleanup code, regardless of whether an exception occurred.

# Example of try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")

# Example with finally
try:
    f = open('nonexistent.txt', 'r')
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup code here.")

Exercise:

Write a program that prompts the user for input and handles ValueError if the input is not a number.
Modify the file handling program to handle FileNotFoundError and print a user-friendly message.
Tips:

Be specific with except clauses to handle different types of exceptions.
Use exceptions to anticipate and handle potential errors in your code.
