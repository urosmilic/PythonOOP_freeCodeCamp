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
        return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken=0):
        super().__init__(name, price, quantity)
        self.broken = broken
        assert broken >= 0, "{broken} should be greater or equals to 0!"

    def calculate_not_broken_phones(self):
        return self.quantity - self.broken


phone1 = Phone("iPhone 13", 700, 5, 3)
phone2 = Phone("iPhone 14", 900, 4, 1)
phone3 = Phone("iPhone 15", 1200, 3)

print(Phone.all)
print("Total number of unbroken phones is", phone1.calculate_not_broken_phones() +
      phone2.calculate_not_broken_phones() + phone3.calculate_not_broken_phones())
