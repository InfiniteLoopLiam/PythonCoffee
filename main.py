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
}

coffee = True
while coffee:

    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        coffee = False
    elif choice == "report":
        for k, v in resources.items():
            print(k + ":", v)

    # TODO 4. Check resources sufficient?
    def can_make_drink(drink):
        global resources
        if all(amount <= resources.get(ingredient, 0) for ingredient, amount in MENU[drink]["ingredients"].items()):
            for ingredient, amount in MENU[drink]["ingredients"].items():
                resources[ingredient] -= amount
            print(f"Resources after making {drink}: {resources}")
            return True
        else:
            print("Sorry, there are not enough resources to make this drink.")
            return False

    print(can_make_drink(choice))
    print(resources)


# TODO 5. Process coins.

# TODO 6. Check transaction successful?

# TODO 7. Make Coffee.
