import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class AgendaHorarioUI:

  def main():
    st.header("Agendar Horário")
    AgendaHorarioUI.agendar_horario()

  def agendar_horario():
    lista_1 = []
    lista_2 = []
    for obj in View.agendar_listar_semana():
      if obj.get_id_cliente() == st.session_state['cliente_nome']:
        if obj not in View.nao_confirmado():
          lista_1.append([datetime.strftime(obj.get_data(), '%d/%m/%Y %H:%M'), obj.get_id_servico()])
          lista_2.append(obj)
    if len(lista_1) == 0: st.write("Nenhum horário disponível")
    else:
      df = pd.DataFrame(lista_1, columns=['Data', 'Serviço'])
      st.dataframe(df, hide_index=True)
      op = st.selectbox('Selecione um serviço e seu horário', lista_2)
      if st.button("Agendar"):
        View.agendar_horario(op.get_id(), datetime.strftime(op.get_data(), '%d/%m/%Y %H:%M'), False, op.get_id_cliente(), op.get_id_servico())
        st.success("Horário agendado com sucesso")
        time.sleep(2)
        st.rerun()