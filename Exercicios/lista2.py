#Escreva um programa que compare se duas sequências digitadas pelo usuário são iguais.   
seq1 = input("Digite uma sequência?")
seq2 = input("Digite uma sequência?")

def compara_sequencia (sq1, sq2):
    if sq1 == sq2:
        print("A Sequencia é compatível")
    else:
        print("A Sequência não é compatível")
compara_sequencia(seq1,seq2)

