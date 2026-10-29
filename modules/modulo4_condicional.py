"""
Módulo 4: Formatação Condicional no Excel & Visualização Inteligente com IA.
Conteúdos e Práticas:
- Regras de realce (Maior que, Menor que, Está entre, Texto que contém, Duplicados)
- Escalas de cor, barras de dados e conjuntos de ícones
- Gerenciamento de regras (editar, prioridade, parar se verdadeiro e excluir)
- Prompts de IA para definição de esquemas de formatação condicional
- Bateria expandida de exercícios práticos e auditoria
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
        "5. Bateria de Exercícios & Prática"
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
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Formatação Condicional")
        st.write("Resolva os exercícios abaixo para se tornar especialista em regras de destaque visual e auditoria:")
        
        # EXERCÍCIO 1
        with st.expander("🚦 Exercício 1: Simulação Interativa — Semáforo de Desempenho", expanded=True):
            st.markdown(
                """
                Observe a tabela dinâmica abaixo. As células da coluna `Atingimento_%` mudam de cor automaticamente 
                conforme a regra:
                - 🟢 **Acima de 100%:** Verde suave (meta superada)
                - 🟡 **Entre 80% e 99.9%:** Amarelo suave (atenção/recuperável)
                - 🔴 **Abaixo de 80%:** Vermelho claro (crítico/ação necessária)
                """
            )
            vendas_df = pd.DataFrame({
                "Vendedor": ["Lucas Mendes", "Camila Silva", "Rafael Santos", "Juliana Lima", "Bruno Souza", "Patrícia Gomes"],
                "Meta_R$": [50000, 50000, 50000, 50000, 50000, 50000],
                "Realizado_R$": [62000, 48500, 31000, 74000, 49900, 28000],
                "Atingimento_%": [124.0, 97.0, 62.0, 148.0, 99.8, 56.0]
            })
            
            def highlight_meta(val):
                if val >= 100.0:
                    return "background-color: #DEF7EC; color: #03543F; font-weight: bold;"
                elif val >= 80.0:
                    return "background-color: #FEF08A; color: #854D0E;"
                else:
                    return "background-color: #FEE2E2; color: #991B1B; font-weight: bold;"
                    
            styler = vendas_df.style
            if hasattr(styler, "map"):
                styled_df = styler.map(highlight_meta, subset=["Atingimento_%"])
            else:
                styled_df = styler.applymap(highlight_meta, subset=["Atingimento_%"])
            st.dataframe(styled_df, use_container_width=True)
            
            st.caption("No Excel real, você cria essas três regras selecionando a coluna -> 'Formatação Condicional' -> 'Regras de Realce das Células'.")

        # EXERCÍCIO 2
        with st.expander("📅 Exercício 2: Monitoramento de Vencimentos e Prazos", expanded=False):
            st.markdown(
                """
                **Cenário:** Você gerencia uma planilha com 200 faturas a receber. A coluna `Vencimento` contém datas.  
                Qual recurso da Formatação Condicional permite que faturas vencidas no passado ou que vencem na data de hoje fiquem destacadas automaticamente sem que você precise digitar fórmulas complexas?
                """
            )
            st.info(
                "**Solução no Excel:**\n"
                "1. Selecione as células de datas.\n"
                "2. Vá em **Formatação Condicional** -> **Regras de Realce das Células** -> **Uma Data que Ocorre...**\n"
                "3. Selecione a opção **'Hoje'** ou **'Ontem'** e escolha o preenchimento vermelho claro.\n"
                "4. Toda vez que você abrir o Excel em um novo dia, o sistema recalculará as datas automaticamente!"
            )

        # EXERCÍCIO 3
        with st.expander("🔍 Exercício 3: Detecção de Cadastros Duplicados", expanded=False):
            st.markdown(
                """
                **Problema de Integridade:** No cadastro de clientes, dois operadores inseriram o mesmo cliente com variações no nome, mas com o mesmo número de CPF.  
                Como identificar visualmente esse erro em 2 segundos?
                """
            )
            st.info(
                "**Passo a Passo Oficial:**\n"
                "1. Clique no cabeçalho da coluna de **CPF** para selecionar a coluna inteira.\n"
                "2. Clique em **Formatação Condicional** -> **Regras de Realce das Células** -> **Valores Duplicados...**\n"
                "3. Clique em **OK**.\n"
                "Todas as linhas com CPFs repetidos ficarão imediatamente destacadas em vermelho!"
            )

        # EXERCÍCIO 4
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m4_quiz_prec",
            question="**Exercício 4 (Quiz de Gerenciamento):** Uma célula possui duas regras condicionais aplicadas: Regra 1 (pinta de verde se for > 100) e Regra 2 (pinta de amarelo se for > 50). Se o valor da célula for 150, qual cor ela assumirá se a Regra 1 estiver no topo da lista?",
            options=[
                "Verde, pois a regra do topo tem maior precedência e é processada primeiro.",
                "Amarelo, pois 50 é menor que 100.",
                "Ficará listrada de verde e amarelo.",
                "O Excel travará por erro de loop infinito."
            ],
            correct_index=0,
            explanation="No gerenciador de regras do Excel, as condições são avaliadas de cima para baixo. A regra no topo da lista tem precedência sobre regras inferiores concorrentes."
        )

        # EXERCÍCIO 5
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m4_quiz_icons",
            question="**Exercício 5 (Quiz de Design Visual):** Por que o uso de 'Conjunto de Ícones' (com setas para cima/baixo ou semáforos) costuma ser mais recomendado para relatórios corporativos do que simplesmente pintar o fundo inteiro de 500 linhas de tabela?",
            options=[
                "Porque ícones são mais leves para o disco rígido do computador.",
                "Porque pintar o fundo de centenas de células gera poluição visual ('efeito arco-íris') que cansa a leitura, enquanto pequenos ícones mantém a elegância e clareza do dado.",
                "Porque o Excel proíbe usar cores de fundo em mais de 10 células.",
                "Não há diferença técnica ou visual."
            ],
            correct_index=1,
            explanation="O excesso de preenchimento colorido em tabelas densas sobrecarrega a cognição visual. Ícones discretos ou barras de dados na célula destacam a anomalia mantendo o relatório limpo."
        )

        # EXERCÍCIO 6
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 6: Laboratório de Prompts para Regras Visuais")
        render_prompt_sandbox(
            module_name="Módulo 4: Formatação Condicional",
            placeholder="Exemplo: Proponha regras de formatação condicional acessíveis para daltônicos em uma coluna de status..."
        )

    render_footer()
