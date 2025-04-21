#Sistema para Loja

#Entrada de dados - peruntando ao usuário quantos produtos foram comprados
quantidade_compras = int(input("Quantos produtos foram comprados? "))

#Lista vazia para armazenar os preços dos produtos
lista_precos = []


#Adicionar preços a lista
for repetidor in range(1, quantidade_compras+1):
    preco = float(input(f"Preço {repetidor}: "))
    lista_precos.append(preco)



#Função para saber o valor total
def valor_total_compra(lista_precos):
    valor_total = sum(lista_precos)

    return valor_total



#Função para saber o maior preço
def maior_preco (lista_precos):
    maior_p = max(lista_precos)

    return maior_p
    

#Função para saber o menor preço    
def menor_preco (lista_precos):
    menor_p = min(lista_precos)

    return menor_p


#Função para saber a média dos preços
def media_dos_precos(lista_precos):
    global media_p
    
    media_p = sum(lista_precos) / len(lista_precos)

    return media_p

#Função para saber os preços acima da média
def preco_acima_da_media(lista_precos, media_p):
    valores_acima_media = []

    for leitor in lista_precos:
        if leitor >= media_p:
            valores_acima_media.append(leitor)

        else:
            continue    

    return valores_acima_media
    


#Imprimindo os valores na tela
value_total = valor_total_compra(lista_precos)
print(f"O valor total da compra foi: R${value_total}")

ma_preco = maior_preco(lista_precos)
print("O maior preço foi: R$", ma_preco)

me_preco = menor_preco(lista_precos)
print("O menor preço foi: R$", me_preco)

media_preços = media_dos_precos(lista_precos)
print(f"A média dos preços foi de: {media_preços}")

p_acima_media = preco_acima_da_media(lista_precos,media_p)
print("Os preços acima da média foram: ",p_acima_media)