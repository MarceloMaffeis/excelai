"""
Sistema de Autenticação e Controle Pedagógico por Senhas Temáticas.
Cada módulo do curso é protegido por uma senha homenageando pioneiros da computação.
A Biblioteca Mundial de Recursos é 100% aberta e não requer senha.
"""

import streamlit as st

MODULES_INFO = {
    "home": {
        "title": "Início & Visão Geral",
        "icon": "🏠",
        "requires_password": False,
        "password": None,
        "pioneer": "Boas-vindas",
        "bio": "Portal do Aluno - Aperfeiçoamento Profissional em Excel Básico com IA Generativa."
    },
    "biblioteca": {
        "title": "Biblioteca Mundial de Recursos",
        "icon": "📚",
        "requires_password": False,
        "password": None,
        "pioneer": "Acesso Livre / Open Knowledge",
        "bio": "Espaço aberto com referências mundiais, documentação oficial Microsoft, guias de IA, ética e bases de dados abertas."
    },
    "modulo1": {
        "title": "Módulo 1: Fundamentos de IA & Ética",
        "icon": "🤖",
        "requires_password": True,
        "password": "lovelace",
        "pioneer": "Ada Lovelace (1815–1852)",
        "bio": "Matemática e escritora inglesa, reconhecida como a primeira programadora da história ao escrever o primeiro algoritmo para a Máquina Analítica de Babbage."
    },
    "modulo2": {
        "title": "Módulo 2: Gerenciamento de Objetos do Excel",
        "icon": "📊",
        "requires_password": True,
        "password": "babbage",
        "pioneer": "Charles Babbage (1791–1871)",
        "bio": "Polímata britânico considerado o 'pai do computador mecânico'. Idealizou a Máquina Diferencial e a Máquina Analítica, precursoras da arquitetura dos computadores."
    },
    "modulo3": {
        "title": "Módulo 3: Fórmulas e Funções no Excel",
        "icon": "➗",
        "requires_password": True,
        "password": "turing",
        "pioneer": "Alan Turing (1912–1954)",
        "bio": "Pai da ciência da computação e da Inteligência Artificial. Decifrou os códigos Enigma na Segunda Guerra e formulou a Máquina de Turing e o Teste de Turing."
    },
    "modulo4": {
        "title": "Módulo 4: Formatação Condicional",
        "icon": "🎨",
        "requires_password": True,
        "password": "boole",
        "pioneer": "George Boole (1815–1864)",
        "bio": "Matemático e filósofo criador da álgebra booleana, estrutura lógica baseada em Verdadeiro/Falso essencial para decisões e condicionais nos sistemas computacionais."
    },
    "modulo5": {
        "title": "Módulo 5: Gráficos e Análise de Dados",
        "icon": "📈",
        "requires_password": True,
        "password": "hopper",
        "pioneer": "Grace Hopper (1906–1992)",
        "bio": "Cientista da computação e almirante da Marinha dos EUA. Pioneira na criação do primeiro compilador, linguagem COBOL e criadora do termo 'bug' e 'debugging'."
    }
}

def init_auth():
    """Inicializa as variáveis de controle de sessão no Streamlit."""
    if "unlocked_modules" not in st.session_state:
        st.session_state.unlocked_modules = {
            "home": True,
            "biblioteca": True,
            "modulo1": False,
            "modulo2": False,
            "modulo3": False,
            "modulo4": False,
            "modulo5": False
        }
    if "active_page" not in st.session_state:
        st.session_state.active_page = "home"

def is_unlocked(module_key: str) -> bool:
    """Verifica se um módulo específico já está desbloqueado."""
    init_auth()
    return st.session_state.unlocked_modules.get(module_key, False)

def unlock_module(module_key: str):
    """Marca um módulo como desbloqueado na sessão."""
    init_auth()
    if module_key in st.session_state.unlocked_modules:
        st.session_state.unlocked_modules[module_key] = True

def verify_password(module_key: str, password_attempt: str) -> bool:
    """Valida a senha informada, normalizando texto (sem distinção de maiúsculas)."""
    if module_key not in MODULES_INFO:
        return False
    
    expected = MODULES_INFO[module_key]["password"]
    if not expected:
        return True
    
    clean_attempt = password_attempt.strip().lower()
    clean_expected = expected.strip().lower()
    
    # Suporte a digitação do nome completo ou sobrenome
    if clean_attempt == clean_expected or clean_expected in clean_attempt:
        unlock_module(module_key)
        return True
    return False

def get_progress():
    """Retorna o progresso de desbloqueio dos 5 módulos com senha."""
    init_auth()
    core_modules = ["modulo1", "modulo2", "modulo3", "modulo4", "modulo5"]
    unlocked_count = sum(1 for m in core_modules if st.session_state.unlocked_modules.get(m, False))
    total_count = len(core_modules)
    percentage = int((unlocked_count / total_count) * 100)
    return unlocked_count, total_count, percentage
