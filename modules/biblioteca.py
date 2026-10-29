"""
Módulo: Biblioteca Mundial de Recursos & Fundamentos da Informática (Acesso Livre).
Área pública sem necessidade de senha contendo curadoria internacional de documentações,
links oficiais da Microsoft, guias de prompt engineering, fundamentos de hardware e software,
ética/LGPD, datasets e curiosidades.
"""

import streamlit as st
from utils.ui_components import render_header, render_footer

def render_biblioteca_page():
    render_header(
        title="Biblioteca Mundial de Recursos & Fundamentos",
        subtitle="Acesso 100% Livre e Gratuito • Curadoria de Referências Internacionais, Hardware e Ferramentas",
        icon="📚"
    )
    
    st.markdown(
        """
        <div class="hero-card" style="background: linear-gradient(135deg, #0F766E 0%, #0D9488 100%);">
            <h2>Conhecimento Aberto para Todo o Mundo</h2>
            <p>
                Esta biblioteca é o espaço do portal com <strong>acesso totalmente livre e sem senha</strong>.
                Aqui reunimos documentações oficiais, fundamentos clássicos da computação e hardware, guias técnicos de ponta,
                referências de ética, planilhas abertas para download e conteúdos históricos que inspiraram a revolução digital.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "💻 Fundamentos da Informática",
        "🏢 Microsoft & Excel Oficial",
        "🧠 IA & Engenharia de Prompt",
        "⚖️ Ética, LGPD & Segurança",
        "📂 Planilhas & Datasets Abertos",
        "🏛️ Pioneiros da Computação"
    ])
    
    with tab1:
        st.markdown("### 💻 Fundamentos da Informática: A Base de Tudo")
        st.write(
            "Antes de dominar planilhas e modelos de IA, todo bom profissional compreende como a informação é processada:"
        )
        
        c_f1, c_f2 = st.columns(2)
        with c_f1:
            st.markdown(
                """
                #### 🖥️ A Tríade da Informática
                - **Hardware:** A parte física palpável (placas, processador, teclado, mouse, monitor).
                - **Software:** A parte lógica (sistemas operacionais como Windows/Linux e aplicativos como Excel/Word).
                - **Peopleware:** As pessoas que utilizam, programam e operam os sistemas.
                
                #### 📦 Classificação dos Softwares
                - **Sistemas Operacionais:** Gerenciam hardware e arquivos (Windows, Linux, macOS).
                - **Aplicativos:** Programas orientados a tarefas do usuário (Excel, Word, navegadores).
                - **Firmware:** Software gravado permanentemente em circuitos eletrônicos (como a BIOS/UEFI da placa-mãe).
                - **Freeware:** Softwares 100% gratuitos para uso livre.
                - **Shareware:** Softwares distribuídos para demonstração com algumas funções limitadas.
                - **Abandonware:** Softwares descontinuados que não possuem mais suporte comercial.
                """
            )
        with c_f2:
            st.markdown(
                """
                #### 🧠 Arquitetura: Processamento e Memórias
                - **Entrada (Input):** Envia dados para a CPU (teclado, mouse, scanner).
                - **CPU (Processador):** Possui a Unidade Lógica e Aritmética (ULA) e executa os cálculos.
                - **Memória RAM:** Acesso aleatório ultrarrápido; volátil (apaga tudo ao desligar o computador).
                - **Memória ROM:** Memória não volátil que permite apenas a leitura dos programas de inicialização.
                - **Memória Cache:** Memória de alta velocidade integrada na CPU para acelerar a troca de dados.
                - **Armazenamento:** Salva os arquivos permanentemente (HD, SSD, Pen Drive/Flash Disk).
                """
            )
            
        st.markdown("---")
        st.markdown("#### 📏 Escala de Medidas: Capacidade e Velocidade")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown(
                """
                | Unidade de Capacidade | Equivalência Real |
                | :--- | :--- |
                | **1 Bit** | Menor unidade (0 ou 1) |
                | **1 Byte** | 8 Bits (representa 1 caractere: 'A', '1') |
                | **1 Kilobyte (KB)** | 1.024 Bytes |
                | **1 Megabyte (MB)** | 1.024 Kilobytes |
                | **1 Gigabyte (GB)** | 1.024 Megabytes |
                | **1 Terabyte (TB)** | 1.024 Gigabytes |
                | **1 Petabyte (PB)** | 1.024 Terabytes |
                """
            )
        with col_m2:
            st.markdown(
                """
                | Unidade de Velocidade (Frequência) | Ciclos por Segundo |
                | :--- | :--- |
                | **1 Hertz (Hz)** | 1 ciclo ou oscilação por segundo |
                | **1 Kilohertz (KHz)** | 1.000 ciclos por segundo |
                | **1 Megahertz (MHz)** | 1.000.000 de ciclos por segundo |
                | **1 Gigahertz (GHz)** | 1.000.000.000 de ciclos por segundo |
                
                *Curiosidade: O processador de um computador moderno opera a 3.0 até 5.0 GHz, ou seja, realiza até 5 bilhões de operações a cada segundo!*
                """
            )

    with tab2:
        st.markdown("### 🏢 Recursos Oficiais Microsoft")
        st.write("Acesse os portais oficiais de capacitação e documentação técnica da Microsoft:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                - 🌐 [Microsoft Learn: Roteiro de Aprendizagem de Excel](https://learn.microsoft.com/pt-br/training/paths/ai-concepts/)
                  *Treinamentos gratuitos e certificados oficiais da Microsoft sobre conceitos de IA e ferramentas do Office.*
                - 📖 [Lista Completa de Funções do Excel (Suporte Microsoft)](https://support.microsoft.com/pt-br/office/fun%C3%A7%C3%B5es-do-excel-por-categoria-5f91f4e9-7b42-46d2-9bd1-63f26a86c0eb)
                  *Referência canônica de todas as fórmulas (`SOMA`, `MÉDIA`, `CONT.SE`, `SE`, `PROCV`, `XLOOKUP`).*
                - ⌨️ [Atalhos de Teclado no Excel para Windows](https://support.microsoft.com/pt-br/office/atalhos-de-teclado-no-excel-1798d9d5-842a-42b8-9c99-9b7213f0040f)
                  *Aumente sua agilidade com combinações essenciais como `Ctrl + T` (Tabela), `Alt + =` (Autosoma), etc.*
                """
            )
        with col2:
            st.markdown(
                """
                - 🤖 [Guia de Primeiros Passos com Microsoft Copilot no Excel](https://support.microsoft.com/pt-br/excel/copilot/get-started-with-copilot-in-excel)
                  *Aprenda como a Microsoft recomenda pedir ajuda à IA para analisar tendências e gerar novas colunas.*
                - 📱 [Integração de Tabelas do Excel com Power Apps](https://learn.microsoft.com/pt-br/power-apps/maker/canvas-apps/connections/connection-excel)
                  *Como formatar sua tabela de dados no Excel para utilizá-la como banco de dados em aplicativos corporativos.*
                """
            )
            
    with tab3:
        st.markdown("### 🧠 Engenharia de Prompts e Inteligência Artificial")
        st.write("Aprenda as técnicas mais avançadas para instruir modelos de linguagem (LLMs):")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                - 📘 [Guia Oficial de Engenharia de Prompt da OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)
                  *Estratégias fundamentais: seja específico, use delimitadores, peça passo a passo e dê exemplos (few-shot).*
                - 🔮 [Documentação do Google AI Studio & Gemini API](https://ai.google.dev/docs)
                  *Entenda a arquitetura de tokens, janelas de contexto e como criar instruções de sistema eficazes.*
                """
            )
        with col2:
            st.markdown(
                """
                - 🎓 [LearnPrompting.org - Curso Mundial de Prompting](https://learnprompting.org/)
                  *A maior plataforma aberta e gratuita do mundo para aprender desde o básico até técnicas avançadas de IA.*
                - 🧪 [Anthropic Interactive Prompt Engineering Tutorial](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
                  *Exemplos visuais de como evitar alucinações e direcionar saídas estruturadas.*
                """
            )

    with tab4:
        st.markdown("### ⚖️ Ética, Privacidade e Lei Geral de Proteção de Dados (LGPD)")
        st.write("Diretrizes vitais para o uso responsável da tecnologia em ambientes corporativos:")
        
        st.markdown(
            """
            - 🛡️ [Portal Oficial da ANPD (Autoridade Nacional de Proteção de Dados - Brasil)](https://www.gov.br/anpd/pt-br)
              *Conheça os direitos do titular, o conceito de dados pessoais sensíveis e as diretrizes brasileiras de privacidade.*
            - 🌐 [Recomendações da UNESCO sobre a Ética da Inteligência Artificial](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)
              *Primeiro instrumento normativo global adotado por 193 países sobre transparência, equidade e supervisão humana.*
            - 🏛️ [Framework de Gestão de Riscos de IA do NIST (EUA)](https://www.nist.gov/itl/ai-risk-management-framework)
              *Padrão internacional para mitigar riscos de viés, alucinações e vazamentos em sistemas inteligentes.*
            """
        )
        st.info(
            "💡 **Regra de Ouro de Segurança:** Ao trabalhar com IA no Excel, trate todo dado de clientes e salários como estritamente confidencial. "
            "Se for pedir auxílio à IA, utilize sempre nomes e valores fictícios ou passe apenas o cabeçalho das colunas!"
        )

    with tab5:
        st.markdown("### 📂 Planilhas de Exemplo e Dados Abertos para Treino")
        st.write("Bases de dados para você importar no Excel e praticar fórmulas, tabelas e gráficos:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                - 🇧🇷 [Portal Brasileiro de Dados Abertos (dados.gov.br)](https://dados.gov.br/)
                  *Milhares de conjuntos de dados públicos sobre educação, transporte, saúde e economia prontos para download em CSV.*
                - 📊 [Kaggle Datasets (Comunidade Global de Dados)](https://www.kaggle.com/datasets)
                  *Tabelas abertas sobre vendas de e-commerce, estoques de varejo e estatísticas esportivas para treinar dashboards.*
                """
            )
        with col2:
            st.markdown(
                """
                - 📥 **Baixar Planilha Modelo de Vendas (Exemplo Prático):**
                """
            )
            # Tabela de exemplo pronta para download
            import pandas as pd
            import io
            
            sample_data = {
                "ID_Venda": [101, 102, 103, 104, 105, 106, 107, 108],
                "Data": ["2026-01-15", "2026-01-16", "2026-01-17", "2026-01-18", "2026-01-19", "2026-01-20", "2026-01-21", "2026-01-22"],
                "Vendedor": ["Ana Lima", "Carlos Souza", "Beatriz Costa", "Daniel Alves", "Ana Lima", "Carlos Souza", "Fernanda Rocha", "Beatriz Costa"],
                "Região": ["Sudeste", "Sul", "Nordeste", "Sudeste", "Centro-Oeste", "Sudeste", "Norte", "Sul"],
                "Produto": ["Teclado Mecânico", "Mouse Sem Fio", "Monitor 24pol", "Headset USB", "Mousepad Gamer", "Monitor 24pol", "Câmera Full HD", "Teclado Mecânico"],
                "Quantidade": [12, 25, 6, 18, 40, 4, 15, 8],
                "Preco_Unitario": [180.00, 75.00, 850.00, 220.00, 45.00, 850.00, 310.00, 180.00]
            }
            df_sample = pd.DataFrame(sample_data)
            df_sample["Valor_Total"] = df_sample["Quantidade"] * df_sample["Preco_Unitario"]
            
            csv_buffer = io.StringIO()
            df_sample.to_csv(csv_buffer, index=False, sep=";")
            
            st.download_button(
                label="📥 Baixar Planilha Modelo de Vendas (CSV/Excel)",
                data=csv_buffer.getvalue().encode("utf-8-sig"),
                file_name="exemplo_vendas_2026.csv",
                mime="text/csv",
                key="btn_dl_sample_sales",
                use_container_width=True
            )
            st.caption("Arquivo separado por ponto e vírgula (`;`), pronto para abrir diretamente no Excel.")

    with tab6:
        st.markdown("### 🏛️ Os Pioneiros da Computação (Nossas Senhas do Conhecimento)")
        st.write("Conheça as histórias fascinantes das mentes que tornaram possíveis os computadores e a Inteligência Artificial:")
        
        pioneiros = [
            ("Ada Lovelace (1815–1852)", "A Primeira Programadora", "Escreveu notas detalhadas sobre a Máquina Analítica e concebeu o primeiro algoritmo executável por uma máquina, vislumbrando que computadores poderiam processar não apenas números, mas símbolos, músicas e ideias."),
            ("Charles Babbage (1791–1871)", "O Pai do Computador Mecânico", "Projetou a Máquina Diferencial e a Máquina Analítica, contendo conceitos equivalentes à memória, unidade lógica de processamento e entrada de dados por cartões perfurados."),
            ("Alan Turing (1912–1954)", "O Pai da Ciência da Computação e da IA", "Criou o conceito teórico de máquina universal que fundamenta todos os computadores modernos. Liderou a decifração da máquina Enigma durante a Segunda Guerra Mundial e formulou o Teste de Turing para inteligência artificial."),
            ("George Boole (1815–1864)", "O Criador da Lógica Booleana", "Criou a álgebra baseada em apenas dois valores: Verdadeiro (1) e Falso (0). Sem suas operações lógicas (E, OU, NÃO), nenhum processador, código ou função condicional (`SE`) existiria."),
            ("Grace Hopper (1906–1992)", "A Rainha do Software & Compiladores", "Cientista pioneira e contra-almirante da Marinha dos EUA. Acreditava que computadores deveriam entender palavras humanas, criando o primeiro compilador da história e liderando a linguagem COBOL. Popularizou o termo 'bug' ao achar uma mariposa presa num circuito.")
        ]
        
        for nome, titulo, bio in pioneiros:
            with st.expander(f"✨ {nome} — *{titulo}*"):
                st.write(bio)
                
    st.markdown("---")
    
    # Seção especial sobre a Licença MIT
    with st.expander("⚖️ Sobre a Licença MIT deste Portal (Garantia de Acesso Livre e Irrevogável)", expanded=False):
        st.markdown(
            """
            ### Por que a Licença MIT foi escolhida?
            A **Licença MIT** é um dos modelos de código aberto mais respeitados e amplamente aceitos no planeta.
            Ela assegura de maneira legal e inequívoca que:
            
            1. **O portal é livre para sempre:** Ninguém pode revogar seu direito de acessar, estudar, copiar ou utilizar este material para seu aprendizado.
            2. **Liberdade de Adaptação:** Professores, alunos e escolas podem duplicar este repositório no GitHub, criar novas versões e adaptar conteúdos para suas realidades locais.
            3. **Sem Custo:** O material é distribuído gratuitamente, incentivando a democratização do conhecimento em Tecnologia da Informação.
            
            Consulte o arquivo `LICENSE` no repositório do projeto para ver a íntegra dos termos legais.
            """
        )

    render_footer()
