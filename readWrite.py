print("---------Print all content---------------")
# print all contents of file
file = open('test.txt')
print(file.read())
file.close()

print("------Print the no of chars---------------")
# print line by line using readline method
file = open('test.txt')
print(file.read(6))
file.close()

print("------Print lines---------------")
# print line by line using readline method
file = open('test.txt')
print(file.readline())
print(file.readline())
file.close()

print("------Print all line after line---------------")
file = open('test.txt')
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

print("------Print lines using for loop---------------")
# print line by line using readlines method
# readlines saves the lines in list
file = open('test.txt')
for line in file.readlines():
    print(line)
file.close()
