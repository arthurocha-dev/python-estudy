#Cálculo de salário com benefícios

#Nome do funcionário
funcionario = input("Nome do funcionário: ")

#Salário base do funcionário                   try except usado para tratação de erros
try:
 salario_base = float(input("Salário base do funcionário: "))

except ValueError:
   print("Erro! digite apenas valores numéricos")

else:
    salario_base
   

#quantidade de filhos do funcionário     
try:
   qtd_filhos = int(input("Quantos filhos o funcionário tem? "))

except ValueError:
   print("Erro! Digite apenas valores númericos")

else:
   qtd_filhos


#Função para aumentar o salário de acordo com a quantidade de filhos
def aumento_salario(salario_base,qtd_filhos):
    aumento = salario_base * (qtd_filhos * 0.05)
    return aumento




#Saída de dados 
salario_aumentado = aumento_salario(salario_base,qtd_filhos)
print(f"O funcionário {funcionario} recebe como salário base R${salario_base:.2f}, tem {qtd_filhos}, por isso seu aumento no salário é de 5%, então seu novo salário vai ser de R$ {salario_aumentado:.2f}")
