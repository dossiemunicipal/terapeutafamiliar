"""
Interface Web para o MVP de Terapia Familiar
"""

import streamlit as st
import os
from config import Config

# Validar configuração na inicialização apenas uma vez
if 'config_validated' not in st.session_state:
    try:
        Config.validate_config()
        st.session_state.config_validated = True
    except Exception as e:
        st.error(f"Erro na configuração: {e}")
        st.stop()

# Configuração da página
st.set_page_config(
    page_title="Terapia Familiar MVP",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado simplificado
st.markdown("""
<style>
    .stAppDeployButton { display: none; }
    
    .main-header {
        color: #2E7D9A;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid #2E7D9A;
        margin-bottom: 1rem;
    }
    
    .user-message {
        background-color: #DCF8C6;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 1rem;
        text-align: left;
    }
    
    .agent-response {
        background-color: #F1F1F1;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 1rem;
        text-align: left;
    }
    
    .agent-badge {
        background-color: #2E7D9A;
        color: white;
        padding: 0.25rem 0.5rem;
        border-radius: 0.5rem;
        font-size: 0.8rem;
        font-weight: bold;
    }
    
    /* Estilização melhorada dos botões */
    .stButton > button {
        border-radius: 0.5rem;
        font-weight: bold;
        height: 3rem;
    }
    
    /* Estilização do textarea */
    .stTextArea > div > div > textarea {
        border-radius: 0.5rem;
        border: 2px solid #E0E0E0;
        min-height: 80px !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #2E7D9A;
        box-shadow: 0 0 0 2px rgba(46, 125, 154, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Inicializa o estado da sessão"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'session_started' not in st.session_state:
        st.session_state.session_started = False
    
    if 'orchestrator' not in st.session_state:
        try:
            from crew_orchestrator import TerapiaCrewOrchestrator
            with st.spinner("Inicializando sistema..."):
                st.session_state.orchestrator = TerapiaCrewOrchestrator()
        except Exception as e:
            st.error(f"Erro ao inicializar o sistema: {e}")
            st.stop()

def display_message(message, is_user=True):
    """Exibe uma mensagem na interface com layout de chat"""
    if is_user:
        st.markdown(f"""
        <div class="user-message">
            <strong>Você</strong><br>
            {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        agent_name = message.get('agente', 'Sistema')
        response = message.get('resposta', 'Sem resposta')
        
        # Se a resposta é um dicionário, extrair o conteúdo relevante
        if isinstance(response, dict):
            response = response.get('resposta', response.get('avaliacao_inicial', str(response)))
        
        st.markdown(f"""
        <div class="agent-response">
            <span class="agent-badge">{agent_name}</span><br>
            {response}
        </div>
        """, unsafe_allow_html=True)

def main():
    """Função principal da aplicação"""
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Terapia Familiar MVP</h1>
        <p>Sistema de apoio emocional baseado na teoria de Carter & McGoldrick</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-content">
            <h3>🤝 Equipe Terapêutica CrewAI</h3>
            <p><strong>🔥 NOVO:</strong> Todos os agentes trabalham juntos!</p>
            <hr>
            <p><strong>👨‍⚕️ Terapeuta Principal:</strong> Conduz e coordena a sessão</p>
            <p><strong>🌳 Genetograma:</strong> Mapeia padrões familiares</p>
            <p><strong>🔄 Ciclo de Vida:</strong> Analisa estágios familiares</p>
            <p><strong>🔍 Padrões:</strong> Identifica repetições</p>
            <p><strong>💭 Reflexão:</strong> Facilita insights</p>
            <br>
            <p style="background-color: #E8F4FD; padding: 0.5rem; border-radius: 0.5rem; font-size: 0.8rem;">
                <strong>💡 Como funciona:</strong><br>
                Toda mensagem é processada pela equipe completa usando CrewAI, 
                com cada especialista contribuindo quando relevante.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Informações da API
        st.markdown("---")
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key and len(api_key) > 10:
            st.success("✅ Gemini API configurada")
        else:
            st.error("❌ Configure GEMINI_API_KEY no arquivo .env")
    
    # Área principal
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Mostrar mensagens se existirem
        if st.session_state.session_started and st.session_state.messages:
            # Mostrar mensagens em ordem cronológica
            for i, message in enumerate(st.session_state.messages):
                display_message(message['user'], is_user=True)
                display_message(message['agent_response'], is_user=False)
        else:
            # Mensagem de boas-vindas quando não há sessão ativa
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #666;">
                <h3>🧠 Bem-vindo ao Sistema de Terapia Familiar</h3>
                <p>Comece sua conversa digitando sua mensagem abaixo.</p>
                <p>Nossa equipe terapêutica especializada está pronta para ajudar.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Campo de entrada sempre visível na parte inferior
        if st.session_state.session_started:
            # Sessão já iniciada - campo para continuar conversa
            nova_mensagem = st.text_area(
                "Nova Mensagem",
                placeholder="Digite sua mensagem aqui... A equipe completa irá processar e responder.",
                height=80,
                key="nova_mensagem",
                label_visibility="collapsed"
            )
            
            col_send, col_clear, col_space = st.columns([1, 1, 2])
            with col_send:
                enviar_mensagem = st.button("📤 Enviar", use_container_width=True, type="primary")
            with col_clear:
                if st.button("🗑️ Nova Conversa", use_container_width=True):
                    st.session_state.orchestrator.limpar_sessao()
                    st.session_state.messages = []
                    st.session_state.session_started = False
                    st.rerun()
            
        else:
            # Primeira sessão - campo para iniciar
            contexto_inicial = st.text_area(
                "Contexto inicial",
                placeholder="Conte um pouco sobre o que está acontecendo com você ou sua família...",
                height=80,
                key="contexto_inicial",
                label_visibility="collapsed"
            )
            
            col_start, col_space = st.columns([1, 3])
            with col_start:
                if st.button("🎯 Iniciar Sessão", use_container_width=True, type="primary"):
                    if contexto_inicial.strip():
                        with st.spinner("Iniciando sua sessão..."):
                            resultado = st.session_state.orchestrator.iniciar_sessao(contexto_inicial)
                        
                        if resultado['success']:
                            st.session_state.messages.append({
                                'user': contexto_inicial,
                                'agent_response': resultado
                            })
                            st.session_state.session_started = True
                            st.rerun()
                        else:
                            st.error(f"Erro: {resultado['error']}")
                    else:
                        st.warning("Por favor, conte um pouco sobre sua situação antes de iniciar.")
        
        # Processar envio de mensagem (se aplicável)
        if st.session_state.session_started and 'enviar_mensagem' in locals() and enviar_mensagem:
            if nova_mensagem and nova_mensagem.strip():
                with st.spinner("🤝 Equipe processando sua mensagem..."):
                    resultado = st.session_state.orchestrator.processar_mensagem(nova_mensagem)
                
                if resultado['success']:
                    st.session_state.messages.append({
                        'user': nova_mensagem,
                        'agent_response': resultado
                    })
                    st.rerun()
                else:
                    st.error(f"Erro: {resultado['error']}")
            else:
                st.warning("Digite uma mensagem antes de enviar.")
    
    with col2:
        st.markdown("### 📊 Status da Sessão")
        
        if st.session_state.session_started:
            num_mensagens = len(st.session_state.messages)
            st.metric("Mensagens trocadas", num_mensagens)
        
        # Informações sobre a equipe
        st.markdown("### ℹ️ Sobre a Equipe Terapêutica")
        
        st.info("🤝 **Equipe Completa:** Todos os especialistas trabalham juntos usando CrewAI para oferecer uma abordagem integrada baseada na teoria de Carter & McGoldrick.")

if __name__ == "__main__":
    main()
