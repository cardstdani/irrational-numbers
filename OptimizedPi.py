from decimal import Decimal, getcontext
import sys

def getPi(maxK):
    getcontext().prec = (maxK * 14) + 2
    a_k, constant, a_sum, b_sum  =  1, 640320**3, 1, 0
    for k in range(1, maxK):
        a_k *= -(Decimal(24)*Decimal((6*k-5)*(2*k-1)*(6*k-1)))/(Decimal(k**3)*Decimal(constant))
        a_sum += a_k
        b_sum += a_k*k
    return 426880*Decimal(10005).sqrt()/Decimal(13591409*a_sum + 545140134*b_sum)

pi = getPi(1200)
print(pi)
