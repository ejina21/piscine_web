class HotBeverage:
    def __init__(self, price=0.30, name='hot beverage', description='Just some hot water in a cup.'):
        self.price = price
        self.name = name
        self.descr = description

    def description(self):
        return self.descr

    def __str__(self):
        return f'name : {self.name}\nprice : {self.price}\ndescription : {self.description()}'


def tests():
    coffee = HotBeverage(0.40, 'coffee', 'A coffee, to stay awake.')
    tea = HotBeverage(name='tea')
    chocolate = HotBeverage(0.50, 'chocolate', 'Chocolate, sweet chocolate...')
    cappuccino = HotBeverage(0.45, 'cappuccino', 'Unpo\' di Italia nella sua tazza!')
    print(coffee)
    print(tea)
    print(chocolate)
    print(cappuccino)


if __name__ == '__main__':
    tests()