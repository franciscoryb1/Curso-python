# Version_1
# En este programa el usuario puede ingresar cuantos numeros quiera y terminar la entrada con el caracter "*".
lista = []
while True:
    variable_numero = input("Ingrese un numero: ")
    if variable_numero == "*":
        break
    try:
        variable_numero = int(variable_numero)
    except ValueError:
        print("El valor ingresado es INCORRECTO.")
        continue
    lista.append(variable_numero)
total = sum(lista)
long = len(lista)
promedio = total / long
print(f"El promedio de los numeros ingresados es: {promedio}")


# Versión_2
# En este programa el usuario al principio indica cuantos numeros va a ingresar y se le solicita la 
# cantidad de numeros indicada.
lista = []
cantidad = int(input("Ingrese la cantidad de numeros: "))
for i in range(cantidad):
        try:
            variable_numero = int(input("Ingrese un numero: "))
        except ValueError:
            print("El valor ingresado es invalido.")
            continue
        lista.append(variable_numero)
total = sum(lista)
long = len(lista)
promedio = total / long
print(f"El promedio de los numeros ingresados es: {promedio}")