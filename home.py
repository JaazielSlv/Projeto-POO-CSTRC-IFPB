import os

historico = []
home = ""

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_interface():
    limpar_tela()

    print("Histórico de Visitas: [", end="")
    print("][".join(historico), end="")
    print("]\n")

    print(f"Home: [{home}]\n")

    print("Digite a url ou #back para retornar à última página visitada.\n")
    print("url: ", end="")

def url_basica_valida(url):
    if len(url) < 2:
        return False
    if url.startswith("www."):
        return True
    if url.startswith("/"):
        return True
    return False

def adicionar_historico(url):
    global home
    if home != "":
        historico.append(home)

def main():
    global home

    while True:
        mostrar_interface()
        entrada = input().strip()

        if entrada == "#sair":
            limpar_tela()
            print("Programa encerrado.")
            break

        if not url_basica_valida(entrada):
            print("\nErro: URL inválida.")
            input("Pressione ENTER para continuar...")
            continue

        adicionar_historico(entrada)
        home = entrada

if __name__ == "__main__":
    main()
