from src.dao.dao_avaria import DaoAvaria

class ControllerAvaria:
    @staticmethod
    def salvar_avarias(form_data):
        """
        Salva as avarias no banco de dados.
        form_data: Dicionário contendo os valores das checkboxes.
        """
        try:
            # Cria a avaria no banco de dados
            avaria = DaoAvaria.criar_avaria(**form_data)
            return avaria
        except Exception as e:
            raise e