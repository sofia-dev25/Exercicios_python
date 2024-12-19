#Imprima os primeiros 10 números da sequência de Fibonacci
a = 1
b = 1
for i in range(10):
    print(i)

fibo = [1,2]
for i in range(1,11):
    fibo.append(fibo[i-1] + fibo[1-2])
  
print(fibo)