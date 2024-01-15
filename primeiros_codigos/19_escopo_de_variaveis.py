"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;

2 - Variáveis locais;

Para declarar variáveis em python fazemos:

nome_da_variavel = valor_da_variavel

Python [e uma linguagem de tipagem din"amica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valos à mesma.
"""

numero = 40    # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 40

if numero > 10:
    novo = numero + 10    # A variável 'novo' está declarada localmente no bloco do if
    print(novo)

print(novo)