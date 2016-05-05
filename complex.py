# the test program is in the main function
# this is for Python 3+

class Complex:

    def __init__(self, real, virl):
        self.real = real
        self.virl = virl

    def __str__(self):
        if self.real == 0 and self.virl == 0:
            return "0"
        elif self.real == 0:
            return str(self.virl) + "j"
        elif self.virl == 0:
            return str(self.real)
        elif self.virl > 0:
            if self.virl == 1:
                return str(self.real) + "+j"
            else:
                return str(self.real) + "+" + str(self.virl) + "j"
        else:
            if self.virl == -1:
                return str(self.real) + "-j"
            else:
                return str(self.real) + str(self.virl) + "j"

    # operator overloads
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.virl + other.virl)
        elif isinstance(other, int) or isinstance(other, float):
            return self + Complex(other, 0)
        else: # something is wrong
            raise TypeError('unsuported operand type')

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.virl - other.virl)
        elif isinstance(other, int) or isinstance(other, float):
            return self - Complex(other, 0)
        else: # something is wrong
            raise TypeError('unsuported operand type')

    def __neg__(self, other):
        return Complex(-self.real, -self.virl)


    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.real * other.real - self.virl * other.virl
            virl = self.real * other.virl + self.virl * other.real
            return Complex(real, virl)
        elif isinstance(other, int) or isinstance(other, float):
            return self * Complex(other, 0)
        else: # something is wrong
            raise TypeError('unsuported operand type')

    def __truediv__(self, other):
        if isinstance(other, Complex):
            result = self * Complex(other.real, -other.virl)
            ratio = other.real * other.real + other.virl * other.virl
            result.real /= ratio
            result.virl /= ratio
            return result
        elif isinstance(other, int) or isinstance(other, float):
            return self / Complex(other, 0)
        else: # something is wrong
            raise TypeError('unsuported operand type')


    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return Complex(0, 0) + other - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return Complex(1, 0) * other / self


#  test program
def main():
    a = Complex(1, 2)
    b = Complex(3, 4)

    print("a = %s" % (a))
    print("b = %s" % (b))

    # operators

    # two complex
    print("a + b = %s" % (a + b))
    print("a - b = %s" % (a - b))
    print("a * b = %s" % (a * b))
    print("a / b = %s" % (a / b))

    # complex with double
    print("a + 1 = %s" % (a + 1))
    print("a - 1 = %s" % (a - 1))
    print("a * 2 = %s" % (a * 2))
    print("a / 2 = %s" % (a / 2))

    # double with complex
    print("-3 + b = %s" % (-3 + b))
    print("3 - b = %s" % (3 - b))
    print("3 * b = %s" % (3 * b))
    print("3 / b = %s" % (3 / b))

main()







