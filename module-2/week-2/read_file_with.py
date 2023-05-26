with open("poem.txt") as file:
    print(file.readline())
    print(file.readline())
    print(file.read())

# no need to close as with automatically does that
