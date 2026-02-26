"""
3 S = Start, Stop, Step
range()
"""

#for i in range(5, 55, 5):
#    print(i)

"""
enumerate
"""

usuarios = ['Matheus', 'Andre', 'Julia', 'Marcos', 'Rodrigo', 'Marcela', 'Luciana', 'Maxwell']

for indice, user in enumerate(usuarios, 1):
    print(f'{user} progesso: {indice}/{len(usuarios)}')