"""
Listas: em python funcionam como vetores ou matrizes, ou seja, arrays. A diferença está em serem DINÂMICAS e aceitarem QUALQUER tipo de dado.

* Dinâmico:



# Podemos facilmente checar se determinado valor está contido na listas
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmnte contar a ocorrência de um valor em uma lista.
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas
print(lista1)
lista1.append(42) #coloca a lista como elemento único (sublista)
print(lista1)
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei na lista')

lista1.extend([123, 44, 17]) #coloca cada elemento da lista como valor adicional à lista
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do índice
# OBS.: isso não substitui o valor inicial. o mesmo será deslocado para direita da lista
lista1.insert(2,'Novo valor')
print(lista1)

# podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)



# podemos facilmente inverter uma lista:

# forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# forma 2
print(lista1[::-1])
print(lista2[::-1])




# podemos contar quantos elementos existem dentro da lista
print(len(lista4))
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y',]

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# podemos remover o último elemento de uma lista
print(lista5)
lista5.pop() # o pop remove e retorna o último elemento
print(lista5)

# podemos remover um elemento pelo índice
# OBS.: os elementos a direita deste índice serão deslocados para a esquerda
print(lista5)
lista5.pop(2)
print(lista5)