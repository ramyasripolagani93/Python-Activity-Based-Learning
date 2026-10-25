subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(subjects):
    mark = float(input("Enter marks: "))
    marks.append(mark)

if any(mark < 0 or mark > 100 for mark in marks):
    print("Marks must be between 0 and 100.")
else:
    final_marks = []

    for mark in marks:
        if mark < 35 and 35 - mark <= 3:
            final_marks.append(35)
        else:
            final_marks.append(mark)

    print("Final marks:", final_marks)

    if all(mark >= 35 for mark in final_marks):
        print("Result: PASS")
    else:
        print("Result: FAIL")

    average = sum(final_marks) / subjects
    print("Average marks:", round(average, 2))