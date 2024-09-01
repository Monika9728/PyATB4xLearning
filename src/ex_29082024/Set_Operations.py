set1 = {1, 2, 3, 4, 63.5, 23, 5, 2, 32, 3, 3, 1, 40, 25, 3, 99}
print("Set1 is:", set1)
set2 = {16, 2.9, 30, 4, 63.5, 203, 54, 2, 32, 3, 3, 11, 40, 2.5, 3, 99}
print("Set2 is:", set2)
common_elements_set = set1.intersection(set2)
print("Set with common elements is:", common_elements_set)
print("-----------------------------------------------------------------------------------------------")
all_elements_set = set1.union(set2)
print("Set with union of elements is:", all_elements_set)
difference = set1.difference(set2)
print("Difference between two sets is:", difference)  # will remove common elemnets from set1 with set2
print("-----------------------------------------------------------------------------------------------")
set1.add("x")
print("Set after adding element:", set1)
