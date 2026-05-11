"""
Demonstration of Python control flow: if-else, for loops, while loops, break, and continue
"""
# ===== IF-ELSE EXAMPLE =====
greet = "Good Morning"
if greet == "Good Morning":
    print(greet)
else:
    print("Value does not match")

print("if else completed\n")

# ===== FOR LOOP EXAMPLE =====
print("****** FOR LOOP *****")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

# Calculate sum with transformation
total = sum(k * 2 for k in range(1, 6))
print("{}{}".format("Total is :", total))

summation = 0
for i in range(1, 6):
    summation = summation + i
print("{} {}".format("Summation is: ", summation))

print("****** FOR JUMPING *****")
for j in range(1, 6, 2):
    print(j)

# ===== RANGE LOOP EXAMPLE =====
print("\n****** SKIP FIRST INDEX *****")
for index in range(10):
    print(index)

# ===== WHILE LOOP EXAMPLE =====
print("\n****** WHILE LOOP *****")
counter = 4
while counter >= 1:
    if counter != 3:
        print(counter)
    counter = counter-1
    #counter -= 1

# ===== BREAK EXAMPLE - Breaks abruptly=====
print("\n****** BREAK *****")
counter = 7
while counter >= 1:
    if counter == 3:
        break
    print(counter)
    counter -= 1

# ===== CONTINUE EXAMPLE =====
print("\n****** CONTINUE *****")
counter = 7
while counter >= 1:
    if counter == 6:
        counter -= 1
        continue  # Skip rest of the iteration

    if counter == 3:
        break
    print(counter)
    counter -= 1
