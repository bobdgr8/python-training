def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


public class Fraction:
    """Implements a fraction class which has a numerator and a denominator"""

    def __init__(self, top=0, bottom=1):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherFraction):
        newnum = self.num * otherFraction.den + self.den * otherFraction.num
        newden = self.den * otherFraction.den

        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
