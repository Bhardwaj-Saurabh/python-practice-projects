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

money = {
    "value": 0,
}

class CoffeeMachine:
    def __init__(self, menu, resoueces):
        self.menu = menu
        self.resoueces = resoueces
        self.deposit = 0

    def check_available_resources(self, order):
        ingredients = self.menu[order]['ingredients']
        if ingredients['water'] < self.resoueces['water'] and ingredients.get('milk', 0) < self.resoueces['milk'] and ingredients['coffee'] < self.resoueces['coffee']:
            return True
        return False

    def get_payment(self):
        pennies = int(input('Please insert the pennies: '))*0.01
        dimes = int(input('Please insert the dimes: '))*0.10
        quarters = int(input('Please insert the quarters: '))*0.25

        total = pennies + dimes + quarters
        print(f"You have submitted total ${total}.")
        return total


    def check_total_cost(total_payment, order):
        cost = MENU[order]['cost']
        if cost > total_payment:
            print(f'You have not provided enough money. Please provide ${cost - total_payment} to continue.')
            return False
        else:
            return True

    def update_available_resources(order):
        ingredients = MENU[order]['ingredients']
        resources['water'] = resources['water'] -  ingredients['water']
        resources['milk'] = resources['milk'] - ingredients.get('milk', 0)
        resources['coffee'] = resources['coffee'] - ingredients['coffee']


    def coffee():
        order = input("What would you like? (espresso/latte/cappuccino): ")
        is_resource_available = check_available_resources(order)
        if is_resource_available:
            total_payment = get_payment()
            is_money_sufficient = check_total_cost(total_payment, order)
            if is_money_sufficient:
                print(f'Here is your {order} 🍵. Enjoy...')
                update_available_resources(order)
            should_continue = print('Would you like to make another order?')
            if should_continue == 'yes':
                return True
            else:
                return False
        else:
            print('Sorry 😒😒, We are out of Coffee. We are on it...')
            return False


    should_continue = False

    while not should_continue:
        user_input = input('What would you like to do (report, order)').lower()
        if user_input == 'report':
            print('The current resoueces available are:\n')
            for k, v in resources.items():
                print(f'{k}: {v}')
        else:
            should_continue = coffee()
