import json
from datetime import datetime

class HistoricoNavegacao:
    def __init__(self):
        self.historico = []
        self.home = ""
        self.arquivo = "historico.json"
        self.carregar()

    def carregar(self):
        """Carrega histórico do arquivo"""
        try:
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                self.historico = dados.get('historico', [])
                self.home = dados.get('home', "")
        except:
            self.historico = []
            self.home = ""

    def salvar(self):
        """Salva histórico no arquivo"""
        dados = {
            'historico': self.historico,
            'home': self.home
        }
        with open(self.arquivo, 'w') as f:
            json.dump(dados, f)

    def adicionar(self, url):
        """Adiciona URL ao histórico e atualiza home"""
        if self.home:
            self.historico.append(self.home)
        self.home = url
        self.salvar()

    def voltar(self):
        """Volta para página anterior"""
        if self.historico:
            self.home = self.historico.pop()
            self.salvar()
            return self.home
        return None

    def mostrar(self):
        """Mostra histórico completo"""
        print("\n--- HISTÓRICO ---")
        for i, url in enumerate(self.historico, 1):
            print(f"{i}. {url}")
        if self.home:
            print(f"\n🏠 Home: {self.home}")

    def limpar(self):
        """Limpa o histórico"""
        self.historico = []
        self.salvar()
        print("Histórico limpo!")
