"""
Cadastro de Usuario
"""

def cadastro_usuario(lista_usuarios:list) -> list:
    try:
        print()
        nome = input("Nome: ")
        idade = int(input("Nome: "))
        novo_usuario = {
            "nome":nome,
            "idade":idade
        }
        lista_usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso!")
        print()
        return lista_usuarios
    except:
        pass

def listar_usuarios_cadastrados(lista_usuarios:list) -> str:
    print()
    for index, usuario in enumerate(lista_usuarios, 1):
        print(f"{index} - {usuario.get('nome')} ({usuario.get("idade")} anos)")
    print()

def analisar_usuarios_cadastrados(lista_usuarios:list) -> str:
    criancas = 0
    adolescentes = 0
    adultos = 0
    idosos = 0
    
    for index, usuario in enumerate(lista_usuarios, 1):
        idade = usuario.get("idade")
        if idade < 12:
            criancas += 1
        elif idade > 12 and idade <= 17:
            adolescentes +=1
        elif idade >= 18 and idade <= 59:
            adultos += 1
        elif idade >= 60:
            idosos += 1
    print()
    print(f"Crianças : {criancas}")
    print(f"Adolescentes : {adolescentes}")
    print(f"Adultos : {adultos}")
    print(f"Idosos : {idosos}")
    print()

#Base de dados de usuarios
lista_usuarios = []

while True:
    # menu
    print("1 - Cadastrar usuário\n2 - Listar usuários\n3 - Analisar idades\n4 - Sair")
    opcao_selecionada = int(input("Escolha: "))
    
    if opcao_selecionada == 1:
        lista_usuarios = cadastro_usuario(lista_usuarios)
    elif opcao_selecionada == 2:
        listar_usuarios_cadastrados(lista_usuarios)
    elif opcao_selecionada == 3:
        analisar_usuarios_cadastrados(lista_usuarios)
    elif opcao_selecionada == 4:
        print("Saindo do sistema...")
        break 
    else:
        print(f"Opção {opcao_selecionada} invalida ...")
