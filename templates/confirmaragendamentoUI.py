import streamlit as st
import pandas as pd
from views import View
import time

class ConfirmarAgendamentosUI:
  def main():
    st.header("Confirmar Agendamentos")
    ConfirmarAgendamentosUI.confirmar()
  
  def confirmar():
    lista = []
    lista_2 = []
    for i in View.nao_confirmado():
        lista.append([i.get_id_cliente(), i.get_data(), i.get_id_servico(), i.get_confirmado()])
        lista_2.append(i)
    df = pd.DataFrame(lista, columns=['Nome', 'Data', 'Serviço', 'Confirmado'])
    st.dataframe(df, hide_index=True)
    op = st.selectbox('Confirmar Agendamento', lista_2)
    if st.button('Salvar'):
       View.confirmar_agendamento(op.get_id(), op.get_data(), True, op.get_id_cliente(), op.get_id_servico())
       st.success('Agendamento confirmado com sucesso')
       time.sleep(2)
       st.rerun()