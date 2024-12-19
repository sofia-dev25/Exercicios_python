# Crie uma função que calcule o IMC.
#fórmula: peso (kg) ÷ (altura x altura) (m).

peso = float(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em meteros:'))
IMC = peso/(altura*altura)
print(IMC)
