from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import AgendaHojeUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfiladminUI import EditarPerfilAdminUI
from templates.editarperfilclienteUI import EditarPerfilClienteUI
from templates.agendarhorarioUI import AgendaHorarioUI
from templates.veragendamentosUI import VerAgendamentosUI
from templates.confirmaragendamentoUI import ConfirmarAgendamentosUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Agenda", "Manter Clientes", "Manter Serviços", "Abrir Agenda do Dia", "Reajustar Preço", "Editar Perfil", "Confirmar Agendamento"])
    if op == "Manter Agenda": ManterAgendaUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Serviços": ManterServicoUI.main()
    if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
    if op == "Reajustar Preço": ServicoReajusteUI.main()
    if op == "Editar Perfil": EditarPerfilAdminUI.main()
    if op == "Confirmar Agendamento": ConfirmarAgendamentosUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Agenda de Hoje", "Editar Perfil", "Agendar Horário", "Ver Agendamentos"])
    if op == "Agenda de Hoje": AgendaHojeUI.main()
    if op == "Editar Perfil": EditarPerfilClienteUI.main()
    if op == "Agendar Horário": AgendaHorarioUI.main()
    if op == "Ver Agendamentos": VerAgendamentosUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      clientes = View.cliente_listar()
      if st.session_state["cliente_nome"] == clientes[0].get_nome(): IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()



