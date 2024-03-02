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

#MATRIZ
print('------------MATRIZ------------')
# Criando uma matriz 3x3 inicializada com zeros
matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Acessando elementos da matriz
print("Elemento na linha 2, coluna 1:", matriz[1][0])

# Modificando um elemento da matriz
matriz[1][0] = 5
print("Nova matriz após modificação:", matriz)

# Iterando sobre a matriz
print("Iterando sobre a matriz:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Pula para a próxima linha

# Adicionando uma nova linha à matriz
nova_linha = [1, 2, 3]
matriz.append(nova_linha)
print("Matriz após adicionar uma nova linha:", matriz)

# Removendo a segunda linha da matriz
del matriz[1]
print("Matriz após remover a segunda linha:", matriz)


