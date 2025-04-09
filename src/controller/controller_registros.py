from PIL import Image, UnidentifiedImageError
import numpy as np

from src.dao.dao_registro import salvar_registro, DaoRegistro
from src.utils.imagem_utils import converter_imagem
from src.models.registros import Registro

def processar_e_salvar_imagem(uploaded_file, id_avaria):
    if uploaded_file is None:
        raise ValueError("Nenhuma imagem enviada.")
    
    imagem_pil = Image.open(uploaded_file)
    imagem_array = np.array(imagem_pil)
    imagem_binaria = converter_imagem(imagem_array)

    salvar_registro(imagem_binaria, id_avaria)
