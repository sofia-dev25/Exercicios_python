def primos_ate_50():
    primos = []
    for num in range(2, 51):
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos.append(num)
    return primos
print(primos_ate_50())

