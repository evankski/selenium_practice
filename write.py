# file = open('test.txt')
#
# file.close()

# this is another way to open a file
# you will not need to close when writing like this -- will auto close
# putting 'w' writes on the file and 'r' reads the file
with open('test.txt', 'r') as reader:
    # read the file and store all the lines in list
    # reverse the list
    # write the list back to the file
    content = reader.readlines()  # all of lines will get stored in a list
    reversed(content)  # this will reverse all of the items presented in the list
    with open('test.txt', 'w') as writer:
        # this will take every line and write back to list
        for line in reversed(content):
            writer.write(line)
            # we reversed the list and wrote it back to the test.txt file

