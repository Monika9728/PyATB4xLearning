set1 = {1, 2, 3, 4, 63.5, 23, 5, 2, 32, 3, 3, 1, 40, 25, 3, 99}
# print("Length of set is:", len(set1))
# for i in set1:
#     print(i, end=",")
print("\n")
for num in set1:
    if num % 2 == 0:
        print("Even numbers in set:\n", num)
    if num % 3 == 0:
        print("Numbers divided by 3 in set:", num)
