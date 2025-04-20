# Os diciionários em python, segue a métodologia dos dicionários dos livros.
#Tem a palavra e em seguida a sua descrição

#Ao invés de armazenar só um elemento, ele armazena PARES de chaves e valor, itens separados por vírgula
#ex: dicionario = {"carro:" "veículo movel de 4 rodas", "salario:" 1000}

# O que diferencia-se de conjutos é por que nos dicionários, usa-se PARES para armazenar elementos
#se não usa-se pares, o python ia interpretar como um conjunto

#Ele só aceita valores ÚNICOS e NÃO REPETIDOS, se por acaso ser repetido, vai ser atualizado o valor 

# Pra criar um dicionario: nomeDicionario = {"nomeChave": valor}

dic_comidas = {"maçã": "fruta vermelha",
               "churrasco": "carne assada",
               "limão" : "fruta azeda",
                "laranja": "a casca verde e dentro amarelo" }

print(dic_comidas)




#os dicionários, tem três métodos importamtes, keys(), values() e items()

#keys() - retorna todas as chaves do dicionário
print(dic_comidas.keys())


#values() - retorna só os valores das chaves
print(dic_comidas.values())



#items() - retorna todos os pares e valor do dicionário
print(dic_comidas.items())



#para remover um item, nós usamos o COMANDO del igual anteriormente
#ex: del nomeDicionario[nomeChave]

del dic_comidas["laranja"]
print(dic_comidas)


#Para alterar um valor de uma chave, é parecido como uma lista
#ex: nomeDicionario[nomeChave] = "novo valor"

dic_comidas["limão"] = "azeda e verde"    # de: "fruta azeda" foi para "azeda e verde"

print(dic_comidas[3])