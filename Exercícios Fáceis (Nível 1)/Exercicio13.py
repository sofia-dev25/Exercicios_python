#Verifique se um ano é bissexto.

Ano_bissexto = int(input('Digite um ano:'))
if Ano_bissexto % 400 == 0:
    print('O ano é bissexto'),
else:
    print('O ano não é bissexto')
