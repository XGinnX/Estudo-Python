from functools import reduce 

#filter
def pares(n):
    if n%2 == 0:
        return n
    
lista = [1,2,3,4,5,6,7,8,9,10]
lista_pares = filter(pares, lista) #filter(funcao, lista)
print(list(lista_pares))

#reduce
def soma(x, y):
    return x + y

soma_total = reduce(soma, lista)  # Aplica reduce() à lista original
print(soma_total)

#zip
lista_brinquedos = ["boneca","casinha", "carrinho", "boneco","bola"]

for numero, nome in zip(lista, lista_brinquedos):
    print(numero, nome)

#map
def dobro (x):
    return x*2

valor = [2,4,6,8,10]

print(dobro(valor)) #Quando multiplica uma lista por 2 ela é concatenada e juntada
valor_dobrado = map(dobro,valor)

for v in valor_dobrado:
    print(v)

valor_quadrado = list(valor_dobrado)

#Lambda
valor_quadrado = map(lambda i:i**2,lista)
print("----ELEVADO A 2 ------")
print(list(valor_quadrado))
