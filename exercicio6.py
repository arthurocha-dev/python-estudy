#Sistema de troco

valor_compra = float(input("Digite o valor total da compra: "))
valor_pago = float(input("Valor pago: "))

def calcular_troco(valor_compra, valor_pago):

    global troco
    if valor_compra > valor_pago:
       falta_pagar = valor_compra - valor_pago

    elif valor_compra < valor_pago:
       troco = valor_pago - valor_compra

    else:
        n_valor = "Não precisa de troco, valor pago suficiente"


    return falta_pagar

def quebrar_troco_em_notas(troco):
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]
    for x in notas:
        if troco % x == 0:
            print(f"1 nota de R${x}")

        return x


troco = calcular_troco(valor_compra, valor_pago)   
print(troco)     
    
q_notas = quebrar_troco_em_notas(troco)
print(q_notas)    

