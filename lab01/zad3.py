import math

class SodaCan:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def get_surface_area(self):
        #pole powierzchni puszki, które składa się z góry i dołu i powierzchni bocznej.
        #góra i dół to dwa koła o promieniu r, a powierzchnia boczna to prostokąt o wysokości h i obwodzie okręgu o promieniu r.
        gora_i_dol = 2 * math.pi * self.radius**2
        pole_boczne = 2 * math.pi * self.radius * self.height
        pole_calkowite = gora_i_dol + pole_boczne
        return pole_calkowite

    def get_volume(self):
        # objętość puszki = objętośc walca
        volume = math.pi * self.radius**2 * self.height
        return volume
    
# przykladowy obiekt klasy SodaCan o wysokości 10 i promieniu 5
soda_can = SodaCan(10, 5)

surface_area = soda_can.get_surface_area()
volume = soda_can.get_volume()

print(f"Pole powierzchni puszki: {surface_area:.2f}")
print(f"Objętość puszki: {volume:.2f}")