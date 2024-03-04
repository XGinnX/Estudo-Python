#função Enumerate

#Descobrindo posições de maneira tradicional
brinquedos = ["boneca","casinha", "carrinho", "boneco","bola"]
for i in range(len(brinquedos)):
    print(i, brinquedos[i])

# Usando função Enumerate
for i, nome in enumerate(brinquedos):
 print(i, nome)