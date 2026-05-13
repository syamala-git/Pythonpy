person = ("Rahul", 25, 5.9)

print(f"Age: {person[1]}")

try:
    person[0] = "Syam"
except TypeError:
    print("Error: 'tuple' object does not support item assignment - Tuples are immutable.")