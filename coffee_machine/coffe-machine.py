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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def report():
    for key, value in resources.items():
        print(key, ":", value)


def check_resource(drink):
    available = 0
    ingredients_items=0
    for drinks in MENU.keys():
        if drinks == drink:
            for key in resources.keys():
                if key in MENU[drinks]["ingredients"].keys():
                    ingredients_items +=1
                    if resources[key] >= MENU[drinks]["ingredients"][key]:
                        available += 1
                    else:
                        print(f"Sorry ther is not enough {key}")
    if available== ingredients_items:
        return  True
    else:
        return False


def process_coins(quart, dim, nik, pen):
    sum_coins = (quart * coins["quarters"] )+( dim * coins["dimes"] )+ (nik * coins["nickles"]) +(pen * coins["pennies"])
    return sum_coins


def check_transaction(inserted_money,drink):
    if inserted_money == MENU[drink]["cost"]:
        return True
    elif inserted_money > MENU[drink]["cost"]:
        remainder= inserted_money - MENU[drink]["cost"]
        return remainder,True
    else:
        return False


def make_coffee(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"].keys():
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    return resources


End_of_proccess= False
while End_of_proccess== False :
    answer = input("What would you like? (espresso/latte/cappuccino):")
    if answer.lower() == "report":
        report()
    elif answer.lower()== "espresso" or answer.lower()== "latte" or answer.lower()== "cappuccino":
        resource_check=check_resource(answer)
        print(resource_check)
        if resource_check ==True:
            print ("please insert your coins.")
            coin1 =int(input("how many quarters?"))
            coin2 =int(input("how many dimes?"))
            coin3 =int(input("how many nickles?"))
            coin4 =int(input("how many pennies?"))
            coins_process=process_coins(coin1,coin2,coin3,coin4)
            check_coins=check_transaction(coins_process,answer)
            if check_coins ==False:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is your {answer} ☕ enjoy")
                make_coffee(answer)

