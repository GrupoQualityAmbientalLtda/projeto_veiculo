from PIL import Image
import io

# Função para converter a imagem do canvas para um formato binário (BLOB)
def converter_imagem(image_data):
    # Converte a imagem numpy para PIL
    img = Image.fromarray(image_data)
    # Salva a imagem em um buffer de bytes
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')  # Salva como PNG
    img_byte_arr = img_byte_arr.getvalue()  # Obtém os dados binários da imagem
    return img_byte_arr