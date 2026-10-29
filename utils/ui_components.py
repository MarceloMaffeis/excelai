"""
Componentes de Interface de Usuário (UI) Reutilizáveis.
Inclui cabeçalhos, rodapé com Licença MIT explícita, caixas de prompt,
desafios anti-alucinação e o laboratório de prompts (Prompt Sandbox).
"""

import streamlit as st
from utils.ai_service import generate_ai_response

def render_header(title: str, subtitle: str = "", icon: str = "📘"):
    """Renderiza o cabeçalho padronizado da página."""
    st.markdown(
        f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 2.2rem;">{icon}</span>
                <h1 style="color: #005A9C; margin: 0; font-size: 2.1rem; font-weight: 800;">{title}</h1>
            </div>
            {f'<p style="color: #475569; font-size: 1.05rem; margin-top: 0.3rem;">{subtitle}</p>' if subtitle else ''}
            <hr style="margin: 0.8rem 0 1.5rem 0; border: none; border-top: 1px solid #E2E8F0;" />
        </div>
        """,
        unsafe_allow_html=True
    )

def render_pioneer_badge(pioneer_name: str, pioneer_bio: str):
    """Exibe o card em homenagem ao pioneiro da computação quando o módulo é aberto."""
    st.markdown(
        f"""
        <div class="pioneer-card">
            <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 1.05rem;">
                <span>🗝️ Módulo Desbloqueado com Sucesso!</span>
            </div>
            <p style="margin: 6px 0 0 0; font-size: 0.95rem;">
                <strong>Homenagem a {pioneer_name}:</strong> {pioneer_bio}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_prompt_card(title: str, prompt_text: str, tip_text: str = ""):
    """Exibe um modelo de prompt formatado e pronto para cópia."""
    st.markdown(f"**💡 Exemplo de Engenharia de Prompt: {title}**")
    st.markdown(
        f"""
        <div class="prompt-box">
{prompt_text}
        </div>
        """,
        unsafe_allow_html=True
    )
    if tip_text:
        st.markdown(
            f"""
            <div class="prompt-tip">
                🔍 <strong>Por que este prompt funciona:</strong> {tip_text}
            </div>
            """,
            unsafe_allow_html=True
        )

def render_audit_alert(alert_text: str):
    """Alerta de auditoria humana e responsabilidade ética (LGPD)."""
    st.markdown(
        f"""
        <div class="audit-box">
            <strong style="display: flex; align-items: center; gap: 6px;">
                🛡️ Auditoria Humana & Proteção de Dados (LGPD)
            </strong>
            <p style="margin: 6px 0 0 0; font-size: 0.92rem; line-height: 1.5;">
                {alert_text}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_anti_hallucination_quiz(key: str, question: str, options: list, correct_index: int, explanation: str):
    """Renderiza um desafio interativo para treinar a Atenção aos Detalhes contra alucinações de IA."""
    st.markdown("### 🧪 Desafio de Atenção aos Detalhes (Anti-Alucinação)")
    st.write(question)
    
    selected = st.radio(
        "Selecione a resposta que você considera tecnicamente correta após auditar:",
        options,
        key=f"quiz_radio_{key}"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Validar Resposta", key=f"quiz_btn_{key}"):
            user_idx = options.index(selected)
            if user_idx == correct_index:
                st.success("🎉 **Excelente auditoria!** Você identificou a resposta correta e não se deixou enganar por erros sutis da IA.")
            else:
                st.error("⚠️ **Atenção aos detalhes!** A IA gerou uma alucinação ou erro de sintaxe nesta opção. Veja a explicação abaixo:")
            st.info(f"**Explicação do Especialista SENAI:** {explanation}")

def render_prompt_sandbox(module_name: str, placeholder: str = ""):
    """Sandbox interativo para o aluno testar prompts diretamente na página."""
    with st.expander(f"🧪 Laboratório de Prompts & IA: {module_name}", expanded=False):
        st.markdown(
            "Digite uma dúvida ou solicitação para a IA resolver tarefas deste módulo. "
            "Avalie criticamente a resposta antes de aplicá-la em suas planilhas!"
        )
        
        user_prompt = st.text_area(
            "Escreva seu Prompt:",
            placeholder=placeholder or "Ex: Crie uma fórmula para calcular o total de vendas...",
            key=f"sandbox_input_{module_name}",
            height=100
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            submit = st.button("Enviar para a IA", key=f"sandbox_btn_{module_name}", type="primary")
            
        if submit and user_prompt.strip():
            with st.spinner("O Tutor de IA está processando seu prompt..."):
                provider = st.session_state.get("selected_ai_provider", "Auto / Simulador Inteligente")
                resp = generate_ai_response(
                    prompt=user_prompt,
                    provider=provider,
                    custom_gemini_key=st.session_state.get("custom_gemini_key", ""),
                    custom_foundry_key=st.session_state.get("custom_foundry_key", ""),
                    custom_foundry_endpoint=st.session_state.get("custom_foundry_endpoint", ""),
                    custom_foundry_model=st.session_state.get("custom_foundry_model", ""),
                    custom_ollama_model=st.session_state.get("custom_ollama_model", "llama3")
                )
                st.markdown("---")
                st.markdown(resp)

def render_footer():
    """Renderiza o rodapé oficial e vinculante de Licença MIT em todas as telas."""
    st.markdown(
        """
        <div class="mit-footer">
            <div style="margin-bottom: 0.6rem;">
                <span class="mit-tag">⚖️ Licença MIT Oficial</span>
                <span class="mit-tag">📖 Software Educacional Aberto</span>
                <span class="mit-tag">🆓 100% Gratuito</span>
                <span class="mit-tag">🛡️ Open Source</span>
            </div>
            <div>
                <strong>Portal Educacional Excel Básico com IA Generativa (SENAI-SP 2026)</strong><br>
                Este sistema é disponibilizado livremente sob os termos da 
                <a href="https://opensource.org/licenses/MIT" target="_blank" style="color: #005A9C; text-decoration: underline;">
                    Licença MIT
                </a>.
                Permitido o uso, estudo, cópia, modificação, fusão, publicação e distribuição ilimitada para fins educacionais,
                comerciais ou de pesquisa, garantindo proteção contra revogação de acesso.
            </div>
            <div style="margin-top: 0.5rem; font-size: 0.78rem; color: #94A3B8;">
                Desenvolvido para fins de qualificação e aperfeiçoamento profissional em Tecnologia da Informação.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
