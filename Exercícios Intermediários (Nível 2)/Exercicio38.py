# Crie função para verificar palíndromo
def eh_palindromo(string):
    string = string.replace(" ", "").lower()  
    return string == string[::-1]
string = "Olá mundo!"
print(f"A string '{string}' é um palíndromo? {eh_palindromo(string)}")
