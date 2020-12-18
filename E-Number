from decimal import *

eNumber = 1
numberIterations = 20000
divisionPrecision = 100
getcontext().prec = divisionPrecision + 1


def factorial(n):
  if n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n+1):
      result *= i
    return result


for i in range(1, numberIterations):
    eNumber += Decimal(1) / factorial(i)
print(eNumber)
