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

profit = 0
resour = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resour_suffi(order_ingre):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingre:
        if order_ingre[item] > resour[item]:
            print(f"​Sorry there is not enough {item} in the stock.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please enter the coins:")
    tot = int(input("How many quarters?: ")) * 0.25
    tot += int(input("How many dimes?: ")) * 0.1
    tot += int(input("How many nickles?: ")) * 0.05
    tot += int(input("How many pennies?: ")) * 0.01
    return tot


def is_transac_success(money_recei, drnk_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recei >= drnk_cost:
        change = round(money_recei - drnk_cost, 2)
        print(f"Here is your ${change}")
        global profit
        profit += drnk_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingre):
    """Deduct the required ingredients from the resources."""
    for item in order_ingre:
        resour[item] -= order_ingre[item]
    print(f"Here is your {drink_name} ☕️. Enjoy your drink!")


is_on = True

while is_on:
    choice = (input("​What do you want to take? (Espresso/Latte/Cappuccino): ")).lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resour['water']}ml")
        print(f"Milk: {resour['milk']}ml")
        print(f"Coffee: {resour['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resour_suffi(drink["ingredients"]):
            payment = process_coins()
            if is_transac_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

#replit: https://replit.com/@Sapthak-Mohajon/CoffeeMachineCodepy#main.py
