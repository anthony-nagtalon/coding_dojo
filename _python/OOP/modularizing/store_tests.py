import store
import product

# Testing:
store1 = store.Store("Nook's Cranny")
prod1 = product.Product("Shovel", 100, "Tools", "shovel")
prod2 = product.Product("Slingshot", 200, "Tools", "slingshot")
prod3 = product.Product("Red Tulip Seeds", 30, "Seeds", "red_tulip_seeds")
prod4 = product.Product("Minimalist Lamp", 500, "Furniture", "minimalist_lamp")
prod5 = product.Product("Anorak Jacket", 1400, "Clothing", "anorak_jacket")
prod6 = product.Product("Annyeong Tee", 640, "Clothing", "annyeong_tee")

store1.add_product(prod1).add_product(prod2).add_product(prod3).add_product(prod4).add_product(prod5).add_product(prod6)

store1.sell_product(3)
print()

store1.products[0].update_price(0.1, True)
store1.products[0].print_info()
print()

store1.inflation(1)
for product in store1.products:
    product.print_info()
print()

store1.set_clearance("Clothing", 0.5)
for product in store1.products:
    product.print_info()
print()

store1.sell_product(unique_id = "anorak_jacket")
print()

store1.sell_product(unique_id = "blue_tulip_seeds")