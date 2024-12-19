#Classifique uma nota de 0 a 10 em conceitos (A(10,9), B(8,7), C(6,5), D(4,3), F(2,0)).

nota = float(input('Valor da nota:'))
if nota >=9 <=10:
    print('O conceito da sua nota é A.'),
elif nota >=7 <=8:
    print('O conceito da sua nota é B.'),
elif nota >=5 <=6:
    print('O conceito da sua nota é C.'),
elif nota >=3 <=4:
    print('O conceito da sua nota é D.'),
else:
    print('O conceito da sua nota é F.'),