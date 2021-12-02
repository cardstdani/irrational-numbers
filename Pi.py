from decimal import *
from math import factorial

def getPi(maxK, digits):
  getcontext().prec = digits+2
  s = Decimal(0)
  for k in range(maxK):    
    a = (Decimal(-1)**Decimal(k))*factorial(Decimal(6)*Decimal(k))*(Decimal(13591409) + Decimal(545140134)*Decimal(k))
    ab = factorial(Decimal(3)*Decimal(k))*(factorial(Decimal(k))**Decimal(3))*Decimal(640320)**(Decimal(3)*Decimal(k) + (Decimal(3)/Decimal(2)))
    s += Decimal(a) / Decimal(ab)
  return Decimal(1)/(Decimal(12)*s)

pi = getPi(15, 30)
print(pi)
