#Caixa eletrônico

#Iniciando o sistema
print("--Caixa eletrônico--")
print("\n")

print("1 - para ver seu saldo")
print("2 - para depositar")
print("3 - para sacar")
print("5 - para encerrar")



saldoInicial = 1000.00

def verSaldo(saldoInicial):
    print(f"Seu saldo atual {saldoInicial}")


def depositar(saldoInicial):
    v_deposito = float(input("Valor a ser depositado: "))
    v_final_deposito = v_deposito + saldoInicial 
    return v_final_deposito

    print(v_final_deposito)




def  sacar(valorInicial):
    try:
      v_sacar = int(input("Valor a ser sacado: "))

      if v_sacar % 10 == 0:
          saldo_sacado = saldoInicial - v_sacar

        
    except:
        print("O valor do saque tem que ser mmúltiplo de 10")

    else:
       var_sacar = return saldo_sacado
    print(saldo_sacado)
    


def historico():
    print(f"Você depositou R${depositar}")
    print(f"Você sacou R$ {sacar}")


while True:
       acao = int(input("Digite o que você quer fazer com o dinheiro:"))

       match acao:
           case 1:
               verSaldo(saldoInicial)

           case 2:
               depositar(saldoInicial)

           case 3:
               sacar(saldoInicial)

           case 4:
               historico(saldoInicial)

           case 5:
               print("Caixa encerrado")
               break   
                     
               
