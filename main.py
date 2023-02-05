from sandwich_maker import SandwichMaker
from cashier import Cashier
import data

### Data ###

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

### Make an instance of SandwichMachine class and write the rest of the codes ###

sandwichMachine = SandwichMachine(data.resources)
resources = data.resources
recipes = data.recipes
sandwichMaker_instance = SandwichMaker()
cashier_instance = Cashier()

on = True
canMake = False

while on == True:
    inpt = input(
        "What would you like? small/medium/large? Type 'resources' to view current resources, 'off' to turn program off ")
    if inpt == "small":
        print("You chose small")
        canMake = sandwichMaker_instance.check_resources(data.recipes["small"])
        if canMake:
            payment = cashier_instance.process_coins()
            cost = data.recipes["small"]["cost"]
            # print(cost)
            coversCost = cashier_instance.transaction_result(payment, data.recipes["small"]["cost"])
            if coversCost:
                sandwichMaker_instance.make_sandwich("small", data.recipes["small"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Bread: ", data.resources["bread"])
                print("Ham: ", data.resources["ham"])
                print("Cheese: ", data.resources["cheese"])
                print("Your small sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money")
    if inpt == "medium":
        print("You chose medium")
        canMake = sandwichMaker_instance.check_resources(data.recipes["medium"])
        if canMake:
            payment = cashier_instance.process_coins()
            cost = data.recipes["medium"]["cost"]
            # print(cost)
            coversCost = cashier_instance.transaction_result(payment, data.recipes["medium"]["cost"])
            if coversCost:
                sandwichMaker_instance.make_sandwich("medium", data.recipes["medium"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Bread: ", data.resources["bread"])
                print("Ham: ", data.resources["ham"])
                print("Cheese: ", data.resources["cheese"])
                print("Your medium sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money");
    if inpt == "large":
        print("You chose large")
        canMake = sandwichMaker_instance.check_resources(data.recipes["large"])
        if canMake:
            payment = cashier_instance.process_coins()
            cost = data.recipes["large"]["cost"]
            # print(cost)
            coversCost = cashier_instance.transaction_result(payment, data.recipes["large"]["cost"])
            if coversCost:
                sandwichMaker_instance.make_sandwich("large", data.recipes["large"]["ingredients"])
                print("That comes out to $", payment - cost, " in change")
                print("Bread: ", data.resources["bread"])
                print("Ham: ", data.resources["ham"])
                print("Cheese: ", data.resources["cheese"])
                print("Your large sandwich is ready. Bon appetit!")
            if coversCost == False:
                print("You don't have enough money")
    if inpt == "resources":
        print("Bread: ", data.resources["bread"])
        print("Ham: ", data.resources["ham"])
        print("Cheese: ", data.resources["cheese"])