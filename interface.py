###########################
####### Interface #########
###########################
class Interface:
    def mostrar(self, historico, home):
        """Exibe a interface principal do navegador"""
        hist_str = "".join([f"[{url}]" for url in historico]) if historico else "[ ]"
        home_str = f"[{home}]" if home else "[ ]"
        
        print(f"Histórico de Visitas: {hist_str}")
        print(f"Home: {home_str}")
        print("Digite a url ou #back para retornar à última página visitada.")

    ###########################
    ####### Exibir Página #####
    ###########################
    def mostrar_pagina(self, url_obj):
        """Exibe o conteúdo da página e links disponíveis"""
        print("\nPágina encontrada!\n")
        
        # Tenta ler o arquivo da página se existir
        if url_obj.arquivo:
            try:
                # Tenta ler como UTF-8 primeiro
                with open(url_obj.arquivo, "r", encoding='utf-8') as f:
                    conteudo = f.read()
                    print(conteudo)
            except UnicodeDecodeError:
                # Se falhar, tenta com encoding padrão do Windows (latin-1 / cp1252)
                try:
                    with open(url_obj.arquivo, "r", encoding='latin-1') as f:
                        conteudo = f.read()
                        print(conteudo)
                except Exception as e:
                    print(f"Erro de codificação ao ler arquivo: {e}")
            except FileNotFoundError:
                print(f"(Arquivo {url_obj.arquivo} não encontrado para esta URL)")
            except Exception as e:
                print(f"Erro ao ler arquivo: {e}")
        
        links = url_obj.get_links()
        if links:
            print("\nLinks disponíveis:\n")
            for link in links:
                print(link)
        print() # Linha em branco para separação

    def mostrar_erro(self, mensagem):
        print(f"\n{mensagem}\n")
