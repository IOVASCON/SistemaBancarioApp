from abc import ABC, abstractmethod
# Importa o módulo ABC (Abstract Base Class) e abstractmethod para definir classes e métodos abstratos

from datetime import datetime
# Importa o módulo datetime para trabalhar com datas e horas

class Cliente:
    # Define a classe Cliente

    def __init__(self, endereco):
        # Método inicializador (construtor) da classe Cliente
        self.endereco = endereco
        # Inicializa o atributo endereco com o valor passado como argumento
        self.contas = []
        # Inicializa o atributo contas como uma lista vazia

    def realizar_transacao(self, conta, transacao):
        # Define o método realizar_transacao, que recebe uma conta e uma transacao como parâmetros
        transacao.registrar(conta)
        # Chama o método registrar da transação, passando a conta como argumento

    def adicionar_conta(self, conta):
        # Define o método adicionar_conta, que recebe uma conta como parâmetro
        self.contas.append(conta)
        # Adiciona a conta à lista de contas do cliente


class PessoaFisica(Cliente):
    # Define a classe PessoaFisica, que herda da classe Cliente

    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Método inicializador (construtor) da classe PessoaFisica
        super().__init__(endereco)
        # Chama o método inicializador da classe base (Cliente) passando o endereco
        self.nome = nome
        # Inicializa o atributo nome com o valor passado como argumento
        self.data_nascimento = data_nascimento
        # Inicializa o atributo data_nascimento com o valor passado como argumento
        self.cpf = cpf
        # Inicializa o atributo cpf com o valor passado como argumento
