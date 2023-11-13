import streamlit as st
from views import View
import time

class EditarPerfilUI:

  def main():
    st.header("Editar Perfil")
    EditarPerfilUI.abrir_agenda()

  def editar_perfil():
    nome = st.text_input("Nome")
    email = st.text_input("E-mail*")
    fone = st.text_input("Fone")
    senha = st.text_input("Senha")
    if st.button("Editar"):
      View.editar_perfil(id, nome, email, fone, senha)
      st.success("Perfil editado com sucesso!")
      time.sleep(2)
      st.rerun()