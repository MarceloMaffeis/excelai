"""
Módulo 2: Gerenciamento de Objetos do Excel & Estruturação com IA.
Conteúdos e Práticas:
- Células, Endereçamento, Linhas, Colunas, Formatação, Filtros e Opções de Colagem
- Planilhas e Pasta de Trabalho
- Formatação como Tabela oficial e integração com Power Apps
- Prompts de IA para geração de estruturas de planilhas formatadas
- Comparativo: Tempo de prompt vs Tempo de execução manual
- Bateria expandida de exercícios práticos e auditoria
"""

import streamlit as st
import pandas as pd
import io
from utils.auth import MODULES_INFO
from utils.ui_components import (
    render_header,
    render_pioneer_badge,
    render_prompt_card,
    render_audit_alert,
    render_anti_hallucination_quiz,
    render_prompt_sandbox,
    render_footer
)

def render_modulo2_page():
    info = MODULES_INFO["modulo2"]
    render_header(
        title=info["title"],
        subtitle="Células, linhas, colunas, tabelas estruturadas, integração de dados e IA para geração de estruturas.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Células & Formatação",
        "2. Pastas & Planilhas",
        "3. Tabelas Oficiais & Power Apps",
        "4. Prompts de Geração de Estruturas",
        "5. Bateria de Exercícios & Prática"
    ])
    
    with tab1:
        st.markdown("### 2.1 — O Coração do Excel: Células e Endereçamento")
        st.write(
            "Toda a mecânica do Microsoft Excel baseia-se em uma grade bidimensional inteligente. "
            "Compreender a anatomia dos objetos é essencial para não cometer erros em fórmulas:"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                - 📌 **Endereçamento:** A interseção entre uma **Coluna** (letra) e uma **Linha** (número). Exemplo: `C5` é a coluna C na linha 5.
                - ➕ **Inserir e Remover:** 
                  - Inserir linha: selecione a linha e tecle `Ctrl + Shift + +`
                  - Excluir linha: selecione a linha e tecle `Ctrl + -`
                - 🎨 **Formatos de Número:**
                  - **Geral:** Padrão inicial sem separadores fixos.
                  - **Moeda / Contábil:** Insere o símbolo monetário (ex: `R$ 1.250,00`) e alinha os decimais.
                  - **Data:** Converte o número de série em formato civil (ex: `29/10/2026`).
                """
            )
        with c2:
            st.markdown(
                """
                - 📋 **Opções Especiais de Colagem (`Colar Especial`):**
                  - **Colar Valores:** Elimina fórmulas e preserva apenas o resultado numérico final (crucial para auditar planilhas).
                  - **Colar Fórmulas:** Mantém a matemática mas não altera a cor ou formatação de destino.
                  - **Transpor:** Converte dados dispostos em linhas para colunas e vice-versa.
                - 🔍 **Filtros e Ordenação:**
                  - Classificar de `A a Z` ou do `Maior para o Menor`.
                  - Filtrar dados para exibir somente registros que atendem a um critério.
                """
            )

    with tab2:
        st.markdown("### 2.2 e 2.3 — Planilhas e Pasta de Trabalho")
        st.write(
            "É comum confundir os termos 'Pasta de Trabalho' e 'Planilha'. No padrão corporativo:"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.info(
                "📁 **Pasta de Trabalho (.xlsx):** É o arquivo completo que você salva no seu computador ou no OneDrive/SharePoint. "
                "Pode conter dezenas de planilhas interligadas entre si."
            )
        with col2:
            st.success(
                "📄 **Planilha (Aba/Sheet):** É a folha de cálculo individual (ex: 'Vendas_Jan', 'Estoque_Geral', 'Resumo_Anual') "
                "localizada na barra inferior do Excel."
            )
            
        st.markdown(
            """
            #### Modos de Exibição no Excel
            1. **Modo Normal:** O modo clássico de trabalho no dia a dia.
            2. **Layout da Página:** Exibe a planilha exatamente como ela será impressa ou convertida em PDF, mostrando margens, cabeçalhos e rodapés.
            3. **Visualização de Quebra de Página:** Permite arrastar as linhas azuis de corte para definir exatamente quais colunas caberão em uma única folha.
            """
        )

    with tab3:
        st.markdown("### 2.4 — O Poder das Tabelas Oficiais do Excel (`Ctrl + T`)")
        st.write(
            "Muitos usuários apenas pintam as células com cores e acham que criaram uma tabela. "
            "No entanto, converter um intervalo em uma **Tabela Oficial do Excel** traz superpoderes:"
        )
        
        st.markdown(
            """
            * ⚡ **Colunas Calculadas Automáticas:** Quando você escreve uma fórmula na primeira linha, o Excel preenche todas as linhas da coluna instantaneamente.
            * 🔄 **Expansão Dinâmica:** Ao digitar um novo dado logo abaixo da última linha, a tabela cresce automaticamente e inclui a nova linha nas fórmulas e gráficos!
            * 🔗 **Integração com Microsoft Power Apps e Power BI:** O Power Apps exige que a fonte de dados seja uma Tabela Nomeada para que um aplicativo de celular possa ler e gravar dados nela.
            * 🤖 **Obrigatório para o Microsoft Copilot:** O Copilot do Excel só consegue realizar análises e automações em dados que foram formalmente convertidos em Tabela.
            """
        )
        
        render_audit_alert(
            "Boas Práticas de Tabela: Dê nomes significativos às suas tabelas no menu 'Design da Tabela' "
            "(ex: 'Tbl_Vendas_2026' em vez do genérico 'Tabela1'). Isso torna suas fórmulas infinitamente mais legíveis "
            "e facilita o entendimento da IA ao ler seus dados."
        )

    with tab4:
        st.markdown("### 6.1 — Engenharia de Prompts para Criação de Estruturas de Planilhas")
        st.write(
            "Uma das maneiras mais eficientes de usar IA é solicitar a **estrutura completa da planilha** "
            "com dados fictícios e colunas já planejadas, pronta para ser colada no Excel."
        )
        
        render_prompt_card(
            title="Geração de Estrutura de Planilha com Formatação e Dados Fictícios",
            prompt_text=(
                "Atue como analista de dados especialista em Microsoft Excel.\n"
                "Preciso criar uma planilha para controle de manutenção preventiva de máquinas industriais.\n\n"
                "Requisitos da estrutura:\n"
                "1. Gere uma tabela em formato Markdown com 8 linhas de exemplos fictícios.\n"
                "2. Colunas necessárias: ID_Maquina, Nome_Equipamento, Setor_Fabril, Data_Ultima_Manutencao, Periodicidade_Dias, Proxima_Data, Status_Operacional.\n"
                "3. Insira valores realistas do setor industrial brasileiro.\n"
                "4. Indique qual formatação de célula aplicar em cada coluna (ex: Data abreviada, Texto, Número)."
            ),
            tip_text="Solicitar a saída em formato de tabela Markdown permite que você selecione o texto, copie e dê 'Colar' diretamente no Excel sem desconfigurar colunas!"
        )
        
        st.markdown("#### ⏱️ Comparativo de Tempo: Manual vs. IA")
        st.write(
            "Criar uma tabela dessas manualmente do zero (pensando nas colunas, inventando 8 exemplos industriais coerentes) "
            "leva cerca de **12 a 15 minutos**. Com um prompt estruturado, a IA entrega a tabela em **15 segundos**, "
            "restando a você mais 2 minutos apenas para auditar e formatar no Excel. Ganho de **80% de produtividade**!"
        )

    with tab5:
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Gerenciamento de Objetos")
        st.write("Resolva os desafios abaixo para consolidar seu domínio prático sobre células, formatações e tabelas:")
        
        # EXERCÍCIO 1
        with st.expander("📊 Exercício 1: Desafio de Estruturação com IA (Controle de Estoque)", expanded=True):
            st.markdown(
                """
                **Missão:** Você foi contratado para organizar o estoque de uma loja de suprimentos de informática.  
                Crie um prompt na caixa abaixo pedindo à IA uma estrutura de planilha completa com 6 colunas essenciais:
                - Código do Produto
                - Descrição
                - Categoria
                - Quantidade em Estoque
                - Preço Unitário
                - Fornecedor Principal
                """
            )
            ex1_prompt = st.text_area(
                "Escreva seu comando de prompt para gerar a tabela:",
                key="ex_m2_p1",
                placeholder="Atue como analista de logística. Crie uma tabela Markdown contendo..."
            )
            if st.button("Ver Prompt Sugerido e Resolução do Exercício 1", key="btn_ex_m2_1"):
                st.info(
                    "**Prompt Recomendado:**\n"
                    "> *'Atue como especialista em Excel e logística. Gere uma tabela em formato Markdown com 8 produtos fictícios de informática contendo as colunas: "
                    "Código (ex: PRD-001), Descrição, Categoria, Qtd_Estoque (inteiro), Preco_Unitario (R$) e Fornecedor. "
                    "Gere dados coerentes para colar direto no Excel.'*\n\n"
                    "**Dica de Aplicação:** No Excel, cole o texto copiado, selecione o intervalo e aperte `Ctrl + T` para converter em tabela oficial!"
                )

        # EXERCÍCIO 2
        with st.expander("📋 Exercício 2: Situação-Problema — Auditoria de Colagem e Segurança", expanded=False):
            st.markdown(
                """
                **Cenário de Negócio:** Você recebeu uma planilha de fechamento mensal cheia de fórmulas que dependem de arquivos externos localizados na rede da empresa.  
                Você precisa enviar um extrato com apenas o faturamento consolidado por filial para a auditoria externa, **mas sem expor as fórmulas originais e sem correr o risco de erro `#REF!`** quando o auditor abrir o arquivo sem acesso à sua rede.
                
                **Qual procedimento você deve executar no Excel?**
                """
            )
            colar_choice = st.radio(
                "Selecione o procedimento técnico correto:",
                [
                    "Copiar as células e dar Ctrl + V direto no novo arquivo.",
                    "Copiar as células, ir na planilha de destino, clicar em Colar Especial e selecionar 'Valores'.",
                    "Copiar e dar Colar Especial -> Transpor.",
                    "Tirar uma captura de tela da tabela e colar no Word."
                ],
                key="ex_m2_colar_radio"
            )
            if st.button("Conferir Solução do Exercício 2", key="btn_ex_m2_2"):
                if "Colar Especial e selecionar 'Valores'" in colar_choice:
                    st.success("🎉 **Resposta Perfeita!** O recurso 'Colar Valores' desfaz o vínculo de fórmulas dinâmicas e fixa o número exato, garantindo integridade e portabilidade do relatório.")
                else:
                    st.error("⚠️ **Incorreto!** Usar Ctrl + V comum tentará buscar os vínculos na rede externa, gerando o temido erro `#REF!` no computador do cliente.")

        # EXERCÍCIO 3
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m2_quiz1",
            question="**Exercício 3 (Quiz de Objetos):** Você precisa transformar uma lista comum de clientes em uma Tabela Oficial do Excel com filtros nativos e expansão dinâmica automática. Qual é o atalho de teclado mais rápido no padrão brasileiro do Excel?",
            options=[
                "Ctrl + C",
                "Ctrl + T (ou Ctrl + Alt + T dependendo da versão)",
                "Alt + F4",
                "Shift + Barra de Espaço"
            ],
            correct_index=1,
            explanation="O atalho `Ctrl + T` (ou `Ctrl + Alt + T`) seleciona todo o bloco contíguo de dados e abre instantaneamente a caixa 'Criar Tabela', ativando filtros e cabeçalhos oficiais."
        )

        # EXERCÍCIO 4
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m2_quiz2",
            question="**Exercício 4 (Quiz de Integração & IA):** Por que o Microsoft Copilot e o Microsoft Power Apps exigem que os dados de uma planilha estejam formatados formalmente como 'Tabela'?",
            options=[
                "Porque o Excel não aceita cores em células que não são tabelas.",
                "Porque a formatação como Tabela cria um esquema estruturado com nomes de colunas e tipos de dados indexados, permitindo que a IA e aplicativos externos leiam e gravem registros de forma confiável.",
                "Porque tabelas comuns gastam 10 vezes mais memória RAM.",
                "É apenas uma exigência estética sem efeito técnico."
            ],
            correct_index=1,
            explanation="Tabelas nomeadas criam objetos com cabeçalhos reconhecíveis por APIs e LLMs (como o Copilot e o conector do Power Apps), evitando erros de referência solta."
        )

        # EXERCÍCIO 5
        st.markdown("---")
        st.markdown("#### 📂 Exercício 5: Prática com Arquivo para Download")
        st.write("Baixe a planilha de dados brutos abaixo, abra no Excel e execute as seguintes instruções:")
        st.markdown(
            """
            1. Converta o intervalo em **Tabela Oficial** (`Ctrl + T`).
            2. Renomeie a tabela para `Tbl_Manutencao_Equipamentos`.
            3. Classifique a coluna `Horas_Uso` do **Maior para o Menor**.
            4. Filtre para exibir apenas o setor de **Usinagem**.
            """
        )
        
        exemplo_df = pd.DataFrame({
            "Código": ["EQ-01", "EQ-02", "EQ-03", "EQ-04", "EQ-05", "EQ-06", "EQ-07"],
            "Máquina": ["Torno CNC", "Fresadora Universal", "Injetora Hidráulica", "Prensa 50T", "Robô Solda", "Centro de Usinagem", "Retífica Plana"],
            "Setor": ["Usinagem", "Usinagem", "Plásticos", "Estamparia", "Montagem", "Usinagem", "Usinagem"],
            "Horas_Uso": [1420, 890, 2300, 3100, 750, 4200, 1150],
            "Status": ["Operacional", "Manutenção", "Operacional", "Alerta", "Operacional", "Operacional", "Manutenção"]
        })
        
        st.dataframe(exemplo_df, use_container_width=True)
        
        csv_buffer = io.StringIO()
        exemplo_df.to_csv(csv_buffer, index=False, sep=";")
        
        st.download_button(
            label="📥 Baixar Planilha para Exercício 5 (CSV)",
            data=csv_buffer.getvalue().encode("utf-8-sig"),
            file_name="tabela_maquinas_exemplo.csv",
            mime="text/csv",
            key="btn_dl_sample_machines_m2"
        )

        # EXERCÍCIO 6
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 6: Laboratório Interativo de Prompts")
        render_prompt_sandbox(
            module_name="Módulo 2: Gerenciamento de Objetos",
            placeholder="Exemplo: Crie a estrutura de colunas para uma planilha de controle de compras corporativas..."
        )

    render_footer()
