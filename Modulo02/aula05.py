"""
break, continue e pass(...)
"""

#for i in range(50):
#    print(i)
#    if i == 30:
#        print('achei')
#        break

for i in range(50):
    if i % 2:
        print(f'Resultado  da operaçao e par')
        continue
    print(i)

for i in range(50):
    ...