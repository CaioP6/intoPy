# IntoPy 🐍

Repositório dedicado aos meus estudos, testes e pequenos projetos desenvolvidos na linguagem **Python**. O repositório contém desde exercícios básicos para fixação da sintaxe até automações de sistema e interfaces gráficas.

---

## 📁 Estrutura do Projeto

O repositório é organizado nas seguintes pastas principais:

### 1. `GuanaQuests/`
Contém uma série de exercícios focados no aprendizado da lógica de programação e das bases do Python (do `ex001.py` ao `ex037.py`). 
Eles abrangem conceitos fundamentais da linguagem, como:
- Operações matemáticas fundamentais.
- Estruturas condicionais e de repetição.
- Criação e uso de funções.
- Manipulação de strings e entrada de dados do usuário.

### 2. `Works/`
Scripts utilitários criados para auxiliar em tarefas e automações do sistema operacional (Windows):
- `Criar_atalho.py`: Script para automação da criação de atalhos de rede (`.lnk`) na Área de Trabalho usando Python integrado ao PowerShell.
- `Delete_atalho.py`: Script complementar para deleção de atalhos criados.

### 3. `otherQuest/`
Uma área de experimentação com scripts mais complexos, testes de lógica e uso de bibliotecas de terceiros para desenvolvimento de interfaces gráficas.
Destaques desta pasta:
- **Kivy (`kivyCalc.py`, `kivyTest.py`, etc)**: Criação de aplicações com interface gráfica usando o framework Kivy (inclui a implementação de uma calculadora funcional com layouts).
- **Utilitários e Manipulação de Arquivos**: Arquivos como `cronometro.py` (contagem de tempo) e `criarTxt.py` (criação e manipulação de arquivos de texto locais).
- **Testes variados**: Arquivos de lógica (`quest1.py`, `quest2.py`, etc) e subpastas de pequenos projetos ou módulos (`login/`, `shop/`, `tvTest/`).

---

## 🛠️ Tecnologias e Bibliotecas

- **Linguagem Principal:** Python 3
- **Frameworks e Bibliotecas Externas:**
  - `Kivy` (Usado para desenvolvimento de interfaces de usuário gráficas / GUI)
- **Módulos Nativos de Destaque:**
  - `os`, `subprocess` (Manipulação de arquivos e chamadas de sistema no Windows)

## 🚀 Como Executar

1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/CaioP6/intoPy.git
   ```
2. Navegue até a pasta do repositório:
   ```bash
   cd intoPy
   ```
3. Se for executar os testes visuais da pasta `otherQuest` (Kivy), é recomendado usar um ambiente virtual:
   ```bash
   python -m venv venv
   # Ative o venv (No Windows)
   venv\Scripts\activate
   # Instale as dependências
   pip install kivy
   ```
4. Navegue até a pasta do arquivo que deseja testar e o execute:
   ```bash
   # Exemplo executando a calculadora
   cd otherQuest
   python kivyCalc.py
   ```
