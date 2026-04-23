class product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

class cart:
    def __init__(self):
        self.items = []
    def add_product(self,product):
        for item in self.items:
            if item.name ==product.name:
                item.price+=product.price
                return
        else:
            self.items.append(product)
            print(f"{product.name} added to cart.")
    def remove_product(self,product):
        for item in self.items:
            if item.name ==product.name:
                self.items.remove(item)
                print(f"{product.name} removed from cart.")
                return
        print(f"{product.name} not found in cart.")
    def total_price(self):
        total = sum(item.price for item in self.items)
        print(f"Total price: ${total}")
    def display_cart(self):
        print("Items in the cart:")
        for item in self.items:
            print(f"{item.name}: ${item.price}")

cart1 = product('laptop',10000)
cart2 = product('mobile',5000)
cart3 = product('headphones',2000)
cart4 = product('headphones',2000)

my_cart = cart()

my_cart.add_product(cart1)
my_cart.add_product(cart2)
my_cart.add_product(cart3)
my_cart.add_product(cart4)

my_cart.display_cart()
print()
my_cart.total_price()
print()
my_cart.remove_product(cart2)
print()
my_cart.display_cart()
print()
my_cart.total_price()   
print()
cart0 = product('tablet',3000)
my_cart.remove_product(cart0)

