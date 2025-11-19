info = {
    "name": "KAWTHER",
    "hometown": "UAE",
    "age":  18 ,
}

print(info["name"], info["hometown"], info["age"], sep="\n")

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age: "))

info = {
    "name": "KAWTHER",
    "hometown": "UAE",
    "age": 18,
}

print(info["name"], info["hometown"], info["age"], sep="\n")

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number!")

info = {
    "name": "KAWTHER",
    "hometown": "UAE",
    "age": 18,
}

print(info["name"], info["hometown"], info["age"], sep="\n")
