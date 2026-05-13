person = ("Rahul", 25, 5.9)

print(f"Age: {person[1]}")

try:
    person[0] = "Syam"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")