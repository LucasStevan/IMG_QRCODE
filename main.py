# Deu mais trabalho lembrar as funções e comentar do que fazer hahahhah. Bom proveito. 

#By: Lucas Oliveira. GitHub: LucasStevan 

import qrcode
from PIL import Image, ImageEnhance, ImageOps

# Caminho para a imagem de fundo
image_path = "img_exemple.jpg"  # Nome da imagem de fundo
data = "https://www.google.com"  # link (adicione o seu)

# Criar QR de lta correção de erro
qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

#imagem do QR em preto e branco
qr_image = qr.make_image(fill_color="black", back_color="white").convert("L")

# Carregar a imagem de fundo e redimensionar para o tamanho do QR
background_image = Image.open(image_path).convert("RGBA")
qr_width, qr_height = qr_image.size
background_image = background_image.resize((qr_width, qr_height))

# Aumentar o contraste da imagem de fundo para os blocos do QR
enhancer = ImageEnhance.Contrast(background_image)
background_image = enhancer.enhance(2)  # Aumenta o contraste da imagem de fundo

# Criar uma nova imagem com fundo transparente para o QR estilizado
stylized_qr = Image.new("RGBA", (qr_width, qr_height), (255, 255, 255, 0))

# Preenche as áreas escuras do QR com os pixels da imagem de fundo
for x in range(qr_width):
    for y in range(qr_height):
        if qr_image.getpixel((x, y)) == 0:  # Aqui o 0 significa área preta do QR code
            stylized_qr.putpixel((x, y), background_image.getpixel((x, y)))
        else:
            # Mantém as áreas brancas do QR code transparentes
            stylized_qr.putpixel((x, y), (255, 255, 255, 0))

# Adicionar borda branca
border_size = 10  # tamanho da borda (fino)
stylized_qr_with_border = ImageOps.expand(stylized_qr, border=border_size, fill="white")

# Salvar
stylized_qr_with_border.save("qr_code_with_border.png")

print("QR code foi salvo como 'qr_code_with_border.png'")
