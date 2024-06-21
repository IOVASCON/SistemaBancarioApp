import unittest
# Importa o módulo unittest para criar e executar testes de unidade

from models.transacao import Saque, Deposito
# Importa as classes Saque e Deposito do módulo transacao

from models.conta import Conta
# Importa a classe Conta do módulo conta

class TestTransacao(unittest.TestCase):
    # Define a classe de teste para as classes de transação

    def test_saque(self):
        # Testa se o saque é registrado corretamente
        conta = Conta(123, "João")
        conta.depositar(500)
        # Realiza um depósito antes do saque
        saque = Saque(200)
        # Cria uma instância de Saque
        saque.registrar(conta)
        # Registra o saque na conta
        self.assertEqual(conta.saldo, 300)
        # Verifica se o saldo da conta é atualizado corretamente após o saque

    def test_deposito(self):
        # Testa se o depósito é registrado corretamente
        conta = Conta(123, "João")
        deposito = Deposito(500)
        # Cria uma instância de Deposito
        deposito.registrar(conta)
        # Registra o depósito na conta
        self.assertEqual(conta.saldo, 500)
        # Verifica se o saldo da conta é atualizado corretamente após o depósito

if __name__ == '__main__':
    unittest.main()
    # Executa os testes se este arquivo for executado diretamente
