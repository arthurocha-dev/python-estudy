#Controle estoque

#Entrada de dados - quantos produtos que o usuário vai querer cadastrar?
quantidade_produtos = int(input("Quantos produtos serão cadastrados? "))

#Criando um dicionário vazio por enquanto
listas_produtos = {}                       #Só o nome que é "lista", mas é um dicionário
    

#Criando um for para o usúario cadastrar os produtos e suas informações, com validação de dados
for repetidor in range(1, quantidade_produtos+1):
     
     global produto
     global quantidade_estoque
     global preco_unidade
     
     try:
          
      produto = input(f"Produto {repetidor}:")
      quantidade_estoque = int(input("Quantidade em estoque: "))
      preco_unidade = float(input("Preço por unidade: "))
     
     except ValueError:
         print("Error! Nos campos onde serão digitado valores numéricos, tem que ser escrito apenas valores númericos, não outro caractér diferente dos mesmos")
     

     else:
      print("--------------------------------") 
      listas_produtos.update({f"Produto {repetidor}": produto, "Quantidade em estoque": quantidade_estoque, "Preçopor unidade": preco_unidade })

     

#Criando um for só pra organizar a saída das informações na tela     
for oraganizar in listas_produtos:
     print(oraganizar)



#Função para saber o valor total do estoque, estoque x produtos
def valor_total_estoque(listas_produtos):
   total_estoque_preco = sum(listas_produtos.values()) * len(listas_produtos)

   return total_estoque_preco


def produto_mais_caro(listas_produtos,preco_unidade):
   p_mais_caro = max(listas_produtos(preco_unidade))
   return produto_mais_caro


def produto_com_mais_etoque(listas_produtos,quantidade_estoque):
   p_mais_estoque = max(listas_produtos(quantidade_estoque))
   return p_mais_estoque



value_total_estoque = valor_total_estoque(listas_produtos)
print("O valor total do estoque é: R$", value_total_estoque)


produto_caro = produto_mais_caro(listas_produtos,preco_unidade)
print("O produto mais caro está com o preço de: R$", produto_caro)

produto_m_estoque = produto_com_mais_etoque(listas_produtos,quantidade_estoque)
print("O produto com mais estoque é: ", produto_m_estoque)






     