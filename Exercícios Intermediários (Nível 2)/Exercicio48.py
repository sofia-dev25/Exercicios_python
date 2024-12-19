#Ordene um dicionário por valores.
def ordenar_por_valores(dicionario):
    return dict(sorted(dicionario.items(), key=lambda item: item[1]))
meu_dicionario = {'a': 3, 'b': 1, 'c': 2}
dicionario_ordenado = ordenar_por_valores(meu_dicionario)
print(dicionario_ordenado)
