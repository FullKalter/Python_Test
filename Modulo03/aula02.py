# Escopo de variaveis


# Escopo global
# x = 10  # variável global

# def mostrar():
#     print(x)

# mostrar()
# print(x)



# Escopo Local
# def exemplo():
#     y = 5  # variável local
#     print(y)

# exemplo()
# print(y)  # erro!


# Quando o escopo causa confusão (caso clássico!)
# x = 10

# def alterar():
#     x = 20  # parece global, mas não é!
#     print("Dentro:", x)

# alterar()
# print("Fora:", x)


# Usando global (Má pratica)
# x = 10

# def alterar():
#     global x
#     x = 20

# alterar()
# print(x)



# O melhor caminho: retorno ao invés de globais (Boa pratica)
# x = 50

# def alterar(valor):
#     return valor * 2

# x = alterar(x)
# print(x)



# Escopo dentro de loops e condicionais
a = 0
if True:
    a = 5

print(a)  # funciona!