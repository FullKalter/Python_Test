## Argumentos de Funções




# Relembrando a função
#def funcao(parametro):
#    return parametro





















# Argumentos Posicionais
#def apresentar(nome, idade):
#    print(f"{nome} tem {idade} anos.")
#
#apresentar("Ana", 25)






















# Argumentos Nomeados
#apresentar(nome="Ana", idade=25)
#apresentar(idade=25, nome="Ana")   # funciona também





















# Parâmetros Opcionais (Valores Padrão)
#def saudacao(nome, mensagem="Olá"):
#    print(f"{mensagem}, {nome}!")
#
#saudacao("Carlos")
#saudacao("Maria", "Bem-vinda")




















# Múltiplos Argumentos Posicionais *args
#def somar(*numeros):
#    total = 0
#    for n in numeros:
#        total += n
#    return total
#
#print(somar(1, 2, 3))
#print(somar(10, 20, 30, 40))





















# **kwargs – Argumentos Nomeados Dinâmicos
#def exibir_info(**dados):
#    for chave, valor in dados.items():
#        print(f"{chave}: {valor}")
#
#exibir_info(nome="Ana", idade=20, cidade="Curitiba")





















# Mini-Projetinho da Aula
"""
Montar um projeto que crie um pedido para uma lanchonete
A função devera receber:
Nome do cliente, os itens pedidos, tipo da entrega e detalhes adicionais
"""

def montar_pedido(cliente, *itens, entrega="normal", **detalhes):
    print(f"Cliente: {cliente}")
    print("Itens:")
    for item in itens:
        print(f"- {item}")
    
    print(f"Tipo da entrega: {entrega}")
    print("Detalhes adicionais:")
    for key, valeu in detalhes.items():
        print(f"{key}: {valeu}")

montar_pedido(
    "Ana",
    "Pizza", "Coca-cola", "Sobremesa",
    entrega="Expressa",
    rua="Rua Tiradentes numero 98",
    cupom="CUPOM2026",
    observacao="Deixar na portaria"
)