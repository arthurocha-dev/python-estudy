# Uma função é um bloco de código com um nome,

#que executa uma tarefa específica e só roda quando for chamado.

#📦 Organizar o código: divide o programa em partes menores e mais fáceis de entender.

#🔁 Evitar repetição: você escreve o código uma vez e pode usar várias vezes.

#⚙️ Reutilizar lógica: pode chamar a função em vários lugares do programa.

#🧠 Facilita manutenção: se precisar mudar algo, muda só dentro da função.

#🧪 Facilita testes: você pode testar uma função separada do resto do programa.










#def_ nomeFunção(arfumentoOpcional):
       #instrução(o quê que ela vai fazer)

# def checkPI():

#   n = int(input("Digite um número: "))
#     if n % 2 == 0:
#         print(f"{n} é par")

#     else:
#         print(f'{n} é ímpar')


#Para chamá-la, nomeFunção(argumento(opcional))
#-checkPI(n)



#Funções com argumentos

#-n1 = int(input("Digite um número: "))
#-n2 = int(input("Digite número 2: "))

#-def multiplicacao(n1,n2):
#-    print(f"multiplicação dos dois é: {n1*n2}")


#substitua as variáveis por valores que você quer
#-multiplicacao(n1,n2)



#usando o return

#- a = int(input("x1:"))
#- b = int(input("x2: "))

# def div(x1,x2):
#     divisao = x1 // x2
#     return divisao  #quando usado return, as próximas linhas da função não serão executadas


#resultado = div(a,b)
#print(resultado)


#Função com valor padrão

def saudacao(nome="visitante"):      #Se o usuário não digitar nada, ele passa o valor que foi 
   print("Olá,", nome)               #que foi estabelecido no argumento da função

saudacao()
saudacao("arthur")                   #como aqui foi digitado um valor, vai aparecer o nome



#Função com vários valores

def vestimentas(*roupa):       #coloque o "*" antes da variável, e a função acumulará
      print(roupa)                        #valores dentro de uma tupla
   

vestimentas("blusa", "calça", "sapato")   


def numeros(*numero):
     print(*numero)


numeros(1,2,5,54,243,2,43,32,3,43,434,)   



def lista_compras(cliente="Cliente", *items):
     print(f"Iae {cliente} suas compras foram: {items}")


lista_compras("arthue", "arroz", "biscoito", "água")     