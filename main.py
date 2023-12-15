from item import Item
from phone import Phone

phone1 = Phone("iPhone 13 pro", 1000, 4, 1)
print(int(phone1.calculate_total_price()))   # here we have a method that includes broken phones with a discount of 50%
print(Item.calculate_total_price(phone1))
