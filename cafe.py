# create a list called menu
menu = []

# request the user to enter at least items into the menu
menu_items = int(input("How many menu items do you want to enter? "))

while menu_items < 4:
    print("Please enter a valid number of items (at least 4).")
    menu_items = int(input("How many menu items do you want to enter? "))

# request the user to input each menu item
for i in range(menu_items):
    item = input("Please enter a menu item: ")
    menu.append(item.capitalize())

# output the list of menu items
print(f"The menu is as follows: {menu}")

# create a dictionary called stock to contain the stock value of each menu item
stock = {}
for item in menu:
    quantity = int(input(f"Enter the stock quantity for {item}: "))
    stock[item] = quantity

# create a dictionary called price to store the price for each menu item
price = {}
for item in menu:
    sell_p = float(input(f"Enter the price for {item}: R "))
    price[item] = sell_p

# determine the total value of the stock and store in a variable called total_stock
total_stock = 0
stock_val = {}
for item in menu:
    item_value = round(float(stock[item] * price[item]), 2)
    print(f"The total value of the {item} to be kept in stock is: R{item_value}")
    stock_val(item) = item_value
    total_stock += item_value

print(f"The total value of stock in the cafe is: R {total_stock}")
