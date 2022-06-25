from cmath import pi
import decimal
from fractions import Fraction
from math import e 
#TIPOS DE NÚMEROS

# Integer
integer_number = 1
print(type(integer_number))
print(type(1))


# Float
float_number = 5757.56756
print(type(float_number))

# Complex
complex_number = 4.0+2.0j
print(type(complex_number))

# Boolean
boolean = False
print(type(boolean))

print(str(2**9))

#Ejemplo de flotantes
print(2e10)
print(3.1416e10)

#Errores en flotantes
sumaRara1 = 0.1 + 0.1 + 0.1 -0.3 
print(sumaRara1)

sumaRara2 = 0.1 + 0.2 
print(sumaRara2)

#DECINMALES 
#Primero se debe importar biblioteca decimal (se hará al inicio del programa) 
print(decimal.getcontext())

D = decimal.Decimal
print (str(D("0.1") + D("0.2")))

decimal.getcontext().prec = 5
#decimal.getcontext().rounding = decimal.ROUND_HALF_UP
# https://docs.python.org/3.10/library/decimal.html#module-decimal
x = D("1") / D("7")
print(x)  # 0.1428571429

decimal.getcontext().prec = 7
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
x = decimal.Decimal("1") / decimal.Decimal("7")
print(x)  # 0.1428571429
print(decimal.getcontext())


Fr = Fraction
print(Fr(1,2) + Fr(4,2))

print(Fraction(1,2) + Fraction(7,4))

Fraction_mas_fraction = (Fraction(1,2)) + (Fraction(7,4))
print(Fraction_mas_fraction)
# Fraction_to_decimal = D(Fraction_mas_fraction)
# print(Fraction_to_decimal)

# Fraction
value = Fraction(16,5)
print(value.numerator)
print(value.denominator)

#value = D(float(value))
#print(value)
#print(type(value))

def decimal_from_fraction(frac):
    return frac.numerator / D(value.denominator)

value2 = decimal_from_fraction(value)
print(value2)
print(type(value2))

#float as fraction
print((2.5).as_integer_ratio( ))


a = 5
b = 5.2 
c = decimal.Decimal(5.33)
d = Fraction(16,5)

e2 = c*3
print(e2)

f = c**a
print(f)

g = d/3
print(g)

print(pi)
print(e)

