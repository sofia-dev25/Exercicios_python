#Desenhe um padrão de asteriscos.
def desenhar_asteristico(tamanho):
    for i in range(tamanho, 0, -1):
        print(' ' * (tamanho - i) + '* ' * i)
