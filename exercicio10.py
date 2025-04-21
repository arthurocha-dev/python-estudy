#Sistema de troco 2

valor_compra = int(input("Valor da compra: "))
valor_pago = int(input("Valor pago:"))

troco =  valor_pago - valor_compra

notas = [100, 50, 20, 10, 5, 2, 1]


def calcular_troco_notas(troco,notas):
  for x in notas:
    quantidade = troco // x

    if quantidade > 0:
      print(f"{quantidade} notas de R${x}")
      troco = troco - (quantidade * x)

    
  return troco


notas_p = calcular_troco_notas(troco,notas)
print(notas_p)