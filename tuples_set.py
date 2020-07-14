#tuples is a collection which is ordered and unchangeable, allow modified

fruits = ("Apples", "Melon", "Grape")
# fruits2 = tuple(("Apples", "Melon", "Grape")) # old declaration tuples

# single value needs trailing comma
fruits2 = ("Apple",)
# print(fruits2, type(fruits2))

# get value
# print(fruits[0])

# try change value?ofcourse is not work
# fruits[0] = "Watermelon"
# print(fruits[0])

# can delete item
# del fruits
# print(fruits)

# get length
print(len(fruits))
# A set is a collection which is unordered and unindexed.No duplicate number

fruits_set = {"Apples", "Melon", "Grape"}

# check if in set
print("Apples" in fruits_set)

# add to set
fruits_set.add("Orange")
print(fruits_set)

# remove from set
fruits_set.remove("Grape")
print(fruits_set)

# clear a set
# Note: clear hanya menghapus isi value dari tuples sedangkan variabelnya masih bisa dipakai
fruits_set.clear()
print(fruits_set)

# delete from set
del fruits_set
print(fruits_set)