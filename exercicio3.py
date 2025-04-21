valoProduto = float(input("Valor do produto: "))
descontoProduto = float (input("Desconto a ser dado: "))

def calcular_total(valoProduto, descontoProduto):
     descontoP = valoProduto * (descontoProduto / 100)
     print(f"O desconto de {descontoProduto}% aplicado sobre o valor de {valoProduto} é: {descontoP} ")
     return descontoP



calcular_total(valoProduto, descontoProduto)