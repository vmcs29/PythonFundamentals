# Sets are Unordered, Unindexed, and no duplicates
my_set = {"Chalk", "Duster", "Board"}
print(my_set)

for x in my_set:
    print(x)

print("Chalk" in my_set)  # Search in Set that will return True or False

my_set.add("Pen")  # To add a value in Set ( this is not by order )
print(my_set)
my_set.update(["Pencil", "Eraser"])  # You can update values
print(my_set)

len(my_set)

my_set.remove("Pencil")  # To delete an element
print(my_set)
my_set.discard("Pen")  # To ignore momentarily from the set
print(my_set)


my_set.pop()  # It will remove elements randomly
my_set.clear()  # it will empty the set but it won't delete the full set, it will leave an "empty" set
print(my_set)

del my_set  # to delete an entire set

my_set_2 = {"Apples", 1, 2, (3, 4, 5)} # you can add different data types
print(my_set_2)

my_list = [1, 2, 3]
print(my_list)
my_set_3 = set(my_list)  # you can cast a list into a set
print(my_set_3)

# In sets you can use math expressions : UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}

print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)