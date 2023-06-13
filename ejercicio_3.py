def obtener_temperatura():
    while True:
        try:
            temp_celcius = float(input("Ingrese una temperatura en grados Celcius: "))
        except ValueError:
            print("El valor ingresado es incorrecto.")
            continue
        else:
            break
    return temp_celcius    

def convertir_a_fahrenheit(num):
    fahrenheit = num * 1.8 + 32
    return fahrenheit

def mostrar_resultados(cel, fh):
    return f"{cel} grados Celsius equivalen a {round(fh, 2)} grados Fahrenheit."

def main():
    celcius = obtener_temperatura()
    fh = convertir_a_fahrenheit(celcius)
    print(mostrar_resultados(celcius, fh))

main()