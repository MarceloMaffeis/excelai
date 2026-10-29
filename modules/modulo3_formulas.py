"""
Módulo 3: Fórmulas e Funções no Excel & Otimização com IA.
Conteúdos e Práticas:
- 4 operações aritméticas básicas e ordem de precedência
- Cálculos com percentuais (acréscimos, descontos e variação)
- Referências: Relativa, Absoluta ($) e Mista
- Funções essenciais: SOMA, MÉDIA, CONT.SE, SE, MAIÚSCULA, MINÚSCULA, CONCAT
- Prompts de IA por descrição e por exemplo de tabela
- Mitigação de riscos de dados sensíveis ao criar prompts
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

def render_modulo3_page():
    info = MODULES_INFO["modulo3"]
    render_header(
        title=info["title"],
        subtitle="Operações aritméticas, percentuais, referências com $, funções essenciais e IA como assistente de fórmulas.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Operações & Percentuais",
        "2. Referências ($)",
        "3. Funções Essenciais",
        "4. Prompts para Fórmulas",
        "5. Bateria de Exercícios & Prática"
    ])
    
    with tab1:
        st.markdown("### 3.1 e 3.2 — Operações Aritméticas e Cálculos com Percentuais")
        st.write(
            "Toda fórmula no Excel **obrigatoriamente se inicia com o sinal de igualdade (`=`)**. "
            "A ordem de precedência matemática segue o padrão universal: primeiro parênteses `()`, "
            "depois multiplicação `*` e divisão `/`, e por último adição `+` e subtração `-`."
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                #### As 4 Operações Básicas
                - **Soma:** `=A1 + B1`
                - **Subtração:** `=A1 - B1`
                - **Multiplicação:** `=A1 * B1`
                - **Divisão:** `=A1 / B1`
                - **Precedência com Parênteses:** 
                  - `=A1 + B1 * 2` (multiplica B1 por 2 primeiro e depois soma A1)
                  - `=(A1 + B1) * 2` (soma primeiro e depois multiplica o resultado por 2)
                """
            )
        with c2:
            st.markdown(
                """
                #### Matemática dos Percentuais
                - **Calcular parcela percentual:** `=B2 * 15%` (ou `=B2 * 0,15`)
                - **Aplicar Desconto (10% off):** `=B2 * (1 - 10%)`
                - **Aplicar Acréscimo / Reajuste (5%):** `=B2 * (1 + 5%)`
                - **Variação Percentual entre Períodos:**
                  `=(Valor_Novo - Valor_Antigo) / Valor_Antigo`
                  *(Depois formate a célula com o botão `%` do Excel).*
                """
            )

    with tab2:
        st.markdown("### 3.3 — Dominando Referências: Relativas, Absolutas e Mistas")
        st.write(
            "O símbolo do cifrão (`$`) no Excel não significa dinheiro em uma fórmula; ele significa **TRAVA/CONGELAMENTO**. "
            "Você pode alternar entre os tipos apertando a tecla **`F4`** do teclado com o cursor sobre o endereço da célula."
        )
        
        st.markdown(
            """
            | Tipo de Referência | Sintaxe | O que acontece ao arrastar para o lado / para baixo? | Quando usar? |
            | :--- | :---: | :--- | :--- |
            | **Relativa** | `A1` | Muda tanto a letra da coluna quanto o número da linha. | Cálculos linha a linha (ex: `Preço * Quantidade`). |
            | **Absoluta** | `$A$1` | **Trava tudo!** Nem a coluna nem a linha mudam jamais. | Multiplicar por uma célula fixa (ex: taxa Selic ou cotação do dólar na célula `$F$1`). |
            | **Mista (Coluna Fixa)** | `$A1` | A coluna A fica travada, mas a linha desce livremente. | Tabelas de dupla entrada onde os produtos estão sempre na coluna A. |
            | **Mista (Linha Fixa)** | `A$1` | A linha 1 fica travada, mas a coluna pode se mover. | Cabeçalhos horizontais de datas ou meses do ano. |
            """
        )

    with tab3:
        st.markdown("### 3.4 — O Arsenal de Funções Básicas do Excel")
        st.write("Conheça as funções mais utilizadas no mercado de trabalho e cobradas nas empresas:")
        
        funcoes = [
            ("SOMA", "=SOMA(intervalo)", "Soma todos os números no intervalo selecionado.", "=SOMA(C2:C10)"),
            ("MÉDIA", "=MÉDIA(intervalo)", "Calcula a média aritmética dos valores numéricos.", "=MÉDIA(D2:D10)"),
            ("CONT.SE", "=CONT.SE(intervalo; critério)", "Conta quantas células atendem a uma condição específica.", "=CONT.SE(E2:E20; \">=7\")"),
            ("SE", "=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)", "Avalia uma condição lógica e retorna valores diferentes dependendo se o resultado é Verdadeiro ou Falso.", '=SE(F2>=1000; "Bônus"; "Sem Bônus")'),
            ("MAIÚSCULA", "=MAIÚSCULA(texto)", "Converte todas as letras de um texto em caixa alta.", '=MAIÚSCULA(B2)'),
            ("MINÚSCULA", "=MINÚSCULA(texto)", "Converte todas as letras de um texto em minúsculas (útil para padronizar e-mails).", '=MINÚSCULA(B2)'),
            ("CONCAT", "=CONCAT(texto1; texto2; ...)", "Junta dois ou mais textos em uma única célula.", '=CONCAT(A2; " - "; B2)')
        ]
        
        for nome, sintaxe, desc, ex in funcoes:
            with st.expander(f"🔹 Função: {nome} — Sintaxe: {sintaxe}"):
                st.write(f"**Finalidade:** {desc}")
                st.code(ex, language="excel")

    with tab4:
        st.markdown("### 6.2 — Prompts de IA para Elaboração de Fórmulas")
        st.write(
            "Ao pedir fórmulas para a IA, existem duas técnicas principais: **Por Descrição** "
            "(quando você narra a regra de negócio) e **Por Exemplo de Tabela** (quando você fornece uma amostra)."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            render_prompt_card(
                title="6.2.1 Por Meio de Descrição",
                prompt_text=(
                    "Atue como especialista em Excel.\n"
                    "Preciso de uma fórmula para o seguinte cálculo:\n"
                    "- Tenho o salário bruto na célula C5.\n"
                    "- Se o salário for maior que R$ 3.000,00, quero aplicar 10% de desconto.\n"
                    "- Caso contrário, quero aplicar 5% de desconto.\n"
                    "- No final, quero que a fórmula já calcule o salário líquido com o desconto aplicado.\n"
                    "Forneça a fórmula em português com explicação da lógica."
                ),
                tip_text="Perfeito para quando você sabe a regra de cabeça e quer que a IA monte a estrutura lógica do SE."
            )
        with col2:
            render_prompt_card(
                title="6.2.2 Utilizando Tabela como Exemplo (Sem Dados Sensíveis)",
                prompt_text=(
                    "Tenho a seguinte estrutura de tabela no Excel:\n"
                    "Linha 1 (Cabeçalho): A1=Aluno, B1=Nota1, C1=Nota2, D1=Média, E1=Resultado\n"
                    "Linha 2 (Amostra Fictícia): A2='Aluno 1', B2=8,0, C2=6,0\n\n"
                    "1. Qual fórmula coloco em D2 para calcular a média das notas?\n"
                    "2. Qual fórmula coloco em E2 para mostrar 'Aprovado' se D2 for maior ou igual a 7, 'Recuperação' se for entre 5 e 6,9, e 'Reprovado' se for menor que 5?\n"
                    "Use padrão brasileiro com ponto e vírgula."
                ),
                tip_text="Note que usamos 'Aluno 1' e notas genéricas, respeitando 100% a privacidade e a LGPD!"
            )
            
        render_audit_alert(
            "Cuidado com o 'Separador Traiçoeiro': Modelos de IA treinados majoritariamente em inglês "
            "costumam gerar fórmulas com vírgula (ex: `=IF(A1>5, \"Sim\", \"Não\")`). Se você colar isso no "
            "Excel em Português, ele gerará um erro genérico de fórmula inválida. "
            "Lembre-se sempre de auditar e exigir ponto e vírgula (`;`)!"
        )

    with tab5:
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Fórmulas & Funções")
        st.write("Resolva os exercícios práticos abaixo para dominar referências, condicionais e textos no Excel:")
        
        # EXERCÍCIO 1
        with st.expander("➗ Exercício 1: Desafio das 4 Operações & Ordem de Precedência", expanded=True):
            st.markdown(
                """
                **Problema:** Você precisa calcular a comissão total de um vendedor que recebe:
                - Salário fixo na célula `B2` (R$ 2.000,00)
                - Vendas realizadas na célula `C2` (R$ 50.000,00)
                - Percentual de comissão na célula `D2` (3%)
                - Bônus fixo de metas na célula `E2` (R$ 500,00)
                
                Qual é a fórmula matematicamente correta para calcular a Remuneração Total em `F2`?
                """
            )
            f1_choice = st.radio(
                "Selecione a fórmula correta:",
                [
                    "=(B2 + C2) * D2 + E2",
                    "=B2 + (C2 * D2) + E2",
                    "=(B2 + C2 * D2 + E2) * 100",
                    "=SOMA(B2:E2) * D2"
                ],
                key="ex_m3_f1_radio"
            )
            if st.button("Validar Exercício 1", key="btn_ex_m3_1"):
                if f1_choice == "=B2 + (C2 * D2) + E2":
                    st.success("🎉 **Correto!** Apenas a venda em C2 é multiplicada pela comissão em D2, somando-se ao fixo B2 e ao bônus E2.")
                else:
                    st.error("⚠️ **Cuidado com a precedência!** Somar B2 com C2 antes de multiplicar geraria um cálculo inflado e incorreto da comissão.")

        # EXERCÍCIO 2
        with st.expander("💲 Exercício 2: O Cifrão de Ouro ($) — Conversão Cambial", expanded=False):
            st.markdown(
                """
                **Problema:** Você tem uma tabela de 50 produtos com preços em Dólar na coluna `B` (de `B2` até `B51`).  
                A cotação do Dólar está digitada em uma única célula isolada: **`$H$1` (R$ 5,60)**.  
                Você escreveu a fórmula `=B2 * H1` em `C2` para converter em Reais e arrastou a alça de preenchimento até `C51`.  
                Ao chegar em `C3`, o valor ficou zero (`0,00`)!
                
                **Por que isso aconteceu e como corrigir?**
                """
            )
            f2_choice = st.radio(
                "Diagnóstico e correção:",
                [
                    "A célula H1 deve ser congelada como $H$1 com a tecla F4 para que a referência não desça para H2, H3, etc.",
                    "O Excel não aceita multiplicação por células isoladas.",
                    "Deveria ter sido usada a fórmula =B2 + $H$1.",
                    "O Dólar deve ser digitado manualmente em todas as 50 linhas."
                ],
                key="ex_m3_f2_radio"
            )
            if st.button("Validar Exercício 2", key="btn_ex_m3_2"):
                if "congelada como $H$1" in f2_choice:
                    st.success("🎉 **Excelente!** Ao arrastar a fórmula, células relativas descem linha a linha. Como H1 não tinha cifrão, virou H2 (que está vazia). A referência absoluta `$H$1` resolve instantaneamente!")
                else:
                    st.error("⚠️ **Incorreto.** A causa raiz é a falta de referência absoluta no endereço da célula de cotação.")

        # EXERCÍCIO 3
        with st.expander("🎯 Exercício 3: Lógica Condicional com a Função SE", expanded=False):
            st.markdown(
                """
                **Desafio Prático:** Construa a fórmula do Excel para a seguinte regra de estoque:
                - Se a quantidade em estoque na célula `C2` for menor que 15, exibir **'Alerta de Reposição'**.
                - Caso contrário, exibir **'Estoque Suficiente'**.
                """
            )
            ex3_formula = st.text_input("Digite a fórmula exatamente como você escreveria no Excel:", placeholder='=SE(C2<15; "Alerta de Reposição"; "Estoque Suficiente")', key="ex_m3_se_input")
            if st.button("Conferir Resposta do Exercício 3", key="btn_ex_m3_3"):
                clean = ex3_formula.strip().upper()
                if "SE(" in clean and "C2" in clean and "<15" in clean and ";" in clean:
                    st.success("🎉 **Perfeito!** Você estruturou o teste lógico `C2<15`, utilizou o separador ponto e vírgula (`;`) e colocou os textos entre aspas duplas.")
                else:
                    st.info(
                        "**Gabarito Oficial:**\n"
                        '```excel\n=SE(C2<15; "Alerta de Reposição"; "Estoque Suficiente")\n```\n'
                        "- Atenção: No Brasil o separador é `;` (ponto e vírgula), nunca vírgula comum!"
                    )

        # EXERCÍCIO 4
        with st.expander("🔡 Exercício 4: Padronização de Nomes e E-mails Corporativos", expanded=False):
            st.markdown(
                """
                **Desafio de Texto:** Na coluna `A` você tem o Nome (ex: *Carlos*) e na coluna `B` o Sobrenome (ex: *Silva*).  
                Você precisa gerar o e-mail corporativo em minúsculas no formato: `carlos.silva@empresa.com`.  
                
                Qual fórmula combina as funções `MINÚSCULA` e `CONCAT` com perfeição?
                """
            )
            st.code('=MINÚSCULA(CONCAT(A2; "."; B2; "@empresa.com"))', language="excel")
            st.caption("Dica: Você também pode usar o operador comercial `&`: `=MINÚSCULA(A2 & \".\" & B2 & \"@empresa.com\")`.")

        # EXERCÍCIO 5
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m3_quiz_audit1",
            question="**Exercício 5 (Quiz Anti-Alucinação):** Você pediu à IA uma fórmula para somar os valores da coluna E apenas se a cidade na coluna D for 'Campinas'. A IA respondeu 4 opções. Qual delas está **tecnicamente correta** para o Excel em Português?",
            options=[
                '=SUMIF(D2:D100, "Campinas", E2:E100)',
                '=SOMASE(D2:D100; "Campinas"; E2:E100)',
                '=SOMA_SE_CIDADE(D2:D100; "Campinas"; E2:E100)',
                '=SOMA(D2:D100 = "Campinas" * E2:E100)'
            ],
            correct_index=1,
            explanation="No Excel em português, a função condicional de soma chama-se `=SOMASE(intervalo_critério; critério; [intervalo_soma])`, separada por ponto e vírgula. `=SUMIF` é a versão em inglês e `SOMA_SE_CIDADE` é uma alucinação clássica de modelo de linguagem."
        )

        # EXERCÍCIO 6
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m3_quiz_audit2",
            question="**Exercício 6 (Quiz de Contagem):** Qual é a diferença fundamental entre a função `=CONT.SE` e a função `=SOMA`?",
            options=[
                "Nenhuma, ambas fazem exatamente o mesmo cálculo.",
                "O SOMA totaliza a grandeza numérica das células (ex: 10 + 20 = 30), enquanto o CONT.SE conta a frequência de ocorrências (quantas células atendem ao critério, ex: 2 produtos).",
                "O CONT.SE só funciona com letras e o SOMA só com números pares.",
                "O SOMA é uma função do Excel 2016 e o CONT.SE exige o Copilot."
            ],
            correct_index=1,
            explanation="SOMA calcula o valor monetário ou volumétrico total; CONT.SE conta 'quantos itens' existem em uma lista sob determinada condição."
        )

        # EXERCÍCIO 7
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 7: Laboratório de Prompts para Fórmulas")
        render_prompt_sandbox(
            module_name="Módulo 3: Fórmulas e Funções",
            placeholder="Exemplo: Crie uma fórmula que junte o Nome da coluna A com o Sobrenome da coluna B em maiúsculas..."
        )

    render_footer()
