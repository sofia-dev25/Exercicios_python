#Converta uma string para título.
def converter_titulo(string):
    return string.title()
string = "esta é uma string de exemplo"
print(f"String original: '{string}'")
print(f"String em formato de título: '{converter_titulo(string)}'")
