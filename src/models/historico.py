from datetime import datetime
# Importa o módulo datetime para trabalhar com datas e horas

class Historico:
    # Define a classe Historico

    def __init__(self):
        # Método inicializador (construtor) da classe Historico
        self._transacoes = []
        # Inicializa o atributo _transacoes como uma lista vazia para armazenar as transações

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
                # Adiciona a data e hora atuais formatadas no formato "dd-mm-YYYY HH:MM:SS"
            }
        )
        # Adiciona um dicionário representando a transacao à lista _transacoes
