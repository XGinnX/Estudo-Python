#Input 
nome = input('Digite seu nome: ')
print('Olá, '+nome)

sobrenome= input("Digite seu sobrenome: ")

#Concatenar
concatenar = nome + " "+ sobrenome;
print("Seja bem vindo, "+ concatenar)

#Cadeia de strings
print (nome[0])
print (sobrenome[0])

#SPlit
poema = "O rato roeu a roupa do rei de ROMA"
minha_lista = poema.split(" ")
print(minha_lista)

#FIND
busca =poema.find("ROMA");
print(busca)

#Replace
print(poema.replace("rei","rainha"))
