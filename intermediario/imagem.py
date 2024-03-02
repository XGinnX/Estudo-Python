from PIL import Image, ImageDraw, ImageFont

# Abrir a imagem marcada
imagem = Image.open("C:\Users\jeans\OneDrive\Área de Trabalho\Estudo-Python\img")

# Criar um objeto ImageDraw
desenho = ImageDraw.Draw(imagem)

# Definir a fonte e o tamanho do texto
fonte = ImageFont.truetype("arial.ttf", 36)

# Coordenadas onde o texto será inserido
x = 100
y = 100

# Texto a ser inserido na imagem
texto = "Exemplo de texto na imagem"

# Inserir o texto na imagem
desenho.text((x, y), texto, fill="white", font=fonte)

# Salvar a imagem com o texto inserido
imagem.save("imagem_com_texto.jpg")

# Mostrar a imagem resultante
imagem.show()
