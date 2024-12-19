#Encontre números primos até 50.
def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = [num for num in range(2, 51) if primo(num)]
print(primos)