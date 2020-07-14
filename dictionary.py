# input command line
# ===============================
# print("Print my name: ")
# x = input("Print my name: ")
# print("My name is ", type(x))

# A dictionary is a collection which is unordered, changeable and indexed.No duplicates number

person = {
    "first_name": "Farhan",
    "last_name": "Snow",
    "age": 19
}

# person = dict(first_name="Farhan",last_name="Snow",age=19)

print("person =>", person)

# Get a value
print("person[first_name] =>", person['first_name'])

# add a dictionary
person['phone'] = '0831-7271-7102'
print("add dictionary =>", person)

# change a value
person['first_name'] = "John"
print("change value =>",person)

# get keys dictionary
print("get keys =>", person.keys())

# get items dictionary
print("get items =>", person.items())

person.pop("first_name")
print('pop =>', person)
# # clear dictionary
# person.clear()
# print(person)

# # delete dictionary
# del(person)
# print(person)


# print a dictionary
personCopy = person.copy()
personCopy['City'] = "Malang"
print("copy dictionary =>", personCopy)

# list of dictionary
person2 = [
    {"first_name":"Farhan","last_name":"Fatur","Age":19},
    {"first_name":"Yasa","last_name":"Anesta","Age":20}
]
print("list of dictionary =>", person2[1]['first_name'])
print("list of dictionary =>", person2)
for i, val in person.items():
    print(f"Item : {i}, value : {val}")