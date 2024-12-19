#Determine se um triângulo pode ser formado.


def pode_formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


lado1 = 3
lado2 = 4
lado3 = 5
if pode_formar_triangulo(lado1, lado2, lado3):
    print("Os lados podem formar um triângulo")
else:
    print("Os lados não podem formar um triângulo")
