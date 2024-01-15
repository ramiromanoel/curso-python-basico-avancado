"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separador de cadas decimais na programação é o ponto e não vírgula.
"""

# Errado do ponto de vis to Float, mas gera um tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS.: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor1)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
