class Cashier:

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins")
        money = 0.00
        dollars = input("How many dollars? ")
        d = float(dollars)
        money = money + d
        # print(money)
        half = input("How many half-dollars? ")
        h = float(half)
        money = money + (h * .5)
        # print(money)
        quarters = input("How many quarters? ")
        q = float(quarters)
        money = money + (q * .25)
        # print(money)
        nickels = input("How many nickels? ")
        n = float(nickels)
        money = money + (n * .05)
        print("You entered $", money)
        return money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##print(coins, cost)
        if coins >= cost:
            return True
        if coins < cost:
            return False