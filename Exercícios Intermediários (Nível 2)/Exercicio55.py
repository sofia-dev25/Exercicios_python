#Substitua palavras em uma frase.
def substituir_palavras(frase, palavra_antiga, palavra_nova):
    return frase.replace(palavra_antiga, palavra_nova)
frase = "O céu é azul"
palavra_antiga = "azul"
palavra_nova = "vermelho"
print(f"Frase original: '{frase}'")
print(f"Frase modificada: '{substituir_palavras(frase, palavra_antiga, palavra_nova)}'")
