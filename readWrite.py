
# creating a var that opens our text file
file = open('test.txt')

# This will read one line
print(file.readline())
# repeating this will cause it to read the line after
print(file.readline())

# ALWAYS close a file after opening it
file.close()