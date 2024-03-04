# list comprehension

#Maneira tradicional caso necessite adicionar o quadrado de uma lista em outra
x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

# Com o list comprehension
a = [1,2,3,4,5]
b = [i**2 for i in a] #[valor_a_adicionar laço condição]

print("Usando list comprehension")
print(b)

c=[i for i in a if i%2==1]
print("Usando list comprehension usando condições")
print(c)
