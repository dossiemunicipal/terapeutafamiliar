"""
Orquestrador CrewAI para sistema de terapia familiar
Usa todos os agentes trabalhando em conjunto como uma crew
"""

from crewai import Crew, Process
from agents.terapeuta_principal import TerapeutaPrincipal  
from agents.genetograma_expert import GenetogramaExpert
from agents.ciclo_vida_analyzer import CicloVidaAnalyzer
from agents.padrao_analyzer import PadraoAnalyzer
from agents.reflexao_facilitator import ReflexaoFacilitator
from config import Config
from typing import Dict, Any
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TerapiaCrewOrchestrator:
    """Orquestrador que usa CrewAI para coordenar todos os agentes"""
    
    def __init__(self):
        # Validar configuração
        Config.validate_config()
        
        # Instanciar todos os agentes especializados
        self.terapeuta_principal = TerapeutaPrincipal()
        self.genetograma_expert = GenetogramaExpert()
        self.ciclo_vida_analyzer = CicloVidaAnalyzer()
        self.padrao_analyzer = PadraoAnalyzer()
        self.reflexao_facilitator = ReflexaoFacilitator()
        
        # Estado da sessão
        self.session_state = {
            "historico": [],
            "contexto_familia": "",
            "insights_coletivos": [],
            "sessao_ativa": False
        }
        
        logger.info("✅ TerapiaCrewOrchestrator inicializado com CrewAI")
    
    def iniciar_sessao(self, contexto_inicial: str) -> Dict[str, Any]:
        """Inicia uma sessão terapêutica com toda a crew trabalhando juntas"""
        try:
            logger.info(f"🚀 Iniciando sessão com contexto: {contexto_inicial[:100]}...")
            
            # Criar crew dinâmica para esta sessão específica
            from crewai import Task
            
            task_inicial = Task(
                description=f"""
                CONTEXTO DO CLIENTE: {contexto_inicial}
                
                INSTRUÇÕES IMPORTANTES:
                - RESPONDA APENAS com base nas informações fornecidas pelo cliente
                - NÃO invente ou assuma informações não mencionadas
                - Se o cliente apenas cumprimentou, faça um acolhimento simples e pergunte como pode ajudar
                - Se há informações específicas, trabalhe com elas
                - Mantenha respostas proporcionais ao que foi compartilhado
                
                Como equipe terapêutica, trabalhem de forma integrada:
                
                1. TERAPEUTA PRINCIPAL: Liderar com acolhimento empático apropriado ao contexto
                2. ESPECIALISTAS: Contribuir APENAS se houver informações relevantes no relato:
                   - Genetograma Expert: Só mencionar se houver informações familiares
                   - Ciclo de Vida: Só analisar se houver dados sobre estágio familiar
                   - Padrão Analyzer: Só identificar padrões se mencionados
                   - Reflexão Facilitator: Fazer perguntas apropriadas ao nível de informação compartilhada
                
                OBJETIVO: Resposta terapêutica proporcional que:
                - Acolha o cliente adequadamente
                - Não assuma informações não fornecidas
                - Seja empática mas não excessiva
                - Convide ao diálogo de forma natural
                
                IMPORTANTE: Se o cliente apenas cumprimentou, responda com acolhimento simples e convite para compartilhar.
                """,
                expected_output="Resposta terapêutica apropriada e proporcional ao contexto compartilhado"
                # Sem agent específico - o manager decidirá quem executa
            )
            
            # Criar crew específica para esta sessão
            crew_sessao = Crew(
                agents=[
                    self.terapeuta_principal.get_agent(),
                    self.genetograma_expert.get_agent(),
                    self.ciclo_vida_analyzer.get_agent(),
                    self.padrao_analyzer.get_agent(),
                    self.reflexao_facilitator.get_agent()
                ],
                tasks=[task_inicial],
                process=Process.hierarchical,
                manager_llm=Config.get_llm(),  # Usar manager_llm em vez de manager_agent
                verbose=Config.DEBUG
                # Removido memory=Config.ENABLE_MEMORY para evitar erros de embeddings
            )
            
            # Executar a crew com inputs
            resultado = crew_sessao.kickoff(inputs={"contexto": contexto_inicial})
            
            # Atualizar estado da sessão
            self.session_state["contexto_familia"] = contexto_inicial
            self.session_state["sessao_ativa"] = True
            self.session_state["historico"].append({
                "tipo": "inicio_sessao",
                "contexto": contexto_inicial,
                "resposta_crew": str(resultado)
            })
            
            logger.info("✅ Sessão iniciada com sucesso pela crew")
            
            return {
                "success": True,
                "agente": "🤝 Equipe Terapêutica Completa",
                "resposta": str(resultado),
                "tipo": "inicio_sessao",
                "emoji": "🚀"
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao iniciar sessão: {e}")
            return {
                "success": False,
                "error": f"Erro ao iniciar sessão: {str(e)}"
            }
    
    def processar_mensagem(self, mensagem: str) -> Dict[str, Any]:
        """Processa uma mensagem usando toda a crew"""
        try:
            logger.info(f"💬 Processando mensagem: {mensagem[:100]}...")
            
            from crewai import Task
            
            # Criar contexto com histórico
            contexto_historico = "\n".join([
                f"- {item['contexto']}: {item['resposta_crew'][:200]}..." 
                for item in self.session_state["historico"][-3:]  # Últimas 3 interações
            ])
            
            task_resposta = Task(
                description=f"""
                CONTEXTO DA SESSÃO: {self.session_state.get('contexto_familia', '')}
                
                HISTÓRICO RECENTE:
                {contexto_historico}
                
                NOVA MENSAGEM DO CLIENTE: {mensagem}
                
                INSTRUÇÕES IMPORTANTES:
                - RESPONDA com base apenas nas informações fornecidas pelo cliente
                - NÃO invente detalhes ou faça análises sem dados concretos
                - Mantenha a resposta proporcional à complexidade da mensagem
                - Use o histórico para manter continuidade, mas não para criar informações
                
                Como equipe terapêutica, trabalhem de forma integrada:
                
                1. TERAPEUTA PRINCIPAL: Coordenar resposta empática e contextual
                2. ESPECIALISTAS: Contribuir APENAS quando há dados relevantes:
                   - Genetograma: Só se mencionou família/relacionamentos
                   - Ciclo de Vida: Só se há informações sobre estágio familiar
                   - Padrões: Só se identificou padrões reais na mensagem
                   - Reflexão: Perguntas apropriadas ao que foi compartilhado
                
                OBJETIVO: Resposta terapêutica contextual que:
                - Demonstre escuta ativa do que foi realmente dito
                - Seja empática mas não excessiva
                - Promova diálogo natural
                - Não assuma informações não fornecidas
                
                IMPORTANTE: Se a mensagem é simples, responda de forma simples e acolhedora.
                """,
                expected_output="Resposta terapêutica contextual e apropriada"
                # Sem agent específico - o manager decidirá quem executa
            )
            
            # Criar crew específica para esta mensagem
            crew_resposta = Crew(
                agents=[
                    self.terapeuta_principal.get_agent(),
                    self.genetograma_expert.get_agent(),
                    self.ciclo_vida_analyzer.get_agent(),
                    self.padrao_analyzer.get_agent(),
                    self.reflexao_facilitator.get_agent()
                ],
                tasks=[task_resposta],
                process=Process.hierarchical,
                manager_llm=Config.get_llm(),  # Usar manager_llm em vez de manager_agent
                verbose=Config.DEBUG
                # Removido memory=Config.ENABLE_MEMORY para evitar erros de embeddings
            )
            
            # Executar crew com inputs
            resultado = crew_resposta.kickoff(inputs={"mensagem": mensagem, "historico": contexto_historico})
            
            # Atualizar histórico
            self.session_state["historico"].append({
                "tipo": "mensagem",
                "contexto": mensagem,
                "resposta_crew": str(resultado)
            })
            
            logger.info("✅ Mensagem processada pela crew")
            
            return {
                "success": True,
                "agente": "🤝 Equipe Terapêutica",
                "resposta": str(resultado),
                "tipo": "resposta",
                "emoji": "💭"
            }
            
        except Exception as e:
            logger.error(f"❌ Erro ao processar mensagem: {e}")
            return {
                "success": False,
                "error": f"Erro ao processar mensagem: {str(e)}"
            }
    
    def limpar_sessao(self):
        """Limpa o estado da sessão"""
        self.session_state = {
            "historico": [],
            "contexto_familia": "",
            "insights_coletivos": [],
            "sessao_ativa": False
        }
        logger.info("🗑️ Sessão limpa")
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna status da sessão"""
        return {
            "sessao_ativa": self.session_state["sessao_ativa"],
            "num_interacoes": len(self.session_state["historico"]),
            "contexto_definido": bool(self.session_state["contexto_familia"])
        }
