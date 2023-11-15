from zad1 import Pizza
from zad2 import Slice

def main():
    # Część dla klasy Pizza
    print("Część dla klasy Pizza:")

    p_1 = Pizza(diameter=30, toppings=["ser", "szynka"])
    p_2 = Pizza(diameter=25, toppings=["pieczarki", "cebula"])

    print("Reprezentacja obiektu p_1:")
    print(p_1)
    print("\nReprezentacja obiektu p_2:")
    print(p_2)

    p_1.diameter = 35
    p_1.add_topping("kurczak")

    print("\nZaktualizowana reprezentacja obiektu p_1:")
    print(p_1)

    print("\nCena pizzy p_1:", p_1.price)

    p_combined = p_1 + p_2
    print("\nWynik dodawania obiektów p_1 i p_2:")
    print(p_combined)

    print("\nCzęść dla klasy Slice:")

    #obiekt
    s_1 = Slice(diameter=30, toppings=["ser", "szynka", "pieczarki"], how_many_slices=6)

    print("Reprezentacja obiektu s_1:")
    print(s_1)

    ordered_slices = 5
    price_for_slices = s_1.part_price(ordered_slices)
    print(f"\nCena za {ordered_slices} kawałków s_1: {price_for_slices}")

if __name__ == "__main__":
    main()