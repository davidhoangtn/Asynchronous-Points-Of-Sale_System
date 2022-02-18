from ast import Num
import asyncio
from inventory import Inventory
import sys
from order_functions import make_order, print_order, get_total_price


def display_catalogue(catalogue):
    burgers = catalogue["Burgers"]
    sides = catalogue["Sides"]
    drinks = catalogue["Drinks"]

    print("--------- Burgers -----------\n")
    for burger in burgers:
        item_id = burger["id"]
        name = burger["name"]
        price = burger["price"]
        print(f"{item_id}. {name} ${price}")

    print("\n---------- Sides ------------")
    for side in sides:
        sizes = sides[side]

        print(f"\n{side}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n---------- Drinks ------------")
    for beverage in drinks:
        sizes = drinks[beverage]

        print(f"\n{beverage}")
        for size in sizes:
            item_id = size["id"]
            size_name = size["size"]
            price = size["price"]
            print(f"{item_id}. {size_name} ${price}")

    print("\n------------------------------\n")

# async def reset():
#     await main()

# async def make_order(ORDERS = {}):
#     order = {}
#     drinks = []
#     burgers = []
#     sides = []
#     combo = []
#     if not ORDERS: 
#         return
#     else:
#         for item_id, item in ORDERS.items():
#             if item["category"] == "Drinks":
#                 drinks.append(item)
#             elif item["category"] == "Burgers":
#                 burgers.append(item)
#             else:
#                 sides.append(item)
#         for i in range(1, 100):
#             if drinks and burgers and sides:
#                 combo = []
#                 drink = drinks.pop(drinks.index(max(drinks, key=lambda x: x['price'])))
#                 burger = burgers.pop(burgers.index(max(burgers, key=lambda x: x['price'])))
#                 side = sides.pop(sides.index(max(sides, key=lambda x: x['price'])))
#                 combo.append(drink)
#                 combo.append(burger)
#                 combo.append(side)
#                 new_combo = combo.copy()
#                 order[f'combo{i}'] = new_combo
#             else:
#                 break
        
#         individual_items = drinks + burgers + sides
#         order['individual_items'] = individual_items
#         return order
        
# async def print_order(order = {}):
#     subtotal = 0
#     tax = 0
#     for key, value in order.items():
#         if 'combo' in key: 
#             combo_price = 0
#             for item in value:
#                 combo_price += item['price']
#                 if item['category'] == 'Burgers':
#                     burger = item['name']
#                 elif item['category'] == 'Sides':
#                     sides = item['size'] + ' ' + item['subcategory']
#                 elif item['category'] == 'Drinks':
#                     drinks = item['size'] + ' ' + item['subcategory']
#             print(f"${round(combo_price*0.85, 2)} Burger Combo\n  {burger}\n  {sides}\n  {drinks}")    
#             subtotal += combo_price*0.85
#         if key == 'individual_items':
#             item_price = 0
#             for item in value:
#                 if item['category'] == 'Burgers':
#                     ret = item['name']
#                 elif item['category'] == 'Sides':
#                     ret = item['size'] + ' ' + item['subcategory']
#                 elif item['category'] == 'Drinks':
#                     ret = item['size'] + ' ' + item['subcategory']
#                 item_price = item['price']
#                 print(f"${item_price} {ret}")
#                 subtotal += item_price
#             tax = 0.05 * subtotal
#             total = tax + subtotal
#             print(f"Subtotal: ${round(subtotal, 2)}\nTax: ${round(tax, 2)}\nTotal: ${round(total, 2)}")

# async def get_total_price(order = {}):
#     subtotal = 0
#     tax = 0
#     for key, value in order.items():
#         if 'combo' in key: 
#             combo_price = 0
#             for item in value:
#                 combo_price += item['price']
#                 if item['category'] == 'Burgers':
#                     burger = item['name']
#                 elif item['category'] == 'Sides':
#                     sides = item['size'] + ' ' + item['subcategory']
#                 elif item['category'] == 'Drinks':
#                     drinks = item['size'] + ' ' + item['subcategory']
#             # print(f"${round(combo_price*0.85, 2)} Burger Combo\n  {burger}\n  {sides}\n  {drinks}")    
#             subtotal += combo_price*0.85
#         if key == 'individual_items':
#             item_price = 0
#             for item in value:
#                 if item['category'] == 'Burgers':
#                     ret = item['name']
#                 elif item['category'] == 'Sides':
#                     ret = item['size'] + ' ' + item['subcategory']
#                 elif item['category'] == 'Drinks':
#                     ret = item['size'] + ' ' + item['subcategory']
#                 item_price = item['price']
#                 # print(f"${item_price} {ret}")
#                 subtotal += item_price
#             tax = 0.05 * subtotal
#             total = tax + subtotal
#             return round(total, 2)
async def reset():
    await main()

async def main():
    NUMBER_OF_ITEMS = await inventory.get_number_of_items()
    # Welcoming the customer and displaying the catalogue
    print("Welcome to the ProgrammingExpert Burger Bar!")
    print("Loading catalogue...")
    display_catalogue(inventory.catalogue)
    # tasks = asyncio.gather()

    print("Please enter the number of items that you would like to add to your order. Enter q to complete your order.")
    item_number = input("Enter an item number: ")
    items = {}
    while True:
        if item_number == "q":
            print("Placing order...")
            break
        elif item_number.isdigit() and int(item_number) in range(1, NUMBER_OF_ITEMS + 1):
            key = int(item_number)
            items[key] = items.get(key, 0) + 1
            item_number = input("Enter an item number: ")
        elif item_number.isdigit() and int(item_number) > NUMBER_OF_ITEMS:
            print("Please enter a number below 21.")
            item_number = input("Enter an item number: ")
        else: 
            print("Please enter a valid number.")
            item_number = input("Enter an item number: ")
    # Tasks need to gather: 
        # get_item(), get_stock(), decrement_stock()
        # output
    ORDERS = {}
    for item_id, quantity in items.items():
        item = await inventory.get_item(item_id)
        new_item = item.copy() 
        for i in range(1, quantity + 1):
            stock = await inventory.get_stock(item_id)
            if stock == 0: 
                print(f"Unfortunately item number {item_id} is out of stock and has been removed from your order. Sorry!")

            else:
                await inventory.decrement_stock(item_id)
                new_item['quantity'] = new_item.get(quantity, 0) + 1
        ORDERS[new_item["id"]] = new_item
    print("Here is a summary of your order:")
    task1 = await make_order(ORDERS)
    task2 = await print_order(task1)
    task3 = asyncio.create_task(get_total_price(task1))
    # print(task2)
    confirm_order = input(f'Would you like to purchase this order for ${await task3}" (yes/no)? ')
    if confirm_order.lower() == 'yes':
        print('Thank you for your order!')
    elif confirm_order.lower() == 'no':
        print('No problem, please come again!')
    next_order = input('Would your like to make another order (yes/no)? ')
    
    if next_order.lower() == 'yes':
        await reset()
    elif next_order.lower() == 'no':
        print("Goodbye!")
        sys.exit()

inventory = Inventory()

if __name__ == "__main__":
    asyncio.run(main())

