# my_list = []

# def my_input():
#     in_num = int(input("Enter a number: "))
#     my_list.append(in_num)

# counter = 0

# while counter < 10:
#     my_input()
#     counter = counter + 1

# print(my_list)

# def my_check(num):
#     if num > 0:
#         print(f"{num} is positive")
#         return True
#     else:
#         return False

# user_input = int(input("Enter a number: "))
# print(my_check(user_input))

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move_forward(self):
        print(f" Your {self.make} is now moving forward.")

    def stop(self):
        print(f"Your {self.make} has stopped.")

    def make_model(self):
        print(f"Your car is a {self.make}. The model is {self.model}.")

bmw = Vehicle("BMW", "330i")

# print statement used to print the string that includes the car info from the class:

print(f"My car is a {bmw.make} {bmw.model}.")

vw = Vehicle("Volkswagen", "Golf")

# Here, no print statement is needed to get the output in the terminal, since the methods defined in the class include a print statement already.

vw.move_forward()
bmw.stop()