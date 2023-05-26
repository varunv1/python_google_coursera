file = open("poem.txt")  # it returns a file descriptor
print(file.readline())  # reads one line from current index position
print(file.readline())
print(file.read())  # reads current to end of the file

# here once we are done with the file, we must close the file
file.close()
