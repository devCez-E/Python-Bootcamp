import data

quarters = 0
dimes = 0
nickles = 0
pennies = 0
main_resources = data.resources

def get_report():
    for resource in main_resources:
        if resource == "coffee":
            print(f"{resource.capitalize()}: {main_resources[resource]}g")
        else:
            print(f"{resource.capitalize()}: {main_resources[resource]}ml")

def calculate_resources(choice):
    isExist = True

    for resource in main_resources:
        if choice == "espresso" and resource == "milk":
            continue

        if main_resources[resource] >= data.MENU[choice]["ingredients"][resource]:
            continue
        else:
            print(f"Sorry there is not enough {resource}.")
            isExist = False
            break

    if isExist : calculate_money(choice)

def use_resource(choice):
    for resource in main_resources:
        if choice == "espresso" and resource == "milk":
            continue
        main_resources[resource] -= data.MENU[choice]["ingredients"][resource]

def calculate_money(choice):
    global quarters, dimes, nickles, pennies

    quarters = int(input("How many quaters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total > data.MENU[choice]['cost']:
        use_resource(choice)
        print(f"Here is ${round(total - data.MENU[choice]['cost'], 2)} in change.")
        print(f"Here is your {choice}. Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")


#----------MAIN----------

while(main_resources["water"] > 49 and main_resources["coffee"] > 17):
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if data.MENU.get(choice) or choice == "report":
        if choice == "report": get_report()
        else: calculate_resources(choice)
    else:
        print("We don't have menu what you choice.")
        break
