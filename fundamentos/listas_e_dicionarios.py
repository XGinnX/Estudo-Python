#listas
frutas = ["abacaxi","laranja","pera","maça","uva"]

print(frutas)

#acessando determinada posição na lista

print(frutas[2])

#tamanho da lista

tamanho = len(frutas)

print(tamanho)

#adicionando na lista
frutas.append("limão")
print(frutas)

#verificando item em lista
if "limão" in frutas:
    print ("fruta está na lista")

#remove item lista
del frutas["limão"]
print (frutas)


