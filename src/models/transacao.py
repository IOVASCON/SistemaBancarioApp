from abc import ABC, abstractmethod
# Importa o módulo ABC (Abstract Base Class) e abstractmethod para definir classes e métodos abstratos

class Transacao(ABC):
    # Define a classe abstrata Transacao, que herda de ABC (Abstract Base Class)

    @property
    @abstractmethod
    def valor(self):
        # Define uma propriedade abstrata valor, que deve ser implementada pelas subclasses
        pass

    @abstractmethod
    def registrar(self, conta):
        # Define um método abstrato registrar, que deve ser implementado pelas subclasses
        pass


class Saque(Transacao):
    # Define a classe Saque, que herda da classe Transacao

    def __init__(self, valor):
        # Método inicializador (construtor) da classe Saque
        self._valor = valor
        # Inicializa o atributo _valor com o valor passado como argumento

    @property
    def valor(self):
        # Implementa a propriedade valor da classe abstrata Transacao
        return self._valor
        # Retorna o valor do saque

    def registrar(self, conta):
        # Implementa o método registrar da classe abstrata Transacao
        sucesso_transacao = conta.sacar(self.valor)
        # Chama o método sacar da conta e armazena o resultado em sucesso_transacao

        if sucesso_transacao:
            # Se o saque for bem-sucedido
            conta.historico.adicionar_transacao(self)
            # Adiciona a transacao ao historico da conta


class Deposito(Transacao):
    # Define a classe Deposito, que herda da classe Transacao

    def __init__(self, valor):
        # Método inicializador (construtor) da classe Deposito
        self._valor = valor
        # Inicializa o atributo _valor com o valor passado como argumento

    @property
    def valor(self):
        # Implementa a propriedade valor da classe abstrata Transacao
        return self._valor
        # Retorna o valor do depósito

    def registrar(self, conta):
        # Implementa o método registrar da classe abstrata Transacao
        sucesso_transacao = conta.depositar(self.valor)
        # Chama o método depositar da conta e armazena o resultado em sucesso_transacao

        if sucesso_transacao:
            # Se o depósito for bem-sucedido
            conta.historico.adicionar_transacao(self)
            # Adiciona a transacao ao historico da conta
