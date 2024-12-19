# Verifique se uma string contém apenas números.
def contem_numeros(string):
    return string.isdigit()
string = '345667'
print(f"A string '{string}' contém apenas números? {contem_numeros(string)}")
