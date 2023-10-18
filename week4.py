# a = 1  
# b = 2  
# print(a == b)

# my_string = "Neptune"
# empty_list = []
# for i in my_string:
#     empty_list += [i]
# print(empty_list[::-1])

# Dictionary list items method:

# my_dict = {
#     "name": "Josh",
#     "age": 27
# }

# for a, b in my_dict.items():
#     print(f"{a}: {b}")

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

# file_name = input("Enter a name for your text file: ")
# while file_name == "":
#     file_name = input("Enter a name for your text file: ")
# user_file = open(f"{file_name}.txt", "w")
# file_int = str({user_number})
# user_file.write(file_int)
# user_file.close()

# # Create and open a text file. The "w" parameter opens the file for writing.
# output_file = open("Output.txt", "w")
# # Create string data to add to the file:
# my_string = "This is a string for the output file.\n"
# # Add the string to the text file:
# output_file.write(my_string)
# output_file.close()
# print(output_file)

# Following on from task 1 above. Modify the script to provide the option to save data to a new file or append the data to an existing file.
file_name = input("Enter a name for your text file: ")
while file_name == "":
    file_name = input("Enter a name for your text file: ")

option = input("If you want to save this data to a new file, enter N. If you want to append it to an existing file, enter A.").upper()
if option == "N":
    file_option = "w"
    user_file = open(f"{file_name}.txt", f"{file_option}")
    file_int = str({user_number})
    user_file.write(file_int)
    user_file.close()
elif option == "A":
    file_option = "a"
    with open(f"{file_name}", f"{file_option}") as user_file:
        user_file.write(str(user_number))
else:
    print("Invalid selection. Saving data as a new file.")
