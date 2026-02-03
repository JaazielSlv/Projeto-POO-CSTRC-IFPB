from url import URL
import os

class Web:
    def __init__(self):
        self.raiz = {}

    def carregar_urls(self):
        caminho_urls = "dados/urls.txt"
        if not os.path.exists(caminho_urls):
            os.makedirs("dados", exist_ok=True)
            with open(caminho_urls, "w"):
                pass
            return

        with open(caminho_urls, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]

        urls.sort(key=len)

        for url_str in urls:
            self.adicionar_url_dinamico(url_str)

    def adicionar_url_dinamico(self, url_str):
        if "/" in url_str:
            partes = url_str.split("/")
            nome_arquivo = partes[-1]
            parent_url_str = "/".join(partes[:-1])
            path_relativo = "/" + partes[-1]
        else:
            nome_arquivo = url_str.split(".")[-2]
            parent_url_str = None
            path_relativo = None

        caminho_arquivo = f"dados/paginas/{nome_arquivo}.txt"
        nova_url = URL(url_str, caminho_arquivo)
        self.raiz[url_str] = nova_url

        if parent_url_str:
            if parent_url_str not in self.raiz:
                parent_url = URL(parent_url_str, None)
                self.raiz[parent_url_str] = parent_url
            else:
                parent_url = self.raiz[parent_url_str]

            parent_url.adicionar_link(path_relativo, nova_url)

    def adicionar_nova_url(self, url_str):
        if self.existe(url_str):
            return False

        self.adicionar_url_dinamico(url_str)

        with open("dados/urls.txt", "a") as f:
            f.write(f"\n{url_str}")
        return True

    def existe(self, endereco):
        return endereco in self.raiz

    def get(self, endereco):
        return self.raiz.get(endereco)
