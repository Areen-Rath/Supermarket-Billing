while True:
    total = 0
    name = input("Enter name: ")
    while True:
        item = input("Enter item: ")
        qty = input("Enter quantity: ")
        if item.lower() == "chips":
            total += 20 * qty
        elif item.lower() == "chocolate":
            total += 20 * qty
        elif item.lower() == "cake":
            total += 100 * qty
        elif item.lower() == "noodles":
            total += 50 * qty
        elif item == "":
            break
        else:
            print("Invalid item. Type again.")
    repeat = input("Do you want to repeat the process? (Y/y/N/n): ")
    if repeat.lower() == "y":
        continue
    else:
        print(f"Name: {name}")
        print(f"Total Cost: {total}")
        print("\nThank you for shopping with us")
    new = input("Go to new customer? (Y/y/N/n): ")
    if new.lower() == "n":
        break