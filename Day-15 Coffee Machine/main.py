from Dict import Menu, resources


# todo: Turn off / Print report
def print_resource():
    if choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}ml")


# todo: Check whether resources are sufficient?
def sufficient(option):
    if Menu[option]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return True
    if Menu[option]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return True
    if Menu[option]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return True
    # for item in option:
    #     if option[item] >= resources[item]:
    #         print(f"Sorry there is not enough {item}.")
    #         return True
    else:
        return False


# todo: Calculate the change.
def calculation(option):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    if total > Menu[option]["cost"]:
        total -= Menu[option]["cost"]
        print(f"Here is ${round(total, 2)} the change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return True


# todo: resources calculation
def res(resource, option):
    for key in Menu[option]["ingredients"]:  # Loop is not repeating, do solve the fault
        resource[key] -= Menu[option]["ingredients"][key]
        return resource[key]


# todo: Main Loop
while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    print_resource()
    if choice == "report":
        continue
    con = sufficient(choice)
    if con:
        continue

    refund = calculation(choice)
    if refund:
        continue

    res(resources, choice)
    print(f"Here is your {choice} ☕ Enjoy!")
