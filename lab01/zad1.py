import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

class NamedPoint(Punkt):
    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.name = name

def main():
    punkt1 = Punkt(0, 0)
    punkt2 = NamedPoint(5, 12, "Point A")

    distance = Punkt.distance(punkt1, punkt2)

    print(f"Dystans między punktami to: {distance}")

if __name__ == "__main__":
    main()

