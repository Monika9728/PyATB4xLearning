# Tuple use less memory ,List uses more memory
# defined with (),List is defined using[]
# can be converted into each other
# Tuples can not be appended,list can be
# tuple can have static,fixed date,Lists have dynamic data,(can be changed later)
# In real scenarios ,we use tuples


cubes = (8, 1000, 27, 64, 513, 216, 343, 729)
print("Initial Tuple:", cubes)
my_list = list(cubes)  # will convert tuple to lists
# now all operations can be performed as in list
print("Tuple converted into list is:", my_list)
