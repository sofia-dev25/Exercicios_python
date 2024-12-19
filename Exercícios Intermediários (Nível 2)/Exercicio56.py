#Receba uma string e retorne ao contrário.
def inverter_string(string):
    return string[::-1]

string = str(input('Digite uma palavra:'))
print(f"A string invertida é: '{inverter_string(string)}'")