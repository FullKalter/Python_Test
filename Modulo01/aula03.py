"""
OPERADORES MATEMATICOS

Principais Operadores:

| Operador  | Exemplo    | Resultado            |
| --------- | ---------- | -------------------- |
| `+`       | `10 + 5`   | 15                   |
| `-`       | `10 - 5`   | 5                    |        
| `*`       | `10 * 5`   | 50                   |
| `/`       | `10 / 3`   | 3.333...             |
| `//`      | `10 // 3`  | 3 (divisão inteira)  |
| `%`       | `10 % 3`   | 1 (resto da divisão) |
| `**`      | `10 ** 3`  | 8 (potência)         |
"""
idade_marcos = 10
idade_lucas = 3

#print(idade_marcos + idade_lucas)
#print(idade_marcos - idade_lucas)
#print(idade_marcos * idade_lucas)
#print(idade_marcos / idade_lucas)
#print(idade_marcos // idade_lucas)
#print(idade_marcos % idade_lucas)
#print(idade_marcos ** idade_lucas)

"""
Usados para comparar  valores -> retornam True ou False.

| Operador  | Significado    | Exemplo              |
| --------- | -------------- | -------------------- |
| `==`      | Igualdade      | `10 == 10 -> True`   |
| `!=`      | Diferente      | `10 != 5 -> True`    |        
| `>`       | Maior que      | `10 > 5 -> True`     |
| `<`       | Menor que      | `10 < 5 -> False`    |
| `>=`      | Maior ou igual | `10 >= 10 -> True`   |
| `<=`      | Menor ou igual | `5 <= 7 -> True`     |
"""
idade_marcos = 10
idade_lucas = 20

#print(idade_marcos == idade_lucas)
#print(idade_marcos != idade_lucas)
#print(idade_marcos > idade_lucas)
#print(idade_marcos < idade_lucas)
#print(idade_marcos >= idade_lucas)
#print(idade_marcos <= idade_lucas)

"""
Usados para combinar expressões  booleanas.

| Operador | Significado                                              | Exemplo                        |
| -------- | -------------------------------------------------------- | ------------------------------ | 
| `and`    | Verdadeiro se **as duas condições** forem verdadeiras    | `(10 > 5) and (8 > 3)` -> True |
| `or`     | Verdadeiro se **pelo menos uma condição** for verdadeira | `(10 > 5) or (8 < 3)` -> True  |      
| `not`    | Inverte o valor lógico                                   | `not (10 > 5)` -> False        |
"""
is_true = True
is_false = False

#print(is_true and is_false)
#print(is_true or is_false)
#print(not is_false)

idade = 20
tem_carteira = True

#print(idade >= 18 and tem_carteira)

nota1 = 8
nota2 = 6
presenca = 80

media= (nota1 + nota2) / 2

print("Média: ", media)

aprovado = (media >= 7) and (presenca >= 75)

print("Aprovado ", aprovado)
