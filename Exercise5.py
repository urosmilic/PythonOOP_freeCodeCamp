import csv


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

    @classmethod
    def instantiate_from_csv_file(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(name=item.get("name"),
                     price=float(item.get("price")),
                     quantity=int(item.get("quantity"))
                     )

    @staticmethod
    def is_number_integer(number):
        if isinstance(number, int):
            return True
        else:
            return False

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_price_after_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):  # method to format object representation in the console
        return f"Item({self.name}, {self.price}, {self.quantity})"


print(Item.is_number_integer(18.5))
print(Item.is_number_integer(18))
