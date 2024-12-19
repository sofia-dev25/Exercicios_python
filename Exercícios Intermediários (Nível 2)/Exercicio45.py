#Encontre a chave com o maior valor.
def maior_valor(dicionario):
    chave_maior = max(dicionario, key=dicionario.get)
    return chave_maior
meu_dicionario = {'a': 10, 'b': 20, 'c': 30}
print(f"A chave com o maior valor é '{maior_valor(meu_dicionario)}'")
