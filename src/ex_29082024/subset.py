set1 = {1, 2, 3, 4, 63.5, 23, 5, 2, 32, 3, 3, 1, 40, 25, 3, 99}
print(set1)
set2 = {16, 2.9, 30, 4, 63.5, 203, 54, 2, 32, 3, 3, 11, 40, 2.5, 3, 99}  # false
set2 = {1, 2, 3, 4, 63.5, 23, 5, 2, 32, 3, 3, 1, 40, 25, 3, 99}  # return true
print(set2)
subset = set1.issubset(set2)
print(subset)
