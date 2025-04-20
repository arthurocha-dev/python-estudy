#As conversões de Conjunto(set), Dicionários, Listas e Tuplas são semelhantes dos tipos básicos3
#set(), dict(), list(), tuple()

#Desse jeito, podemos transformar uma estrutura na outra (com o dic() vai ser meio complexo)
#fazer isso, pois o mesmo precisa de pares de chave e valor


#criando uma lista

nomes = ["Arthur", "João", "Mário", "Ana"]
print(type(nomes))


#convertendo para tuplas
nomes = tuple(nomes)
print(type(nomes))



#convertendo para conjuntos
nomes = set(nomes)
print(type(nomes))


#convertendo para ser um dicionário
estados_cidades = (['CE', 'Fortaleza'], ["SP", 'São Paulo'], ['SC', 'Balneáriu']) 


#Você tem que criar uma lista de tuplas, ou vice-versa, ou só tuplas dentro de tuplas, ou listas em listas 
estados_cidades = dict(estados_cidades)

print(estados_cidades)
print(type(estados_cidades))