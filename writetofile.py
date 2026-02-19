# another command to open and close file
# can specify the read r or write w mode

# read the file and store al lines to file
# Also reverse the order of the texts

#reader,writer - object , content - variable
with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
