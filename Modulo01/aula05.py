"""
Converão de tipos
"""

nome =  str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

print("Nome: ", nome, "Idade: ", idade , "Altura: ", altura, "Peso: ", peso)

print(type(idade))
idade = str(idade)

print("Nome: "+ nome + "Idade: " + idade + "Altura: ", altura, "Peso: ", peso)

print(isinstance(idade, str))

