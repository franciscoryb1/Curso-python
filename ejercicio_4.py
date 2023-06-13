for i in range(1,11):
    lista = []
    for x in range(1,11):
        lista.append(i*x)
    # print(str(lista))
    lista_2 = [str(a) for a in lista]
    print(" " . join(lista_2))