#Crie um dicionário de estoque de produtos.
estoque = {
    'produto1': {'nome': 'Caneta', 'quantidade': 100, 'preco': 1.50},
    'produto2': {'nome': 'Caderno', 'quantidade': 50, 'preco': 10.00},
    'produto3': {'nome': 'Borracha', 'quantidade': 200, 'preco': 0.75},
    'produto4': {'nome': 'Lápis', 'quantidade': 150, 'preco': 0.50}
}
for produto, detalhes in estoque.items():
    print(f"Produto: {detalhes['nome']}, Quantidade: {detalhes['quantidade']}, Preço: R${detalhes['preco']:.2f}")
