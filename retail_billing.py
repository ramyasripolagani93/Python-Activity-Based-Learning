item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

if quantity < 0 or price < 0:
    print("Quantity and price cannot be negative.")
else:
    subtotal = quantity * price

    if subtotal >= 5000:
        discount_rate = 0.15
    elif subtotal >= 2000:
        discount_rate = 0.10
    else:
        discount_rate = 0

    discount = subtotal * discount_rate
    amount = subtotal - discount
    tax = amount * 0.05
    total = amount + tax

    print("\n--- Retail Bill ---")
    print("Item:", item_name)
    print("Quantity:", quantity)
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Amount to pay:", total)