from punkt import Punkt

class NazwanyPunkt(Punkt):
    __slots__ = ('_nazwa',)

    def __init__(self, x=0, y=0, nazwa=""):
        super().__init__(x, y)
        self._nazwa = nazwa

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, value):
        self._nazwa = value

    @nazwa.deleter
    def nazwa(self):
        del self._nazwa

    def __repr__(self):
        return f'NazwanyPunkt({self._x}, {self._y}, "{self._nazwa}")'

    def __str__(self):
        return f'({self._x}, {self._y}, "{self._nazwa}")'
