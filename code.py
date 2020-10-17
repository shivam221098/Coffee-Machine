# Write your code here
# Comments
"""
print('''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!''')
water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))
no_of_cups = min(water // 200, milk // 50, beans // 15)
if cups == no_of_cups:
    print("Yes, I can make that amount of coffee")
elif no_of_cups > cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)".format(no_of_cups - cups))
else:
    print("No, I can make only {} cups of coffee".format(no_of_cups))
"""
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def water_check(x):  # for checking availability of water
    return True if water // x > 0 else False


def milk_check(x):  # for checking availability of milk
    return True if milk // x > 0 else False


def beans_check(x):  # for checking availability of coffee beans
    return True if beans // x > 0 else False


def buy():
    global water
    global milk
    global beans
    global money
    global cups
    category = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if category == "1":
        if not water_check(250):
            print("Sorry, not enough water!")
        elif not beans_check(16):
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
    elif category == "2":
        if not water_check(350):
            print("Sorry, not enough water!")
        elif not milk_check(75):
            print("Sorry, not enough milk!")
        elif not beans_check(20):
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
    elif category == "3":
        if not water_check(200):
            print("Sorry, not enough water!")
        elif not milk_check(100):
            print("Sorry, not enough milk!")
        elif not beans_check(12):
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
    elif category.lower() == "back":
        main()
    else:
        pass
    main()


def fill():  # is used for filling resources again
    global water
    global milk
    global beans
    global money
    global cups
    water += int(input("Write how many ml of water do you want to add: "))
    milk += int(input("Write how many ml of milk do you want to add: "))
    beans += int(input("Write how many grams of coffee beans do you want to add: "))
    cups += int(input("Write how many disposable cups of coffee do you want to add: "))


def take():  # is used for taking money from the machine
    global money
    print("I gave you ${}".format(money))
    money = 0


def print_():  # is used for printing of all the resources
    print("The coffee machine has: ")
    print("{} of water ".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans ".format(beans))
    print("{} of disposable cups".format(cups))
    print("{} of money".format(money))


def main():  # its not a main function, the real main function is below this function
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action.lower() == "buy":
        buy()
    elif action.lower() == "fill":
        fill()
    elif action.lower() == "take":
        take()
    elif action.lower() == "remaining":  # if we got remaining as input then we are calling print()_ function
        print_()
    elif action.lower() == "exit":
        exit(0)
    else:
        pass


while True:  # our main function (❁´◡`❁)
    main()
