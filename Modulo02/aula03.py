"""
Laço de repetiçao while
"""

senha_user = '12345'

while True:
    senha_entrada = input('Digite sua senha: ')

    if senha_entrada == senha_user:
        print('Login feito com sucesso!')
        break
    else:
        print('Senha errada! Tente novamente')