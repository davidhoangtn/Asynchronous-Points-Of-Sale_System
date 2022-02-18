"""
Combos: any combination of any burger, side and drink 
    _most expensive items are added to combos first

display_catalogue(catalogue): output all items in the catalogue
    _in main.py

show_catalogue(catalogue): display all item_id in the catalogue

User Interface:
    Start: by welcoming the customer and displaying the catalogue

    User will be prompted to enter one item number at a time and 
    have their input validated
        _no delay that user have to wait before adding another
        item to their order
    
    Place their order by entering "q"
        _validate that there is sufficient stock of the items
        and inform them if an item is out of stock

    Order passed: create any possible combos and display an 
    order summary 
        _(outline combo and their price as well
        as individual item)

    Display subtotal, tax and total (subtotal + tax)
        _tax rate = 5%
    
    Confirm they would like to purchase this order
        _After purchasing or declining purchase, program
        should ask them if they would like to order again

"""

async def make_order(ORDERS = {}):
    order = {}
    drinks = []
    burgers = []
    sides = []
    combo = []
    if not ORDERS: 
        return
    else:
        for item_id, item in ORDERS.items():
            if item["category"] == "Drinks":
                drinks.append(item)
            elif item["category"] == "Burgers":
                burgers.append(item)
            else:
                sides.append(item)
        for i in range(1, 100):
            if drinks and burgers and sides:
                combo = []
                drink = drinks.pop(drinks.index(max(drinks, key=lambda x: x['price'])))
                burger = burgers.pop(burgers.index(max(burgers, key=lambda x: x['price'])))
                side = sides.pop(sides.index(max(sides, key=lambda x: x['price'])))
                combo.append(drink)
                combo.append(burger)
                combo.append(side)
                new_combo = combo.copy()
                order[f'combo{i}'] = new_combo
            else:
                break
        
        individual_items = drinks + burgers + sides
        order['individual_items'] = individual_items
        return order
        
async def print_order(order = {}):
    subtotal = 0
    tax = 0
    for key, value in order.items():
        if 'combo' in key: 
            combo_price = 0
            for item in value:
                combo_price += item['price']
                if item['category'] == 'Burgers':
                    burger = item['name']
                elif item['category'] == 'Sides':
                    sides = item['size'] + ' ' + item['subcategory']
                elif item['category'] == 'Drinks':
                    drinks = item['size'] + ' ' + item['subcategory']
            print(f"${round(combo_price*0.85, 2)} Burger Combo\n  {burger}\n  {sides}\n  {drinks}")    
            subtotal += combo_price*0.85
        if key == 'individual_items':
            item_price = 0
            for item in value:
                if item['category'] == 'Burgers':
                    ret = item['name']
                elif item['category'] == 'Sides':
                    ret = item['size'] + ' ' + item['subcategory']
                elif item['category'] == 'Drinks':
                    ret = item['size'] + ' ' + item['subcategory']
                item_price = item['price']
                print(f"${item_price} {ret}")
                subtotal += item_price
            tax = 0.05 * subtotal
            total = tax + subtotal
            print(f"Subtotal: ${round(subtotal, 2)}\nTax: ${round(tax, 2)}\nTotal: ${round(total, 2)}")

async def get_total_price(order = {}):
    subtotal = 0
    tax = 0
    for key, value in order.items():
        if 'combo' in key: 
            combo_price = 0
            for item in value:
                combo_price += item['price']
                if item['category'] == 'Burgers':
                    burger = item['name']
                elif item['category'] == 'Sides':
                    sides = item['size'] + ' ' + item['subcategory']
                elif item['category'] == 'Drinks':
                    drinks = item['size'] + ' ' + item['subcategory']
            # print(f"${round(combo_price*0.85, 2)} Burger Combo\n  {burger}\n  {sides}\n  {drinks}")    
            subtotal += combo_price*0.85
        if key == 'individual_items':
            item_price = 0
            for item in value:
                if item['category'] == 'Burgers':
                    ret = item['name']
                elif item['category'] == 'Sides':
                    ret = item['size'] + ' ' + item['subcategory']
                elif item['category'] == 'Drinks':
                    ret = item['size'] + ' ' + item['subcategory']
                item_price = item['price']
                # print(f"${item_price} {ret}")
                subtotal += item_price
            tax = 0.05 * subtotal
            total = tax + subtotal
            return round(total, 2)
