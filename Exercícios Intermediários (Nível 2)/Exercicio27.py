#Filtre números pares de uma lista.
lista_num = [8,4,9,45,39,88,64,17,92,54,6,23]
lista_pares =[]
for item in lista_num:
    if item % 2 == 0:
        lista_pares.append(item)
print(lista_pares)
