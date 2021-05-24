import product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id = -1, unique_id = None):
        if not unique_id == None:
            index = self.check_unique_id(unique_id)
            if index < 0:
                print("Product \"{}\" does not exist!".format(unique_id))
            else:
                print("Sold:")
                self.products.pop(index).print_info()
        elif 0 <= id < len(self.products):
            print("Sold:")
            self.products.pop(id).print_info()
        else:
            print("Store \"{}\" does not have Product ID #{}".format(self.name, id))
        return self

    def check_unique_id(self, unique_id):
        for i in range(len(self.products)):
            if self.products[i].unique_id == unique_id:
                return i
        return -1

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self