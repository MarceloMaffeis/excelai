"""
Módulo 2: Gerenciamento de Objetos do Excel & Estruturação com IA.
Conteúdos e Práticas:
- Células, Endereçamento, Linhas, Colunas, Formatação, Filtros e Opções de Colagem
- Evolução das Dimensões do Excel e Tipos de Dados (Constantes vs Calculados)
- Validação de Dados (Listas Suspensas) e Proteção de Fórmulas
- Planilhas e Pasta de Trabalho
- Formatação como Tabela oficial e integração com Power Apps
- Prompts de IA para geração de estruturas de planilhas formatadas
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
        subtitle="Células, dimensões, tipos de dados, validação, proteção de fórmulas, tabelas oficiais e geração por IA.",
        icon=info["icon"]
    )
    
    render_pioneer_badge(info["pioneer"], info["bio"])
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1. Células, Dimensões & Tipos",
        "2. Validação & Proteção",
        "3. Pastas & Planilhas",
        "4. Tabelas Oficiais & Power Apps",
        "5. Prompts de Estruturação",
        "6. Bateria de Exercícios"
    ])
    
    with tab1:
        st.markdown("### 2.1 — O Coração do Excel: Células, Endereçamento e Tipos de Dados")
        st.write(
            "Toda a mecânica do Microsoft Excel baseia-se em uma grade bidimensional inteligente. "
            "Compreender a anatomia dos objetos e os tipos de dados é essencial para evitar falhas em fórmulas:"
        )
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                #### 📌 Endereçamento e Dimensões
                - **Endereço da Célula:** A interseção entre uma **Coluna** (letra) e uma **Linha** (número). Ex: `C5`.
                - **A Fantástica Evolução da Capacidade:**
                  - *Versões Anteriores (até 2003):* 256 colunas $\\times$ 65.536 linhas = **16.777.216 células**.
                  - *Versões Modernas (2007 até Microsoft 365):* 16.384 colunas $\\times$ 1.048.576 linhas = **mais de 17 BILHÕES de células**!
                - **Inserir e Remover Linhas/Colunas:** 
                  - Inserir: selecione e tecle `Ctrl + Shift + +`
                  - Excluir: selecione e tecle `Ctrl + -`
                """
            )
        with c2:
            st.markdown(
                """
                #### 🏷️ Os 2 Grandes Tipos de Dados
                1. **Dados Constantes (Entrada Direta):**
                   - **Texto:** Ex: `"Parafuso Aço"`, `"São Paulo"` (alinhado à esquerda por padrão).
                   - **Número:** Ex: `1250`, `45,90` (alinhado à direita por padrão).
                   - **Data:** Ex: `29/10/2026` (armazenado internamente como número de série).
                   - **Hora:** Ex: `14:30:00` (fração de um dia de 24 horas).
                2. **Dados Calculados (Fórmulas e Funções):**
                   - Começam sempre com o sinal de igualdade (`=`) e reagem dinamicamente quando as células de origem são alteradas.
                """
            )
            
        st.markdown("---")
        st.markdown("#### 📋 Opções Especiais de Colagem (`Colar Especial`)")
        st.write(
            "Dominar o Colar Especial poupa horas de retrabalho e evita desastres em relatórios:"
        )
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            st.info(
                "**1. Colar Valores:**\n\n"
                "Elimina a fórmula matemática e grava apenas o número estático final. Imprescindível para auditar planilhas e evitar erros `#REF!`."
            )
        with col_c2:
            st.info(
                "**2. Colar Fórmulas:**\n\n"
                "Copia a lógica matemática sem herdar a cor, bordas ou preenchimentos da célula de origem."
            )
        with col_c3:
            st.info(
                "**3. Transpor:**\n\n"
                "Gira a orientação da tabela: o que estava organizado em colunas vira linhas, e vice-versa, com 1 clique!"
            )

    with tab2:
        st.markdown("### 2.2 — Validação de Dados & Proteção de Fórmulas")
        st.write(
            "Dois dos recursos profissionais mais importantes ensinados em cursos corporativos são a **blindagem de digitação** "
            "e a **proteção contra exclusão acidental de fórmulas**:"
        )
        
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🛡️ Validação de Células (Listas Suspensas)</h4>
                    <p style="font-size: 0.92rem; color: #334155;">
                        Evita que operadores digitem nomes errados ou valores fora do padrão aceitável.
                    </p>
                    <ul style="font-size: 0.88rem; color: #475569; padding-left: 1.1rem;">
                        <li><strong>Como fazer:</strong> Menu <code>Dados</code> &rarr; <code>Validação de Dados</code>.</li>
                        <li><strong>Permitir Lista:</strong> Digite os itens separados por ponto e vírgula: <code>Ativo;Inativo;Manutenção</code>. Uma setinha suspensa aparecerá na célula!</li>
                        <li><strong>Permitir Número Inteiro:</strong> Exige que o valor esteja, por exemplo, entre <code>1</code> e <code>100</code>.</li>
                        <li><strong>Mensagem de Erro:</strong> Configure uma mensagem personalizada de bloqueio quando o usuário tentar burlar a regra.</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_v2:
            st.markdown(
                """
                <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 1.2rem; border-radius: 8px;">
                    <h4 style="color: #005A9C; margin-top: 0;">🔒 O Segredo da Proteção de Planilha</h4>
                    <p style="font-size: 0.92rem; color: #334155;">
                        Como permitir que o funcionário preencha apenas os dados de entrada sem conseguir alterar suas fórmulas:
                    </p>
                    <ol style="font-size: 0.88rem; color: #475569; padding-left: 1.1rem;">
                        <li>Por padrão, todas as células do Excel vêm com o atributo "Bloqueada" ativado (mas ele só funciona se a planilha for protegida).</li>
                        <li><strong>Passo 1:</strong> Selecione apenas as células onde o usuário <em>PODE</em> digitar (ex: colunas de Nome e Quantidade).</li>
                        <li><strong>Passo 2:</strong> Clique com o botão direito &rarr; <code>Formatar Células</code> &rarr; aba <code>Proteção</code> &rarr; <strong>DESMARQUE</strong> a caixa "Bloqueada".</li>
                        <li><strong>Passo 3:</strong> Vá no menu <code>Revisão</code> (ou Ferramentas) &rarr; <code>Proteger Planilha</code> &rarr; digite uma senha.</li>
                        <li><strong>Resultado:</strong> Suas fórmulas ficam blindadas e o usuário só consegue clicar e preencher nos campos liberados!</li>
                    </ol>
                </div>
                """,
                unsafe_allow_html=True
            )

    with tab3:
        st.markdown("### 2.3 — Planilhas e Pasta de Trabalho")
        st.write(
            "No padrão corporativo, a hierarquia de documentos funciona da seguinte forma:"
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

    with tab4:
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

    with tab5:
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

    with tab6:
        st.markdown("### 🧪 Bateria de Exercícios Práticos: Gerenciamento de Objetos")
        st.write("Resolva os desafios abaixo para consolidar seu domínio prático sobre células, formatações, validação e proteção:")
        
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
        with st.expander("🛡️ Exercício 3: Blindagem de Fórmulas e Proteção de Planilha", expanded=False):
            st.markdown(
                """
                **Desafio:** Você construiu uma calculadora de custos no Excel cheia de fórmulas em `D2:D50`. Usuários precisam digitar apenas as quantidades em `C2:C50`.  
                Para que eles não consigam apagar as fórmulas por engano, qual é a sequência correta?
                """
            )
            st.info(
                "**Sequência Técnica Correta:**\n"
                "1. Selecione `C2:C50` (onde o usuário digita) &rarr; `Formatar Células` &rarr; `Proteção` &rarr; **Desmarque 'Bloqueada'**.\n"
                "2. Vá em `Revisão` &rarr; `Proteger Planilha` e defina uma senha.\n"
                "Agora as fórmulas continuam travadas e seguras, e os dados de entrada podem ser digitados normalmente!"
            )

        # EXERCÍCIO 4
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m2_quiz1",
            question="**Exercício 4 (Quiz de Objetos):** Você precisa transformar uma lista comum de clientes em uma Tabela Oficial do Excel com filtros nativos e expansão dinâmica automática. Qual é o atalho de teclado mais rápido no padrão brasileiro do Excel?",
            options=[
                "Ctrl + C",
                "Ctrl + T (ou Ctrl + Alt + T dependendo da versão)",
                "Alt + F4",
                "Shift + Barra de Espaço"
            ],
            correct_index=1,
            explanation="O atalho `Ctrl + T` (ou `Ctrl + Alt + T`) seleciona todo o bloco contíguo de dados e abre instantaneamente a caixa 'Criar Tabela', ativando filtros e cabeçalhos oficiais."
        )

        # EXERCÍCIO 5
        st.markdown("---")
        render_anti_hallucination_quiz(
            key="m2_quiz2",
            question="**Exercício 5 (Quiz de Dimensões e Integração):** Quantas linhas e colunas possui uma planilha moderna do Excel (a partir da versão 2007 e Microsoft 365)?",
            options=[
                "256 colunas e 65.536 linhas",
                "16.384 colunas e 1.048.576 linhas (mais de 17 bilhões de células)",
                "100 colunas e 1.000 linhas",
                "Linhas e colunas infinitas limitadas apenas pela velocidade da internet"
            ],
            correct_index=1,
            explanation="Desde a versão 2007 (formato .xlsx), o Excel expandiu sua grade para exatamente 16.384 colunas (da coluna A até XFD) e 1.048.576 linhas, comportando mais de 17 bilhões de células!"
        )

        # EXERCÍCIO 6
        st.markdown("---")
        st.markdown("#### 📂 Exercício 6: Prática com Arquivo para Download")
        st.write("Baixe a planilha de dados brutos abaixo, abra no Excel e execute as seguintes instruções:")
        st.markdown(
            """
            1. Converta o intervalo em **Tabela Oficial** (`Ctrl + T`).
            2. Renomeie a tabela para `Tbl_Manutencao_Equipamentos`.
            3. Crie uma **Validação de Dados** na coluna `Status` permitindo apenas a lista: `Operacional;Manutenção;Alerta`.
            4. Classifique a coluna `Horas_Uso` do **Maior para o Menor**.
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
            label="📥 Baixar Planilha para Exercício 6 (CSV)",
            data=csv_buffer.getvalue().encode("utf-8-sig"),
            file_name="tabela_maquinas_exemplo.csv",
            mime="text/csv",
            key="btn_dl_sample_machines_m2"
        )

        # EXERCÍCIO 7
        st.markdown("---")
        st.markdown("#### 🧪 Exercício 7: Laboratório Interativo de Prompts")
        render_prompt_sandbox(
            module_name="Módulo 2: Gerenciamento de Objetos",
            placeholder="Exemplo: Crie a estrutura de colunas e dados fictícios para controle de compras industriais..."
        )

    render_footer()
