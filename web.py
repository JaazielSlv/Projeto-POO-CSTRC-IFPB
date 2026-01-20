from url import URL
import os

###########################
####### Web ###############
###########################
class Web:
    def __init__(self):
        self.raiz = {} # Armazena todas as URLs cadastradas: chave=endereco_str, valor=objeto_URL

    ###########################
    ####### Carregar URLs ####
    ###########################
    def carregar_urls(self):
        """Carrega as URLs do arquivo db/urls.txt e monta a estrutura"""
        caminho_urls = "dados/urls.txt"
        if not os.path.exists(caminho_urls):
            # Tenta criar arquivo vazio se não existir
            os.makedirs("dados", exist_ok=True)
            with open(caminho_urls, "w") as f:
                pass
            return

        with open(caminho_urls, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]

        # Ordena por tamanho para garantir que pais sejam criados antes dos filhos (se a lista não estiver ordenada)
        urls.sort(key=len)

        for url_str in urls:
            self.adicionar_url_dinamico(url_str)

    ###########################
    ####### Add Dinâmico ######
    ###########################
    def adicionar_url_dinamico(self, url_str):
        # Determina o nome do arquivo baseado na última parte da URL
        if "/" in url_str:
            partes = url_str.split("/")
            nome_arquivo = partes[-1]
            parent_url_str = "/".join(partes[:-1])
            path_relativo = "/" + partes[-1]
        else:
            nome_arquivo = url_str.split(".")[-2] # ex: ifpb de www.ifpb.edu.br (simplificação)
            if "ifpb" in url_str: nome_arquivo = "ifpb" # Ajuste específico para o exemplo
            parent_url_str = None
            path_relativo = None
            
        caminho_arquivo = f"dados/paginas/{nome_arquivo}.txt"
        
        # Cria ou recupera o objeto URL
        nova_url = URL(url_str, caminho_arquivo)
        self.raiz[url_str] = nova_url

        # Se tem pai, conecta
        if parent_url_str and parent_url_str in self.raiz:
            parent_url = self.raiz[parent_url_str]
            parent_url.adicionar_link(path_relativo, nova_url)

    ###########################
    ####### Add Nova URL ######
    ###########################
    def adicionar_nova_url(self, url_str):
        """Adiciona uma nova URL em tempo de execução e salva no arquivo"""
        if self.existe(url_str):
            return False
            
        self.adicionar_url_dinamico(url_str)
        
        # Salva no arquivo
        with open("dados/urls.txt", "a") as f:
            f.write(f"\n{url_str}")
        return True

    def existe(self, endereco):
        return endereco in self.raiz

    def get(self, endereco):
        return self.raiz.get(endereco)
