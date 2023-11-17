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
    lista_3 = []
    for obj in View.agendar_listar_semana():
      if obj.get_id_cliente() == st.session_state['cliente_nome']:
        lista_1.append([datetime.strftime(obj.get_data(), '%d/%m/%Y %H:%M'), obj.get_id_servico()])
        lista_2.append(datetime.strftime(obj.get_data(), '%d/%m/%Y %H:%M'))
        lista_3.append(obj.get_id_servico())
    if len(lista_1) == 0: st.write("Nenhum horário disponível")
    else:
      df = pd.DataFrame(lista_1, columns=['Data', 'Serviço'])
      st.dataframe(df, hide_index=True)
      horario = st.selectbox("Selecione um horário", lista_2)
      servicos = st.selectbox("Selecione um serviço", set(lista_3))
      for i in View.agenda_listar():
        i = i.get_id() 
      nome = st.session_state['cliente_nome']
      if st.button("Agendar"):
        View.agendar_horario(i, horario, False, nome, servicos)
        st.success("Horário agendado com sucesso")
        time.sleep(2)
        st.rerun()