"""
Módulo 1: Fundamentos da Inteligência Artificial & Ética.
Cobre tópicos essenciais:
- IA Analítica vs IA Generativa (histórico, diferenças e aplicações)
- Pilares Éticos (Responsabilidade, Privacidade/LGPD, Transparência, Imparcialidade, Inclusão)
- Engenharia de Prompts e Boas Práticas
- IA Especialista & Microsoft Copilot
- Revisão Humana Crítica e Combate a Alucinações
"""

import streamlit as st
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

def render_modulo1_page():
    info = MODULES_INFO["modulo1"]
    render_header(
        title=info["title"],
        subtitle="Conceitos fundamentais, ética, proteção de dados (LGPD), engenharia de prompt e Copilot.",
        icon=info["icon"]
    )
    
    # Homenagem ao Pioneiro (Lovelace)
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. IA Analítica vs Generativa",
        "2. IA Especialista & Copilot",
        "3. Os 5 Pilares Éticos & LGPD",
        "4. Engenharia de Prompts",
        "5. Bateria de Exercícios & Prática"
    ])
    
    with tab1:
        st.markdown("### 1.1 e 1.2 — Fundamentos: IA Analítica vs. IA Generativa")
        st.write(
            "Para utilizar a tecnologia com eficiência no ambiente de trabalho, o primeiro passo "
            "é compreender que nem todo problema de dados deve ser resolvido da mesma forma. "
            "A Inteligência Artificial divide-se em duas grandes vertentes complementares:"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                """
                <div style="background: #F1F5F9; padding: 1.2rem; border-radius: 8px; border-left: 4px solid #64748B;">
                    <h4 style="margin-top: 0; color: #0F172A;">📊 IA Analítica (Tradicional)</h4>
                    <p style="font-size: 0.92rem; color: #334155;">
                        Focada em analisar dados históricos existentes para encontrar padrões, classificar eventos e realizar 
                        <strong>predições numéricas</strong> precisas.
                    </p>
                    <ul style="font-size: 0.9rem; color: #475569; padding-left: 1.2rem;">
                        <li><strong>Histórico:</strong> Evoluiu a partir da estatística e algoritmos de Machine Learning (como regressões e árvores de decisão).</li>
                        <li><strong>Exemplos:</strong> Previsão de demanda de vendas para o próximo mês; detecção de fraudes em cartões; score de crédito.</li>
                        <li><strong>Vantagem:</strong> Determinística e altamente precisa para números e tendências quantitativas.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                """
                <div style="background: #EFF6FF; padding: 1.2rem; border-radius: 8px; border-left: 4px solid #005A9C;">
                    <h4 style="margin-top: 0; color: #005A9C;">✨ IA Generativa (Moderna)</h4>
                    <p style="font-size: 0.92rem; color: #1E3A8A;">
                        Baseada em Redes Neurais Profundas e Modelos de Linguagem Grande (LLMs), treinada para 
                        <strong>criar novos conteúdos</strong> originais (textos, códigos, fórmulas e tabelas).
                    </p>
                    <ul style="font-size: 0.9rem; color: #1E40AF; padding-left: 1.2rem;">
                        <li><strong>Histórico:</strong> Impulsionada pela arquitetura Transformer (2017) e popularizada pelo ChatGPT, Gemini e Copilot.</li>
                        <li><strong>Exemplos:</strong> Escrever fórmulas complexas do Excel a partir de pedidos em português; gerar tabelas estruturadas; redigir relatórios e insights.</li>
                        <li><strong>Vantagem:</strong> Capacidade semântica de entender intenções em linguagem natural.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        st.markdown("#### ⚖️ Comparativo de Aplicação Prática no Dia a Dia")
        comparison_data = {
            "Cenário de Negócio": [
                "Prever o faturamento de vendas de dezembro com base nos últimos 5 anos",
                "Escrever uma fórmula para calcular comissão escalonada",
                "Descobrir por que a fórmula `#N/D` está acontecendo na célula F12",
                "Classificar clientes em risco de cancelamento (Churn)"
            ],
            "Tecnologia Mais Adequada": [
                "IA Analítica (Regressão / Séries Temporais)",
                "IA Generativa (Geração de Sintaxe de Código)",
                "IA Generativa (Interpretação e Correção de Erros)",
                "IA Analítica (Classificação Estatística)"
            ],
            "Por que?": [
                "A IA Analítica lida com números puros sem o risco de 'alucinação de valores'.",
                "A IA Generativa traduz com perfeição a regra de negócio em português para a sintaxe `=SE(...)`.",
                "Modelos de linguagem conseguem ler mensagens de erro e explicar a causa em linguagem humana.",
                "Modelos analíticos aprendem correlações estatísticas rigorosas sobre comportamento do cliente."
            ]
        }
        st.dataframe(comparison_data, use_container_width=True)

    with tab2:
        st.markdown("### 1.5 — IA Especialista e o Microsoft Copilot no Excel")
        st.write(
            "Uma **IA Especialista** é um modelo treinado ou ajustado (*fine-tuned*) para um domínio específico, "
            "diferente de uma IA de propósito geral que apenas conversa sobre qualquer assunto genérico."
        )
        
        st.markdown(
            """
            #### Como funciona o Microsoft Copilot agregado ao Excel?
            O Copilot no Excel conecta o modelo de linguagem avançado da OpenAI/Microsoft diretamente ao 
            **Microsoft Graph** e ao modelo de objetos da sua planilha.
            
            1. **Requisito Fundamental:** Seus dados precisam estar formatados como uma **Tabela Oficial do Excel** (`Ctrl + T`).
            2. **Acesso Semântico:** Ele não apenas lê o texto, mas compreende quais colunas são números, datas ou categorias.
            3. **Execução Segura:** Quando você pede ao Copilot para criar uma coluna de cálculo, ele gera a **fórmula nativa do Excel** para você inspecionar antes de aplicar, em vez de alterar seus dados de forma invisível.
            """
        )

    with tab3:
        st.markdown("### 1.3 — Os 5 Pilares Éticos no Uso da Inteligência Artificial")
        st.write(
            "No ambiente corporativo e profissional moderno, a tecnologia deve sempre respeitar "
            "padrões de segurança, integridade e governança. Conheça os 5 pilares:"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                1. **🛡️ Responsabilidade:**
                   * O usuário humano é o responsável final pelo documento. Nunca justifique um erro corporativo dizendo que *"foi a IA que calculou errado"*. Você é o auditor.
                2. **🔒 Privacidade & LGPD (Lei Geral de Proteção de Dados):**
                   * Jamais cole tabelas reais com CPF, endereços, prontuários de saúde ou demonstrativos de pagamento de funcionários em chats públicos de IA.
                3. **🔍 Transparência:**
                   * Deixe claro quando um relatório ou análise contou com a assistência de ferramentas automatizadas.
                """
            )
        with c2:
            st.markdown(
                """
                4. **⚖️ Imparcialidade (Combate a Vieses):**
                   * Dados históricos podem conter preconceitos do passado. Verifique se a IA não está priorizando ou desfavorecendo grupos de forma injusta.
                5. **🤝 Inclusão & Acessibilidade:**
                   * As planilhas e relatórios gerados devem ser compreensíveis para todos, prevendo formatos legíveis para leitores de tela e pessoas com deficiência.
                """
            )
            
        render_audit_alert(
            "Técnica de Ofuscação e Proteção Recomendada: Ao solicitar apoio da IA para resolver um problema "
            "em uma planilha de RH ou financeira, substitua os nomes reais por 'Colaborador A', 'Colaborador B' "
            "e multiplique os valores por fatores fictícios (ex: 100, 200, 300). Passe apenas a estrutura lógica!"
        )

    with tab4:
        st.markdown("### 1.4 — Engenharia de Prompts no Excel: As 4 Regras de Ouro")
        st.write(
            "A **Engenharia de Prompt** é a habilidade de estruturar comandos claros para que o modelo "
            "entregue exatamente a fórmula, tabela ou solução necessária na primeira tentativa."
        )
        
        st.markdown(
            """
            | Elemento | Objetivo | Exemplo Prático |
            | :--- | :--- | :--- |
            | **1. Papel (Persona)** | Define o tom e o nível técnico | *"Atue como um especialista avançado em Microsoft Excel para finanças."* |
            | **2. Contexto da Tabela** | Descreve as colunas e tipos de dados | *"Minha tabela possui as colunas A (Data), B (Vendedor), C (Região) e D (Faturamento)."* |
            | **3. Instrução Direta** | O que a IA deve calcular ou gerar | *"Crie uma fórmula para calcular o total de faturamento apenas para o vendedor 'Carlos' na região 'Sudeste'."* |
            | **4. Formato de Saída** | Como você quer a resposta | *"Retorne a fórmula em português do Brasil (usando ponto e vírgula como separador) com breve explicação."* |
            """
        )
        
        render_prompt_card(
            title="Prompt Perfeito para Criação de Fórmulas no Excel",
            prompt_text=(
                "Atue como instrutor especialista em Microsoft Excel e IA.\n"
                "Tenho uma planilha de controle de estoque no Excel com as seguintes colunas:\n"
                "- Coluna A: Código_Produto\n"
                "- Coluna B: Quantidade_Atual (número inteiro)\n"
                "- Coluna C: Estoque_Mínimo (número inteiro)\n\n"
                "Necessidade: Na Coluna D (Status), preciso de uma fórmula com a função SE que compare se a Quantidade_Atual é menor que o Estoque_Mínimo. Se for, deve exibir 'COMPRAR', caso contrário, 'NORMAL'.\n\n"
                "Regras:\n"
                "1. Forneça a fórmula no padrão Excel em Português do Brasil (usando ponto e vírgula).\n"
                "2. Explique a sintaxe e onde colar na planilha."
            ),
            tip_text="O prompt fornece as colunas exatas, tipos de dados e a regra de negócio sem expor nenhum dado confidencial real."
        )
        
        st.markdown("#### ⏳ Autogestão do Tempo: Manual vs. IA")
        st.write(
            "Uma das competências fundamentais avaliadas é a **Autogestão do Tempo**. "
            "Não gaste 5 minutos escrevendo um prompt longo para somar duas células quando você pode "
            "simplesmente teclar `Alt + =` no Excel em 1 segundo! Use a IA para tarefas repetitivas, "
            "fórmulas aninhadas complexas e análise exploratória de grandes volumes."
        )

    with tab5:
        st.markdown("### 🧪 Bateria Completa de Exercícios Práticos & Desafios")
        st.write("Realize os exercícios abaixo para fixar os conceitos éticos, operacionais e de engenharia de prompt:")
        
        # EXERCÍCIO 1
        with st.expander("📝 Exercício 1: Reescrita e Refinamento de Prompt (Engenharia de Prompt)", expanded=True):
            st.markdown(
                """
                **Cenário:** Um colega de trabalho digitou o seguinte comando em um chat de IA:  
                > *"Me ajuda com uma planilha de vendas"*  
                
                **Seu Desafio:** Identifique por que esse prompt falhará e reescreva-o aplicando as **4 Regras de Ouro** (Persona, Contexto, Instrução Direta e Formato de Saída).
                """
            )
            user_reprompt = st.text_area(
                "Escreva seu Prompt Otimizado aqui:",
                key="ex1_reprompt",
                placeholder="Atue como... Minha tabela possui... Preciso de... Retorne em formato..."
            )
            if st.button("Ver Gabarito Sugerido do Exercício 1", key="btn_ex1_ans"):
                st.info(
                    "**Gabarito Recomendado:**\n"
                    "> *'Atue como especialista em Excel. Tenho uma tabela com colunas: Data (coluna A), Vendedor (coluna B) e Faturamento (coluna C). "
                    "Crie uma fórmula em Português do Brasil para somar apenas as vendas do vendedor \"João\". Retorne a fórmula e uma breve explicação passo a passo.'*\n\n"
                    "**Por que está melhor?** Define o papel, as colunas exatas, o objetivo e o idioma do Excel!"
                )
        
        # EXERCÍCIO 2
        with st.expander("🛡️ Exercício 2: Desafio de Anonimização & Conformidade LGPD", expanded=False):
            st.markdown(
                """
                **Cenário:** Você precisa de ajuda da IA para calcular a média salarial e o tempo de casa dos funcionários da sua empresa.  
                A planilha original contém:
                - Coluna A: Nome Completo (Ex: João da Silva Santos)
                - Coluna B: CPF (Ex: 123.456.789-00)
                - Coluna C: Salário Real (Ex: R$ 8.450,00)
                - Coluna D: Data de Admissão (Ex: 12/03/2018)
                
                **Pergunta de Auditoria:** Qual é a conduta correta antes de enviar o problema para um modelo público de IA?
                """
            )
            lgpd_choice = st.radio(
                "Selecione o procedimento de maior conformidade com a LGPD:",
                [
                    "Copiar a planilha inteira e pedir sigilo no texto do prompt.",
                    "Apagar as colunas de Nome e CPF, e enviar apenas o cabeçalho com 2 linhas de valores fictícios mascarados.",
                    "Enviar apenas a coluna de CPF com nomes abreviados.",
                    "Tirar uma foto da tela com o celular e subir a imagem na IA."
                ],
                key="ex2_lgpd_radio"
            )
            if st.button("Conferir Resposta do Exercício 2", key="btn_ex2_ans"):
                if "Apagar as colunas de Nome e CPF" in lgpd_choice:
                    st.success("🎉 **Perfeito!** Nunca suba dados reais de pessoas ou salários. Ao enviar apenas a estrutura com dados fictícios, você obtém a fórmula correta sem colocar a empresa em risco de multas da ANPD.")
                else:
                    st.error("⚠️ **Risco de Violação de LGPD!** Lembre-se: pedir segredo no prompt não garante que os dados não fiquem retidos para treinamento de modelos públicos.")

        # EXERCÍCIO 3
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m1_quiz1",
            question="**Exercício 3 (Quiz Anti-Alucinação):** Você pediu à IA uma fórmula para calcular a média de uma coluna no Excel em Português do Brasil. Qual das alternativas abaixo está **tecnicamente correta**?",
            options=[
                "=AVERAGE(C2, C10)",
                "=MÉDIA(C2:C10)",
                "=MEDIA_PONDERADA(C2; C10)",
                "=CALCULAR_MEDIA(C2..C10)"
            ],
            correct_index=1,
            explanation="No Excel em português do Brasil, a função é `=MÉDIA(início:fim)` com acento agudo. O separador de intervalo contínuo é dois-pontos (`:`). A IA frequentemente sugere a função em inglês `=AVERAGE` ou alucina funções inexistentes como `CALCULAR_MEDIA`."
        )
        
        # EXERCÍCIO 4
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m1_quiz2",
            question="**Exercício 4 (Quiz de Diagnóstico Tecnológico):** Sua diretoria solicitou um modelo preditivo para estimar o faturamento diário da fábrica para os próximos 6 meses com base em 10 anos de histórico de produção. Qual ferramenta você deve propor?",
            options=[
                "Pedir ao ChatGPT/Gemini para adivinhar os números e colar na planilha.",
                "Usar IA Analítica com modelos estatísticos de regressão/séries temporais, pois calculam tendências numéricas determinísticas sem alucinação de dados.",
                "Criar uma fórmula de soma simples e multiplicar por 10.",
                "Usar um gerador de imagens para desenhar o gráfico futuro."
            ],
            correct_index=1,
            explanation="Predições numéricas rigorosas em séries temporais exigem algoritmos de IA Analítica/Estatística. LLMs generativos são feitos para linguagem e códigos, e inventariam números sem embasamento matemático real."
        )
        
        # EXERCÍCIO 5
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 5: Laboratório Prático de Teste de Prompts")
        render_prompt_sandbox(
            module_name="Módulo 1: Fundamentos de IA",
            placeholder="Exemplo: Como criar uma persona de especialista em auditoria de planilhas para a IA me orientar?"
        )

    render_footer()
