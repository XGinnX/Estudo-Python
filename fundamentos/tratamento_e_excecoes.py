# O que é tratamento de exceções
# Importância
n1=2
n2=0
n3=5
n4=10

#Estrutura básica Try - Except
try:
    print(n1/n2)
except:
    print("Não é permitida divisão por 0")

#Except nomeadas
try:
    print(n1/n2)
except ZeroDivisionError:
    print("Não é permitida divisão por 0")

#Estrutura Try - Except - Else
try:
    resultado = n4 / n3
except  ZeroDivisionError:
    print("Erro: Divisão por zero!")
else:
    # Bloco de código executado se nenhuma exceção for lançada dentro do bloco try
    print("Resultado:", resultado)

#Estrutura Try - Except - finally
try:
    resultado = n2 / n1
except ZeroDivisionError:
    print("Erro: Zero não é dívisivel")
finally:
    #independentemente de ter ocorrido uma exceção ou não
    print("Continua independente do resultado")


