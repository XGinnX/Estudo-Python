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
frutas.remove("limão")
print(frutas)

#remove item lista por indice
del frutas[2]
print(frutas)

#Criando lista vazia e adicionando valor
mercado = []
print(mercado)
mercado.append("arroz")
mercado.append("feijão")
mercado.append("açucar")
print(mercado)

# Ordenação de lista
lista = [2,55,1500,33,42,12,5,6,7,100,15,]
# 1. Utilizando o sort
lista.sort() 
print(lista)

#2. Utilizando o Sorted
lista = sorted(lista) 

print(lista)

# Ordernar a lista de forma decrescente
lista.sort(reverse=True) 
print(lista)

#2. Inverter lista
lista.reverse() 
print(lista)

# Dicionários
print('------------DICIONÁRIO------------')
#Estrutura {Chave:Valor}
dicionario = {"A":"AMOR","B":"BORBOLETA","C":"CORAÇÃO"}
print(dicionario)

# consultando dicionario
print(dicionario["A"])

#Passando pelo dicionario e exibe chave e valor
#1. Forma
for chave in dicionario:
    print(chave+":"+dicionario[chave])
#2. Item
for elemento in dicionario.items():
    print(elemento)
# Passando pelos dicionarios e exibindo valores
for elemento in dicionario.values():
    print(elemento)

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


