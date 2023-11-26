"""
Name: Jasroop Singh
Project: Final Project
Class: CS 2520.01
"""

from ItemToPurchase import ItemToPurchase

print("")
print("Item 1")

name1 = input("Please enter the item name: ")
price1 = float(input("Please enter the item price: "))
qty1 = int(input("Please enter the item quantity: "))
desc1 = input("Please enter the item description: ")

item1 = ItemToPurchase(name1, price1, qty1, desc1)

print("")
print("Item 2")

name2 = input("Please enter the item name: ")
price2 = float(input("Please enter the item price: "))
qty2 = int(input("Please enter the item quantity: "))
desc2 = input("Please enter the item description: ")

item2 = ItemToPurchase(name2, price2, qty2, desc2)

print()
item1.print_item_cost()
item2.print_item_cost()

totalCost = (price1 * qty1) + (price2 * qty2)
print()
print("Total Cost: $" + str(totalCost))
