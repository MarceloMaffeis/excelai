"""
Conector Unificado de Inteligência Artificial para o Portal Educacional.
Suporta:
- Google AI Studio (Gemini API)
- Palantir Foundry / Azure OpenAI / OpenAI compatível
- Ollama (LLM Local em http://localhost:11434)
- Simulador Pedagógico Offline (Garante 100% de disponibilidade mesmo sem internet/chaves)
"""

import json
import requests
import streamlit as st

def get_secret(key_name: str, default: str = "") -> str:
    """Tenta obter chave do st.secrets com fallback seguro."""
    try:
        return st.secrets.get(key_name, default)
    except Exception:
        return default

def simulate_offline_response(prompt: str, system_context: str = "") -> str:
    """
    Gera uma resposta pedagógica heurística caso não haja conexão com IA externa.
    Garante que o aluno sempre receba feedback didático no estilo SENAI.
    """
    lower = prompt.lower()
    
    if "soma" in lower or "total" in lower:
        return (
            "### 🎓 Tutor Educacional (Modo Simulado SENAI)\n\n"
            "**Solução Recomendada no Excel:**\n"
            "Para somar valores no Excel, utilize a função nativa `=SOMA(intervalo)`.\n\n"
            "**Exemplo de Fórmula:**\n"
            "```excel\n=SOMA(B2:B20)\n```\n\n"
            "**💡 Sugestão de Engenharia de Prompt:**\n"
            "> *'Atue como especialista em Excel. Crie uma fórmula de SOMA que considere apenas a coluna B da linha 2 até a linha 20 e me explique passo a passo.'*\n\n"
            "**🛡️ Auditoria Humana (Atenção a Detalhes & LGPD):**\n"
            "- Verifique se as células contêm números reais ou texto formatado como número.\n"
            "- **Jamais** compartilhe valores salariais ou CPF de pessoas reais no prompt."
        )
    elif "média" in lower or "media" in lower:
        return (
            "### 🎓 Tutor Educacional (Modo Simulado SENAI)\n\n"
            "**Solução Recomendada no Excel:**\n"
            "A função `=MÉDIA(intervalo)` calcula a média aritmética dos valores numéricos desconsiderando células vazias.\n\n"
            "**Exemplo de Fórmula:**\n"
            "```excel\n=MÉDIA(C2:C50)\n```\n\n"
            "**💡 Sugestão de Engenharia de Prompt:**\n"
            "> *'Qual é a sintaxe da função MÉDIA no Excel em português e como tratar possíveis divisões por zero se o intervalo estiver vazio?'*\n\n"
            "**🛡️ Auditoria Humana:**\n"
            "- Se uma célula tiver o número 0, ele entra na média! Se estiver vazia, é ignorada. Fique atento a essa diferença lógica."
        )
    elif "se" in lower or "condição" in lower or "condicional" in lower:
        return (
            "### 🎓 Tutor Educacional (Modo Simulado SENAI)\n\n"
            "**Solução Recomendada no Excel:**\n"
            "A função lógica `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)` permite tomar decisões automáticas na planilha.\n\n"
            "**Exemplo Prático (Aprovado/Reprovado):**\n"
            "```excel\n=SE(D2>=7; \"Aprovado\"; \"Recuperação\")\n```\n\n"
            "**💡 Sugestão de Engenharia de Prompt:**\n"
            "> *'Construa uma fórmula SE no Excel para validar se um vendedor atingiu a meta de R$ 10.000, retornando \"Bônus 5%\" ou \"Sem bônus\".'*\n\n"
            "**🛡️ Atenção a Detalhes (Anti-Alucinação):**\n"
            "- No Excel em Português (Brasil), o separador de argumentos é ponto e vírgula (`;`), e não vírgula (`,`). A IA frequentemente alucina a sintaxe em inglês!"
        )
    elif "cont.se" in lower or "contar" in lower:
        return (
            "### 🎓 Tutor Educacional (Modo Simulado SENAI)\n\n"
            "**Solução Recomendada no Excel:**\n"
            "A função `=CONT.SE(intervalo; critérios)` conta a quantidade de células que atendem a uma condição específica.\n\n"
            "**Exemplo:**\n"
            "```excel\n=CONT.SE(E2:E100; \">1000\")\n```\n\n"
            "**💡 Sugestão de Prompt:**\n"
            "> *'Como usar o CONT.SE para contar quantos clientes são de \"São Paulo\" em uma tabela com 500 linhas?'*\n\n"
            "**🛡️ Auditoria Humana:**\n"
            "- Lembre-se de colocar critérios com operadores textuais entre aspas duplas, como `\">=10\"`."
        )
    elif "gráfico" in lower or "grafico" in lower or "dashboard" in lower:
        return (
            "### 🎓 Tutor Educacional (Modo Simulado SENAI)\n\n"
            "**Recomendação de Visualização:**\n"
            "- **Colunas/Barras:** Ideal para comparar categorias (ex: vendas por região).\n"
            "- **Linhas:** Ideal para evolução temporal contínua (ex: faturamento mensal ao longo do ano).\n"
            "- **Pizza:** Utilize apenas para partes de um todo (máximo de 5 a 6 fatias).\n"
            "- **Dispersão XY:** Para correlação entre duas variáveis quantitativas.\n\n"
            "**💡 Prompt Recomendado:**\n"
            "> *'Tenho dados de vendas por produto em 12 meses. Qual é o melhor tipo de gráfico no Excel e como formatar os eixos para clareza visual?'*\n\n"
            "**🛡️ Auditoria Humana:**\n"
            "- Menos é mais: remova linhas de grade desnecessárias e use títulos autoexplicativos."
        )
    elif "ética" in lower or "lgpd" in lower or "privacidade" in lower:
        return (
            "### 🎓 Tutor Educacional: Ética & LGPD no uso de IA\n\n"
            "**Diretrizes Fundamentais do SENAI:**\n"
            "1. **Anonimização Prévia:** Nunca envie dados com CPF, nomes completos de clientes, salários ou informações sigilosas da empresa para ferramentas de IA públicas.\n"
            "2. **Estrutura vs Conteúdo:** Envie apenas o cabeçalho e a lógica da tabela (ex: *Coluna A: Data, Coluna B: Valor*), nunca a base de clientes real.\n"
            "3. **Responsabilidade Humana:** A IA é apenas assistente. A assinatura e responsabilidade técnica pelo relatório são sempre suas!"
        )
    else:
        return (
            f"### 🎓 Tutor Educacional SENAI (Resposta Pedagógica)\n\n"
            f"Você consultou sobre: **'{prompt}'**.\n\n"
            "**Recomendações Práticas:**\n"
            "1. **Estruturação:** Certifique-se de que seus dados no Excel estão em formato de Tabela (`Ctrl + Alt + T`).\n"
            "2. **Engenharia de Prompt:** Ao formular sua dúvida para a IA, indique: seu objetivo, o formato da planilha (colunas e tipos) e o resultado desejado.\n"
            "3. **Auditoria Humana:** Sempre teste a fórmula ou sugestão em 2 ou 3 linhas conhecidas antes de aplicar em toda a planilha.\n\n"
            "*Dica: Configure uma chave de API na barra lateral para habilitar respostas em tempo real com modelos generativos online.*"
        )

