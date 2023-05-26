items_to_write = ["Hey ", "there", ", ", "I ", "am ", "writing ", "a ", "novel "]
with open("novel.txt", "w") as novel:
    for item in items_to_write:
        novel.write(item)

# now, lets verify if we were able to write

with open("novel.txt") as novel:
    if novel.read() == "".join(items_to_write):
        print("Written successfully")
    else:
        print("Failed to write")
