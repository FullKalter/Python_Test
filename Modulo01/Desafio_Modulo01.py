"""
Calculadora de IMC
"""
# Pegar os dados do usuario
Nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# Calculo do IMC
imc = peso / (altura * altura)

# Exibir os dados
print("=== Dados do Usuario ===")
print("Nome: ", Nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Peso: ", peso)
print("IMC: ", imc)
print("="*25)

# Classificar o IMC
print("== Classificado do IMC ==")
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")
print("="*25)