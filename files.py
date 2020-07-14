# file = open("myFile.txt", "w")

# print("Name :", file.name)
# print("Is Closes :", file.closed)
# print("Opening Mode :", file.mode)

# # Write to file
# file.write("I love Python")
# file.write(" and Javascript")
# file.close()

# # Append to file
# file = open("myFile.txt", "a")
# file.write(", I also like Golang")
# file.close()

# Read file
file = open("myFile.txt", "r")
text = file.read(100)
print(text)