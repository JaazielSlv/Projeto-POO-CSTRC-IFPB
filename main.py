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

    while True:
        limpar_tela()
        ###########################
        ####### Exibição da Interface
        ###########################
        # Prepara dados para exibição
        hist_lista = historico.mostrar() # Retorna lista de URLs
        home_str = url_atual.endereco if url_atual else None
        
        interface.mostrar(hist_lista, home_str)
        
        try:
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
                url_atual = url_anterior
                if url_atual:
                    interface.mostrar_pagina(url_atual)
            else:
                interface.mostrar_erro("Histórico vazio ou início alcançado.")
                time.sleep(1)

        elif entrada.startswith("#add "):
            parts = entrada.split(maxsplit=1)
            if len(parts) == 2:
                nova_url = parts[1]
                if web.adicionar_nova_url(nova_url):
                    print(f"URL {nova_url} adicionada com sucesso.")
                else:
                    print(f"URL {nova_url} já existe ou inválida.")
            else:
                print("Uso: #add <url>")
            time.sleep(1)

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
                        interface.mostrar_erro("Página não encontrada (404)")
                else:
                    interface.mostrar_erro("Nenhuma página aberta para navegar relativamente.")
            
            # Navegação absoluta
            else:
                if web.existe(entrada):
                    nova_url_obj = web.get(entrada)
                else:
                    interface.mostrar_erro("Página não encontrada (404)")

            # Se encontrou uma nova página
            if nova_url_obj:
                # Se já tinha uma página, salva no histórico
                if url_atual:
                    historico.adicionar(url_atual)
                
                url_atual = nova_url_obj
                interface.mostrar_pagina(url_atual)

        # Pequena pausa ou limpeza se necessário, mas o loop limpa ou redesenha?
        # A implementação original não limpava tela sempre, mas o input fica rolando.
        # Vamos manter o histórico de comandos visível e mostrar o cabeçalho novamente a cada loop.
        print("-" * 50)

if __name__ == "__main__":
    main()
