#try e except são usados para tratar erros que podem acontecer durante a execução de um código.

#O bloco try tenta executar um trecho de código que pode causar erro.

#Se um erro ocorrer, o bloco except é executado, evitando que o programa seja interrompido.


# try:
#     n1 = int(input("Digite um número: "))
#     n2 = int(input("Digite outro número: "))

#     soma = n1 + n2
#     print(soma)
# except:
#     print("digite números")



# try:
#     numero = int(input("Digite um valor númerico: "))
    
# except ValueError:
#     print("Error! Digite um número")

# else:
#     print("Seu número é: ", numero) #O else roda caso o programa dê certo

# finally:                #O finally encerra seu programa independente de ter dado certo ou não
#     print("Sistema encerrado")



#  Exercício

print("Cálculo divisão")

try:
   number1 = int(input("Digite número1: "))
   number2 = int(input("Digite número2: "))
   resultado = number1 / number2

except ValueError:
    print("Entrada inválida! Use apenas números.")

except ZeroDivisionError:
     print("Erro! Divisão por zero não permitida.")

else:
    print(f"Resultado da divisão = {resultado:.2f}")

finally:
    print("programa encerrado.")    




