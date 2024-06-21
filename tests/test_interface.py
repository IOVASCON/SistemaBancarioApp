import unittest
# Importa o módulo unittest para criar e executar testes de unidade

from ui.interface import BancoApp
# Importa a classe BancoApp do módulo interface no pacote ui

import tkinter as tk
# Importa o módulo tkinter para criar interfaces gráficas

class TestInterface(unittest.TestCase):
    # Define a classe de teste para a interface gráfica

    def setUp(self):
        # Configuração inicial antes de cada teste
        self.root = tk.Tk()
        # Cria a janela principal da interface gráfica
        self.app = BancoApp(self.root)
        # Cria uma instância da classe BancoApp

    def tearDown(self):
        # Limpeza após cada teste
        self.root.destroy()
        # Destroi a janela principal da interface gráfica

    def test_novo_usuario(self):
        # Implementar teste para novo_usuario
        pass

    def test_nova_conta(self):
        # Implementar teste para nova_conta
        pass

    def test_depositar(self):
        # Implementar teste para depositar
        pass

    def test_sacar(self):
        # Implementar teste para sacar
        pass

if __name__ == '__main__':
    unittest.main()
    # Executa os testes se este arquivo for executado diretamente
