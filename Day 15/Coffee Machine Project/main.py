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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}


money = 0

COIN_VALUES = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

customer_input = input("What would you like? (espresso/latte/cappuccino): ")

if customer_input == "off":
    exit()

elif customer_input == "report":
    for item, amount in resources.items():
        print(f"{item.title()}: {amount}")

    print(f"Money: ${money}")

elif customer_input in ["espresso", "latte", "cappuccino"]:

    print("Please insert coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = (
        quarters * COIN_VALUES["quarters"]
        + dimes * COIN_VALUES["dimes"]
        + nickles * COIN_VALUES["nickles"]
        + pennies * COIN_VALUES["pennies"]
    )

    money += total

    MENU[customer_input]["ingredients"]

