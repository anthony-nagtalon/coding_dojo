class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100
    
    def display_info(self):
        print("{} ({})".format(self.name, self.__class__.__name__))
        print("Age: {}".format(self.age))
        print("Health: {} | Happiness: {}".format(self.health, self.happiness))
        return self
    
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

class Bird(Animal):
    def __init__(self, name, color, age = 0):
        super().__init__(name, age)
        self.color = color
    
    def display_info(self):
        super().display_info()
        print("Color: {}".format(self.color))

class Lion(Animal):
    def __init__(self, name, age = 0):
        super().__init__(name, age)
        self.groomed = True
        self.steak_count = 0

    def display_info(self):
        super().display_info()
        print("Groomed: {}".format(self.groomed))
        print("Steak Count: {}".format(self.steak_count))

class Panda(Animal):
    def __init__(self, name, age = 0):
        super().__init__(name, age)
        self.bamboo_count = 10
    
    def display_info(self):
        super().display_info()
        print("Bamboo: {}".format(self.bamboo_count))
        
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_bird(self, name, color):
        self.animals.append( Bird(name, color) )

    def add_lion(self, name):
        self.animals.append( Lion(name) )

    def add_panda(self, name):
        self.animals.append( Panda(name) )

    def print_all_info(self):
        print("-" * 10, self.name, "-" * 10)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Out the Wa-Zoo")
zoo1.add_bird("Polly", "Blue")
zoo1.add_lion("Simba")
zoo1.add_panda("Po")
zoo1.add_panda("Chris")
zoo1.print_all_info()