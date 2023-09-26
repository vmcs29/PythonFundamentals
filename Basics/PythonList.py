
my_list = ["Tokyo", "Mexico", "London", "NYC"]
print(my_list)  # To Print the full list
print my_list[2]  # To print specific index position

my_list[2] = "Brazil"  # To change the value of an specific position in the list
print my_list

for val in my_list:  # To iterate a list of values one by one
    print val

print len(my_list)  # To print the length of the list

my_list.append("Boston")  # To add a new value to the list
print my_list

my_list.insert(3, "Canada")  # This also works to add a new value in the list but with specific position
print my_list

my_list.remove("Tokyo")  # To remove an specific element
print my_list

my_list.pop()  # Using pop without index, will remove the last object from the list
print my_list

my_list.pop(1)  # Using pop without index, will remove the last object from the list
print my_list

fruits = ["orange", "apple", "cherry"]
print fruits
fruits.reverse()  # To print a list in reverse order
print fruits

my_list_2 = ["apple", 1, 3.0, 'right']  # You can create list with different types of data
my_list_3 = ["apple", [1, 2, 3], ['a', 'b', 'c']]  # You can have nested lists
print my_list_3
print my_list_3[1][1] 