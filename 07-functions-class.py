my_list = []

def my_input():
    in_num = int(input("Enter a number: "))
    my_list.append(in_num)

counter = 0

while counter < 10:
    my_input()
    counter = counter + 1

print(my_list)