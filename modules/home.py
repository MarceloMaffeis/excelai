"""
Página Inicial (Home) do Portal Educacional.
Apresenta o curso, visão geral pedagógica, barra de progresso,
cards interativos para desbloqueio por senha e acesso direto à Biblioteca Aberta.
"""

import streamlit as st
from utils.auth import MODULES_INFO, is_unlocked, verify_password, get_progress
from utils.ui_components import render_header, render_footer

def render_home_page():
    render_header(
        title="Portal do Aluno: Excel Básico com IA Generativa",
        subtitle="Formação Inicial e Continuada • Aperfeiçoamento Profissional (20h) • SENAI-SP",
        icon="🚀"
    )
    
    # Hero Banner
    st.markdown(
        """
        <div class="hero-card">
            <h2>Bem-vindo à sua jornada de produtividade com Excel e IA!</h2>
            <p>
                Este portal foi desenvolvido para apoiar seu aprendizado prático no curso de 
                <strong>Excel Básico impulsionado pela Inteligência Artificial Generativa</strong>. 
                Aqui você dominará desde a estruturação de planilhas e fórmulas essenciais até o uso 
                avançado de prompts para automação, análise de dados e criação de gráficos, 
                sempre com foco no <strong>uso ético, conformidade com a LGPD e auditoria crítica</strong>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Barra de Progresso
    unlocked_count, total_count, pct = get_progress()
    col_p1, col_p2 = st.columns([3, 1])
    with col_p1:
        st.markdown(f"**Progresso de Desbloqueio dos Módulos:** {unlocked_count} de {total_count} módulos disponíveis ({pct}%)")
        st.progress(pct / 100)
    with col_p2:
        if st.button("📚 Ir para Biblioteca (Acesso Livre)", use_container_width=True, type="secondary"):
            st.session_state.active_page = "biblioteca"
            st.rerun()
            
    st.markdown("---")
    
    # Informações Pedagógicas (Competências Socioemocionais)
    with st.expander("🎯 Competências e Habilidades Desenvolvidas no Curso (Metodologia SENAI)", expanded=False):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("#### ⏳ Autogestão & Tempo")
            st.write(
                "Aprender a dosar o tempo entre a execução manual e o uso da IA, "
                "priorizando prompts onde a automação realmente gera valor de produtividade."
            )
        with c2:
            st.markdown("#### 🛡️ Responsabilidade & LGPD")
            st.write(
                "Auditar criticamente todo conteúdo gerado pela IA e jamais compartilhar "
                "dados sensíveis corporativos em plataformas públicas."
            )
        with c3:
            st.markdown("#### 🔍 Atenção a Detalhes")
            st.write(
                "Identificar alucinações, erros lógicos e sintaxes incorretas em fórmulas "
                "propostas pela inteligência artificial antes de aplicá-las."
            )
            
    st.markdown("### 📑 Módulos Curriculares")
    st.caption("Insira a senha fornecida pelo instrutor em sala de aula para desbloquear cada módulo no momento adequado.")
    
    # Grid de Módulos
    modules_list = [
        ("biblioteca", "Biblioteca Mundial de Recursos", "📚", "Documentações internacionais, tutoriais Microsoft, guias de prompt e datasets gratuitos."),
        ("modulo1", "Módulo 1: Fundamentos de IA & Ética", "🤖", "IA Analítica vs Generativa, IA Especialista (Copilot), Pilares Éticos, LGPD e Técnicas de Prompt."),
        ("modulo2", "Módulo 2: Gerenciamento de Objetos", "📊", "Células, linhas, colunas, formatação, planilhas, tabelas inteligentes e prompts para gerar estruturas."),
        ("modulo3", "Módulo 3: Fórmulas e Funções Básicas", "➗", "4 operações, referências relativas/absolutas, SOMA, MÉDIA, CONT.SE, SE e prompts para cálculo."),
        ("modulo4", "Módulo 4: Formatação Condicional", "🎨", "Regras de realce, escalas de cor, gerenciamento de formatação e prompts para destacar metas visuais."),
        ("modulo5", "Módulo 5: Gráficos e Análise de Dados", "📈", "Colunas, barras, pizza, dispersão XY, layouts, geração de gráficos ideais e extração de insights com IA.")
    ]
    
    for key, title, icon, desc in modules_list:
        unlocked = is_unlocked(key)
        
        with st.container():
            col_info, col_action = st.columns([3, 1])
            
            with col_info:
                badge = '<span class="badge-free">Acesso Livre</span>' if key == "biblioteca" else (
                    '<span class="badge-unlocked">🔓 Desbloqueado</span>' if unlocked else '<span class="badge-locked">🔒 Bloqueado por Senha</span>'
                )
                st.markdown(
                    f"""
                    <div style="margin-bottom: 0.4rem;">
                        <span style="font-size: 1.3rem;">{icon}</span> 
                        <strong style="font-size: 1.15rem; color: #0F172A;">{title}</strong>
                        &nbsp;{badge}
                    </div>
                    <div style="color: #64748B; font-size: 0.95rem; margin-bottom: 0.5rem;">
                        {desc}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
            with col_action:
                if unlocked:
                    if st.button(f"Entrar no Módulo", key=f"enter_btn_{key}", use_container_width=True, type="primary"):
                        st.session_state.active_page = key
                        st.rerun()
                else:
                    # Campo de senha para desbloquear
                    with st.popover("🔑 Digitar Senha", use_container_width=True):
                        st.write(f"Digite a senha para acessar o **{title}**:")
                        st.caption("Dica: Nome de um pioneiro ou pioneira da computação.")
                        input_pwd = st.text_input("Senha:", type="password", key=f"pwd_input_{key}")
                        if st.button("Confirmar", key=f"confirm_btn_{key}", use_container_width=True):
                            if verify_password(key, input_pwd):
                                st.success("Desbloqueado com sucesso!")
                                st.rerun()
                            else:
                                st.error("Senha incorreta. Verifique com seu professor.")
                                
            st.markdown("<hr style='margin: 0.5rem 0 1rem 0; border: none; border-top: 1px solid #F1F5F9;' />", unsafe_allow_html=True)

    render_footer()
