#Desenvolva função para contar vogais em uma string.
def contar_vogais(string):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador


texto = "Olá mundo!"
numero_de_vogais = contar_vogais(texto)
print(f"O número de vogais em '{texto}' é {numero_de_vogais}")





