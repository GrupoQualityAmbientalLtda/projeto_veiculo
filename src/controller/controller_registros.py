from PIL import Image, UnidentifiedImageError
import numpy as np

from src.dao.dao_registro import DaoRegistro
from src.utils.imagem_utils import converter_imagem
from src.models.registros import Registro
from src.database.db import create_session

class ControllerRegistro:
    @staticmethod
    def salvar_registro(imagem_binaria, id_avaria, id_formulario):
        """Chama o DAO para salvar o registro no banco."""
        with create_session() as session:
            return DaoRegistro.criar_registro(session, imagem_binaria, id_avaria, id_formulario)

    @staticmethod
    def processar_e_salvar_imagem(uploaded_file, id_avaria, id_formulario):
        """Processa a imagem e chama a função para salvar no banco."""
        if uploaded_file is None:
            raise ValueError("Nenhuma imagem enviada.")

        try:
            # Processa a imagem
            imagem_pil = Image.open(uploaded_file)
        except UnidentifiedImageError:
            raise ValueError("Arquivo enviado não é uma imagem válida.")

        imagem_array = np.array(imagem_pil)
        imagem_binaria = converter_imagem(imagem_array)

        # Salva o registro no banco
        return ControllerRegistro.salvar_registro(imagem_binaria, id_avaria, id_formulario)


