def carregar_urls(self,arquivo):
    '''
    Lê o arquivo de URLs válidas e armazena na lista 'urls_validas'
    Se o arquivo não existir, irá criar um novo arquivo vazio.
    '''
    try:
        with open(arquivo, 'r') as f:
            self.urls_validas = [linha.strip() for linha in f if linha.strip()]
        print('URLs carregadas com sucesso!')
    except FileNotFoundError:
        print('Arquivo de URLs não encontrado! Criando um novo....')
        self.urls_validas = []
        open(arquivo, 'w').close()

def verificar_url(self, url):
    '''
    Verifica se a URL digitada é válida (existe na lista 'urls_validas')
    Irá retornar True/False se for válida ou não.
    '''
    return url in self.urls_validas

def adicionar_url(self, nova_url):
    '''
    Adiciona uma nova URL ao arquivo e à lista, caso ainda não exista.
    Comando usado: #add <url>
    '''
    if nova_url in self.urls_validas:
        print('Essa URL já está cadastrada.')
        return
    
    self.urls_validas.append(nova_url)
    try:
        with open('urls.txt', 'a') as f:
            f.write(f'{nova_url}\n')
        print(f'URL adicionada com sucesso: {nova_url}')
    except Exception as e:
        print('Erro ao salvar no arquivo:', e)

def acessar_url(self, url):
    '''
    Acessa uma URL VÁLIDA!!!!!!
    - Atualiza o histórico com a home anterior.
    - Define a nova home como a URL acessada.
    - Caso a URL não exista, mostra mensagem de erro.
    '''
    if not self.verficar_url(url):
        print('Página não econtrada!')
        return
    
    if self.home:
        self.historico.append(self.home)

    self.home = url
    print(f'Página não encontrada: {self.home}')
