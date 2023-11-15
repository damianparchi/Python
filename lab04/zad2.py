from zad1 import Pizza

class Slice(Pizza):
    def __init__(self, diameter, toppings=None, how_many_slices=6):
        super().__init__(diameter, toppings)
        self._how_many_slices = 0
        self.how_many_slices = how_many_slices

    @property
    def how_many_slices(self):
        return self._how_many_slices

    @how_many_slices.setter
    def how_many_slices(self, value):
        if value < 4 or value > 12 or value % 2 != 0:
            print("Błędna ilość kawałków. Program kończy działanie.")
            exit(-10)

        self._how_many_slices = value

    def part_price(self, ordered_slices):
        if ordered_slices > self._how_many_slices:
            print("Błędna liczba zamówionych kawałków. Program kończy działanie.")
            exit(-10)

        total_slices = self._how_many_slices
        price_per_slice = self._price / total_slices
        return price_per_slice * ordered_slices

    def __repr__(self):
        pizza_info = super().__repr__()
        return f"{pizza_info}kawałki {self._how_many_slices} cena za kawałek {self._price / self._how_many_slices}"

sliced_pizza = Slice(diameter=30, toppings=["ser", "szynka", "pieczarki"], how_many_slices=6)

print(sliced_pizza)

ordered_slices = 3
price_for_slices = sliced_pizza.part_price(ordered_slices)
print(f"Cena za {ordered_slices} kawałki: {price_for_slices}")