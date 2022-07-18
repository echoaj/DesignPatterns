from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class ThreeCheezePizza(Pizza):
    description = "Mozzarella, Swiss, Parmesan Cheese Pizza"
    cost = 10.50

    def set_description(self, d):
        self.description = d
        
    def set_cost(self, c):
        self.cost = c

    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    

class PlainPizza(Pizza):
    def get_description(self):
        return "Thin dough"

    def get_cost(self):
        print("Dough cost: ", 6.00)
        return 6.00


class ToppingDecorator(Pizza):
    def __init__(self, new_pizza):
        self.temp_pizza = new_pizza

    def get_description(self):
        return self.temp_pizza.get_description()

    def get_cost(self):
        return self.temp_pizza.get_description()


class Mozzarella(ToppingDecorator):
    def __init__(self, new_pizza):
        super(Mozzarella, self).__init__(new_pizza)
        print("Adding Mozzerella")

    def get_description(self):
        return self.temp_pizza.get_description() + ", Mozzerella"

    def get_cost(self):
        print("Mozzerella cost: ", 0.50)
        return self.temp_pizza.get_cost() + 0.50


class TomatoSauce(ToppingDecorator):
    def __init__(self, new_pizza):
        super(TomatoSauce, self).__init__(new_pizza)
        print("Adding Tomato Sauce")

    def get_description(self):
        return self.temp_pizza.get_description() + ", Tomato Sauce"

    def get_cost(self):
        print("Tomato Sauce cost: ", 0.35)
        return self.temp_pizza.get_cost() + 0.35


basicPizza = TomatoSauce(Mozzarella(PlainPizza()))

print("Ingrediants: " + basicPizza.get_description())
print("Cost: ", basicPizza.get_cost())

print()

basicPizza = TomatoSauce(Mozzarella(ThreeCheezePizza()))

print("Ingrediants: " + basicPizza.get_description())
print("Cost: ", basicPizza.get_cost())







