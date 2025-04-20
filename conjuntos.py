#Os conjuntos, NÃO tem uma ORDEM DEFINIDA e NÃO pode ter elementos REPETIDOS

#Se tiver valores repetidos, vai ser armazenado só um valor dos repetidos

#Sua criação usa-se chaves{}

primeiroConjunto = {"Rodrigo", 3432, True, False, 190.98}
print(primeiroConjunto)

segundoConjunto = {"arroz", 12, "frango", 2,2,2,2, "arroz"}
print(segundoConjunto)



# Para adicionar um item, usa-se o MÉTODO add
#nomeConjunto.add("nomeItem")

primeiroConjunto.add("item adicionado")
print(primeiroConjunto)



# Para acessar um item de forma direta, não tem como acessá-lo sem ter que remover o item
# você tem que criar uma variável u usar o método pop()
# variavel = nomeConjubto.pop()
# print(nomeConjunto)
# e ele remove de forma aleátoria


item = segundoConjunto.pop()
print(segundoConjunto)


# Você pode verificar se há um item na lista, usando in no print
# print("nomeItem" in nomeCojunto)

print("arroz" in segundoConjunto)