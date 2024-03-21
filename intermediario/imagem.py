from PIL import Image, ImageDraw, ImageFont

# Abrir a imagem marcada
imagem = Image.open(r"C:\Users\jeans\OneDrive\Área de Trabalho\Estudo-Python\img\escala.png")

# Criar um objeto ImageDraw
desenho = ImageDraw.Draw(imagem)

# Definir a fonte e o tamanho do texto
fonte = ImageFont.truetype("arial.ttf", 75)

# Coordenadas onde o texto será inserido
#x = 110
x = [110, 445, 840,1350,1855]
y = 950
#y = 1125

# Texto a ser inserido na imagem
texto =[
        {"evento":"CULTO", "data":"10/04","projeção":"Jean","captação":"André","backup":"Fany"},
        {"evento":"SALA", "data":"10/04","projeção":"Mariah","captação":"Nina","backup":"Dani"}]
#texto = "Culto"
#data = "10/02"
#projecao = "Jean"
#captacao = "Daniel"
#backup = "Mathew"

contador = 0 
# Inserir o texto na imagem
while contador < 2:
    
    desenho.text((x[0], y), texto[contador].get("evento"), fill="white", font=fonte)
    desenho.text((x[1], y), texto[contador].get("data"), fill="yellow", font=fonte)
    desenho.text((x[2], y), texto[contador].get("projeção"), fill="white", font=fonte)
    desenho.text((x[3], y), texto[contador].get("captação"), fill="white", font=fonte)
    desenho.text((x[4], y), texto[contador].get("backup"), fill="white", font=fonte)
    y = y+180
    contador+=1

# Salvar a imagem com o texto inserido
imagem.save(r"C:\Users\jeans\OneDrive\Área de Trabalho\Estudo-Python\img\imagem_com_texto.png")

# Mostrar a imagem resultante
imagem.show()
