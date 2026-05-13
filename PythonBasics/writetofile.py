# another command to open and close file
# can specify the read r or write w mode

# read the file and store al lines to file
# Also reverse the order of the texts

# reader,writer - object , content - variable
with open('test.txt', 'r') as reader:  # r is opening the file in read mode, reader is object name
    content = reader.readlines()  # [ajjv, bsdfdsf, csdss, dsdde, ewer]
    reversed(content)  # [ewer,dsdde,csdss,bsdfdsf,ajjv ]
    # w mode will replace the current file content with new content
    with open('test.txt', 'w') as writer: # w-opening the file in write mode, writer is object name
        for line in reversed(content): # using for loop and reading each line
            writer.write(line) # writing into file

