from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken=0):
        super().__init__(name, price, quantity)
        self.broken = broken
        assert broken >= 0, "{broken} should be greater or equals to 0!"

    def calculate_total_price(self):
        return (self.quantity - self.broken) * self.price + self.broken * self.price * 0.5

    def calculate_not_broken_phones(self):
        return self.quantity - self.broken
