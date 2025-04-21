#Salários de Funcionários
print("---------Cadastre salários!--------")

#Dando espaçamento para melhor organização na tela
print("\n")

#Sabendo quantos salários seram cadastrados pelo usuário
qtd_salarios = int(input("Quantos salários você quer cadastrar? "))

print("\n")


#Criando a lista vazia ainda não preenchida pelo usuário
salarios = []

#Algoritimo para adicionar os salários na lista acima
for x in range(1,qtd_salarios+1):
    try:
     v_salario = float(input(f"Salário {x}: "))
    

    except ValueError:       #Se no try o usuário digitar algo que não seja número, esse bloco vai ser executado
        print("Error! Apenas valores númericos podem ser escritos")

    else:                    #Se ocorrer tudo bem no try, o salário vai ser adcionado
      salarios.append(v_salario)
      



#Função pra calcular a média dos salários
def media_salarial(salarios):
    
    soma_salarios = sum(salarios)
    media_salarios_calculo = soma_salarios // len(salarios)

 
    return media_salarios_calculo


#Função pra saber os salarios acima da média
def salarios_acima_media(salarios):

    soma_salarios_acima = sum(salarios)                           #veja que eu repeti o mesmo calculo da função anterior,
    media_salarios_acima = soma_salarios_acima // len(salarios)   #pois não consegui usar a variável da media feita lá usar aqui  

    s_acima = []

    for y in salarios:                         #O y vai percorrer sobre a lista de salários
        if y >= media_salarios_acima:          #se o y iterar o salário, e ele for maior que a média da lista de salário
            print(f"O salário:{y} está acima da média") #será imprimido o salário
            s_acima.append(y) 
        else:                                   #Se o salário iterado não for maior que a média, o y vai apenas pular
            continue                            #esse número, e continuar percorrendo a lista

    return s_acima

#Função pra definir o maior salário   
def maior_salario(salarios):
    m_salario = max(salarios)

    return m_salario

#Função pra definir o menor salário
def menor_salario(salarios):
    men_salario = min(salarios)

    return men_salario


print("\n")

#Imprimir os resultados das funções
media_s = media_salarial(salarios)
print("A média salarial é: ", media_s)

acima_da_media = salarios_acima_media(salarios)
print("Os salários acima da média são: ", acima_da_media)


ma_salario = maior_salario(salarios)
print("O maior salário é: ", ma_salario)

me_salario = menor_salario(salarios)
print("O menor salário é: ", me_salario)