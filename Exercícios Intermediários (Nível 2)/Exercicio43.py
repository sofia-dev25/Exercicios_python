#Some os valores de um dicionário.
def somar_valores(dicionario):
    return sum(dicionario.values())
v_dicionario = {'a': 10, 'b': 20, 'c': 30}
print(f"A soma dos valores é {somar_valores(v_dicionario)}")
