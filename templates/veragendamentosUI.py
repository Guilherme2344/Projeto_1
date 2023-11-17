import streamlit as st
import pandas as pd
from views import View
from datetime import datetime

class VerAgendamentosUI:
  def main():
    st.header("Ver Agendamentos")
    VerAgendamentosUI.ver()
  
  def ver():
    lista = []
    for i in View.nao_confirmado():
      if i.get_id_cliente() == st.session_state['cliente_nome']:
        lista.append([datetime.strftime(i.get_data(), '%d/%m/%Y %H:%M'), i.get_id_servico(), i.get_confirmado()])
    if len(lista) == 0: st.write('Nenhum agendamento solicitado')
    else:
      df = pd.DataFrame(lista, columns=['Data', 'Serviço', 'Confirmado'])
      st.dataframe(df, hide_index=True)