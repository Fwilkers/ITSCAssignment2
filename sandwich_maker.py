import data

class SandwichMaker:

    def check_resources(self, ingredients):
        breadCost = data.resources['bread'] - ingredients['ingredients']['bread']
        # print(breadCost)
        hamCost = data.resources['ham'] - ingredients['ingredients']['ham']
        # print(hamCost)
        cheeseCost = data.resources['ham'] - ingredients['ingredients']['cheese']
        # print(cheeseCost)
        if (breadCost < 0):
            print("Not enough bread for this order. Please restock")
            return False
        if (hamCost < 0):
            print("Not enough ham for this order. Please restock")
            return False
        if (cheeseCost < 0):
            print("Not enough cheese for this order. Please restock")
            return False
        return True
        """Returns True when order can be made, False if ingredients are insufficient."""

    def make_sandwich(self, sandwich_size, order_ingredients):
            """Deduct the required ingredients from the resources.
               Hint: no output"""
            data.resources['bread'] = data.resources['bread'] - order_ingredients['bread']
            data.resources['ham'] = data.resources['ham'] - order_ingredients['ham']
            data.resources['cheese'] = data.resources['cheese'] - order_ingredients['cheese']