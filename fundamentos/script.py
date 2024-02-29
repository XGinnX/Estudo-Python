# Primeiro Hello world
print('Olá mundo');
print('----------------Operações---------------')
# Operacoes matematicas
#Adição
print (2+2);
#multiplicação
print (5*5);
#subtração
print(3 - 1.5);
#divisão
print(165 / 5);
#exponenciação
print(2**10)
#Módulo - Retorna o resto
print(10 % 3)

print('-----------Variaveis------------------')
#variaveis
mensagem = "Adicionando váriavel string"; #variável string
numero_inteiro = 1; #Número Inteiro
numero_float = 2.2; #Número flutuante
booleano = True;
print (mensagem);
print(numero_inteiro);
print(numero_float);
print(booleano);

print('-------------- Operadores --------------')

#operadores
print(1 == 1) #Igualdade
print(2.2 != numero_float) #Diferença
print(numero_float >= numero_inteiro) #Maior ou igual
print(numero_inteiro <= 0) #menor ou igual

print("------------Operadores Relacionais----------")
x = 5;
y = 4;
z = 5;

print(z == z or y == z) #OR - Uma das condições devem ser verdadeiras
print(z == z and y == z) #AND - Ambas as condições devem ser verdadeiras

print('--------- Condicionais -------------')

#IF e Else
time_casa_gols = 4;
time_fora_gols = 1;

if time_casa_gols > time_fora_gols:
    print("O Time da casa ganhou em gols")
else:
    print ("O Time de fora tem mais gols que o time de casa")

# Elif
n1 = 5;
n2 = 6;

if n1 == n2:
    print('N1 é igual N2');
elif n2 > n1:
    print('N2 é maior que N1');
else:
    print('N2 é menor que N1');

#Laço de repetição
#while
print('Contagem regressiva de 5 a 1 usando while');
cont = 5
while cont > 0:
    print(cont)
    cont -= 1

# FOR
print('Iterando sobre os elementos de uma lista usando for')
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

#Foreach - embora Python não tenha um loop foreach explícito, podemos alcançar o mesmo resultado com for
print(' Iterando sobre os caracteres de uma string usando for')
palavra = "Python"
for letra in palavra:
    print(letra)

