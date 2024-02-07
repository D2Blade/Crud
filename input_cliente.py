from createbd import cliente
def cadastrar_cliente():

    cad_cliente = cliente.create(nome = input("Nome:\n"), nasc = input("Data de nascimento:\n"), cpf = input("CPF:\n"), ativo = input("Ativar/desativar Cliente S/N:\n"))