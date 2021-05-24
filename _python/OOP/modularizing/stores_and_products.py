class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        if 0 <= id < len(self.products):
            self.products.pop(id).print_info()
        else:
            print("Store \"{}\" does not have Product ID #{}".format(self.name, id))
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
    
    def print_info(self):
        print("Name: {}".format(self.name))
        print("Category: {}".format(self.category))
        print("Price: {}".format(self.price))

# Testing:
store1 = Store("Nook's Cranny")
prod1 = Product("Shovel", 100, "Tools")
prod2 = Product("Slingshot", 200, "Tools")
prod3 = Product("Red Tulip Seeds", 30, "Seeds")
prod4 = Product("Minimalist Lamp", 500, "Furniture")
prod5 = Product("Anorak Jacket", 1400, "Clothing")
prod6 = Product("Annyeong Tee", 640, "Clothing")

store1.add_product(prod1).add_product(prod2).add_product(prod3).add_product(prod4).add_product(prod5).add_product(prod6)

store1.sell_product(3)

store1.products[0].update_price(0.1, True)
store1.products[0].print_info()

store1.inflation(1)
for product in store1.products:
    product.print_info()
print()

store1.set_clearance("Clothing", 0.5)
for product in store1.products:
    product.print_info()
