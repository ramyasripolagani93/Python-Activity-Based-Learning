employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

if basic_salary < 0:
    print("Salary cannot be negative.")
else:
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    gross_salary = basic_salary + hra + da

    deduction = gross_salary * 0.08
    net_salary = gross_salary - deduction

    print("Employee name:", employee_name)
    print("Basic salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("Gross salary:", gross_salary)
    print("Deduction:", deduction)
    print("Net salary:", net_salary)