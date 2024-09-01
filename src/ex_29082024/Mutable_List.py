# Lists are mutable in nature
number = [1, 2, 15, 4, 9, 6, 3, 2, 7, 9, 10]
number[4] = 33
print(number)
rivers = ["The Ganges", "Yamuna", "Saraswati", "Kaveri", "Mahanadi", "Tapti"]
print("Original List is:")
print(rivers)
rivers[4] = "Beas"
print("List after mutation is:")
print(rivers)
