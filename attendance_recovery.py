held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Please enter valid class counts.")
else:
    attendance = attended / held * 100
    print("Current attendance:", round(attendance, 2), "%")

    if attendance >= 75:
        print("Attendance requirement is satisfied.")
    else:
        additional = 0

        while (attended + additional) / (held + additional) * 100 < 75:
            additional += 1

        print("Attend the next", additional,
              "classes without absence to reach 75%.")