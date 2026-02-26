"""
laço de repetiçao for

quando usar?
"""

#frutas = ['maça', 'mamâo' , 'laranja', 'pera', 'banana']
#for fruta in frutas:
#    print(fruta)

#for i in range(5):
#    print(i)

caixa_brinquedos = ['pelucia', 'hotweels', 'bolinha de ping pong', 'soldadinho', 'carrinho de friqçao', 'max steel']
briquedos_para_doacao = []
briquedos_para_uso = []

for briquedos in caixa_brinquedos:
    print(briquedos)
    if briquedos in ['max steel', 'hotweels', 'soldadinho']:
        briquedos_para_uso.append(briquedos)
    else:
        briquedos_para_doacao.append(briquedos)

print(f"Brinquedos para doaçao: {briquedos_para_doacao}")
print(f"Brinquedos para uso: {briquedos_para_uso}")