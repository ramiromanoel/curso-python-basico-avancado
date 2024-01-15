"""
for numero in range(1 , 10):
    print(numero)


for valor in enumerate(nome):
    print(valor)


qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe do {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


"""

# Original U+1F60D
# Modificado U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
