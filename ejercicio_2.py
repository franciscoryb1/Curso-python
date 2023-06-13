while True:
    try:
        numero = int(input("Ingrese un numero: "))
    except ValueError:
        print("Incorrecto.")
        continue
    if numero < 0:
        print("Incorrecto.")
        continue
    else:
        break

suma = 0
for i in range(1, numero+1):
    if i % 2 == 0:
        suma += i
print(f"La suma de todos los números pares desde 1 hasta {numero} es: {suma}")
