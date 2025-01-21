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

class CoffeeMachine:
    def __init__(self, menu, resources):
        self.menu = menu
        self.resources = resources
        self.deposit = 0

    def check_available_resources(self, order):
        ingredients = self.menu[order]['ingredients']
        if ingredients['water'] < self.resources['water'] and ingredients.get('milk', 0) < self.resources['milk'] and ingredients['coffee'] < self.resources['coffee']:
            return True
        return False

    def get_payment(self):
        pennies = int(input('Please insert the pennies: '))*0.01
        dimes = int(input('Please insert the dimes: '))*0.10
        quarters = int(input('Please insert the quarters: '))*0.25

        self.deposit = pennies + dimes + quarters
        print(f"You have submitted total ${self.deposit}.")


    def check_total_cost(self, order):
        cost = self.menu[order]['cost']
        if cost > self.deposit:
            print(f'You have not provided enough money. Please provide ${cost - self.deposit} to continue.')
            return False
        else:
            return True

    def update_available_resources(self, order):
        ingredients = self.menu[order]['ingredients']
        self.resources['water'] = self.resources['water'] -  ingredients['water']
        self.resources['milk'] = self.resources['milk'] - ingredients.get('milk', 0)
        self.resources['coffee'] = self.resources['coffee'] - ingredients['coffee']

    def update_resources(self):
        water = int(input('How much water would you like to add: '))
        milk = int(input('How much milk you wouild like to add: '))
        coffee = int(input('How much coffee you would like to add: '))

        self.resources['water'] += water
        self.resources['milk'] += milk
        self.resources['coffee'] += coffee

    def take_order(self):
        order = input("What would you like? (espresso/latte/cappuccino): ")
        is_resource_available = self.check_available_resources(order)
        if is_resource_available:
            self.get_payment()
            is_money_sufficient = self.check_total_cost(order)
            if is_money_sufficient:
                print(f'Here is your {order} 🍵. Enjoy...')
                self.update_available_resources(order)
                
            should_continue = input('Would you like to make another order?: ')
            if should_continue == 'yes':
                return True
            else:
                return False
        else:
            print('Sorry 😒😒, We are out of Coffee. We are on it...')
            return False

    def process_order(self):
        should_continue = True

        while should_continue:
            while True:
                user_input = input('What would you like to do (report, order, update): ').lower()
                if user_input in ['report', 'order', 'update']:
                    break
                else:
                    print('Please enter either Report or Order or Update.')
            if user_input == 'report':
                print('The current resoueces available are:\n')
                for k, v in self.resources.items():
                    print(f'{k}: {v}')
            elif user_input == 'update':
                self.update_resources()
                print('The current resoueces available are:\n')
                for k, v in self.resources.items():
                    print(f'{k}: {v}')
            else:
                should_continue = self.take_order()


if __name__ == "__main__":
    coffee_machine  = CoffeeMachine(MENU, resources)
    coffee_machine.process_order()