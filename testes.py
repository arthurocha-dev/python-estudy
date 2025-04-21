# nome = input("Nome: ")
# idade = int(input("Idade: "))
# estado = input("Estado: ")

# informaçoes = {}

# informaçoes["nome"] = nome
# informaçoes["idade"] = idade
# informaçoes["estado"] = estado 

# print(informaçoes)


# dic = {"arroz": 12.98, "macarrão": 43.23, "água": 24.43}

# soma_total = sum(dic.values)
# print(soma)



lista = [100, 50, 20, 10, 5, 2, 1]

def notas(troco):
    for x in lista:
        if troco // x == 0:
            print(f"1 nota de R${x}")

        else:
            continue