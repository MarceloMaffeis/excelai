"""
Módulo 5: Gerenciamento de Gráficos, Análise de Negócios & Automação VBA com IA.
Conteúdos e Práticas:
- Tipos de gráficos e seus objetivos (Colunas/Barras, Pizza, Dispersão XY)
- Inserir gráficos e formatar layout (Legendas, Títulos, Eixos e Cores)
- Tabelas Dinâmicas, Gráficos Dinâmicos e Subtotais
- Análise de Decisão: Atingir Meta (Goal Seek) e Cenários
- Bônus Especial: Automação com Macros e Códigos VBA gerados por IA
- Prompts de IA para escolha de gráfico, storytelling e automação VBA
- Bateria expandida de exercícios práticos e auditoria
"""

import streamlit as st
import pandas as pd
import altair as alt
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

def render_modulo5_page():
    info = MODULES_INFO["modulo5"]
    render_header(
        title=info["title"],
        subtitle="Gráficos, dashboards, Tabelas Dinâmicas, Atingir Meta, Storytelling e Automação VBA com IA.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1. Tipos de Gráficos & Objetivos",
        "2. Formatação de Layout",
        "3. Tabelas Dinâmicas & Atingir Meta",
        "4. Bônus: Macros e VBA com IA",
        "5. IA para Storytelling & Prompts",
        "6. Bateria de Exercícios"
    ])
    
    with tab1:
        st.markdown("### 5.1 e 5.2 — Tipos de Gráficos e Seus Objetivos de Negócio")
        st.write(
            "Um gráfico não serve apenas para deixar o relatório 'bonito'; sua função é permitir "
            "que um tomador de decisão compreenda a mensagem em menos de **5 segundos**. "
            "A escolha do tipo de gráfico depende diretamente da pergunta que você quer responder:"
        )
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">📊 Colunas e Barras</h4>
                    <p style="font-size: 0.9rem; color: #334155;"><strong>Quando usar:</strong> Comparar grandezas entre categorias distintas.</p>
                    <ul style="font-size: 0.85rem; color: #475569; padding-left: 1rem;">
                        <li><strong>Colunas (Verticais):</strong> Melhor para poucos itens ou evolução temporal de poucos períodos.</li>
                        <li><strong>Barras (Horizontais):</strong> Perfeito para categorias com nomes longos (evita textos inclinados).</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with c2:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🥧 Pizza / Rosca</h4>
                    <p style="font-size: 0.9rem; color: #334155;"><strong>Quando usar:</strong> Representar a proporção de partes em relação a um todo (100%).</p>
                    <ul style="font-size: 0.85rem; color: #475569; padding-left: 1rem;">
                        <li><strong>Regra de Ouro:</strong> Nunca use pizza com mais de 5 a 6 fatias!</li>
                        <li>Se houver muitas fatias finas, os olhos humanos não conseguem comparar áreas com precisão.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with c3:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">📍 Dispersão XY</h4>
                    <p style="font-size: 0.9rem; color: #334155;"><strong>Quando usar:</strong> Investigar se existe correlação matemática entre duas variáveis numéricas.</p>
                    <ul style="font-size: 0.85rem; color: #475569; padding-left: 1rem;">
                        <li>Exemplo: Horas de treinamento vs Produtividade dos operadores.</li>
                        <li>Permite traçar uma 'Linha de Tendência' (regressão linear).</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab2:
        st.markdown("### 5.3 — Formatação de Layout: O Design da Clareza")
        st.write(
            "As boas práticas de visualização recomendam remover elementos visuais poluentes e priorizar o foco na mensagem:"
        )
        
        st.markdown(
            """
            * 🏷️ **Título Acionável:** Em vez de títulos passivos como *"Vendas 2026"*, use títulos que contem a conclusão: *"Região Sudeste lidera faturamento com 42% do total"*.
            * 📌 **Legenda Eficiente:** Se o gráfico tiver apenas uma série de dados (ex: apenas faturamento de um ano), **apague a legenda**! Ela é redundante e rouba espaço nobre da tela.
            * 📏 **Eixos e Rótulos de Dados:**
              - Se você adicionar rótulos de dados diretamente em cima de cada barra (ex: R$ 50k, R$ 80k), pode ocultar os números do eixo vertical para deixar o gráfico mais limpo.
            * 🎨 **Cores Estratégicas:** Use tons neutros (cinza suave) para todas as barras normais e aplique a cor de destaque (azul corporativo ou verde) **apenas na categoria que você quer enfatizar** na apresentação.
            """
        )

    with tab3:
        st.markdown("### 5.4 — Análise Avançada: Tabela Dinâmica, Subtotais e Atingir Meta")
        st.write(
            "Para analisar grandes volumes de dados sem precisar escrever dezenas de fórmulas manuais, o Excel oferece ferramentas analíticas de alto nível:"
        )
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">📊 Tabela Dinâmica (Pivot Table)</h4>
                    <p style="font-size: 0.92rem; color: #334155;">
                        Permite cruzar milhares de linhas em segundos arrastando campos para 4 áreas:
                    </p>
                    <ul style="font-size: 0.88rem; color: #475569; padding-left: 1.1rem;">
                        <li><strong>Linhas:</strong> As categorias principais (ex: Vendedor, Produto).</li>
                        <li><strong>Colunas:</strong> As subdivisões (ex: Região, Meses).</li>
                        <li><strong>Valores:</strong> Onde ocorrem os cálculos automáticos (Soma de Vendas, Contagem, Média).</li>
                        <li><strong>Filtros:</strong> Permite segmentar por Filial ou Ano com 1 clique.</li>
                        <li><strong>Gráfico Dinâmico:</strong> Gráficos conectados diretamente à tabela que se redesenham conforme você filtra!</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_t2:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🎯 Atingir Meta (Goal Seek)</h4>
                    <p style="font-size: 0.92rem; color: #334155;">
                        Cálculo reverso: você diz o resultado final que quer alcançar e o Excel descobre quanto você precisa vender!
                    </p>
                    <p style="font-size: 0.88rem; color: #475569;">
                        <strong>Como acionar:</strong> Menu <code>Dados</code> &rarr; <code>Teste de Hipóteses</code> &rarr; <code>Atingir Meta</code>.<br><br>
                        1. <strong>Definir célula:</strong> A célula com a fórmula do lucro (ex: B10).<br>
                        2. <strong>Para valor:</strong> Digite a meta (ex: R$ 100.000).<br>
                        3. <strong>Alternando célula:</strong> A célula da quantidade de vendas (ex: B2).<br>
                        O Excel roda o cálculo em milissegundos e mostra a resposta exata!
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab4:
        st.markdown("### 5.5 — Bônus Especial: Automação com Macros e VBA impulsionados por IA")
        st.write(
            "O **VBA (Visual Basic for Applications)** é o ambiente de programação embutido dentro do Excel. "
            "Antigamente, era necessário meses de estudo de sintaxe para criar automações. "
            "Hoje, **a Inteligência Artificial Generativa escreve o código VBA para você em 10 segundos**!"
        )
        
        c_vba1, c_vba2 = st.columns(2)
        with c_vba1:
            st.markdown(
                """
                #### ⚙️ O que é uma Macro e Objetos do VBA?
                - **Macro:** Um conjunto de instruções em código gravadas para executar tarefas repetitivas automaticamente com uma tecla de atalho (`Ctrl + Shift + M`).
                - **Objetos Fundamentais do VBA:**
                  - `Range("A1:C10")` : Seleciona ou altera um intervalo de células.
                  - `ActiveCell` : Manipula a célula atualmente selecionada.
                  - `Cells(linha, coluna)` : Navega por coordenadas numéricas (ex: `Cells(2, 3)` é a célula C2).
                  - `ActiveCell.Offset(1, 0)` : Desloca o cursor 1 linha para baixo mantendo a mesma coluna.
                """
            )
        with c_vba2:
            st.markdown(
                """
                #### 🚀 Exemplo de Código VBA Gerado por IA
                Rotina para limpar e formatar uma planilha automaticamente:
                ```vba
                Sub LimparEFormatar()
                    ' Código gerado via Engenharia de Prompt
                    With Range("A1:F1")
                        .Font.Bold = True
                        .Font.ColorIndex = 2 ' Branco
                        .Interior.Color = RGB(0, 90, 156) ' Azul Corporativo
                    End With
                    Columns("A:F").AutoFit ' Auto-ajuste de largura
                    MsgBox "Planilha padronizada com sucesso!", vbInformation, "Automação"
                End Sub
                ```
                """
            )
            
        render_prompt_card(
            title="Como pedir para a IA escrever códigos VBA para o Excel",
            prompt_text=(
                "Atue como desenvolvedor especialista em Excel e VBA.\n"
                "Preciso de uma Macro em VBA para fazer o seguinte:\n"
                "1. Percorrer a coluna D da linha 2 até a linha 50.\n"
                "2. Se o valor da célula for menor que 10, pintar o fundo da célula de vermelho claro (RGB: 254, 226, 226) e a fonte de vermelho escuro.\n"
                "3. No final, exibir uma MsgBox informando quantas células foram destacadas.\n"
                "Comente o código linha por linha para que eu aprenda como funciona."
            ),
            tip_text="A IA entrega o código pronto para você abrir no Excel teclando Alt + F11 (Editor VBA), colar em um Módulo e rodar!"
        )

    with tab5:
        st.markdown("### 6.4 e 6.5 — Prompts de IA para Storytelling e Visualização")
        st.write(
            "Ficou em dúvida sobre qual visual escolher? Descreva suas variáveis para a IA e peça a recomendação de design e storytelling:"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            render_prompt_card(
                title="Escolha do Gráfico Ideal em Função dos Dados",
                prompt_text=(
                    "Atue como especialista em visualização de dados e dashboards no Excel.\n"
                    "Tenho uma tabela com 15 departamentos da empresa e o respectivo orçamento de gastos em reais de cada um.\n\n"
                    "1. Qual é o gráfico mais recomendado pelo padrão de design corporativo para essa comparação?\n"
                    "2. Por que o gráfico de pizza seria uma escolha inadequada para 15 categorias?\n"
                    "3. Quais ajustes de layout (título, eixos, ordenação e cores) devo fazer no Excel para que a diretoria visualize o maior gastador imediatamente?"
                ),
                tip_text="O prompt orienta a IA a explicar a razão técnica do design, reforçando seu aprendizado crítico."
            )
        with col2:
            render_prompt_card(
                title="Extração de Insights Analíticos a partir de Resumo Numérico",
                prompt_text=(
                    "Atue como consultor de negócios.\n"
                    "Analisei os resultados trimestrais de vendas no Excel e obtive os seguintes números totais:\n"
                    "- 1º Trimestre: R$ 120.000 (meta: R$ 100.000)\n"
                    "- 2º Trimestre: R$ 145.000 (meta: R$ 130.000)\n"
                    "- 3º Trimestre: R$ 90.000 (meta: R$ 140.000)\n"
                    "- 4º Trimestre: R$ 180.000 (meta: R$ 150.000)\n\n"
                    "Necessidade:\n"
                    "1. Identifique o principal ponto de atenção (anomalia) e calcule o percentual de queda do 3º trimestre.\n"
                    "2. Redija 3 tópicos executivos com hipóteses de negócio para explicar essa oscilação aos diretores.\n"
                    "3. Sugira uma recomendação prática de controle para o próximo ano."
                ),
                tip_text="Perceba como transformamos números brutos em storytelling executivo de alto impacto!"
            )
            
        render_audit_alert(
            "Auditoria de Raciocínio Matemático da IA: Modelos de linguagem às vezes cometem erros "
            "ao calcular variações percentuais de cabeça. Sempre verifique o cálculo matemático na sua própria "
            "fórmula do Excel `=(Novo - Antigo) / Antigo` antes de publicar a conclusão no relatório corporativo!"
        )

    with tab6:
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Gráficos, Análise & Automação")
        st.write("Resolva os desafios práticos abaixo para dominar a arte de transformar dados brutos em decisões visuais e automatizadas:")
        
        # EXERCÍCIO 1
        with st.expander("📊 Exercício 1: Laboratório Visual Interativo — Destaque de Categoria", expanded=True):
            st.write("Analise o gráfico de barras interativo abaixo. Note como o uso intencional da cor destaca o líder sem poluir a visão:")
            
            dados_vendas = pd.DataFrame({
                "Categoria": ["Eletrodomésticos", "Informática", "Móveis", "Telefonia", "Acessórios"],
                "Vendas_Milhares_R$": [450, 680, 290, 810, 195],
                "Destaque": ["Normal", "Normal", "Normal", "Líder de Vendas", "Normal"]
            })
            
            chart = alt.Chart(dados_vendas).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
                x=alt.X("Categoria:N", sort="-y", title="Categorias de Produtos"),
                y=alt.Y("Vendas_Milhares_R$:Q", title="Vendas (em milhares de R$)"),
                color=alt.Color("Destaque:N", scale=alt.Scale(domain=["Normal", "Líder de Vendas"], range=["#94A3B8", "#005A9C"]), legend=None),
                tooltip=["Categoria", "Vendas_Milhares_R$"]
            ).properties(height=320)
            
            st.altair_chart(chart, use_container_width=True)
            st.caption("Exercício mental: Como você formataria esse gráfico no Excel? (Resposta: pintar a série toda de cinza e clicar duas vezes apenas na coluna de Telefonia para colori-la de azul).")

        # EXERCÍCIO 2
        with st.expander("🎯 Exercício 2: Diagnóstico de Visual — Qual Gráfico Usar?", expanded=False):
            st.markdown(
                """
                **Desafio:** Relacione mentalmente a necessidade de negócio ao tipo de gráfico correto:
                1. Acompanhar a evolução diária do preço do barril de petróleo ao longo dos últimos 180 dias.
                2. Mostrar a divisão do orçamento familiar entre 4 categorias (Moradia, Alimentação, Saúde, Lazer).
                3. Comparar o faturamento de 25 filiais com nomes extensos (ex: 'Filial São José dos Campos Centro').
                4. Descobrir se funcionários mais velhos cometem menos erros de digitação em um software.
                """
            )
            if st.button("Ver Resolução Técnica do Exercício 2", key="btn_ex_m5_2"):
                st.info(
                    "**Gabarito do Especialista:**\n"
                    "1. **Gráfico de Linhas:** Ideal para séries temporais contínuas longas (180 pontos).\n"
                    "2. **Gráfico de Pizza ou Rosca:** Perfeito para poucas fatias (apenas 4) totalizando 100% do orçamento.\n"
                    "3. **Gráfico de Barras Horizontais:** Imprescindível para nomes longos, pois evita rótulos na diagonal ou cortados.\n"
                    "4. **Gráfico de Dispersão XY:** O único capaz de traçar correlação entre duas variáveis contínuas (Idade vs Quantidade de Erros)."
                )

        # EXERCÍCIO 3
        with st.expander("🎯 Exercício 3: O Poder do 'Atingir Meta' (Goal Seek)", expanded=False):
            st.markdown(
                """
                **Cenário de Planejamento:** Você vende cursos a R$ 250,00 cada. Seus custos fixos mensais são R$ 8.000,00.  
                A célula `C10` calcula o lucro líquido com a fórmula `=(Quantidade * 250) - 8000`.  
                Você precisa saber exatamente quantos cursos deve vender para atingir **R$ 30.000,00 de lucro**.
                
                Como configurar a caixa do **Atingir Meta** no Excel?
                """
            )
            st.info(
                "**Configuração do Atingir Meta:**\n"
                "- **Definir célula:** `C10`\n"
                "- **Para valor:** `30000`\n"
                "- **Alternando célula:** Célula da Quantidade de Cursos.\n"
                "O Excel calcula em 1 segundo: você precisa vender exatamente **152 cursos**!"
            )

        # EXERCÍCIO 4
        with st.expander("🤖 Exercício 4: Automação com Macro & IA (Desafio Prático)", expanded=False):
            st.markdown(
                """
                **Desafio:** Crie um prompt para a IA gerar uma Macro em VBA que crie um botão de 'Limpar Dados' na planilha, apagando o conteúdo do intervalo `B2:D20` sem apagar as cores de formatação.
                """
            )
            st.code(
                'Sub LimparDados()\n'
                '    Range("B2:D20").ClearContents \' Limpa apenas os valores, preservando cores e bordas\n'
                '    MsgBox "Campos de entrada limpos com sucesso!", vbInformation, "Limpeza"\n'
                'End Sub',
                language="vba"
            )

        # EXERCÍCIO 5
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m5_quiz1",
            question="**Exercício 5 (Quiz Anti-Alucinação):** Uma IA sugeriu criar um gráfico de pizza para comparar o faturamento diário de uma loja ao longo de todos os 365 dias do ano. Qual é a avaliação técnica correta sobre essa recomendação?",
            options=[
                "A recomendação é excelente, pois a pizza divide perfeitamente os 365 dias em 100%.",
                "A recomendação é um erro grave de visualização; um gráfico de linhas contínuo ou colunas mensais é a escolha técnica correta.",
                "Deveríamos usar um gráfico de dispersão com 365 fatias de pizza.",
                "O Excel não permite criar gráficos de pizza com mais de 10 dias."
            ],
            correct_index=1,
            explanation="Uma pizza com 365 fatias geraria uma mancha ilegível e incompreensível. Acompanhamento de tempo contínuo exige gráficos de LINHAS ou agregação em colunas mensais."
        )

        # EXERCÍCIO 6
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m5_quiz2",
            question="**Exercício 6 (Quiz de Tabela Dinâmica):** Em uma Tabela Dinâmica do Excel, onde você deve arrastar o campo 'Faturamento em R$' para que o Excel calcule automaticamente a soma monetária de todas as vendas?",
            options=[
                "Para a área de Filtros",
                "Para a área de Valores (Somatório de Valores)",
                "Para a área de Colunas",
                "Para a lixeira do Excel"
            ],
            correct_index=1,
            explanation="A área de 'Valores' é o coração do cálculo na Tabela Dinâmica; qualquer coluna numérica arrastada para lá recebe automaticamente operações de Soma, Média ou Contagem."
        )

        # EXERCÍCIO 7
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 7: Laboratório de Prompts & Storytelling")
        render_prompt_sandbox(
            module_name="Módulo 5: Gráficos e Storytelling",
            placeholder="Exemplo: Crie um código VBA para destacar linhas com vendas negativas..."
        )

    render_footer()
