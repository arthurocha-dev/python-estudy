#Checkar se um número é primo ou não

print("-----Checke se seu número é primo!------")

#Dando espaçamento na tela para melhor organização
print("\n")

#Informando o usuário se for True é primo, se não for primo é False a saída
print("Se a resposta for True, seu número é primo, caso contrário, é False")
print("\n")


n = int(input("Digite um número: "))

def eh_primo(n):
   if n <= 1:
      print("Número primo não é menor que 1, e tem que ser número natural")
      return False
   
   for c in range(2,n):                                               #Aqui o for vai percorrer números, até chegar no número
      if n % c == 0:                                         #digitado, se até lá, ele encontrar um número que seja dividido           
         print("Divisível por outros números")               # por n e reste 0 na divisão, esse número é primo
         return False                                        #então vai retornar false, se nenhum dos if's rodarem
                                                             # é primo, retorna True          
                  
                                                             
   return True
         


print(eh_primo(n))



