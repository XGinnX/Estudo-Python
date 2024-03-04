#função Enumerate
# Permite percorrer uma lista mantendo o controle do índice e do valor de cada elemento.


#Descobrindo posições de maneira tradicional
brinquedos = ["boneca","casinha", "carrinho", "boneco","bola"]
for i in range(len(brinquedos)):
    print(i, brinquedos[i])

# Usando função Enumerate
for i, nome in enumerate(brinquedos):
 print(i, nome)