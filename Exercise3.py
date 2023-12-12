class Item:
    pay_rate = 0.8  # price after the discount of 20%
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the assigned arguments
        assert price >= 0, f"assertion fails, {price} should be greater or equals to 0!"
        assert quantity >= 0, f"assertion fails, {quantity} should be greater or equals to 0!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # add instance to the list of all instances
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_price_after_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):  # method to format object representation in the console
        return f"Item({self.name}, {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("TV", 500, 2)
item4 = Item("Headphones", 80, 8)
item5 = Item("Keyboard", 40, 4)

print(Item.all)
