"""
Módulo 3: Fórmulas e Funções no Excel & Otimização com IA.
Conteúdos e Práticas:
- 4 operações aritméticas básicas, potências (^), raízes e ordem de precedência
- Cálculos com percentuais (acréscimos, descontos e variação)
- Referências: Relativa, Absoluta ($) e Mista
- Funções essenciais: SOMA, MÉDIA, MÁXIMO, MÍNIMO, CONT.SE, SE, E, OU, SE Aninhado
- Funções de procura (PROCV e ÍNDICE + CORRESP) e Tratamento de Erros (SEERRO)
- Funções de texto: MAIÚSCULA, MINÚSCULA, CONCAT
- Prompts de IA por descrição e por exemplo de tabela
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
        subtitle="Operações, potências, raízes, precedência, referências $, funções lógicas (E/OU), PROCV, SEERRO e IA assistente.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1. Operações, Potências & Precedência",
        "2. Referências & Cifrão ($)",
        "3. Funções Matemáticas & Lógicas (E/OU)",
        "4. Procura (PROCV) & Erros (SEERRO)",
        "5. Prompts de IA para Fórmulas",
        "6. Bateria de Exercícios"
    ])
    
    with tab1:
        st.markdown("### 3.1 — Operações Aritméticas, Potências e Ordem de Precedência")
        st.write(
            "Toda fórmula no Excel **obrigatoriamente se inicia com o sinal de igualdade (`=`)**. "
            "A ordem em que o Excel resolve as contas segue uma hierarquia matemática estrita:"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                #### 🔢 Operadores Matemáticos & Prioridade
                1. **1º Prioridade: Parênteses `()`**  
                   *Tudo o que estiver entre parênteses é calculado antes de qualquer outra coisa.*
                2. **2º Prioridade: Potenciação `^` e Raízes**  
                   - Potência: `=2^3` (resultado: 8)
                   - Raiz Quadrada: `=49^(1/2)` (resultado: 7) ou `=RAIZ(49)`
                   - Raiz Cúbica: `=27^(1/3)` (resultado: 3)
                3. **3º Prioridade: Multiplicação `*` e Divisão `/`**  
                   *Resolvidas da esquerda para a direita.*
                4. **4º Prioridade: Adição `+` e Subtração `-`**
                """
            )
        with c2:
            st.markdown(
                """
                #### 📊 Matemática dos Percentuais
                - **Calcular parcela percentual:** `=B2 * 15%` (ou `=B2 * 0,15`)
                - **Aplicar Desconto (10% off):**  
                  `=B2 - (B2 * 10%)` ou a forma direta `=B2 * (1 - 10%)`
                - **Aplicar Acréscimo / Reajuste (5%):**  
                  `=B2 + (B2 * 5%)` ou a forma direta `=B2 * (1 + 5%)`
                - **Variação Percentual entre Períodos:**  
                  `=(Valor_Novo - Valor_Antigo) / Valor_Antigo`  
                  *(Depois formate a célula com o botão `%` do Excel).*
                """
            )

    with tab2:
        st.markdown("### 3.2 — Dominando Referências: Relativas, Absolutas e Mistas")
        st.write(
            "O símbolo do cifrão (`$`) no Excel não significa dinheiro em uma fórmula; ele significa **TRAVA/CONGELAMENTO**. "
            "Você pode alternar entre os tipos apertando a tecla **`F4`** do teclado com o cursor sobre o endereço da célula."
        )
        
        st.markdown(
            """
            | Tipo de Referência | Sintaxe | O que acontece ao arrastar a fórmula? | Quando usar? |
            | :--- | :---: | :--- | :--- |
            | **Relativa** | `A1` | Muda tanto a coluna quanto a linha. | Cálculos linha a linha (ex: `Preço * Quantidade`). |
            | **Absoluta** | `$A$1` | **Trava tudo!** Nem a coluna nem a linha mudam jamais. | Multiplicar por uma célula fixa (ex: taxa Selic ou cotação do dólar na célula `$F$1`). |
            | **Mista (Coluna Fixa)** | `$A1` | A coluna A fica travada, mas a linha desce livremente. | Tabelas de dupla entrada onde os produtos estão sempre na coluna A. |
            | **Mista (Linha Fixa)** | `A$1` | A linha 1 fica travada, mas a coluna pode se mover. | Cabeçalhos horizontais de datas ou meses do ano. |
            """
        )

    with tab3:
        st.markdown("### 3.3 — Funções Essenciais e Lógica Avançada (SE, E, OU)")
        st.write("Aprenda a criar decisões inteligentes na planilha combinando operadores de comparação e funções lógicas:")
        
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown(
                """
                #### ⚖️ Operadores de Comparação
                - `=` : Igual a
                - `<>` : **Diferente de** (ex: `A1 <> "Cancelado"`)
                - `>` : Maior que
                - `<` : Menor que
                - `>=` : Maior ou igual a
                - `<=` : Menor ou igual a
                
                #### 🧮 Funções Estatísticas Básicas
                - `=SOMA(intervalo)` : Total numérico.
                - `=MÉDIA(intervalo)` : Média aritmética.
                - `=MÁXIMO(intervalo)` : Localiza o maior valor.
                - `=MÍNIMO(intervalo)` : Localiza o menor valor.
                - `=CONT.SE(intervalo; critério)` : Conta quantas células atendem a uma condição.
                """
            )
        with col_l2:
            st.markdown(
                """
                #### 🧠 Lógica Booleana: SE, E, OU
                1. **Função `SE` Simples:**  
                   `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)`
                2. **Função `E` (Conjunção):**  
                   Todos os testes devem ser verdadeiros para retornar VERDADEIRO:  
                   `=SE(E(Nota>=7; Frequencia>=75%); "Aprovado"; "Reprovado")`
                3. **Função `OU` (Disjunção):**  
                   Basta um dos testes ser verdadeiro para retornar VERDADEIRO:  
                   `=SE(OU(Idade>=65; Tempo_Contribuicao>=35); "Aposenta"; "Trabalha")`
                4. **A Regra de Ouro do SE Aninhado:**  
                   Se você tem 3 respostas possíveis (ex: Aprovado, Recuperação, Reprovado), você precisará de **2 SEs**!  
                   Fórmula: **`Nº de SE = Nº de Respostas - 1`**
                """
            )

    with tab4:
        st.markdown("### 3.4 — Funções de Procura (PROCV / ÍNDICE+CORRESP) e Tratamento de Erros (SEERRO)")
        st.write(
            "Funções de busca conectam tabelas diferentes sem você precisar digitar dados duas vezes. "
            "E o tratamento de erros garante relatórios limpos sem o feio `#N/D`:"
        )
        
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🔍 PROCV (Pesquisa Vertical)</h4>
                    <p style="font-size: 0.9rem; color: #334155;">
                        Procura um valor na <strong>primeira coluna</strong> de uma tabela e retorna a informação de uma coluna à direita.
                    </p>
                    <p><code>=PROCV(valor_procurado; tabela_matriz; coluna_retorno; [procurar_intervalo])</code></p>
                    <p style="font-size: 0.88rem; color: #475569;">
                        Exemplo: <code>=PROCV(A2; Tbl_Precos; 2; FALSO)</code><br>
                        <em>Regra: use sempre <code>0</code> ou <code>FALSO</code> no final para busca exata!</em>
                    </p>
                    <h5 style="color: #005A9C; margin-bottom: 4px;">🏆 A Dupla Dinâmica: ÍNDICE + CORRESP</h5>
                    <p style="font-size: 0.88rem; color: #475569;">
                        Supera as limitações do PROCV (pois consegue buscar para a esquerda):<br>
                        <code>=ÍNDICE(coluna_retorno; CORRESP(valor; coluna_busca; 0))</code>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with c_p2:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🛡️ Tratamento Profissional de Erros: SEERRO</h4>
                    <p style="font-size: 0.9rem; color: #334155;">
                        Quando o PROCV não encontra um código ou quando ocorre uma divisão por zero (<code>#DIV/0!</code>), o Excel exibe uma mensagem técnica que assusta a diretoria.
                    </p>
                    <p><code>=SEERRO(fórmula_original; valor_se_der_erro)</code></p>
                    <p style="font-size: 0.88rem; color: #475569;">
                        Exemplo Elegante:<br>
                        <code>=SEERRO(PROCV(A2; Tbl_Precos; 2; 0); "Não Encontrado")</code><br><br>
                        Se o código existir, traz o preço. Se não existir, em vez de <code>#N/D</code>, exibe com elegância <em>"Não Encontrado"</em> ou <code>0,00</code>!
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab5:
        st.markdown("### 6.2 — Prompts de IA para Elaboração de Fórmulas")
        st.write(
            "Ao pedir fórmulas para a IA, existem duas técnicas principais: **Por Descrição** "
            "(quando você narra a regra de negócio) e **Por Exemplo de Tabela** (quando você fornece uma amostra)."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            render_prompt_card(
                title="6.2.1 Por Meio de Descrição com Lógica Condicional",
                prompt_text=(
                    "Atue como especialista em Excel.\n"
                    "Preciso de uma fórmula para o seguinte cálculo:\n"
                    "- Tenho o salário bruto na célula C5 e o tempo de empresa em anos na célula D5.\n"
                    "- Se o funcionário tiver mais de 5 anos de empresa E o salário for menor que R$ 3.000,00, conceder 10% de reajuste.\n"
                    "- Caso contrário, conceder 3% de reajuste.\n"
                    "- Utilize a função SE combinada com a função E.\n"
                    "Forneça a fórmula em português com ponto e vírgula como separador."
                ),
                tip_text="Perfeito para quando você quer que a IA monte a estrutura lógica do SE com E aninhado."
            )
        with col2:
            render_prompt_card(
                title="6.2.2 PROCV com Tratamento de Erros por Exemplo de Tabela",
                prompt_text=(
                    "Tenho duas tabelas no Excel:\n"
                    "- Tabela 1: Coluna A (Código_Produto), Coluna B (Preço_Venda)\n"
                    "- Tabela 2 (Catálogo): Coluna X (Código), Coluna Y (Nome_Produto), Coluna Z (Preço_Tabela)\n\n"
                    "1. Qual fórmula de PROCV coloco em B2 da Tabela 1 para buscar o Preço_Tabela da Tabela 2?\n"
                    "2. Como envolver essa fórmula na função SEERRO para exibir 0,00 caso o código não seja encontrado?\n"
                    "Use o padrão do Excel em Português."
                ),
                tip_text="Note como estruturamos a busca entre tabelas sem passar nenhum dado sensível de clientes!"
            )
            
        render_audit_alert(
            "Cuidado com o 'Separador Traiçoeiro': Modelos de IA treinados majoritariamente em inglês "
            "costumam gerar fórmulas com vírgula (ex: `=IF(A1>5, \"Sim\", \"Não\")`). Se você colar isso no "
            "Excel em Português, ele gerará um erro genérico de fórmula inválida. "
            "Lembre-se sempre de auditar e exigir ponto e vírgula (`;`)!"
        )

    with tab6:
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Fórmulas & Funções")
        st.write("Resolva os exercícios práticos abaixo para dominar referências, potências, lógica e buscas no Excel:")
        
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
        with st.expander("🧠 Exercício 3: Lógica Avançada — SE com E (Bônus de Qualidade)", expanded=False):
            st.markdown(
                """
                **Desafio Industrial:** Uma fábrica de autopeças usina peças onde:
                - Dimensão está na célula `B2`.
                - A peça é **Aprovada** se a dimensão for $\\ge 9.0$ **E** $\\le 10.5$ mm. Caso contrário, é **Reprovada**.
                
                Como estruturar essa fórmula no Excel com a função `E` embutida no `SE`?
                """
            )
            st.code('=SE(E(B2>=9; B2<=10,5); "Aprovada"; "Reprovada")', language="excel")
            st.caption("A função E garante que ambos os limites de tolerância sejam checados simultaneamente.")

        # EXERCÍCIO 4
        with st.expander("🔍 Exercício 4: Busca Blindada com PROCV e SEERRO", expanded=False):
            st.markdown(
                """
                **Desafio:** Ao buscar um produto pelo código em `A2` na tabela de catálogo `Tbl_Produtos` com `PROCV(A2; Tbl_Produtos; 2; 0)`, você quer evitar que apareça `#N/D` caso o código não seja cadastrado.  
                Qual fórmula resolve isso com perfeição?
                """
            )
            st.code('=SEERRO(PROCV(A2; Tbl_Produtos; 2; 0); "Código Inexistente")', language="excel")

        # EXERCÍCIO 5
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m3_quiz_se_count",
            question="**Exercício 5 (A Regra de Ouro do SE Aninhado):** Você precisa classificar o conceito de um aluno entre quatro opções: 'Excelente', 'Bom', 'Regular' ou 'Insuficiente'. Quantas funções SE você precisará aninhar na fórmula?",
            options=[
                "1 função SE",
                "3 funções SE (Regra: Nº de Respostas - 1)",
                "4 funções SE",
                "Nenhuma, basta usar o SOMA"
            ],
            correct_index=1,
            explanation="Para 4 respostas possíveis, você faz 3 perguntas lógicas consecutivas. Se a primeira não for, testa a segunda; se não for, testa a terceira; e o que sobrar é a 4ª opção por eliminação! Logo: 4 - 1 = 3 funções SE."
        )

        # EXERCÍCIO 6
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m3_quiz_audit1",
            question="**Exercício 6 (Quiz Anti-Alucinação):** Você pediu à IA uma fórmula para somar os valores da coluna E apenas se a cidade na coluna D for 'Campinas'. A IA respondeu 4 opções. Qual delas está **tecnicamente correta** para o Excel em Português?",
            options=[
                '=SUMIF(D2:D100, "Campinas", E2:E100)',
                '=SOMASE(D2:D100; "Campinas"; E2:E100)',
                '=SOMA_SE_CIDADE(D2:D100; "Campinas"; E2:E100)',
                '=SOMA(D2:D100 = "Campinas" * E2:E100)'
            ],
            correct_index=1,
            explanation="No Excel em português, a função condicional de soma chama-se `=SOMASE(intervalo_critério; critério; [intervalo_soma])`, separada por ponto e vírgula. `=SUMIF` é a versão em inglês e `SOMA_SE_CIDADE` é uma alucinação clássica de modelo de linguagem."
        )

        # EXERCÍCIO 7
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 7: Laboratório de Prompts para Fórmulas")
        render_prompt_sandbox(
            module_name="Módulo 3: Fórmulas e Funções",
            placeholder="Exemplo: Crie uma fórmula de PROCV combinada com SEERRO para buscar preços sem erros..."
        )

    render_footer()
