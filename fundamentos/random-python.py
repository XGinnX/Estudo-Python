import random as rd

#mantém o mesmo número após o sorteador
# rd.seed(1)

#Sorteia um número inteiro aleatório entre o 0,10
numero = rd.randint(0,10)
print(numero)

lista_numeros = [9,10,7,15,43,66,91,123]

numero_listado = rd.choice(lista_numeros)
print(numero_listado)