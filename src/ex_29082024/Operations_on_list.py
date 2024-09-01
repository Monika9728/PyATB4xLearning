my_list = [1, "Monika", 3, 22.5, False]
print("My List is:", my_list)
print("-------------------------------------------------------------")
# OPERATIONS ON LIST
# 1.Append : append is only used  to add  single value at the end of the list
# however we can not add multiple values in one go,so
my_list.append(10.9)
my_list.append(22)
my_list.append(4.0)
print("My Appended list is: ", my_list)
print("-------------------------------------------------------------")
# The alternative is to use EXTEND To add multiple elements at a time
my_list.extend("ext")  # print single characters in one go
my_list.extend(["extend", 9, 576])
print("My Extended list is: ", my_list)
print("-------------------------------------------------------------")
# INSERT and shift--> To add an element at  specific index
my_list.insert(1, "hello")
print(my_list)  # it will take 2 arguments ,Ist is index value and second is the element name
print("My Inserted list is: ", my_list)
print("---------------------------------------------------------------------------")
my_list.insert(-1, "Python")  # will print from the right at index 1
print("My Inserted list is: ", my_list)
print("---------------------------------------------------------------------------")

# copy: to copy a list
copied_list = my_list.copy()
print("My Copied List is: ", copied_list)
print("---------------------------------------------------------------------------")
# Clearing a List:
my_list.clear()
copied_list.remove("Monika")
print("List after replacing Monika", "is:", copied_list)
print("---------------------------------------------------------------------------")

# SORT :To sort a list
number = [1, 2, 15, 4, 9, 6, 3, 2, 7, 9, 10]
number.sort()
print("My Sorted List is: ", number)
number.sort(reverse=True)
print("---------------------------------------------------------------------------")
number.reverse()
print("Reversed list is: ", number)
print("---------------------------------------------------------------------------")

# List concatenation

combined_list = number + copied_list
print("Concatenated List is: ", combined_list)
print("---------------------------------------------------------------------------")

# for loop for multiple times removal of element
# for x in combined_list:
#     combined_list.remove(2)
# print("List after removing Removing 2 is:", combined_list)
