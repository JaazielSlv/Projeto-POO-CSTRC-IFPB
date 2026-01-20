###########################
####### Class Historico ###
###########################
class Historico:
    def __init__(self):
        self.pilha = []

    def adicionar(self, url):
        self.pilha.append(url)

    def voltar(self):
        if self.pilha:
            return self.pilha.pop()
        return None

    def mostrar(self):
        return self.pilha.copy()
