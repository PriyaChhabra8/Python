Lesson 4: File Handling and Error Handling
Topic 8: File Handling

Explanation:
File handling allows you to work with files on your computer:

open(): Open a file for reading or writing.
read() and write(): Read from or write to a file.
close(): Close the file to free up system resources.

# Example of file handling
# Writing to a file
with open('data.txt', 'w') as f:
    f.write("Hello, Python!\n")
    f.write("This is a text file.")

# Reading from a file
with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

Exercise:

Write a program that reads numbers from a file, calculates their sum, and prints the result.
Create a new file and write a list of your favorite books to it.
Tips:

Use 'r' for reading, 'w' for writing (creates a new file or overwrites existing content), and 'a' for appending to a file.
Always close files using close() or use the with statement for automatic cleanup.
