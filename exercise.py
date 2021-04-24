#!/bin/python

# Read in a file in the current working directory, r tells python to read the file
file_object = open('dummy.txt', 'r')


# reading a file as a string use the .read() method
s = file_object.read()
print(s)

s = file_object.read()
print(s)

# you cannot read the file multiple times. The second read() method will return an empty string, because the memory is at the bottom of the file

# writing a new file in the current working directory, us w to write to the file
new_file = open ('my-new-file.txt', 'w')

# add something to the new file using the .write()

new_file.write("Hello there. \n General Kenobi")

# when you are done writing or reading a file, it should be closed, similar to making figures with r

new_file.close()
file_object.close()

print(file_object.closed)
print(new_file.closed)

