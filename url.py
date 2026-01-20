###########################
####### Class URL #########
###########################
class URL:
    def __init__(self, endereco, arquivo):
        self.endereco = endereco
        self.arquivo = arquivo
        self.links = {}

    def adicionar_link(self, nome, url_obj):
        self.links[nome] = url_obj

    def get_links(self):
        return self.links

    def __str__(self):
        return self.endereco

    def __repr__(self):
        return self.endereco
