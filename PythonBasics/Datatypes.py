print("Hallo")

b, c, d = 2, 3.4, "String"  # simple asignment of values

print("{} {}".format("Value is", b))

print(type(d))

#Lists
values = [1, 2, "syam", 56, 5j]

print(values[-1])  # last index in list

print(values[-3:-1])

# inserting values in between
values.insert(3, "shetty")
print(values)

#Adding new values at end
values.append(678)
print(values)

# Update existing with new values
values[0] = 123
print(values)

# deleting
del values[-2]
print(values)

# Datatype - TUPLE - same as list data type but immutable
val = (12, 35.6, "tup")
print(val)

# Datatype - DICTIONARY

a = {1: 34, 2: 56.7, 3: "star"}
print(a[1])

# if key or value is string - put in quotes
b = {"a": 123, 2: 45.7, 3: "wyd", "d": "usa"}
print(b["d"])


