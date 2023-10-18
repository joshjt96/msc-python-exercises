# Create and open a text file. The "w" parameter opens the file for writing.
output_file = open("Output.txt", "w")
# Create string data to add to the file:
my_string = "This is a string for the output file.\n"
# Add the string to the text file:
output_file.write(my_string)
output_file.close()
print(output_file)

# read_file = open("Output.txt", "r")
# print(read_file)