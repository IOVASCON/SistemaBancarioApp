import unittest
# Importa o módulo unittest para criar e executar testes de unidade

from models.cliente import Cliente, PessoaFisica
# Importa as classes Cliente e PessoaFisica do módulo cliente

class TestCliente(unittest.TestCase):
    # Define a classe de teste para a classe Cliente

    def test_adicionar_conta(self):
        # Testa se uma conta é adicionada corretamente a um cliente
        cliente = PessoaFisica("João", "01-01-1990", "12345678900", "Rua A, 123")
        # Cria uma instância de PessoaFisica
        self.assertEqual(len(cliente.contas), 0)
        # Verifica se o cliente começa com zero contas
        
        cliente.adicionar_conta("Conta 1")
        # Adiciona uma conta ao cliente
        self.assertEqual(len(cliente.contas), 1)
        # Verifica se o cliente tem uma conta
        self.assertIn("Conta 1", cliente.contas)
        # Verifica se "Conta 1" está na lista de contas do cliente

    def test_realizar_transacao(self):
        # Implementar teste para realizar_transacao
        pass

if __name__ == '__main__':
    unittest.main()
    # Executa os testes se este arquivo for executado diretamente
