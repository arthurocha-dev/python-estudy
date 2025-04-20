#É uma forma compacta e eficiente de criar listas em Python, em uma única linha de código.

#lista = [a, b , c]
#sintaxe:  nova lista = [expressão for item in lista]


# numeros = [1, 2, 4,]

# n_quadrados = [interator *2 for interator in numeros]

# print(n_quadrados)


# idades = [15, 18, 21, 13, 30, 17, 40]

# maiorIdade = []

# #sem usar a list comprehension
# for x in idades:
#     if x >= 18:
#         maiorIdade.append(x)

# print(maiorIdade)        


#com a lista comprehension
idades = [15, 18, 21, 13, 30, 17, 40]

maiorIdade = [ x for x in idades if x >= 18]

print(maiorIdade)