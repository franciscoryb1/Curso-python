def separar_contenido(cadena):
    #esta funcion retorna una lista donde cada elemento es una palabra del texto
    texto = cadena
    lista = texto.split(" ")
    return lista

def main():
    #obtener nombre del archivo
    nombre = str(input("Ingrese el nombre del archivo: "))
    archivo = open(nombre, "r")
    #separar contenido
    separado = separar_contenido(archivo.read())
    #contar elementos
    longitud = len(separado)
    print(f"Su archivo tiene {longitud} palabras.")


main()
