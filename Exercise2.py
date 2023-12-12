class Item:
    pay_rate = 0.8  # price after the discount of 20%

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the assigned arguments
        assert price >= 0, f"assertion fails, {price} should be greater or equals to 0!"
        assert quantity >= 0, f"assertion fails, {quantity} should be greater or equals to 0!"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_price_after_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item2.color = "Red"
item2.pay_rate = 0.7

print(item1.name, item1.price, item1.quantity, item1.pay_rate)
print(item1.calculate_total_price())
item1.calculate_price_after_discount()
print(item1.calculate_total_price())
print("===============================")

print(item2.name, item2.price, item2.quantity, item2.pay_rate, item2.color)
print(f"Total {item2.name} price before discount:", item2.calculate_total_price())
item2.calculate_price_after_discount()
print(f"Total {item2.name} price after discount:", item2.calculate_total_price())
