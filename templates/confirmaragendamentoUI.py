import streamlit as st
import pandas as pd
from views import View
import time

class ConfirmarAgendamentosUI:
  df_format = None
  @classmethod
  def main(cls):
    st.header("Confirmar Agendamentos")
    ConfirmarAgendamentosUI.confirmar()
  
  @classmethod
  def confirmar(cls):
    lista = []
    lista_2 = []
    for i in View.nao_confirmado():
        lista.append([i.get_id(), i.get_id_cliente(), i.get_data(), i.get_id_servico(), i.get_confirmado()])
        lista_2.append(i)
    if len(lista) == 0: st.write('Nenhum agendamento solicitado')
    else:
      df = pd.DataFrame(lista, columns=['Id', 'Nome', 'Data', 'Serviço', 'Confirmado'])
      cls.df_format = st.data_editor(df, hide_index=True, disabled=('Id', 'Nome', 'Data', 'Serviço'), on_change=ConfirmarAgendamentosUI.salvar())
      # op = st.selectbox('Confirmar Agendamento', lista_2)
      #if st.button('Salvar'):
        #confirmado = df_format['Confirmado'].bool()
        #View.confirmar_agendamento(op.get_id(), op.get_data(), confirmado, op.get_id_cliente(), op.get_id_servico())
        #st.success('Agendamento confirmado com sucesso')
        #time.sleep(2)
        #st.rerun()

  @classmethod
  def salvar(cls):
    if cls.df_format is not None:
      View.confirmar_agendamento(int(cls.df_format['Id']))
      st.success('Agendamento confirmado com sucesso')
      time.sleep(2)