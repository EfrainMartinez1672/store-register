update = []

def name():
    products1 = str(input("What product do you to sell?: "))
    price(products1)

def price(products1):
        try:
            price1 = float(input("enter the price of the product: "))
            quantity(products1, price1)
        except ValueError:
            print("Error, just enter numbers.")
            price(products1)

def quantity(products1, price1): 
        try:
            quantity1 = int(input("How many would you like purchase?: "))
            total_cost = quantity1 * price1
            update.append(f"name the product: {products1} | unit price: {price1} | quantity: {quantity1} | total cost: {total_cost}")
        except ValueError:
            print("Error, just enter integer numbers.")
            quantity(products1, price1)
name()
for dc in update:
    print(dc)


