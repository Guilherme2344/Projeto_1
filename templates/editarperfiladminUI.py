import streamlit as st
from views import View
import time

class EditarPerfilAdminUI:

  def main():
    st.header("Editar Perfil")
    EditarPerfilAdminUI.editar_perfil()

  def editar_perfil():
    id = st.session_state['cliente_id']
    email = st.text_input("E-mail")
    fone = st.text_input("Fone")
    senha = st.text_input("Senha")
    if st.button("Editar"):
      View.editar_perfil_admin(id, "admin", email, fone, senha)
      st.success("Perfil editado com sucesso!")
      time.sleep(2)
      st.rerun()