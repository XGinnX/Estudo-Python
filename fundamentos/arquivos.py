# -*- coding: utf-8 -*- 
# Abre um arquivo
arquivo = open("./arquivos/arquivo.txt")
print(arquivo)

#Lê a linha de um arquivos
linhas = arquivo.readlines()
#Exibição
#1. Exibe as linhas como uma lista
print(linhas)
#2. Lê linha por linhas
for linha in linhas:
    print(linha)

texto_completo = arquivo.read()
print("TEXTO COMPLETO" + texto_completo)

#Criando Arquivo
w = open("./arquivos/arquivo.txt","w")
w.write("Adicionando texto no meu arquivo novo\n")
w.close()