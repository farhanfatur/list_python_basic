name = "Farhan"
age = 19

# concate
# print("Name : " + name + ", age : " + str(age))

# argument by positions
# print("Name : {name}, age : {age}".format(name=name, age=age))

# F-string
# print(f"Name : {name}, age : {age}")

s = "farhan fatur rozzi"

# capitalize
print("Capitalize : " + s.capitalize())

# uppercase string
print("Uppercase : " + s.upper())

# lowercase string
print("Lowercase : " + s.lower())

# swapcase string
print("Swapcase : " + s.swapcase())

# Length string
print("Length : " + str(len(s)))

# replace string
print("Replace : " + s.replace("rozzi", "setiawan"))

sub = 'a'
# count string with character ''
print("Count : " + str(s.count(sub)))

# split into a list
print("Split : " + str(s.split()))

# startwith string
print(s.startswith("f"))

# endwith string
print(s.endswith("i"))

# find string
print(s.find("r"))

# is all alphanumeric string
print(s.isalnum())

# is all alphabetic
print(s.isalpha())