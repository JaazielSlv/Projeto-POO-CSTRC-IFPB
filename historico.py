###########################
####### Class Historico ###
###########################
class Historico:
    def __init__(self):
        self.pilha = []            # guarda as URLs visitadas

    def adicionar(self, url):
        self.pilha.append(url)      # Adiciona uma URL ao histórico

    def voltar(self):
        if self.pilha:
            return self.pilha.pop()  # Remove e retorna a última URL (voltar)
        return None      # Se estiver vazio, não há para onde voltar

    def mostrar(self):
        return self.pilha.copy()  # Retorna uma cópia do histórico
