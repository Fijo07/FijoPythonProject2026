# 3 wayws, pice x no of ordrd, no of pck x no of item/item is pck, qty + etra loss on trimming cut coner
from math import floor


#Let's start with the following problem.
# In the online store we have products available, which, depending on the type, are priced based on the:
# 1. Number of pieces (piece price x number of pieces ordered)
# 2. Number of packages (package price * (number of ordered items / number of items in a package rounded up))
# 3. Quantity + extra extra % loss on trimmings, cut corners etc.
# Start with the dictionary we know, i.e. a variable that contains data in the format
# "key": "value", which stores the product parameters:


# functions
def piece_or_pack_ask():
    print("Enter no of pieces")
    return int(input())

def amount_ask(unit_name):
    print("Enter quanity ({})".format(unit_name))
    return floor(int(input()))

def piece_print(quantity):
    print("you ordered {} quanitity".format(quantity))

def pack_print(quantity, pack_size):
    packs = int((quantity + pack_size -1) / pack_size)
    print("ordered {} the no of packs".format(packs))

def amount_print(quantity, unit):
    print("You ordered {} quanityt".format(quantity, unit))

def price_piece(price, quantity):
    return price * quantity

def price_pack(price, pack_size, quantity):
    packs = int((quantity + pack_size - 1) / pack_size)
    return packs * price

def price_amount(price, loss, quantity):
    return price * quantity * (1 + loss)



#Varaiables
#collection
products = {
    "paint_can": {"price": 60}, # product with art price
    "paint_brush": {"price": 45}, # product with art price
    "floor_tiles_white": {"price": 120, "size": 15},# product with price in pck
    "floor_tiles_black": {"price": 140, "size": 20},# product with price in pck
    "planks": {"price": 80, "loss": 0.1, "unit": "meters"},# product with price with qty with loss
    "concrete": {"price": 60, "loss": 0.05, "unit": "kgs"}, # product with price with qty with loss
}

#set
products_piece = {"paint_can", "paint_brush"}
products_pack = {"floor_tiles_white", "floor_tiles_black"}
products_amount = {"planks", "concrete"}


total_price = 0

while True:
    product = input("What product would you like? or leave blank line if you wnat to end")

    if not product:
        break

    if product not in products:
        print("wrong product anme, avalialbel prdts:")
        print("\n".join(products.keys()))

    if product in products_piece or product in products_pack:
        quantity = piece_or_pack_ask()
    if product in products_amount:
        quantity = amount_ask(products[product]["unit"])



    if product in products_piece:
        piece_print(quantity)
    if product in products_pack:
        pack_print(quantity, products[product]["size"])
    if product in products_amount:
        amount_print(quantity, products[product]["unit"])

    #calc
    if product in products_piece:
        total_price += price_piece(products[product]["price"], quantity)

    if product in products_pack:
        total_price += price_pack(products[product]["price"], products[product]["size"], quantity)

    if product in products_amount:
        total_price += price_amount(products[product]["price"], products[product]["loss"], quantity)

print("total order cost {}".format(total_price))


