rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Number of rows must be positive.")
else:
    print("Number Triangle:")

    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("Repeated Number Triangle:")

    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()

    print("Floyd's Triangle:")

    number = 1
    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()