#Sistemas de cadastro de produtos

#Definindo o produto
# nomeProduto = input("Digite o nome do produto: ")
# precoProduto = float(input("Digite o preço: "))






print("Cadastre seus produtos!")

print("\n")  

print("escreva 'sair' para encerrar, caso queira encerrar antes")

print("\n")

#Sabendo a quantidade de produtos que o usuário quer cadastrar
quantidadedesProdutos = int(input("Quantos item você quer cadastrar? "))

print("\n")

#Criando dicionário
produtos = {}




#Enquanto a quantidade de produtos não for cadastradas, execute isso
for x in range(1,quantidadedesProdutos+1):
    nomeProduto = input(f"Nome do produto {x}: ")
    if nomeProduto == "sair":                       #se o usuário digitar sair, ele encerra o programa, se não
        print("Cadatro de produtos encerrados")       #ele continua a adicionar os produtos
        break

    else:
      try:
       precoProduto = float(input(f"Preço do produto {x}: "))
       print("-------------------------------------")
       

      except ValueError:                                            #Se o usuário digitar algo que não seja número
         print("Error ao digitar o preço! Digite apenas números")   #vai exibir esse erro

      else:                                                         #Se não tiver nenhum problema, o programa continua
         produtos[nomeProduto] = precoProduto                       #com else


    

print("\n")

#Exibindo os produtos e seus preços um por vez
print("Produtos adicionados:")
for y in produtos:
   print(f"{y}: {produtos[y]}")




#Soma dos produtos
soma = sum(produtos.values())         #Aqui com a função sum, vai somar todos os valores do dicionário produtos, usando
                                    #values para acessá-los                                     

#Média dos produtos
media = soma / quantidadedesProdutos


print("\n")
print(f"A média dos seus produtos é: {media}")


#Mostrando os produtos a cima da média
for a in produtos:
   if produtos[a] >= media:
      print(f"Produto a cima da média: {a} com o valor de {produtos[a]:.2f}")

   else:
      continue

print("\n")

print("Programa encerrado")   
















