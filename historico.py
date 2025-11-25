import json

class HistoricoNavegacao:
    ####################
    # Estrutura de Dados: Pilha (Stack) para o histórico
    ####################
    def __init__(self, arquivo="historico_estado.json"):
        self.historico = []      # 1. PILHA: Armazena URLs na ordem LIFO (Last-In-First-Out)
        self.home = ""           # 2. Guarda a URL atual (topo da pilha virtual)
        self.arquivo = arquivo   # 3. Arquivo para persistência dos dados
        self.carregar()          # 4. Recupera estado anterior ao iniciar

    ####################
    # Carrega estado de navegação ao iniciar.
    ####################
    def carregar(self):
        try:
            # 5. Tenta abrir o arquivo de histórico existente
            with open(self.arquivo, 'r') as f:
                # 6. Converte JSON para dicionário Python
                dados = json.load(f)
                # 7. Recupera a pilha de histórico (ou lista vazia)
                self.historico = dados.get('historico', [])
                # 8. Recupera a URL atual (home)
                self.home = dados.get('home', "")
        except FileNotFoundError:
            pass  # 9. Se arquivo não existe, ignora (primeira execução)
        except Exception as e:
            # 10. Se outro erro, reinicia com valores vazios
            self.historico = []
            self.home = ""

    ####################
    # Salva estado de navegação ao sair.
    ####################
    def salvar(self):
        # 11. Prepara dados para serialização
        dados = {
            'historico': self.historico,  # 12. Salva toda a pilha
            'home': self.home             # 13. Salva a URL atual
        }
        try:
            # 14. Abre arquivo para escrita
            with open(self.arquivo, 'w') as f:
                # 15. Converte para JSON com formatação bonita
                json.dump(dados, f, indent=4)
        except Exception as e:
            # 16. Trata erro de gravação
            print(f"❌ Erro ao salvar o histórico: {e}")

    ####################
    # Adiciona nova URL e move Home para o histórico (Push).
    ####################
    def adicionar(self, url):
        # 17. Se já existe uma página atual, empurra para o histórico
        if self.home:
            self.historico.append(self.home)  # 18. PUSH: Adiciona ao final da lista
        # 19. A nova URL se torna a página atual
        self.home = url
        # 20. Persiste imediatamente a mudança
        self.salvar()

    ####################
    # Retorna para a página anterior (#back) (Pop).
    ####################
    def voltar(self):
        # 21. Verifica se há páginas no histórico para voltar
        if self.historico:
            # 22. POP: Remove e pega a última URL do histórico
            nova_home = self.historico.pop()
            # 23. Torna essa URL a nova página atual
            self.home = nova_home
            # 24. Salva o novo estado
            self.salvar()
            return self.home  # 25. Retorna a URL para navegação
        
        return None  # 26. Se histórico vazio, retorna None

    ####################
    # Lista o histórico completo (#showhist).
    ####################
    def mostrar(self):
        print("\n--- SITUAÇÃO ATUAL DA NAVEGAÇÃO ---")
        # 27. Mostra a página atual (home)
        if self.home:
            print(f"🏠 Home (Página Atual): {self.home}")
        else:
            print("🏠 Home (Página Atual): [Vazio]")

        # 28. Mostra todo o histórico em ordem cronológica
        print("\n📜 Histórico de Visitas (Ordem do Mais Antigo ao Mais Recente):")
        if not self.historico:
            print("   [O histórico está vazio]")
        else:
            # 29. Enumera cada URL do histórico (mais antiga primeiro)
            for i, url in enumerate(self.historico, 1):
                print(f"   {i}. {url}")
        print("------------------------------------\n")
