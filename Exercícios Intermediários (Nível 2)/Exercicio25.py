# Encontre o maior e menor número em uma lista.

def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor
lista_num = [8,4,9,45,39,88,64,17,92,54,6,23]
maior, menor = maior_menor(lista_num)
print(f"O maior número é {maior} e o menor número é {menor}")
