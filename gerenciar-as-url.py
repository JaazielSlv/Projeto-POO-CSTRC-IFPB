# url_manager.py

class URLManager:
    ####################
    # Inicializa o gerenciador de URLs
    ####################
    def __init__(self, arquivo='urls.txt'):
        self.arquivo = arquivo
        self.urls_validas = []
        self.carregar_urls()

    ####################
    # Carrega URLs válidas do arquivo.
    ####################
    def carregar_urls(self):
        try:
            with open(self.arquivo, 'r') as f:
                self.urls_validas = [linha.strip() for linha in f if linha.strip()]
        except FileNotFoundError:
            self.urls_validas = []
            try:
                open(self.arquivo, 'w').close()
            except Exception as e:
                print(f"Erro ao criar o arquivo: {e}")

    ####################
    # Verifica se a URL está cadastrada.
    ####################
    def verificar_url(self, url):
        return url in self.urls_validas

    ####################
    # Adiciona nova URL (Comando #add).
    ####################
    def adicionar_url(self, nova_url):
        if not nova_url:
            print('❌ Erro: A URL a ser adicionada não pode ser vazia.')
            return

        if nova_url in self.urls_validas:
            print(f'⚠️ A URL "{nova_url}" já está cadastrada.')
            return
        
        self.urls_validas.append(nova_url)
        try:
            with open(self.arquivo, 'a') as f:
                f.write(f'{nova_url}\n')
            print(f'✅ URL adicionada com sucesso: {nova_url}')
        except Exception as e:
            print(f'❌ Erro ao salvar no arquivo {self.arquivo}: {e}')
