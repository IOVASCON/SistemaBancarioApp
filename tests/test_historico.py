import unittest
# Importa o módulo unittest para criar e executar testes de unidade

from models.historico import Historico
# Importa a classe Historico do módulo historico

from models.transacao import Saque, Deposito
# Importa as classes Saque e Deposito do módulo transacao

from models.conta import Conta
# Importa a classe Conta do módulo conta

class TestHistorico(unittest.TestCase):
    # Define a classe de teste para a classe Historico

    def test_adicionar_transacao(self):
        # Testa se a transação é adicionada corretamente ao histórico
        historico = Historico()
        # Cria uma instância de Historico
        conta = Conta(123, "João")
        # Cria uma instância de Conta
        saque = Saque(100)
        # Cria uma instância de Saque
        
        saque.registrar(conta)
        # Registra o saque na conta
        historico.adicionar_transacao(saque)
        # Adiciona a transação de saque ao histórico
        
        self.assertEqual(len(historico.transacoes), 1)
        # Verifica se há uma transação no histórico
        self.assertEqual(historico.transacoes[0]['tipo'], 'Saque')
        # Verifica se o tipo da transação é 'Saque'
        self.assertEqual(historico.transacoes[0]['valor'], 100)
        # Verifica se o valor da transação é 100

if __name__ == '__main__':
    unittest.main()
    # Executa os testes se este arquivo for executado diretamente
