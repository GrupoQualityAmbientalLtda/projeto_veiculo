import streamlit as st
import pandas as pd

from src.controller.controller_avaria import ControllerAvaria
from src.dao.dao_avaria import DaoAvaria
from src.models.avaria import Avaria
from src.database.db import create_session

st.title('Consulta de Avarias')
st.subheader("Pesquisa:")