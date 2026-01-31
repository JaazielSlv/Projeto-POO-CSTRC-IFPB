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
