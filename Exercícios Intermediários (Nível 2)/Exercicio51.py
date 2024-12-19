# Remova espaços extras de uma string.
def remover_espacos_extras(string):
    return ' '.join(string.split())

string = "  Esta   é  uma   string   com  espaços  extras.  "
print(f"String original: '{string}'")
print(f"String sem espaços extras: '{remover_espacos_extras(string)}'")

