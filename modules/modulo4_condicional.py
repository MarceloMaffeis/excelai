"""
Módulo 4: Formatação Condicional no Excel & Visualização Inteligente com IA.
Conteúdos e Práticas:
- Regras de realce (Maior que, Menor que, Está entre, Texto que contém, Duplicados)
- Escalas de cor, barras de dados e conjuntos de ícones
- Gerenciamento de regras (editar, prioridade, parar se verdadeiro e excluir)
- Prompts de IA para definição de esquemas de formatação condicional
"""

import streamlit as st
import pandas as pd
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

def render_modulo4_page():
    info = MODULES_INFO["modulo4"]
    render_header(
        title=info["title"],
        subtitle="Regras de realce de células, escalas de cores, barras de dados e uso de IA para visualização analítica.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Regras de Realce",
        "2. Escalas de Cor & Ícones",
        "3. Gerenciar Regras",
        "4. Prompts de Formatação",
        "5. Visualizador & Desafio"
    ])
    
    with tab1:
        st.markdown("### 4.1 — Regras de Realce das Células")
        st.write(
            "A formatação condicional altera automaticamente a aparência visual de uma célula (cor de fundo, "
            "cor da fonte ou borda) assim que o valor atende a um critério lógico pré-estabelecido. "
            "É o conceito puro da **Álgebra Booleana de George Boole** aplicado a relatórios!"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                #### Principais Regras de Realce:
                * 📈 **É Maior do que...** Realça números superiores a uma meta (ex: vendas acima de R$ 5.000 em verde claro).
                * 📉 **É Menor do que...** Destaca valores perigosos (ex: estoque com menos de 10 unidades em vermelho claro).
                * ↔️ **Está entre...** Monitora faixas operacionais aceitáveis (ex: temperatura de máquinas entre 60°C e 85°C em amarelo).
                * 🎯 **É Igual a...** Localiza um valor exato ou status pré-determinado.
                """
            )
        with c2:
            st.markdown(
                """
                #### Regras Baseadas em Texto e Integridade:
                * 🔤 **Texto que Contém...** Procura palavras específicas (ex: pinta em vermelho sempre que o status for *"Atrasado"* ou *"Reprovado"*).
                * 📅 **Uma Data que Ocorre...** Destaca vencimentos ocorrendo *"Hoje"*, *"Amanhã"*, *"Nesta semana"* ou *"No mês passado"*.
                * ⚠️ **Valores Duplicados...** Uma das ferramentas mais valiosas para limpeza de dados: pinta instantaneamente códigos de produtos, CPFs ou notas fiscais inseridas mais de uma vez por engano!
                """
            )

    with tab2:
        st.markdown("### 4.2 — Escalas de Cores, Barras de Dados e Ícones")
        st.write(
            "Nem sempre queremos apenas pintar uma célula de vermelho ou verde. "
            "O Excel oferece recursos gráficos integrados diretamente dentro da célula:"
        )
        
        st.markdown(
            """
            * 🟢🟡🔴 **Escalas de Cores (Gradiente de Calor):**
              - **Escala de 3 Cores:** O valor mais alto fica verde escuro, a média fica amarela e os piores valores ficam em tons graduais de vermelho. Ótimo para mapas de calor (*heatmaps*) de vendas.
            * 📊 **Barras de Dados:**
              - Desenha uma barra horizontal proporcional dentro da própria célula numérica. Permite enxergar quem vendeu mais como se fosse um mini-gráfico de barras embutido na tabela.
            * 🚦 **Conjunto de Ícones:**
              - Insere semáforos (bolinhas vermelha, amarela e verde), bandeiras ou setas direcionais (▲ verde para subida, ► amarela para estável, ▼ vermelha para queda) com base em percentuais calculados.
            """
        )

    with tab3:
        st.markdown("### 4.3 — Gerenciamento e Organização de Regras")
        st.write(
            "Em planilhas corporativas complexas, várias regras podem ser aplicadas na mesma coluna. "
            "O menu **Formatação Condicional -> Gerenciar Regras** permite ter controle total:"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                #### Ordem de Precedência e 'Parar se Verdadeiro'
                - As regras são avaliadas de cima para baixo.
                - Se duas regras forem verdadeiras para a mesma célula, a regra do topo tem prioridade.
                - A caixa de seleção **'Parar se Verdadeiro'** evita que regras inferiores continuem sendo processadas quando uma condição crítica já foi atendida.
                """
            )
        with c2:
            st.markdown(
                """
                #### Ajuste de Intervalo e Limpeza
                - Campo **Aplica-se a:** Permite expandir uma regra para novas linhas sem precisar refazer tudo (ex: de `=$C$2:$C$10` para `=$C$2:$C$1000`).
                - **Limpar Regras:** Opção de excluir regras apenas das células selecionadas ou da planilha inteira de uma só vez para remover formatações corrompidas.
                """
            )

    with tab4:
        st.markdown("### 6.3 — Prompts de IA para Elaboração de Regras Visuais")
        st.write(
            "Ao planejar relatórios executivos, use a IA para propor um sistema de cores harmônico e profissional, "
            "evitando poluição visual que cansa a visão dos gestores."
        )
        
        render_prompt_card(
            title="Planejamento de Regras Condicionais com IA",
            prompt_text=(
                "Atue como designer de dashboards e especialista em Excel corporativo.\n"
                "Tenho uma planilha de controle financeiro com a coluna 'Margem_Lucro_%'.\n\n"
                "Preciso que você proponha um esquema de Formatação Condicional profissional:\n"
                "1. Quais critérios lógicos devo configurar para realçar margens acima da média, na média e abaixo do aceitável?\n"
                "2. Quais cores suaves (códigos hexadecimais ou nomes de preenchimento do Excel) você recomenda para não cansar a visão da diretoria?\n"
                "3. Como configurar a regra no Excel passo a passo pelo menu 'Gerenciar Regras'?"
            ),
            tip_text="Pedir cores suaves e critérios percentuais evita que o relatório vire um 'carnaval' de cores berrantes."
        )
        
        render_audit_alert(
            "Atenção à Acessibilidade Visual: No ambiente corporativo moderno e inclusivo, "
            "lembre-se de que cerca de 8% dos homens possuem algum grau de daltonismo (dificuldade de distinguir vermelho e verde). "
            "Sempre que possível, combine cores com símbolos ou utilize tons de azul e laranja para garantir inclusão total."
        )

    with tab5:
        st.markdown("### 🧪 Visualizador Interativo de Regras Condicionais")
        st.write("Veja como a tabela abaixo destaca automaticamente desempenhos com base em regras de realce:")
        
        vendas_df = pd.DataFrame({
            "Vendedor": ["Lucas Mendes", "Camila Silva", "Rafael Santos", "Juliana Lima", "Bruno Souza"],
            "Meta_R$": [50000, 50000, 50000, 50000, 50000],
            "Realizado_R$": [62000, 48500, 31000, 74000, 49900],
            "Atingimento_%": [124.0, 97.0, 62.0, 148.0, 99.8]
        })
        
        # Estilização visual interativa usando pandas styler
        def highlight_meta(val):
            if val >= 100.0:
                return "background-color: #DEF7EC; color: #03543F; font-weight: bold;"
            elif val >= 80.0:
                return "background-color: #FEF08A; color: #854D0E;"
            else:
                return "background-color: #FEE2E2; color: #991B1B; font-weight: bold;"
                
        styled_df = vendas_df.style.applymap(highlight_meta, subset=["Atingimento_%"])
        st.dataframe(styled_df, use_container_width=True)
        
        # Desafio Anti-Alucinação
        render_anti_hallucination_quiz(
            key="m4_quiz",
            question="**Cenário de Auditoria:** Você precisa aplicar uma regra de formatação condicional para encontrar se existem códigos de clientes duplicados em uma lista de 500 linhas. Qual recurso nativo do Excel faz isso em um clique?",
            options=[
                "Formatação Condicional -> Escalas de Cor -> Vermelho",
                "Formatação Condicional -> Regras de Realce das Células -> Valores Duplicados",
                "Formatação Condicional -> Barra de Dados -> Gradiente",
                "Inserir -> Tabela Dinâmica de Duplicados"
            ],
            correct_index=1,
            explanation="A opção 'Valores Duplicados' dentro de 'Regras de Realce das Células' analisa todo o intervalo selecionado e pinta instantaneamente qualquer valor que apareça 2 ou mais vezes, sendo ideal para auditoria cadastral."
        )
        
        st.markdown("---")
        render_prompt_sandbox(
            module_name="Módulo 4: Formatação Condicional",
            placeholder="Exemplo: Como criar uma formatação condicional que destaque datas de entrega vencidas..."
        )

    render_footer()
