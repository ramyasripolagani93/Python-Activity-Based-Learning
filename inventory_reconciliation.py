item_name = input("Enter item name: ")

opening_stock = int(input("Enter opening stock: "))
received = int(input("Enter quantity received: "))
dispatched = int(input("Enter quantity dispatched: "))
physical_stock = int(input("Enter physical stock: "))

if (opening_stock < 0 or received < 0
        or dispatched < 0 or physical_stock < 0):
    print("Stock quantities cannot be negative.")
else:
    expected_stock = opening_stock + received - dispatched

    difference = physical_stock - expected_stock

    print("\n--- Inventory Report ---")
    print("Item:", item_name)
    print("Expected stock:", expected_stock)
    print("Physical stock:", physical_stock)

    if difference == 0:
        print("Status: Stock matches.")
    elif difference > 0:
        print("Status: Surplus of", difference, "units.")
    else:
        print("Status: Shortage of", abs(difference), "units.")