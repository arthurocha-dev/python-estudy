# Funções lambda são uma forma rápida e compacta de criar funções anônimas (sem nome)

#variavel = lambda x: operação 

x = 5
dobro = lambda x: x *2
print(dobro(x))

#ou

dobro = lambda x: x *2
print(dobro(5))


#Com dois parâmetros

n1 = int(input("numero1:"))
n2 = int(input("numero2: "))
soma = lambda x,y: x + y

print(soma(n1,n2))


#Usada com map
numeros = [1,2,3,4,5,]
quadrados = list(map(lambda a:a**2, numeros))

print(quadrados)