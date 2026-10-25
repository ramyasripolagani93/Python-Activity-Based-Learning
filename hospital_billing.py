patient_name = input("Enter patient name: ")
days = int(input("Enter number of hospital days: "))
room_rate = float(input("Enter room charge per day: "))
treatment_charge = float(input("Enter treatment charge: "))
medicine_charge = float(input("Enter medicine charge: "))

if days < 0 or room_rate < 0 or treatment_charge < 0 or medicine_charge < 0:
    print("Days and charges cannot be negative.")
else:
    room_charge = days * room_rate
    total = room_charge + treatment_charge + medicine_charge

    if total >= 50000:
        category = "High-cost patient"
    elif total >= 20000:
        category = "Medium-cost patient"
    else:
        category = "Low-cost patient"

    print("\n--- Hospital Bill ---")
    print("Patient:", patient_name)
    print("Room charge:", room_charge)
    print("Treatment charge:", treatment_charge)
    print("Medicine charge:", medicine_charge)
    print("Total bill:", total)
    print("Classification:", category)