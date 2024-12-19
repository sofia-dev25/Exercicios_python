#Filtre dicionário por condição específica.
estoque = {
    'produto1': {'nome': 'Caneta', 'quantidade': 100, 'preco': 1.50},
    'produto2': {'nome': 'Caderno', 'quantidade': 50, 'preco': 10.00},
    'produto3': {'nome': 'Borracha', 'quantidade': 200, 'preco': 0.75},
    'produto4': {'nome': 'Lápis', 'quantidade': 150, 'preco': 0.50}
}

def filtrar_estoque(estoque, quantidade_minima):
    return {k: v for k, v in estoque.items() if v['quantidade'] > quantidade_minima}
quantidade_minima = float(input('Digite a quantidade minima:'))
estoque_filtrado = filtrar_estoque(estoque, quantidade_minima)
print(estoque_filtrado)
