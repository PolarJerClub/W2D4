import random

shop_cart = {}

random_add = ["Here ya go!", "Voila!", "Pop goes the weasel!", "Shazam!", "BOOM BABY!"]
random_remove = ["I'll take that!", "Up Up and Away!", "Go'n Git!", "Get outta my garbage", "Sayonara Sucka!"]

def add_item():
    item = input("What would you like to add? ")
    quantity = int(input(f"how many {item} would you like? "))
    print(random.choice(random_add))

    if item not in shop_cart:
        shop_cart[item] = quantity

def remove_item():
    item = input("What would you like to remove?")
    del shop_cart[item]
    print(random.choice(random_remove))

def see_cart():
    print(shop_cart)

def checkout(cart):
    print("Thanks for shopping!")
    print("Your cart:")
    for item, quantity in shop_cart.items():
        print("{} ({})".format(item, quantity))

while True:
    welcome = input("Welcome to your shopping cart! Tell me if you would like to add, remove, or show items in your shopping cart: ")

    if welcome.lower() == 'add':
        add_item()
    
    elif welcome.lower() == 'remove':
        remove_item()
    
    elif welcome.lower() == 'show':
        see_cart()
    
    elif welcome.lower() == 'quit':
        checkout(shop_cart)
        break
    else:
        print("Please enter add, remove, show, or quit")