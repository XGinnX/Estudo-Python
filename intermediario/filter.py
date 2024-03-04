from functools import reduce 

# Filter
 # Filtra elementos de uma lista com base em uma condição definida por uma função, retornando apenas os elementos que atendem à condição.
def pares(n):
    if n%2 == 0:
        return n
    
lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = filter(pares, lista) #filter(funcao, lista)
print(list(lista_pares))

# Reduce
# Aplica uma função a pares de itens de uma lista, reduzindo-os a um único valor.
def soma(x, y):
    return x + y

soma_total = reduce(soma, lista)  # Aplica reduce() à lista original
print(soma_total)

# Zip
# Combina elementos de duas ou mais listas em pares, úteis para percorrer múltiplas listas simultaneamente.
lista_brinquedos = ["boneca","casinha", "carrinho", "boneco","bola"]

for numero, nome in zip(lista, lista_brinquedos):
    print(numero, nome)

# MAP
# Aplica uma função a todos os itens de uma lista e retorna uma nova lista com os resultados.

def dobro (x):
    return x*2

valor = [2,4,6,8,10]

print(dobro(valor)) #Quando multiplica uma lista por 2 ela é concatenada e juntada
valor_dobrado = map(dobro,valor)

for v in valor_dobrado:
    print(v)

valor_quadrado = list(valor_dobrado)

# Lambda
 # Cria funções anônimas de forma rápida e simples, geralmente usadas para funções de uma única expressão.

valor_quadrado = map(lambda i:i**2,lista)
print("----ELEVADO A 2 ------")
print(list(valor_quadrado))
