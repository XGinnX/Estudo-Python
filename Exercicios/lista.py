#Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.
idade = int(input('Digite a sua idade: '))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.   
nota_primeiro_semestre = float(input('Digite a nota do primeiro semestre:'))
nota_segundo_semestre = float(input('Digite a nota do segundo semestre: '))

nota_anual = (nota_primeiro_semestre + nota_segundo_semestre) / 2

if nota_anual >= 6:
    print("O Aluno foi aprovado com nota:", nota_anual)
elif nota_anual < 6 and nota_anual >= 5:
    print("Aluno vai para o conselho devido à nota:", nota_anual)
else:
    print("Aluno Reprovado!")

#Escreva um programa que resolva uma equação de segundo grau.   

#Escreva um programa que ordene uma lista numérica com três elementos.   
primeiro = int(input("Digite um numero:"))
segundo = int(input("Digite um numero:"))
terceiro = int(input("Digite um numero:"))


if primeiro > segundo and primeiro > terceiro:
    if segundo > terceiro:
        print(primeiro, "> ", segundo, "> ", terceiro)
    else:
        print(primeiro, "> ", terceiro, "> ", segundo)
elif segundo > primeiro and segundo > terceiro:
    if primeiro > terceiro:
        print(segundo, "> ", primeiro, "> ", terceiro)
    else:
        print(segundo, "> ", terceiro, "> ", primeiro)
else:
    if primeiro > segundo:
        print(terceiro, "> ", primeiro, "> ", segundo)
    else:
        print(terceiro, "> ", segundo, "> ", primeiro)




#Se primeiro for maior que o segundo
 #Se o segundo for maior que o terceiro
  #1. Primeiro > segundo > terceiro
 #else 
   # Se o primeiro for maior que o terceiro:
   # 1. Primeiro > terceiro > segundo
   # else
   # terceiro > primeiro > segundo
#else
   #Se o primeiro for maior que o terceiro
    #1. Segundo > primeiro > terceiro
   #else
   #se o segundo > que o terceiro
   #else


#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 
numero1 = float(input("Digite o primeiro número: "))
operador = input("Digite um operador matemático: ")
numero2 = float(input("Digite um número: "))
resultado = 0

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    print("Operador inválido!")

print("O resultado da operação é:", resultado)
