"""
Módulo 3: Fórmulas e Funções no Excel & Otimização com IA.
Cobre 100% da Ementa SENAI:
- 4 operações aritméticas básicas e ordem de precedência
- Cálculos com percentuais (acréscimos, descontos e variação)
- Referências: Relativa, Absoluta ($) e Mista
- Funções essenciais: SOMA, MÉDIA, CONT.SE, SE, MAIÚSCULA, MINÚSCULA, CONCAT
- Prompts de IA por descrição e por exemplo de tabela
- Mitigação de riscos de dados sensíveis ao criar prompts
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
        "5. Simulador & Auditoria"
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
        st.markdown("### 🧪 Simulador Interativo de Fórmulas e Auditoria")
        st.write("Experimente o simulador abaixo para ver como as funções reagem a dados fictícios:")
        
        sim_df = pd.DataFrame({
            "Aluno": ["Mariana Santos", "Pedro Costa", "Juliana Lima", "Lucas Silva", "Beatriz Rocha"],
            "Nota_1": [8.5, 5.0, 9.0, 4.0, 7.0],
            "Nota_2": [7.5, 4.5, 8.0, 6.0, 6.5]
        })
        sim_df["Média"] = (sim_df["Nota_1"] + sim_df["Nota_2"]) / 2
        sim_df["Situação"] = sim_df["Média"].apply(lambda m: "Aprovado" if m >= 7.0 else ("Recuperação" if m >= 5.0 else "Reprovado"))
        
        st.dataframe(sim_df, use_container_width=True)
        
        # Desafio Anti-Alucinação
        render_anti_hallucination_quiz(
            key="m3_quiz",
            question="**Cenário de Auditoria:** Você precisa calcular a comissão de uma equipe multiplicando a venda de cada vendedor pela taxa fixa de 10% que está digitada isoladamente na célula `G1`. Ao arrastar a fórmula para as outras 50 linhas, qual fórmula evitará erros?",
            options=[
                "=B2 * G1",
                "=B2 * $G$1",
                "=B2 * G$1$",
                "=$B$2 * G1"
            ],
            correct_index=1,
            explanation="Para que a célula G1 não se desloque para G2, G3, etc. ao arrastar para baixo, é obrigatório congelá-la com referência absoluta: `$G$1`. O cifrão vem antes da letra e antes do número."
        )
        
        st.markdown("---")
        render_prompt_sandbox(
            module_name="Módulo 3: Fórmulas e Funções",
            placeholder="Exemplo: Crie uma fórmula que junte o Nome da coluna A com o Sobrenome da coluna B em maiúsculas..."
        )

    render_footer()
