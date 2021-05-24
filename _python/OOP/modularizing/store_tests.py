import store
import product

# Testing:
store1 = store.Store("Nook's Cranny")
prod1 = product.Product("Shovel", 100, "Tools")
prod2 = product.Product("Slingshot", 200, "Tools")
prod3 = product.Product("Red Tulip Seeds", 30, "Seeds")
prod4 = product.Product("Minimalist Lamp", 500, "Furniture")
prod5 = product.Product("Anorak Jacket", 1400, "Clothing")
prod6 = product.Product("Annyeong Tee", 640, "Clothing")

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
