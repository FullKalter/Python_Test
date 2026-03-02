"""
Lista → caixa organizada que você pode alterar (mutável)

Tupla → caixa lacrada, não dá para mudar (imutável)

Dicionário → caixa com etiquetas

Set → caixa que não aceita duplicatas
"""

# Lista
# produtos = ["Banana", "Maça", "Pera", "Abacaxi"]
# print(type(produtos))

# produtos.append("Abacate")
# produtos.append("Tamarindo")
# produtos.insert(1, "Jiló")
# produtos[0] = "Alface"
# produtos.remove("Alface")
# produtos.sort()
# produtos.reverse()
# produtos.pop(-1)
# print(produtos[1])
# print(produtos)





# Tupla
# produtos = ("azul", "vermelho", "amarelo")
# print(type(produtos))

# print(produtos[-1])


# Dicionario
# produtos = {
#     "nome": "Ana",
#     "idade": 25,
#     "cidade":"Curitiba",
#     "e_brasileira": True,
#     "cidadania": "Brasileira",
#     "filmes_favoritos": ["Tazan", "Conderela", "Branca de neve"]
# }
# print(type(produtos))

# produtos["nome"] = "Ana Gomes"
# print(produtos["nome"])
# print(produtos.get("cidadania", "nao tem"))

# print(produtos.keys())
# print(produtos.values())
# print(produtos.items())
# for key, value in produtos.items():
#     print(f"key: {key} - value: {value}")



# Set
produtos_01 = {1,2,2,3,3,3}
produtos_02 = {3,4,5,5,5,5,6,6,6}
print(type(produtos_01))

# produtos_01.add(4)
# produtos_01.remove(3)

print(produtos_01 & produtos_02)