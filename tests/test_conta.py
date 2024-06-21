import unittest
# Importa o módulo unittest para criar e executar testes de unidade

from models.conta import Conta, ContaCorrente
# Importa as classes Conta e ContaCorrente do módulo conta

class TestConta(unittest.TestCase):
    # Define a classe de teste para a classe Conta

    def test_depositar(self):
        # Testa se o depósito é realizado corretamente
        conta = Conta(123, "João")
        # Cria uma instância de Conta
        self.assertTrue(conta.depositar(100))
        # Verifica se o depósito foi bem-sucedido
        self.assertEqual(conta.saldo, 100)
        # Verifica se o saldo da conta é atualizado corretamente

    def test_sacar(self):
        # Testa se o saque é realizado corretamente
        conta = Conta(123, "João")
        conta.depositar(100)
        # Realiza um depósito antes do saque
        self.assertTrue(conta.sacar(50))
        # Verifica se o saque foi bem-sucedido
        self.assertEqual(conta.saldo, 50)
        # Verifica se o saldo da conta é atualizado corretamente
        self.assertFalse(conta.sacar(100))
        # Verifica se o saque falha quando o saldo é insuficiente

    def test_limite_saques(self):
        # Testa o limite de saques de uma conta corrente
        conta = ContaCorrente(123, "João", limite=500, limite_saques=3)
        conta.depositar(1000)
        # Realiza um depósito inicial
        self.assertTrue(conta.sacar(100))
        # Verifica se o primeiro saque é bem-sucedido
        self.assertTrue(conta.sacar(100))
        # Verifica se o segundo saque é bem-sucedido
        self.assertTrue(conta.sacar(100))
        # Verifica se o terceiro saque é bem-sucedido
        self.assertFalse(conta.sacar(100))
        # Verifica se o quarto saque falha devido ao limite de saques excedido

if __name__ == '__main__':
    unittest.main()
    # Executa os testes se este arquivo for executado diretamente
