from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime

class View:
  def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_email() == "admin": return
    View.inserir(Cliente(0, "admin", "admin", "0000", "admin"))

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None

  def servico_listar():
    return NServico.listar()

  def servico_listar_id(id):
    return NServico.listar_id(id)

  def servico_inserir(descricao, valor, duracao):
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.inserir(Servico(0, descricao, valor, duracao))

  def servico_atualizar(id, descricao, valor, duracao):
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.atualizar(Servico(id, descricao, valor, duracao))

  def servico_excluir(id):
    NServico.excluir(Servico(id, "", 0, 10))

  def servico_reajustar(percentual):
    for servico in View.servico_listar():    
      NServico.atualizar(Servico(servico.get_id(), servico.get_descricao(), servico.get_valor() * (1 + percentual/100), servico.get_duracao()))

  def agenda_listar():
    return NAgenda.listar()

  def agenda_listarhoje():
    r = []
    hoje = datetime.datetime.today()
    for horario in View.agenda_listar():
      if horario.get_confirmado() == False and horario.get_data().date() == hoje.date():
        r.append(horario)
    return r    

  def agenda_inserir(data, confirmado, id_cliente, id_servico):
    NAgenda.inserir(Agenda(0, data, confirmado, id_cliente, id_servico))

  def agenda_atualizar(id, data, confirmado, id_cliente, id_servico):
    NAgenda.atualizar(Agenda(id, data, confirmado, id_cliente, id_servico))

  def agenda_excluir(id):
    NAgenda.excluir(Agenda(id, "", "", 0, 0))

  def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
    data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
    delta = datetime.timedelta(minutes = intervalo) 
    aux = data_inicio
    while aux <= data_fim :
      NAgenda.inserir(Agenda(0, aux, True, 0, 0))
      aux = aux + delta

  def editar_perfil(id, nome, email, fone, senha):
    NCliente.atualizar(Cliente(id, nome, email, fone, senha))

  def agendar_listar_semana():
    semana = []
    hoje = datetime.datetime.today()
    for horario in View.agenda_listar():
      if horario.get_data().date() - hoje.date() <= datetime.timedelta(days=7):
        semana.append(horario)
    return semana
  
  def nao_confirmado():
    return NAgenda.listar_nao_confirmados()
    
  def agendar_horario(id, horario, confirm, nome, servico):
    NAgenda.atualizar(Agenda(id, datetime.datetime.strptime(horario, '%d/%m/%Y %H:%M'), confirm, nome, servico))

  def ver_agendamentos():
    lista = []
    lista_2 = []
    for agendamentos in View.agenda_listar():
      if agendamentos in View.nao_confirmado(): 
        lista.append(agendamentos)
        return lista
      else:
        lista_2.append(agendamentos)
    return lista_2
  
  def confirmar_agendamento(id, horario, confirm, nome, servico):
    NAgenda.atualizar(Agenda(id, horario, confirm, nome, servico))
