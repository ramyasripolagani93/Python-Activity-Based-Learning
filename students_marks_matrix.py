students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Students and subjects must be positive numbers.")
else:
    marks_matrix = []

    for i in range(students):
        row = []
        print(f"Enter marks for Student {i + 1}:")

        for j in range(subjects):
            mark = float(input(f"  Subject {j + 1}: "))
            row.append(mark)

        marks_matrix.append(row)

    if any(mark < 0 or mark > 100
           for row in marks_matrix for mark in row):
        print("Marks must be between 0 and 100.")
    else:
        print("\n--- Marks Matrix ---")

        for i, row in enumerate(marks_matrix):
            print(f"Student {i + 1}: " +
                  "  ".join(f"{mark:g}" for mark in row))

        print("\nStudent averages:")
        averages = []

        for i, row in enumerate(marks_matrix):
            average = sum(row) / subjects
            averages.append(average)
            print(f"Student {i + 1}: {average:.2f}")

        highest_index = averages.index(max(averages))
        print(f"Highest average: Student {highest_index + 1} "
              f"({averages[highest_index]:.2f})")
