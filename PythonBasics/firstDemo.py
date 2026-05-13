# INDENTATION fails the code. use CTRL + ALT + L to adjust indentation
'''print("Hello")
# comment it out -with hash
a = 3
print(a)

Str = "I am String"
print(Str)

a, b, c = 5, 6.6, "string"

# print("Value is :"+b)
# CANNOT add values of two different data types
# integer and float can be added
# integer is converted to float and the result is of type -float

print("{} {}".format("Value is", b))

print("first" + "second")
print(type(a))
print(type(b))
print(type(a + b))

# Data type LIST
values = [1, 2, 4.5, "syam", 6.77]

print(values[0])  # 1
# Add new value at an index
values.insert(3, "kov")
print(values)

# Add value at end
values.append("end")
values.append("end1")
print(values)

# Update a value
values[3] = "SYAM"

# remove a value
values.remove("end1")
print(values)

#deleting a value
del values[-1]
print(values)

# TUPLES - same as list datatype but cannot be modified
# need to convert to list to do the modifications
hvalues = (23, 45.6, "tuple", "try")
#hvalues[0] = 25
print(hvalues)
'''

# DICTIONARY data type - KEY:VALUE pair
dic = {"abc": 2, 3: "dcb", "dh": "sd"}

print(dic["abc"])

# Declare empty dictionary and enter the values
dict = {}
dict["first"] = "syam"
dic["last"] = "kov"
dict["int"] = "Read"
print(dict)