def call_gemini(prompt: str, api_key: str, system_instruction: str = "") -> str:
    """Chama a API do Google AI Studio (Gemini Flash)."""
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    if system_instruction:
        payload["systemInstruction"] = {
            "parts": [{"text": system_instruction}]
        }
        
    headers = {"Content-Type": "application/json"}
    response = requests.post(endpoint, headers=headers, json=payload, timeout=20)
    
    if response.status_code == 200:
        data = response.json()
        candidates = data.get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "")
        return "Não foi possível extrair a resposta do modelo Gemini."
    else:
        raise Exception(f"Erro na API Gemini ({response.status_code}): {response.text}")

def call_foundry_openai(prompt: str, endpoint: str, api_key: str, model: str, system_instruction: str = "") -> str:
    """Chama endpoints compatíveis com OpenAI / Palantir Foundry LLM."""
    url = endpoint.rstrip("/")
    if not url.endswith("/chat/completions"):
        url += "/chat/completions"
        
    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model or "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.4
    }
    
    response = requests.post(url, headers=headers, json=payload, timeout=25)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Erro na API Foundry/OpenAI ({response.status_code}): {response.text}")

def call_ollama_local(prompt: str, model: str = "llama3", system_instruction: str = "") -> str:
    """Chama instância local do Ollama em http://localhost:11434."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model or "llama3",
        "prompt": prompt,
        "system": system_instruction,
        "stream": False
    }
    response = requests.post(url, json=payload, timeout=30)
    if response.status_code == 200:
        data = response.json()
        return data.get("response", "")
    else:
        raise Exception(f"Erro no Ollama Local ({response.status_code}): {response.text}")

def generate_ai_response(
    prompt: str,
    provider: str = "Auto / Simulador Inteligente",
    custom_gemini_key: str = "",
    custom_foundry_key: str = "",
    custom_foundry_endpoint: str = "",
    custom_foundry_model: str = "",
    custom_ollama_model: str = "llama3"
) -> str:
    """
    Roteador inteligente de requisições de IA.
    Prioriza o provedor selecionado com fallback elegante para o simulador se houver erro.
    """
    system_prompt = (
        "Você é o Tutor Virtual do curso 'Excel Básico com IA Generativa' do SENAI-SP. "
        "Sua missão é explicar conceitos de Excel básico, sugerir fórmulas corretas em Português "
        "(lembrando que no Brasil usamos ponto e vírgula ';' como separador), ensinar engenharia de prompt "
        "e reforçar sempre a responsabilidade humana, auditoria contra alucinações e respeito à privacidade (LGPD)."
    )
    
    # 1. Google AI Studio
    if provider == "Google AI Studio (Gemini)":
        key = custom_gemini_key or get_secret("GEMINI_API_KEY")
        if not key:
            return "⚠️ **Chave da API Gemini não informada.** Adicione sua chave na barra lateral ou selecione o modo 'Simulador Inteligente'."
        try:
            return call_gemini(prompt, key, system_prompt)
        except Exception as e:
            return f"❌ **Erro na comunicação com o Gemini:** {str(e)}\n\n" + simulate_offline_response(prompt)
            
    # 2. Palantir Foundry / OpenAI
    elif provider == "Palantir Foundry / OpenAI":
        key = custom_foundry_key or get_secret("FOUNDRY_API_KEY")
        endpoint = custom_foundry_endpoint or get_secret("FOUNDRY_ENDPOINT")
        model = custom_foundry_model or get_secret("FOUNDRY_MODEL", "gpt-4o-mini")
        if not key or not endpoint:
            return "⚠️ **Endpoint ou Chave do Foundry/OpenAI ausentes.** Configure na barra lateral."
        try:
            return call_foundry_openai(prompt, endpoint, key, model, system_prompt)
        except Exception as e:
            return f"❌ **Erro na comunicação com Foundry/OpenAI:** {str(e)}\n\n" + simulate_offline_response(prompt)
            
    # 3. Ollama Local
    elif provider == "Ollama Local (http://localhost:11434)":
        try:
            return call_ollama_local(prompt, custom_ollama_model, system_prompt)
        except Exception as e:
            return f"⚠️ **Não foi possível conectar ao Ollama local:** Certifique-se de que o executável do Ollama está rodando na sua máquina.\n\n" + simulate_offline_response(prompt)
            
    # 4. Modo Simulador Inteligente / Offline
    else:
        # Se houver chave Gemini no secrets, tenta chamar, senão usa simulador
        key = get_secret("GEMINI_API_KEY")
        if key:
            try:
                return call_gemini(prompt, key, system_prompt)
            except Exception:
                pass
        return simulate_offline_response(prompt, system_prompt)
