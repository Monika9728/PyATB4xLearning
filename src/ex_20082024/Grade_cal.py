# you have to ask interviewver what is the data type

marks = int(input("Enter you marks: "))
if marks >= 90 and marks <= 100:
    print("You fall in: Grade A with marks: ", marks)
elif marks >= 80 and marks <= 89:
    print("You fall in: Grade B with marks: ", marks)
elif marks >= 70 and marks <= 79:
    print("You fall in: Grade C with marks: ", marks)
elif 60 < marks <= 69:  # by hovering on the condition ,we can find a
    # better option for chain comparison
    print("You fall in: Grade D with marks: ", marks)
elif marks >= 50 and marks <= 59:
    print("You fall in: Grade E with marks: ", marks)
elif marks > 100:
    print("You are unnatural")
else:
    print("You fall in: Grade F with marks: ", marks)
