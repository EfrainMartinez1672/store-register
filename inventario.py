
def name():
    try:
        products1 = (input("What product do you to sell?: "))
        price()
    except ValueError:
        print("Error")

def price():
        try:
            price1 = float(input("enter the price of the product: "))
            quantity()
        except ValueError:
            print("Error, just enter numbers.")
            price()

def quantity(): 
        try:
            quantity1 = int(input("How many would you like purchase?: "))
        except ValueError:
            print("Error, just enter integer numbers.")
            quantity()

