import os
import sys

class Browser:
    def __init__(self):
        self.web = {}
        self.home = None
        self.historico = []

    def carregar_web(self):
        self.web = {
            "www.ifpb.edu.br": {
                "tsi": {
                    "professores": {},
                    "alunos": {}
                },
                "rc": {}
            }
        }

    def help(self):
        print("""
#back
#showhist
#help
#sair
""")

    def acessar(self, entrada):
        if entrada.startswith("/"):
            if not self.home:
                print("Nenhuma página base.")
                return
            url = self.home + entrada
        else:
            url = entrada

        partes = url.split("/")
        dominio = partes[0]
        caminhos = partes[1:]

        if dominio not in self.web:
            print("Página não encontrada.")
            return

        atual = self.web[dominio]
        for p in caminhos:
            if p in atual:
                atual = atual[p]
            else:
                print("Página não encontrada.")
                return

        if self.home:
            self.historico.append(self.home)
        self.home = url

        print(f"Página encontrada: {self.home}")
        self.exibir_pagina(url)

    def exibir_pagina(self, url):
        nome = url.replace("/", "_") + ".txt"
        caminho = f"paginas/{nome}"

        if os.path.exists(caminho):
            with open(caminho, "r") as f:
                print(f.read())
        else:
            print("(Página sem conteúdo)")

