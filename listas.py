#Uma lista se organiza de maneira ordenada, começa do índe 0, e pode armezanar valor de todos os tipos, ela também repetir valores

lista = ['Arthur' , 24, True, 12.3, 'Arthur' ]

#para acessar um item específico tem que colocar entre chaves o índice do item:
#-print(lista[0])



#para acessar o último ou antecessor elemento de forma rápida, uma opção
#é passar uma posicão negativa, ex:

#-print(lista[-1])
#-print(lista[-3])


#para adicionar elementos use o MÉTODO "nomeDalista.append(item)":

lista.append("Teclado")
#-print(lista)





# Para deletar um item, tem dois jeitos:
# 1 é usando o COMANDO del, del nomeDaLista[índice]:

del lista[4] # vai remover o item da lista "Arthur"
print(lista)

# 2 é usando o MÉTODO remove, nomeDaLista.remove(nomeDoIndice):
lista.remove('Teclado')
print(lista)




# Para editar ou substituir um elememto na lista
# tem que atualizala, nomeDaLista[índice] = novoValor

lista[3] = 12.8       #de 12.3 vai para 12.8
print(lista)


# Para saber o tamanho da lista, use a FUNÇÃO len
# print(len(nomeDaLista))

print(len(lista))


#Curiosidade, as strings se comportam como uma lista, um exemplo é quando 
# for acessar um elemento específico de uma lista, no caso da strings
# vai ser acessado o caractér, exemplo

frase = "Programaçao é um pouco chatinha, mas é legal e interessante"
print(frase[-2]) # vai acessar a penúltima letra, que é p "t"