


# idade = 20

# def calcular_idade_maior_dezoito(idade):
#     if idade < 18:
#         print("Você é maior de 18 anos")
#     if idade == 20:
#         print("Você tem exatamente 20 anos")
#     if idade > 18 or idade < 25:
#         print("Sua idade esta entre 18 e 25 anos")


# print(calcular_idade_maior_dezoito(idade))


def calculcular_desconto(valor, desconto, cupom=None):
    if cupom == "PYTHONBRASIL20":
        print("CUPOM APLICADO")
        desconto += 0.1

    return valor - (valor * desconto)


produtos = [
    {
        'nome': 'nootebook',
        'preco':899.90,
        'desconto':0.5,
        #'cupom': 'PYTHONBRASIL20'
    },
    {
        'nome': 'Teclado',
        'preco':159.90,
        'desconto':0.1
    },
    {
        'nome': 'Mouse',
        'preco':59.9,
        'desconto':0.5
    },
    {
        'nome': 'Headset',
        'preco':299.90,
        'desconto':0.5
    }
]

for indice, produto in enumerate(produtos, 1):
    print(f"Calculando desconto do produto {indice} - {produto['nome']}")
    cupom = produto.get('cupom', None)
    valor_descontado = calculcular_desconto(produto['preco'], produto['desconto'], cupom=cupom)
    print(f'O produto estava no preco {produto['preco']} e agora esta por apenas {valor_descontado}')