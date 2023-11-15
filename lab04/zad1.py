import math

class Pizza:
    def __init__(self, diameter, toppings=None):
        if diameter < 20:
            print("Błędna średnica. Program kończy działanie.")
            exit(-10)

        self._diameter = diameter
        self._toppings = toppings if toppings else []
        self._price = self.calculate_price()

    @staticmethod
    def area(diameter):
        radius = diameter / 2
        return math.pi * (radius ** 2)

    def calculate_price(self):
        toppings_cost = len(self._toppings) * 2
        return 0.005 * self.area(self._diameter) + toppings_cost

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, new_diameter):
        if new_diameter < 20:
            print("Błędna średnica. Program kończy działanie.")
            exit(-10)

        self._diameter = new_diameter
        self._price = self.calculate_price()

    @property
    def toppings(self):
        return self._toppings

    def add_topping(self, topping):
        self._toppings.append(topping)
        self._price += 2

    @property
    def price(self):
        return self._price

    def __add__(self, other):
        if not isinstance(other, Pizza):
            raise ValueError("Można dodawać tylko obiekty klasy Pizza")

        new_diameter = max(self._diameter, other._diameter)
        new_toppings = self._toppings + other._toppings

        return Pizza(diameter=new_diameter, toppings=new_toppings)

    def __str__(self):
        if self._toppings:
            toppings_str = ", ".join(self._toppings)
            return f"Pizza: średnica: {self._diameter}, dodatki: {toppings_str}, cena: {self._price}"
        else:
            return f"Pizza: średnica: {self._diameter}, cena: {self._price}"

    def __repr__(self):
        if self._toppings:
            toppings_str = ", ".join(self._toppings)
            return f"Pizza: średnica: {self._diameter}, dodatki: {toppings_str}, cena: {self._price}"
        else:
            return f"Pizza: średnica: {self._diameter}, cena: {self._price}"

pizza1 = Pizza(diameter=30, toppings=["ser", "szynka", "pieczarki"])
pizza2 = Pizza(diameter=25, toppings=["oliwki", "papryka"])

print("Pizza 1:")
print(pizza1)

pizza1.diameter = 35
pizza1.add_topping("kurczak")

print("Zaktualizowana Pizza 1:")
print(pizza1)

print("\nPizza 2:")
print(pizza2)

pizza2.add_topping("pomidor")

print("Zaktualizowana Pizza 2:")
print(pizza2)

pizza_combined = pizza1 + pizza2

print("\nPołączona Pizza:")
print(pizza_combined)

print("\nPierwsza pizza:")
print(repr(pizza1))
