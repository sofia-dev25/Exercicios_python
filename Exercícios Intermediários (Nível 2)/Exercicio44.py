#Mescle dois dicionários.
contatos = {
    'Anna': '999999999',
    'Maria': '999999990',
    'Clarisse': '999999991',
    'Joana': '999999992',
    'Antônia': '999999999',
 }
v_dicionario = {'a': 10, 'b': 20, 'c': 30}

def mesclar_dicionarios(dic1, dic2):
    dic_mesclado = dic1.copy()  
    dic_mesclado.update(dic2)   
    return dic_mesclado

dicionario_mesclado = mesclar_dicionarios(contatos, v_dicionario)
print(dicionario_mesclado)
