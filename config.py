"""
Configuração centralizada para o MVP de Terapia Familiar
"""

import os
from crewai import LLM
import logging

# Tentar carregar .env para desenvolvimento local
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv não disponível - isso é normal no Streamlit Cloud
    pass

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    """Classe de configuração centralizada"""
    
    # API Keys
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-fake-key-for-crewai-validation-only")
    
    # Configurações do LLM
    MODEL = os.getenv("MODEL", "gemini/gemini-1.5-flash")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "2048"))
    
    # Configurações da aplicação
    APP_TITLE = os.getenv("APP_TITLE", "Terapia Familiar MVP")
    APP_DESCRIPTION = os.getenv("APP_DESCRIPTION", "Sistema de apoio emocional baseado em Carter & McGoldrick")
    
    # Configurações de Memória CrewAI
    ENABLE_MEMORY = os.getenv("ENABLE_MEMORY", "false").lower() == "true"  # Desabilitado temporariamente
    MEMORY_PROVIDER = os.getenv("MEMORY_PROVIDER", "local")
    MEMORY_DIR = os.getenv("MEMORY_DIR", "./crew_memory")
    
    # Para Cloud Run
    PORT = int(os.getenv("PORT", 8080))
    
    # Configurações de Debug
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    VERBOSE = os.getenv("VERBOSE", "true").lower() == "true"
    
    @classmethod
    def get_llm(cls, temperature: float = None) -> LLM:
        """Retorna uma instância configurada do LLM usando CrewAI"""
        
        # Configurar variáveis de ambiente necessárias
        os.environ["GEMINI_API_KEY"] = cls.GEMINI_API_KEY
        os.environ["OPENAI_API_KEY"] = cls.OPENAI_API_KEY
        
        llm = LLM(
            model=cls.MODEL,
            temperature=temperature or cls.LLM_TEMPERATURE,
        )
        
        logger.info(f"✅ LLM configurado: {cls.MODEL}")
        return llm
    
    @classmethod
    def validate_config(cls):
        """Valida se todas as configurações necessárias estão presentes"""
        
        if not cls.GEMINI_API_KEY:
            # Mensagem mais informativa para deployment
            error_msg = """
❌ GEMINI_API_KEY não configurada!

Para configurar no Streamlit Cloud:
1. Vá para https://share.streamlit.io
2. Clique em 'Settings' do seu app
3. Na aba 'Secrets', adicione:
   GEMINI_API_KEY = "sua_chave_aqui"

Para desenvolvimento local:
1. Crie um arquivo .env
2. Adicione: GEMINI_API_KEY=sua_chave_aqui
            """
            raise ValueError(error_msg.strip())
        
        logger.info("✅ Configuração validada com sucesso")
        logger.info(f"📱 Modelo: {cls.MODEL}")
        logger.info(f"🌡️ Temperature: {cls.LLM_TEMPERATURE}")
        logger.info(f"🧠 Memória: {cls.ENABLE_MEMORY}")
        logger.info(f"🔍 Debug: {cls.DEBUG}")
        
        return True
