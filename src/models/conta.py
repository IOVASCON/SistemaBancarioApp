from datetime import datetime
# Importa o módulo datetime para trabalhar com datas e horas

class Historico:
    # Define a classe Historico

    def __init__(self):
        # Método inicializador (construtor) da classe Historico
        self._transacoes = []
        # Inicializa o atributo _transacoes como uma lista vazia

    @property
    def transacoes(self):
        # Define um método getter para o atributo _transacoes
        return self._transacoes
        # Retorna a lista de transações

    def adicionar_transacao(self, transacao):
        # Define o método adicionar_transacao, que recebe uma transacao como parâmetro
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                # Adiciona o nome da classe da transacao como tipo
                "valor": transacao.valor,
                # Adiciona o valor da transacao
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                # Adiciona a data e hora atuais formatadas
            }
        )


class Conta:
    # Define a classe Conta

    def __init__(self, numero, cliente):
        # Método inicializador (construtor) da classe Conta
        self._saldo = 0
        # Inicializa o atributo _saldo com 0
        self._numero = numero
        # Inicializa o atributo _numero com o valor passado como argumento
        self._agencia = "0001"
        # Inicializa o atributo _agencia com "0001"
        self._cliente = cliente
        # Inicializa o atributo _cliente com o valor passado como argumento
        self._historico = Historico()
        # Inicializa o atributo _historico como uma instância da classe Historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        # Define um método de classe para criar uma nova conta
        return cls(numero, cliente)
        # Retorna uma nova instância da classe Conta

    @property
    def saldo(self):
        # Define um método getter para o atributo _saldo
        return self._saldo

    @property
    def numero(self):
        # Define um método getter para o atributo _numero
        return self._numero

    @property
    def agencia(self):
        # Define um método getter para o atributo _agencia
        return self._agencia

    @property
    def cliente(self):
        # Define um método getter para o atributo _cliente
        return self._cliente

    @property
    def historico(self):
        # Define um método getter para o atributo _historico
        return self._historico

    def sacar(self, valor):
        # Define o método sacar, que recebe um valor como parâmetro
        saldo = self.saldo
        # Armazena o saldo atual
        excedeu_saldo = valor > saldo
        # Verifica se o valor do saque excede o saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            # Informa que a operação falhou devido a saldo insuficiente

        elif valor > 0:
            self._saldo -= valor
            # Subtrai o valor do saque do saldo
            print("\n=== Saque realizado com sucesso! ===")
            # Informa que o saque foi realizado com sucesso
            return True
            # Retorna True indicando que o saque foi bem-sucedido

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            # Informa que a operação falhou devido a valor inválido

        return False
        # Retorna False indicando que o saque falhou

    def depositar(self, valor):
        # Define o método depositar, que recebe um valor como parâmetro
        if valor > 0:
            self._saldo += valor
            # Adiciona o valor do depósito ao saldo
            print("\n=== Depósito realizado com sucesso! ===")
            # Informa que o depósito foi realizado com sucesso
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            # Informa que a operação falhou devido a valor inválido
            return False
            # Retorna False indicando que o depósito falhou

        return True
        # Retorna True indicando que o depósito foi bem-sucedido


class ContaCorrente(Conta):
    # Define a classe ContaCorrente, que herda da classe Conta

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Método inicializador (construtor) da classe ContaCorrente
        super().__init__(numero, cliente)
        # Chama o método inicializador da classe base (Conta)
        self.limite = limite
        # Inicializa o atributo limite com o valor passado como argumento ou 500
        self.limite_saques = limite_saques
        # Inicializa o atributo limite_saques com o valor passado como argumento ou 3

    def sacar(self, valor):
        # Define o método sacar, que recebe um valor como parâmetro
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )
        # Conta o número de saques realizados

        excedeu_limite = valor > self.limite
        # Verifica se o valor do saque excede o limite
        excedeu_saques = numero_saques >= self.limite_saques
        # Verifica se o número de saques excede o limite de saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            # Informa que a operação falhou devido ao valor do saque exceder o limite

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            # Informa que a operação falhou devido ao número máximo de saques ter sido excedido

        else:
            return super().sacar(valor)
            # Chama o método sacar da classe base (Conta)

        return False
        # Retorna False indicando que o saque falhou

    def __str__(self):
        # Define o método especial __str__ para retornar uma representação em string da ContaCorrente
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
        # Retorna uma string formatada com os detalhes da conta
