# Implemente função para calcular área de formas geométricas.
import math

def area_quadrado(lado):
    return lado ** 2
lado = float(input('digite o lado:'))
print(f"A área do quadrado é {area_quadrado(lado)}")
print('---------------------------------------------------')

def area_circulo(raio):
    return math.pi * raio ** 2
raio = float(input('digite o raio:'))
print(f"A área do círculo é {area_circulo(raio)}")
print('---------------------------------------------------')


def area_retangulo(largura, altura):
    return largura * altura
largura = float(input('digite a largura:'))
altura = float(input('digite altura:'))
print(f"A área do retângulo é {area_retangulo(largura, altura)}")
print('---------------------------------------------------')

def area_triangulo(base, altura):
    return (base * altura) / 2
base = float(input('digite a base:'))
altura = float(input('digite altura:'))
print(f"A área do triângulo é {area_triangulo(base, altura)}")
