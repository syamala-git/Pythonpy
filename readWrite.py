file = open('test.txt')

'''
print("---")
print(file.readline())
print(file.readline())
file.close()

#print line by line using readline method

file = open('test.txt')
line = file.readline()
while line!= "":
    print(line)
    line = file.readline()

file.close()
'''

# print line by line using readlines method
for line in file.readlines():
    print(line)
