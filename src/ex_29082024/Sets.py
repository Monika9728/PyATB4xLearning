# sets is a collection of unique items :--> To remove duplicate items
list_of_unique_items = {1, 2, 3, 4, 5, 5, 6, 7, 10, 8, 9, 9}
print("Set without having duplicate items:", list_of_unique_items)
duplicates_list = [2243, 3, 21, 3, 4, 23, 21, 54, 42, 23, 23, 23]
print("List1 with duplicate items:",duplicates_list)
# conversion of LIST into SET
set1 = set(duplicates_list)
print("List2 converted into set is:", set1)
# conversion of TUPLE into LIST
tuple_with_duplicates = [2243, 3, 21, 3, 4, 23, 21, 54, 42, 23, 23, 23]
print("Tuple With Duplicates is:", tuple_with_duplicates)
print("----------------------------------------------------------------------------------------------------")
converted_set = set(tuple_with_duplicates)
print("Tuple converted into set is:", converted_set)
