import os
import sys
from historico import HistoricoNavegacao
from gerenciarurl import URLManager

####################
# Inicializa as classes
####################
historico_browser = HistoricoNavegacao()
gerenciador_urls = URLManager()


####################
# Limpa o console.
####################
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

####################
# Desenha a interface.
####################
def mostrar_interface():
    limpar_tela()

    # Histórico de Visitas (Interface do Checkpoint 1)
    print("Histórico de Visitas: [", end="")
    print("][".join(historico_browser.historico), end="")
    print("]\n")

    # Home (Página Atual)
    print(f"Home: [{historico_browser.home}]\n")

    print("Digite a url ou um comando especial (ex: #back, #sair, #showhist, #add <url>).\n")
    print("url: ", end="")

####################
# Processa comandos do usuário.
####################
def processar_comando(entrada):
    
    # #sair
    if entrada == "#sair":
        historico_browser.salvar()
        limpar_tela()
        print("Programa encerrado. Estado de navegação salvo.")
        sys.exit(0)

    # #back
    elif entrada == "#back":
        anterior = historico_browser.voltar()
        if anterior:
            print(f"\n✅ Retornando para: {anterior}")
        else:
            print("\n⚠️ Histórico vazio. Não é possível retornar mais.")
        return

    # #showhist
    elif entrada == "#showhist":
        historico_browser.mostrar()
        return

    # #add <url>
    elif entrada.startswith("#add "):
        url_add = entrada[5:].strip() 
        gerenciador_urls.adicionar_url(url_add)
        return
    
    # Acesso à URL
    if gerenciador_urls.verificar_url(entrada):
        # URL válida: adiciona ao histórico e atualiza a home
        historico_browser.adicionar(entrada) 
        print("\n✅ Página encontrada!")
    else:
        # URL não cadastrada
        print(f"\n❌ Página não encontrada (Erro 404): {entrada}")


####################
# Loop principal do programa.
####################
def main():
    
    print("Iniciando Histórico de Navegação...")
    
    while True:
        try:
            mostrar_interface()
            entrada = input().strip()

            if not entrada:
                continue

            processar_comando(entrada)
            
            if entrada not in ["#sair"]:
                 input("\nPressione ENTER para continuar...")

        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
