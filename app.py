"""
Portal Educacional: Excel Básico com IA Generativa (2026)
Ponto de Entrada Principal da Aplicação Streamlit.
Disponibilizado sob os termos da Licença MIT (Open Source).
"""

import os
import streamlit as st

# 1. Configuração Inicial da Página
st.set_page_config(
    page_title="Excel com IA Generativa | Portal Educacional",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Carregar Estilos CSS Customizados
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 3. Importar Utilitários e Módulos
from utils.auth import init_auth, is_unlocked, verify_password, get_progress, MODULES_INFO
from modules.home import render_home_page
from modules.biblioteca import render_biblioteca_page
from modules.modulo1_ia_etica import render_modulo1_page
from modules.modulo2_planilhas import render_modulo2_page
from modules.modulo3_formulas import render_modulo3_page
from modules.modulo4_condicional import render_modulo4_page
from modules.modulo5_graficos import render_modulo5_page

# Inicializar Estado de Sessão
init_auth()

# 4. Barra Lateral de Navegação e Configurações
with st.sidebar:
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 2.8rem; line-height: 1;">📊</div>
            <h2 style="color: #005A9C; margin: 0.2rem 0 0 0; font-size: 1.35rem; font-weight: 800;">
                Excel + IA Generativa
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Navegação entre Páginas com Botões Estilizados (Totalmente Confiável)
    st.markdown("#### 🧭 Menu Curricular")
    
    nav_options = [
        ("home", "🏠 Início & Visão Geral"),
        ("biblioteca", "📚 Biblioteca de Recursos (Livre)"),
        ("modulo1", f"{'🔓' if is_unlocked('modulo1') else '🔒'} Módulo 1: Fundamentos & Ética"),
        ("modulo2", f"{'🔓' if is_unlocked('modulo2') else '🔒'} Módulo 2: Objetos do Excel"),
        ("modulo3", f"{'🔓' if is_unlocked('modulo3') else '🔒'} Módulo 3: Fórmulas e Funções"),
        ("modulo4", f"{'🔓' if is_unlocked('modulo4') else '🔒'} Módulo 4: Formatação Condicional"),
        ("modulo5", f"{'🔓' if is_unlocked('modulo5') else '🔒'} Módulo 5: Gráficos e Análise")
    ]
    
    for key, label in nav_options:
        is_active = (st.session_state.active_page == key)
        btn_type = "primary" if is_active else "secondary"
        if st.button(label, key=f"sidebar_nav_{key}", use_container_width=True, type=btn_type):
            st.session_state.active_page = key
            st.rerun()
            
    st.markdown("---")
    
    # Indicador de Progresso Rápido
    unlocked_c, total_c, pct = get_progress()
    st.caption(f"Progresso de Desbloqueio: **{unlocked_c}/{total_c} Módulos ({pct}%)**")
    st.progress(pct / 100)
    
    st.markdown("---")
    
    # Configuração de Provedores de IA
    with st.expander("⚙️ Conexão de IA (Modelos)", expanded=False):
        st.caption("Escolha o provedor de IA para alimentar o laboratório e assistente:")
        
        provider = st.selectbox(
            "Provedor Ativo:",
            [
                "Auto / Simulador Inteligente",
                "Google AI Studio (Gemini)",
                "Palantir Foundry / OpenAI",
                "Ollama Local (http://localhost:11434)"
            ],
            key="selected_ai_provider"
        )
        
        if provider == "Google AI Studio (Gemini)":
            st.text_input(
                "Chave API Gemini:",
                type="password",
                key="custom_gemini_key",
                help="Cole sua chave gerada em https://aistudio.google.com/"
            )
        elif provider == "Palantir Foundry / OpenAI":
            st.text_input("Endpoint URL:", key="custom_foundry_endpoint", placeholder="https://seu-servico/v1")
            st.text_input("API Key / Bearer Token:", type="password", key="custom_foundry_key")
            st.text_input("Nome do Modelo:", key="custom_foundry_model", value="gpt-4o-mini")
        elif provider == "Ollama Local (http://localhost:11434)":
            st.text_input("Modelo Ollama:", key="custom_ollama_model", value="llama3")
            st.caption("Certifique-se de que o Ollama está rodando localmente no seu computador.")
        else:
            st.info("💡 Modo Simulador ativado: Respostas pedagógicas pré-programadas com 100% de disponibilidade sem consumir créditos!")
            
    st.markdown("---")
    
    # Selo de Licença MIT na barra lateral
    st.markdown(
        """
        <div style="font-size: 0.78rem; color: #64748B; text-align: center; padding: 0.5rem 0;">
            <strong>⚖️ Licença MIT Oficial</strong><br>
            Software Livre para Fins Educacionais<br>
            Acesso Aberto e Irrevogável (2026)
        </div>
        """,
        unsafe_allow_html=True
    )

# 5. Roteamento de Páginas com Verificação de Senha
active_page = st.session_state.active_page

if active_page == "home":
    render_home_page()
elif active_page == "biblioteca":
    render_biblioteca_page()
else:
    # Páginas dos Módulos 1 a 5 (requerem validação)
    if is_unlocked(active_page):
        if active_page == "modulo1":
            render_modulo1_page()
        elif active_page == "modulo2":
            render_modulo2_page()
        elif active_page == "modulo3":
            render_modulo3_page()
        elif active_page == "modulo4":
            render_modulo4_page()
        elif active_page == "modulo5":
            render_modulo5_page()
    else:
        # Tela amigável de solicitação de senha caso o aluno selecione diretamente o módulo bloqueado
        info = MODULES_INFO.get(active_page, {})
        st.markdown(
            f"""
            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; padding: 2rem; border-radius: 12px; max-width: 650px; margin: 2rem auto; text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🔒</div>
                <h2 style="color: #005A9C; margin: 0;">Módulo Bloqueado</h2>
                <h4 style="color: #475569; margin: 0.3rem 0 1rem 0;">{info.get('title', 'Módulo')}</h4>
                <p style="color: #64748B; font-size: 0.95rem; line-height: 1.5;">
                    Para acessar o conteúdo explicativo e os exercícios deste módulo, 
                    insira a senha temática informada pelo instrutor da turma.
                </p>
                <div style="background: #F8FAFC; padding: 0.8rem; border-radius: 6px; font-size: 0.88rem; color: #334155; margin-bottom: 1.2rem;">
                    💡 <strong>Dica Cultural:</strong> A senha é o sobrenome ou nome de uma grande mente pioneira da história da computação.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col_c1, col_c2, col_c3 = st.columns([1, 2, 1])
        with col_c2:
            input_pwd = st.text_input("Digite a senha do módulo:", type="password", key=f"direct_unlock_{active_page}")
            if st.button("🔓 Desbloquear Acesso", key=f"btn_unlock_screen_{active_page}", use_container_width=True, type="primary"):
                if verify_password(active_page, input_pwd):
                    st.success("Módulo desbloqueado com sucesso! Redirecionando...")
                    st.rerun()
                else:
                    st.error("Senha incorreta. Solicite ao professor ou instrutor da turma.")
                    
            if st.button("⬅️ Voltar para o Início", key=f"btn_back_home_{active_page}", use_container_width=True):
                st.session_state.active_page = "home"
                st.rerun()
