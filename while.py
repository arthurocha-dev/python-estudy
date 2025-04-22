print("Mensagens 💬")

n_usuario = input(" User1: digite seu nome de usuário com '@' pra iniciar a conversa: ")
n_usuario2 = input("User2: digite seu nome de usuário com  \'@\' pra iniciar a conversa:")

print("\n")

print("Digite \"x\" pra terminar a conversa ")
print("Digite \"tr\" pra trocar de usuário")


print("\n")

userAtual = n_usuario  #vai começar com o usuário1

while True:
    mensagem = input (f"{userAtual}: ")  #vai começar com o usuário1

    if mensagem == "tr":                 #se a mensagem digitada for "tr",
        if userAtual == n_usuario:       #ele vai executar esse item, que: se o usuário atual, for o usuário1, a variável usuário atual vai atualizar para usuário2
            userAtual = n_usuario2

        else:                           #caso a mensagem digitada seja "tr" e o usuário atual, não seja usuário1 (então userAtual é 2 agora), a variável usuário atual vai ser atualizada para usuário1  
            userAtual = n_usuario

    if mensagem == "x":
        break

print("Conversa terminada!")    
