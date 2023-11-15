import streamlit as st
import pandas as pd
from views import View

class VerAgendamentosUI:
  def main():
    st.header("Ver Agendamentos")
    VerAgendamentosUI.ver()
  
  def ver():
    lista = []
    for i in View.ver_agendamentos():
      if i.get_id() == st.session_state['cliente_id']:
        lista.append([i.get_data(), i.get_id_servico(), i.get_confirmado()])
    df = pd.DataFrame(lista, columns=['Data', 'Serviço', 'Confirmado'])
    st.dataframe(df, hide_index=True)