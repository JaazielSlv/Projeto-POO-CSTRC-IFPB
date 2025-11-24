import json

class HistoricoNavegacao:
    ####################
    # Estrutura de Dados: Pilha (Stack) para o histórico
    ####################
    def __init__(self, arquivo="historico_estado.json"):
        self.historico = [] 
        self.home = ""      
        self.arquivo = arquivo
        self.carregar()

    ####################
    # Carrega estado de navegação ao iniciar.
    ####################
    def carregar(self):
        try:
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                self.historico = dados.get('historico', [])
                self.home = dados.get('home', "")
        except FileNotFoundError:
            pass 
        except Exception as e:
            self.historico = []
            self.home = ""

    ####################
    # Salva estado de navegação ao sair.
    ####################
    def salvar(self):
        dados = {
            'historico': self.historico,
            'home': self.home
        }
        try:
            with open(self.arquivo, 'w') as f:
                json.dump(dados, f, indent=4)
        except Exception as e:
            print(f"❌ Erro ao salvar o histórico: {e}")

    ####################
    # Adiciona nova URL e move Home para o histórico (Push).
    ####################
    def adicionar(self, url):
        if self.home:
            self.historico.append(self.home) 
        self.home = url
        self.salvar()

    ####################
    # Retorna para a página anterior (#back) (Pop).
    ####################
    def voltar(self):
        if self.historico:
            nova_home = self.historico.pop() 
            self.home = nova_home
            self.salvar()
            return self.home
        
        return None

    ####################
    # Lista o histórico completo (#showhist).
    ####################
    def mostrar(self):
        print("\n--- SITUAÇÃO ATUAL DA NAVEGAÇÃO ---")
        if self.home:
            print(f"🏠 Home (Página Atual): {self.home}")
        else:
            print("🏠 Home (Página Atual): [Vazio]")

        print("\n📜 Histórico de Visitas (Ordem do Mais Antigo ao Mais Recente):")
        if not self.historico:
            print("   [O histórico está vazio]")
        else:
            for i, url in enumerate(self.historico, 1):
                print(f"   {i}. {url}")
        print("------------------------------------\n")
