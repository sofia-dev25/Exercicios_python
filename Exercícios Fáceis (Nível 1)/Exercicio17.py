# Gere a tabuada de multiplicação de um número
for i in range(11):
    print(3*i)

# Solicita ao usuário para inserir um número
numero = int(input("Digite um número para ver sua tabuada: "))
# Gera a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")