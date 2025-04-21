#Verificador de Pares e ímpares
#                                                          Poderia ter colocado um try except 
#                                                          para todos os inputs que pedissem
#                                                          números, mas quando lembrei 
#                                                          já tinha feito muitas coisas 
                                                                   



#Entrada de dados - quantos números o usuário quer digitar
qtd_numeros = int(input("Quantos números serão digitados? "))


#Lista vazia para ser adicionados números depois
lista_numeros = []


#Criando um loop que acaba só quando todos os números forem digitados
for leitor in range(1,qtd_numeros):
    numero = int(input(f"Número {leitor}: "))
    lista_numeros.append(numero)


lista_numros_pares = []   #Lista vazia para adicionar os números pares depois

#Criando uma função para os números pares
def numeros_pares(lista_numros):
    for x in lista_numeros:
        if x %2 == 0:
            lista_numros_pares.append(x)

        else:
            continue

    return lista_numros_pares



#Criando uma lista vazia para adicionar números ímapares depois
lista_numeros_impares = []

#Criando uma função para os números ímpares
def numeros_impares(lista_numros):
    for y in lista_numeros:
        if y != 0:
            lista_numeros_impares.append(y)

        else:
            continue

    return lista_numeros_impares

print(f"A sua lista completa sobre  o que você escreveu: {lista_numeros_impares}")

n_par = numeros_pares(lista_numeros)
print(f"A lista de númros pares é: {n_par}")

n_impar = numeros_impares(lista_numeros)
print(f"A lista de númros ímpares é: {n_impar}")
