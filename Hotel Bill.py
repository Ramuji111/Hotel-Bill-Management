menu = {
    "pizza": {
        "small": {"cost": 100, "quantity": 0},
        "medium": {"cost": 200, "quantity": 0},
        "large": {"cost": 300, "quantity": 0}
    },
    "burger": {
        "small": {"cost": 100, "quantity": 0},
        "medium": {"cost": 100, "quantity": 0},
        "large": {"cost": 100, "quantity": 0}
    },
    "coke": {
        "small": {"cost": 100, "quantity": 0},
        "medium": {"cost": 200, "quantity": 0},
        "large": {"cost": 300, "quantity": 0}
    },
    "chicken": {
        "small": {"cost": 100, "quantity": 0},
        "medium": {"cost": 200, "quantity": 0},
        "large": {"cost": 300, "quantity": 0}
    }
}

def calculate_bill(menu):
    total_bill = 0
    for item in menu:
        for size in menu[item]:
            total_bill += menu[item][size]["cost"] * menu[item][size]["quantity"]
    return total_bill

def place_order(menu):
    while True:
        print("OUR MENU\n1. Pizza\n2. Burger\n3. Coke\n4. Chicken\n")
        item = input("\nENTER THE ITEM YOU WANT TO ORDER: ").lower()
        
        if item not in menu:
            print("SORRY! THE ITEM IS NOT AVAILABLE IN OUR MENU.")
            continue
        
        print("SIZES AVAILABLE: Small, Medium, Large\n")
        size = input("ENTER THE SIZE OF THE ITEM: ").lower()
        
        if size not in menu[item]:
            print("SORRY! WE DON'T HAVE THAT SIZE.")
            continue
        
        quantity = int(input("ENTER THE QUANTITY: "))
        menu[item][size]["quantity"] += quantity
        print("YOUR ORDER HAS BEEN PLACED.")
        print("YOUR BILL IS:", calculate_bill(menu))
        
        choice = input("\nTHANK YOU FOR YOUR ORDER. DO YOU WANT TO ORDER MORE? (Y/N): ").lower()
        if choice == "n":
            break

place_order(menu)
