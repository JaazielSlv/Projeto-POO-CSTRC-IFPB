# Simulador de Browser via Terminal

Este projeto é uma simulação de um navegador web simplificado, rodando via terminal, focado na implementação de estruturas de dados (Pilhas, Árvores) e conceitos de Orientação a Objetos.

## 👥 Equipe de Desenvolvimento

*   **Jaaziel Silva**
*   **Cosme Cristiano**
*   **Cauã Pablo**

---



## 📂 Estrutura do Projeto

*   **`main.py`**: Arquivo principal. Controla o fluxo do programa, inputs do usuário e ciclo de vida da interface.
*   **`web.py`**: Simula a "Internet" e o Servidor DNS. Gerencia o banco de dados de URLs válidas e carrega a estrutura hierárquica.
*   **`historico.py`**: Implementa a estrutura de dados **Pilha (Stack)** para gerenciar o histórico de navegação e a função "Voltar" (`#back`).
*   **`url.py`**: Classe Objeto que representa uma página web, contendo seu endereço, caminho do arquivo de conteúdo e links para sub-páginas.
*   **`interface.py`**: Responsável pelo Frontend. Formata strings e exibe o conteúdo dos arquivos `.txt` (HTML simulado) na tela.
*   **`dados/`**: Pasta que contém o "banco de dados" (`urls.txt`) e os arquivos de conteúdo das páginas (`.txt`).

## 🛠 Comandos Disponíveis

Ao rodar o programa, você pode usar:

*   **Digitar uma URL**: Ex: `www.ifpb.edu.br`.
*   **Digitar um caminho relativo**: Ex: `/trc` (se estiver dentro de ifpb).
*   **`#back`**: Retorna para a página anterior (remove do topo da pilha).
*   **`#showhist`**: Exibe o histórico atual.
*   **`#add <url>`**: Adiciona uma nova URL ao sistema permanentemente.
*   **`#help`**: Lista todos os comandos.
*   **`#sair`**: Encerra o navegador.

## 🧠 Decisões Técnicas

*   **Histórico como Pilha (LIFO)**: A estrutura de pilha é a representação natural da navegação "Voltar". O último site visitado deve ser o primeiro a ser recuperado.
*   **Web como Grafo/Árvore**: As URLs são organizadas de forma hierárquica (Domain Driven), onde uma URL pai contém referências para URLs filhas.
*   **Persistência em Arquivo**: O sistema lê e escreve em arquivos de texto plano para simular um banco de dados simples e editável.

---
**Instituição:** Instituto Federal da Paraíba (IFPB)
**Curso:** Redes de Computadores
**Disciplina:** Programação Orientada a Objetos
**Semestre:** 2025.2


## 📚 Armazenamento e Histórico de Navegação  

Funciona como um navegador web simulado no terminal, e para isso ele precisa de dois mecanismos fundamentais: um sistema de armazenamento das páginas e um controle de histórico de navegação.  

##🔹 1. Armazenamento das Páginas e URLs  
O sistema de armazenamento do projeto é dividido em duas partes: arquivos físicos e objetos em memória.  
      1.1 Armazenamento em Arquivos (pasta dados)  
    A pasta dados/ funciona como o banco de dados do projeto.Nela estão guardados arquivos .txt que contêm:  
          - A lista de todas as URLs válidas.  
          - O conteúdo das páginas.  
          - Os links que conectam uma página a outras.   
      Esses arquivos são lidos pelo programa sempre que ele inicia, Esse armazenamento é persistente, pois mesmo que você feche o programa, os dados continuam gravados.   

  1.2 Armazenamento em Memória (objetos Python)  
Depois que o programa lê os arquivos da pasta dados/, ele transforma essas informações em objetos, que facilitam o acesso durante a execução.A peça central disso é a classe Url, que representa uma página da internet.  

Cada objeto Url guarda:  
    - o endereço da página (ex: www.ifpb.edu.br),  
    - o texto da página,  
    - os links para outras páginas.  
Esses objetos são carregados e organizados pela classe Web (arquivo web.py).
    - Ela funciona como o “servidor DNS” interno do programa
    - armazena todas as páginas lidas dos arquivos,
    - gerencia as conexões entre elas,
    - procura a página correta quando o usuário digita uma URL.
Dessa forma, o projeto usa uma estrutura semelhante a um grafo, onde:
    - cada página é um nó,
    - cada link entre páginas é uma aresta.
Isso permite simular navegação de forma realista.
