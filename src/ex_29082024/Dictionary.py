# Dictionary --> Key-value pair,unordered collection of elements
student_info = {
    "emp_Id": 101,
    "emp_name": "Pramod",
    "emp_age": 60,
    # "emp_age": 620, #will ignore earlier values and print later one
    "emp_address": "Bengaluru",

}
print("The data about employee is:", student_info)
print(student_info["emp_Id"])
print(student_info["emp_name"])
print(student_info["emp_address"])
print(student_info["emp_age"])

#User can change the values
student_info["emp_name"]="Monika" #can be changed later by user only
print(student_info["emp_name"])
