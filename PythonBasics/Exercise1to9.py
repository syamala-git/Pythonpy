# Exercise 2
print("-----Exercise 2-----")
age = 25
height = 5.9
favorite_color = "blue"
print("{}{}{}{}".format("Age: ", age, " | Type: ", type(age)))
print("{}{}{}{}".format("Height: ", height, " | Type: ", type(height)))
print("{}{}{}{}".format("Favorite Color: ", favorite_color, " | Type: ", type(favorite_color)))
print("\n")

# Exercise 3
print("-----Exercise 3-----")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit: " + fruits[0])
print("Last fruit: " + fruits[-1])
print("{}{}".format("Fruits from index 1 to 2: ", fruits[1:3]))
print("\n")

# Exercise 4
print("-----Exercise 4-----")
person = ("Rahul", 25, 5.9)
print("{}{}".format("Age: ", person[1]))
print("\n")

# Exercise 5
print("-----Exercise 5-----")
car = {"make": "Toyota", "model": "Camry", "year": 2020, "color": "Blue"}
print("{}{}".format("Car model: ", car['model']))
car["owner"] = "Rahul"
print("{}{}".format("Updated car dictionary: ", car))
print("\n")

# Exercise 6
print("-----Exercise 6 if else-----")
greeting = "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greeting!")

print("Program has completed.")  # final message in any condition
print("\n")

# Exercise 7
print("-----Exercise 7 Number Comparison-----")
b = 15
if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison code is completed.")

b = 5
if b > 10:
    print("Number is greater than 10")
else:
    print("Number is 10 or less")
print("Comparison code is completed.")
print("\n")

# Exercise 8
print("-----Exercise 8 Doubling numbers with For loop-----")
numbers = [1, 4, 7, 10]
for i in numbers:
    print(i * 3)
print("\n")

# Exercise 9
print("-----Exercise 9 -Customized Greeting based on time of day-----")
user = 16
if 5 <= user <= 11:
    print("Good Morning")
elif 12 <= user <= 17:
    print("Good Afternoon")
elif 18 <= user <= 21:
    print("Good Evening")
else:
    print("Good Night")

print("Greeting code has completed.")


