#Adicione, remova e atualize informações no dicionário.
contatos = {
    'Anna': '999999999',
    'Maria': '999999990',
    'Clarisse': '999999991',
    'Joana': '999999992',
    'Antônia': '999999999',
 }
contatos['Jaqueline']= 999999993
print(contatos)

del contatos ['Maria']
print(contatos)

contatos.update({'Anna':'899999999'})
for chave,valor in contatos.items(): 
   print(f'{chave} : {valor}')