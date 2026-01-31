from web import Web
from historico import Historico
from interface import Interface
from utils import limpar_tela
import time

###########################
####### Função Principal ##
###########################
def main():
    web = Web()
    web.carregar_urls()

    historico = Historico()
    interface = Interface()

    url_atual = None
    mensagem_aviso = None

    while True:
        limpar_tela()
        ###########################
        ####### Exibição da Interface
        ###########################
        # Prepara dados para exibição
        hist_lista = historico.mostrar() # Retorna lista de URLs
        home_str = url_atual.endereco if url_atual else None
        
        interface.mostrar(hist_lista, home_str)
        
        # Se houver página atual, exibe o conteúdo dela (persistência na tela)
        if url_atual:
            interface.mostrar_pagina(url_atual)

        # Se houver mensagem de aviso temporária
        if mensagem_aviso:
            print(f"\n>> MENSAGEM: {mensagem_aviso}")
            mensagem_aviso = None
        
        try:
            print("-" * 50)
            entrada = input("url: ").strip()
        except EOFError:
            break

        if not entrada:
            # Se vazio, apenas continua o loop (refresh)
            continue

        ###########################
        ####### Comandos ##########
        ###########################
        if entrada == "#sair":
            break

        elif entrada == "#help":
            print("""
---------------------------------------------------------
COMMANDOS
#back             - Retornar à última página visitada
#showhist         - Listar histórico completo
#add <url>        - Adicionar nova URL ao sistema
#sair             - Encerrar o programa
---------------------------------------------------------
""")
            input("Pressione ENTER para continuar...")

        elif entrada == "#showhist":
            interface.mostrar(hist_lista, home_str)
            # O enunciado diz "lista na tela a situação atual". A interface já mostra na parte superior.
            # Mas vamos forçar uma exibição explicita se desejado ou apenas pausar.
            print("\n(Histórico já exibido no topo)\n")
            input("Pressione ENTER para continuar...")

        elif entrada == "#back":
            url_anterior = historico.voltar()
            if url_anterior:
                # Se voltou, a página atual vira a anterior
                url_atual = url_anterior
                # (Conteúdo será exibido no próximo loop)
            else:
                # Se não tem para onde voltar, mas o histórico tá vazio, 
                # talvez devêssemos limpar a url atual se já estivéssemos no inicio?
                # Pela lógica do enunciado "esta referência sairia do informativo".
                # Se voltamos e não tem mais nada, talvez url_atual fique None?
                # O enunciado diz: "Se considerarmos que o usuário digitou um #back , então a localização da página atual passa a ser a última url visitada."
                # Se não há ultima visitada, estamos no estado inicial.
                
                # Se url_atual existe, mas o histórico está vazio, significa que estamos na primeira página?
                # Não, o enunciado diz "O registro no histórico só acontecerá a partir do momento que você tiver visitado a primeira url. Então, a cada nova url visitada, a url atual deve ser armazenada"
                # Se estamos na 1a página, histórico é []. Se dermos back, voltamos pra onde? Estado inicial (None)?
                
                if url_atual:
                    # Estamos em uma página mas não tem histórico atrás.
                    # Simular "sair" da navegação ou apenas avisar?
                    # "E neste caso, essa referência sairia do informativo Páginas Visitadas." 
                    # Assumindo que voltamos ao estado 'em branco' se o histórico acabar.
                    url_atual = None
                    mensagem_aviso = "Retornou ao início."
                else:
                    mensagem_aviso = "Histórico já está vazio."

        elif entrada.startswith("#add "):
            parts = entrada.split(maxsplit=1)
            if len(parts) == 2:
                nova_url = parts[1]
                if web.adicionar_nova_url(nova_url):
                    mensagem_aviso = f"URL {nova_url} adicionada com sucesso."
                else:
                    mensagem_aviso = f"URL {nova_url} já existe ou inválida."
            else:
                mensagem_aviso = "Uso: #add <url>"

        ###########################
        ####### Navegação #########
        ###########################
        else:
            nova_url_obj = None
            
            # Navegação relativa
            if entrada.startswith("/"):
                if url_atual:
                    links = url_atual.get_links()
                    if entrada in links:
                        nova_url_obj = links[entrada]
                    else:
                        mensagem_aviso = "Página não encontrada (404)"
                else:
                    mensagem_aviso = "Nenhuma página aberta para navegar relativamente."
            
            # Navegação absoluta
            else:
                if web.existe(entrada):
                    nova_url_obj = web.get(entrada)
                else:
                    mensagem_aviso = "Página não encontrada (404)"

            # Se encontrou uma nova página
            if nova_url_obj:
                # Se já tinha uma página, salva no histórico
                if url_atual:
                    historico.adicionar(url_atual)
                
                url_atual = nova_url_obj
                # Interface será atualizada no próximo loop

if __name__ == "__main__":
    main()
