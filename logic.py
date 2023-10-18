# num = int(input("How many numbers to print"))
# for i in range(0, num):
#    print(i)

customers = ["Susan", "Alex", "Nick", "Mary"]
for count, value in enumerate(customers):
     print(count, value)
print(f"Loop executed {count+1} times")