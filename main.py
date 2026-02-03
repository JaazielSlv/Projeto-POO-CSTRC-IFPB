from web import Web
from historico import Historico
from interface import Interface
from utils import limpar_tela

def main():
    web = Web()
    web.carregar_urls()

    historico = Historico()
    interface = Interface()

    url_atual = None
    mensagem_aviso = None
    pular_limpeza = False

    while True:
        if not pular_limpeza:
            limpar_tela()
        pular_limpeza = False

        hist_lista = historico.mostrar()
        home_str = url_atual.endereco if url_atual else None

        interface.mostrar(hist_lista, home_str)

        if url_atual:
            interface.mostrar_pagina(url_atual)

        if mensagem_aviso:
            print(f"\n>> MENSAGEM: {mensagem_aviso}")
            mensagem_aviso = None

        print("-" * 50)
        entrada = input("url: ").strip()

        if not entrada:
            continue

        if entrada == "#sair":
            break

        elif entrada == "#help":
            print("""
---------------------------------------------------------
COMANDOS
#back             - Retornar à última página visitada
#showhist         - Listar histórico completo
#add <url>        - Adicionar nova URL ao sistema
#sair             - Encerrar o programa
---------------------------------------------------------
""")
            input("Pressione ENTER para continuar...")

        elif entrada == "#showhist":
            pular_limpeza = True
            limpar_tela()
            print("Histórico de Navegação:\n")
            for url in historico.mostrar():
                print(f"- {url}")
            input("\nPressione ENTER para continuar...")

        elif entrada == "#back":
            url_anterior = historico.voltar()
            if url_anterior:
                url_atual = url_anterior
            else:
                if url_atual:
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

        else:
            nova_url_obj = None

            if entrada.startswith("/"):
                if url_atual:
                    links = url_atual.get_links()
                    if entrada in links:
                        nova_url_obj = links[entrada]
                    else:
                        mensagem_aviso = "Página não encontrada (404)"
                else:
                    mensagem_aviso = "Nenhuma página aberta para navegação relativa."
            else:
                if web.existe(entrada):
                    nova_url_obj = web.get(entrada)
                else:
                    mensagem_aviso = "Página não encontrada (404)"

            if nova_url_obj:
                if url_atual:
                    historico.adicionar(url_atual)
                else:
                    historico.adicionar(nova_url_obj)

                url_atual = nova_url_obj

if __name__ == "__main__":
    main()
