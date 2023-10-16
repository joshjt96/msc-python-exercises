a = 1  
b = 2  
print(a == b)

my_string = "Neptune"
empty_list = []
for i in my_string:
    empty_list += [i]
    print(empty_list[::-1])

# Dictionary list items method:

my_dict = {
    "name": "Josh",
    "age": 27
}

for a, b in my_dict.items():
    print(f"{a}: {b}")

# 3. Create a script which asks the user for their age. 
# If the value is less than 0 or greater than 130 then an appropriate warning message should appear. 
# The script should continue to ask for the users age until a valid age is entered. 

# age = int(input("Enter your age: "))
# while age > 130 or age < 0:
#     print("Number invalid, please re-enter")
#     age = int(input("Enter your age: "))
# print(f"Valid age entered: {age}")

# 5. Create a script which asks the user to enter a series of integer data values. 
# To end data entry the user must enter one or more characters. 
# The user must be able to specify the name of the file (including extension) to which the data is saved. 
# There must be only one data item per line in the saved file.

values = input("Enter a series of whole numbers: ")
while values == "":
    values = input("Enter a series of whole numbers: ")
user_number = int(values)
print(f"Numbers entered: {user_number}")