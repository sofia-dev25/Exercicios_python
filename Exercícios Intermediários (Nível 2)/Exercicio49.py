#49. Conte quantas vezes uma letra aparece em uma string.
def contar_letra(string, letra):
    contador = 0
    for char in string:
        if char == letra:
            contador += 1
    return contador
string = "abracadabra"
letra = "a"
print(f"A letra '{letra}' aparece {contar_letra(string, letra)} vezes na string '{string}'.")

