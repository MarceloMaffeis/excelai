"""
Módulo 5: Gerenciamento de Gráficos & Storytelling com IA.
Cobre 100% da Ementa SENAI:
- Tipos de gráficos e seus objetivos (Colunas/Barras, Pizza, Dispersão XY)
- Inserir gráficos e formatar layout (Legendas, Títulos, Eixos e Cores)
- Prompts de IA para escolha do gráfico ideal em função dos dados
- Prompts de IA para análise de resultados e extração de insights de negócios
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
        subtitle="Gráficos de barras, pizza, dispersão XY, formatação de layout e análise de insights com IA.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Tipos de Gráficos & Objetivos",
        "2. Formatação de Layout",
        "3. IA para Escolha do Gráfico",
        "4. IA para Insights & Storytelling",
        "5. Gráfico Interativo & Auditoria"
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
            "O padrão SENAI recomenda remover elementos visuais poluentes e priorizar o foco na mensagem:"
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
        st.markdown("### 6.4 — Prompts de IA para Auxiliar na Geração do Gráfico Ideal")
        st.write(
            "Ficou em dúvida sobre qual visual escolher? Descreva suas variáveis para a IA e peça a recomendação de design:"
        )
        
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

    with tab4:
        st.markdown("### 6.5 — Prompts de IA para Auxiliar na Análise de Resultados e Gráficos")
        st.write(
            "Após gerar o gráfico no Excel, a IA Generativa pode atuar como sua analista júnior, "
            "ajudando a redigir o resumo executivo com os principais **insights** (achados de negócio):"
        )
        
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

    with tab5:
        st.markdown("### 🧪 Gráfico Interativo & Laboratório Analítico")
        st.write("Veja como a visualização dos dados abaixo destaca a discrepância entre categorias:")
        
        dados_vendas = pd.DataFrame({
            "Categoria": ["Eletrodomésticos", "Informática", "Móveis", "Telefonia", "Acessórios"],
            "Vendas_Milhares_R$": [450, 680, 290, 810, 195],
            "Destaque": ["Normal", "Normal", "Normal", "Líder de Vendas", "Normal"]
        })
        
        # Gráfico interativo com Altair
        chart = alt.Chart(dados_vendas).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
            x=alt.X("Categoria:N", sort="-y", title="Categorias de Produtos"),
            y=alt.Y("Vendas_Milhares_R$:Q", title="Vendas (em milhares de R$)"),
            color=alt.Color("Destaque:N", scale=alt.Scale(domain=["Normal", "Líder de Vendas"], range=["#94A3B8", "#005A9C"]), legend=None),
            tooltip=["Categoria", "Vendas_Milhares_R$"]
        ).properties(height=320)
        
        st.altair_chart(chart, use_container_width=True)
        
        # Desafio Anti-Alucinação
        render_anti_hallucination_quiz(
            key="m5_quiz",
            question="**Cenário de Auditoria:** Uma IA sugeriu criar um gráfico de pizza para comparar o faturamento diário de uma loja ao longo de todos os 365 dias do ano. Qual é a avaliação técnica correta sobre essa recomendação?",
            options=[
                "A recomendação é excelente, pois a pizza divide perfeitamente os 365 dias em 100%.",
                "A recomendação é um erro grave de visualização; um gráfico de linhas contínuo ou colunas mensais é a escolha técnica correta.",
                "Deveríamos usar um gráfico de dispersão com 365 fatias de pizza.",
                "O Excel não permite criar gráficos de pizza com mais de 10 dias."
            ],
            correct_index=1,
            explanation="Uma pizza com 365 fatias geraria uma mancha ilegível e incompreensível. Acompanhamento de tempo contínuo exige gráficos de LINHAS ou agregação em colunas mensais."
        )
        
        st.markdown("---")
        render_prompt_sandbox(
            module_name="Módulo 5: Gráficos e Storytelling",
            placeholder="Exemplo: Tenho uma tabela com dados de pesquisa de satisfação de clientes (notas de 1 a 5). Qual o melhor gráfico?"
        )

    render_footer()
