from sympy import product


class Customer:
    def __init__(self,name):
        self.name = name
class Product:
    def __init__(self,name,price):
        self.name =name
        self.price= price
class Order:
    def __init__(self,customer):
        self.customer= customer
        self.items=[]
    def add_product(self,product,quantity):
        if quantity<=0:
            print("invalid qnt")
            return 
        self.items.append((product,quantity))
        print(f"Product: {product.name} x {quantity}, added to the cart!")
    def calculate_total(self):
        total = 0
        for product,qty in self.items:
            total+=product.price *qty
        return total
    def show_order(self):
        print("Customer: ",self.customer.name)
        print("Items")
        for product,qty in self.items:
            print(f'{product.name}-{qty}x{product.price}')
        print("total: ",self.calculate_total())
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)
p3 = Product("Keyboard", 1500)

customer = Customer("Tejas")

order = Order(customer)

order.add_product(p1,1)
order.add_product(p2,2)
order.add_product(p3,1)

order.show_order()