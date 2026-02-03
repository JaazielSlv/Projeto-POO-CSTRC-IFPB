from url import URL
import os

class Web:
    def __init__(self):
        self.raiz = {}  # Dicionário para armazenar URLs (chave: URL string, valor: objeto URL)

    def carregar_urls(self):
        """Carrega URLs do arquivo urls.txt e as adiciona à estrutura"""
        caminho_urls = "dados/urls.txt"
        
        # Cria arquivo e diretório se não existirem
        if not os.path.exists(caminho_urls):
            os.makedirs("dados", exist_ok=True)
            with open(caminho_urls, "w"):
                pass  # Arquivo vazio
            return

        # Lê e processa URLs do arquivo
        with open(caminho_urls, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]  # Remove linhas vazias

        urls.sort(key=len)  # Ordena por tamanho para garantir que URLs pai sejam processadas primeiro

        # Adiciona cada URL à estrutura
        for url_str in urls:
            self.adicionar_url_dinamico(url_str)

    def adicionar_url_dinamico(self, url_str):
        """Adiciona uma URL à estrutura, criando relações pai-filho quando aplicável"""
        
        # Verifica se a URL tem estrutura de diretório (contém "/")
        if "/" in url_str:
            partes = url_str.split("/")
            nome_arquivo = partes[-1]  # Última parte como nome do arquivo
            parent_url_str = "/".join(partes[:-1])  # URL pai (tudo exceto última parte)
            path_relativo = "/" + partes[-1]  # Caminho relativo para o link
        else:
            # URL sem diretórios (arquivo na raiz)
            nome_arquivo = url_str.split(".")[-2]  # Assume extensão .txt, pega nome sem extensão
            parent_url_str = None
            path_relativo = None

        # Define caminho do arquivo correspondente
        caminho_arquivo = f"dados/paginas/{nome_arquivo}.txt"
        
        # Cria objeto URL
        nova_url = URL(url_str, caminho_arquivo)
        self.raiz[url_str] = nova_url  # Armazena no dicionário

        # Se houver URL pai, estabelece relação
        if parent_url_str:
            # Cria URL pai se não existir
            if parent_url_str not in self.raiz:
                parent_url = URL(parent_url_str, None)  # Pai pode não ter arquivo próprio
                self.raiz[parent_url_str] = parent_url
            else:
                parent_url = self.raiz[parent_url_str]

            # Adiciona link do pai para o filho
            parent_url.adicionar_link(path_relativo, nova_url)

    def adicionar_nova_url(self, url_str):
        """Adiciona nova URL ao sistema e ao arquivo de persistência"""
        # Verifica duplicata
        if self.existe(url_str):
            return False

        # Adiciona à estrutura em memória
        self.adicionar_url_dinamico(url_str)

        # Persiste no arquivo
        with open("dados/urls.txt", "a") as f:
            f.write(f"\n{url_str}")
        return True

    def existe(self, endereco):
        """Verifica se URL já existe no sistema"""
        return endereco in self.raiz

    def get(self, endereco):
        """Retorna objeto URL correspondente ao endereço"""
        return self.raiz.get(endereco)
