import beverages
import random


class CoffeeMachine:
    def __init__(self):
        self.count_cup = 0

    class EmptyCup(beverages.HotBeverage):
        def __init__(self, price=0.90, name='empty cup', description='An empty cup?! Gimme my money back!'):
            super().__init__(price, name, description)

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired.')

    def repair(self):
        self.count_cup = 0

    def serve(self, instance):
        if self.count_cup >= 10:
            raise self.BrokenMachineException
        self.count_cup += 1
        return random.choice([instance, self.EmptyCup()])


def tests():
    machine = CoffeeMachine()
    coffee = beverages.HotBeverage(0.40, 'coffee', 'A coffee, to stay awake.')
    tea = beverages.HotBeverage(name='tea')
    chocolate = beverages.HotBeverage(0.50, 'chocolate', 'Chocolate, sweet chocolate...')
    cappuccino = beverages.HotBeverage(0.45, 'cappuccino', 'Unpo\' di Italia nella sua tazza!')
    try:
        for i in range(11):
            print(machine.serve(random.choice([coffee, tea, chocolate, cappuccino])))
    except machine.BrokenMachineException as e:
        print('------------------------')
        print(e)
        print('------------------------')
        machine.repair()
    finally:
        print(machine.serve(random.choice([coffee, tea, chocolate, cappuccino])))


if __name__ == '__main__':
    tests()