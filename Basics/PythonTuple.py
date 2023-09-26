# Tuples are collections that are ordered | indexed | unchangeable | duplicates | can't be deleted
my_tuple = ("Oranges", "apples", "cherry")
print my_tuple
print my_tuple[2]
print my_tuple[-1]
print my_tuple[0:2]

for val in my_tuple:
    print val

print len(my_tuple)

my_tuple_2 = ("Banana", (1, 2, 3), ["Tokyo", "Mexico"])    # A list created inside a Tuple
print my_tuple_2
print my_tuple_2[2][1]

my_tuple_2[2][1] = "USA"  # Values can't be change in Tupple but can in lists even if they are store inside of a tupple
print my_tuple_2

print "Banana" in my_tuple_2  # T his will return True or false if the String is present in a Tupple
print "Cherry" in my_tuple_2
print "Tokyo" in my_tuple_2 