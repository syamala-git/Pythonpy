print("-----------------------------------")
print("Reading and Printing files contents")
print("-----------------------------------")
file = open('file1.txt')
print(file.read())
file.close()
print("\n")

print("-----------------------------------")
print("Count lines in a file")
print("-----------------------------------")
file = open("file1.txt")
count = sum (1 for line in file)
print(f"Total number of lines: {count}")
file.close()

file = open("file1.txt")
summation = 0
for line in file:
    summation = summation + 1
print(f"Total number of lines: {summation}")
file.close()
