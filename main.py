MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


# Function for processing coins
def insert_coins(money):
    global resources
    try:
        penny = int(input("How many pennies?: ")) * 0.01
        nickel = int(input("How many nickels?: ")) * 0.05
        dime = int(input("How many dimes?: ")) * 0.10
        quarter = int(input("How many quarters?: ")) * 0.25
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return False
    total = round(penny + nickel + dime + quarter, 2)
    if total >= money:
        resources["profit"] += money
        change = round(total - money, 2)
        if change > 0:
            print(f"Change: ${change}")
        return True
    else:
        print(f"Insufficient funds. I have refunded ${total}. Have a nice day!")


# Function to check if there are sufficient resources
def can_make_drink(drink):
    global resources
    if all(amount <= resources.get(ingredient, 0) for ingredient, amount in MENU[drink]["ingredients"].items()):
        if insert_coins(MENU[drink]["cost"]):  # call function to process coins
            for ingredient, amount in MENU[drink]["ingredients"].items():
                resources[ingredient] -= amount
    else:
        print(f"Sorry, there are not enough resources to make this drink.")
        return False


operating = True
while operating:

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        coffee = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['profit']}")
    elif choice in ("espresso", "latte", "cappuccino"):
        if can_make_drink(choice):
            print(f"Here is your {choice}. Enjoy!")
    else:
        print("Invalid Input")
