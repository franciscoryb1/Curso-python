def suma(num1, num2):
    return num1 + num2

try:
    assert suma(2,3) == 5
except AssertionError:
    print("El resultado es INCORRECTO.")
else:
    print("El resultado es CORRECTO.")

try:
    assert suma(0,0) == 1
except AssertionError:
    print("El resultado es INCORRECTO.")
else:
    print("El resultado es CORRECTO.")

try:
    assert suma(-2,5) == 3
except AssertionError:
    print("El resultado es INCORRECTO.")
else:
    print("El resultado es CORRECTO.")