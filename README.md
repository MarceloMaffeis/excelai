# 📊 Portal Educacional: Excel Básico com IA Generativa

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B.svg)](https://streamlit.io/)

Portal interativo e aplicação web completa desenvolvida para apoiar o curso de **Aperfeiçoamento Profissional em Excel Básico com IA Generativa**.

O sistema foi concebido para empoderar alunos (a partir de 14 anos) no domínio de planilhas eletrônicas impulsionadas por Inteligência Artificial, priorizando a **execução técnica manual primeiro, aceleração por IA depois, responsabilidade ética com a LGPD e auditoria crítica constante contra alucinações**.

---

## ⚖️ Licença MIT (Software Aberto e Gratuito)

Este projeto é disponibilizado sob a **Licença MIT**. Isso assegura proteção legal irrevogável de que o software é:
* **100% Gratuito:** Livre de mensalidades ou travas proprietárias.
* **Aberto para Estudo e Modificação:** Qualquer pessoa, escola ou empresa pode clonar, adaptar e utilizar o código sem restrições.
* **Garantia contra Revogação:** Nenhum terceiro pode revogar ou expropriar o acesso a esta ferramenta pedagógica.

---

## 🚀 Funcionalidades Principais

1. **Biblioteca Mundial de Recursos (Acesso Livre):**
   * Espaço público sem necessidade de senha, com curadoria de links oficiais da Microsoft, tutoriais de prompt engineering internacionais, diretrizes da ANPD/LGPD, dados abertos e história da computação.
2. **Controle Pedagógico por Senhas Temáticas:**
   * Os 5 módulos técnicos são protegidos por senhas com nomes de pioneiros da tecnologia para permitir ao professor ditar o ritmo pedagógico em sala.
3. **Conector de IA Multi-Provedor com Modo Offline Resiliente:**
   * Suporte nativo ao **Google AI Studio (Gemini)**, **Palantir Foundry / Azure OpenAI / OpenAI**, **Ollama Local** e um **Simulador Didático Inteligente** que funciona mesmo sem conexão de internet ou chaves de API.
4. **Laboratório de Prompts & Desafios Anti-Alucinação:**
   * Quizzes interativos em cada módulo para treinar a capacidade socioemocional de *Atenção aos Detalhes*.

---

## 🔑 Mapeamento de Módulos e Senhas (Guia do Docente)

| Módulo | Conteúdo Curricular | Senha | Pioneiro Homenageado |
| :--- | :--- | :---: | :--- |
| **Biblioteca** | Links oficiais, documentação e datasets abertos | *Livre* | Acesso Aberto ao Conhecimento |
| **Módulo 1** | Fundamentos de IA, Ética, LGPD, Copilot e Prompts | `lovelace` | Ada Lovelace (Primeira programadora) |
| **Módulo 2** | Células, formatação, tabelas e integração com Power Apps | `babbage` | Charles Babbage (Pai do computador mecânico) |
| **Módulo 3** | Operações, percentuais, referências ($) e funções essenciais | `turing` | Alan Turing (Pai da computação e da IA) |
| **Módulo 4** | Regras de realce, escalas de cor e gerenciamento condicional | `boole` | George Boole (Criador da álgebra booleana) |
| **Módulo 5** | Gráficos (colunas, pizza, dispersão), layout e storytelling | `hopper` | Grace Hopper (Criadora do 1º compilador) |

*(Nota: O sistema aceita as senhas sem distinção de letras maiúsculas ou minúsculas).*

---

## 💻 Como Executar Localmente

### 1. Pré-requisitos
* Python 3.10 ou superior instalado.
* Git instalado.

### 2. Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/excel-ia-portal.git
cd excel-ia-portal

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Execução
```bash
streamlit run app.py
```
O portal abrirá automaticamente no seu navegador padrão em `http://localhost:8501`.

---

## 🌐 Como Fazer Deploy Gratuito no Streamlit Cloud (`share.streamlit.io`)

1. **Crie um Repositório no GitHub:**
   * Crie um repositório público ou privado no GitHub (ex: `excel-ia-portal`).
   * Suba todos os arquivos deste projeto para a branch `main`.

2. **Conecte ao Streamlit Community Cloud:**
   * Acesse [share.streamlit.io](https://share.streamlit.io/) e faça login com sua conta do GitHub.
   * Clique em **"New app"**.
   * Selecione o seu repositório, a branch `main` e defina o arquivo principal como `app.py`.

3. **Configuração de Chaves (Opcional):**
   * Nas configurações do aplicativo no Streamlit Cloud, acesse a aba **"Secrets"**.
   * Cole as suas credenciais conforme o exemplo em `.streamlit/secrets.toml.example`:
     ```toml
     GEMINI_API_KEY = "sua_chave_do_google_ai_studio"
     ```
   * Clique em **Save**. O aplicativo reiniciará e estará online para todos os seus alunos!

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Framework Web:** Streamlit
* **Manipulação de Dados:** Pandas
* **Gráficos Interativos:** Altair
* **Exportação:** OpenPyXL
* **Comunicação com IA:** Requests (REST APIs para Gemini, OpenAI/Foundry e Ollama)

---

## 📜 Declaração de Direitos

Desenvolvido para fins de qualificação e aperfeiçoamento profissional em Tecnologia da Informação.  
Licença MIT © 2026 Portal Educacional Excel Básico com IA Generativa.
