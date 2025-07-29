"""
Orquestrador principal do sistema de terapia MVP
"""

from agents.terapeuta_principal import TerapeutaPrincipal
from agents.genetograma_expert import GenetogramaExpert
from agents.ciclo_vida_analyzer import CicloVidaAnalyzer
from agents.padrao_analyzer import PadraoAnalyzer
from agents.reflexao_facilitator import ReflexaoFacilitator
from typing import Dict, Any, List
from config import Config

# Validar configuração na inicialização
Config.validate_config()

class TerapiaOrchestrator:
    def __init__(self):
        # Inicializar agentes
        self.terapeuta = TerapeutaPrincipal()
        self.genetograma_expert = GenetogramaExpert()
        self.ciclo_vida_analyzer = CicloVidaAnalyzer()
        self.padrao_analyzer = PadraoAnalyzer()
        self.reflexao_facilitator = ReflexaoFacilitator()
        
        # Estado da sessão
        self.session_state = {
            "historico": [],
            "contexto_familia": "",
            "estagio_identificado": None,
            "padroes_identificados": [],
            "genetograma_ativo": False
        }
    
    def iniciar_sessao(self, contexto_inicial: str = None) -> Dict[str, Any]:
        """Inicia uma nova sessão terapêutica"""
        try:
            resposta = self.terapeuta.iniciar_sessao(contexto_inicial)
            
            # Adicionar ao histórico
            self.session_state["historico"].append({
                "tipo": "inicio_sessao",
                "agente": "terapeuta_principal",
                "contexto": contexto_inicial,
                "resposta": resposta["resposta"]
            })
            
            return {
                "success": True,
                "agente": "Terapeuta Principal",
                "resposta": resposta["resposta"],
                "quebra_gelo": resposta.get("quebra_gelo", {}),
                "session_id": len(self.session_state["historico"])
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao iniciar sessão: {str(e)}",
                "agente": "Sistema"
            }
    
    def processar_mensagem(self, mensagem: str, agente_preferido: str = "terapeuta") -> Dict[str, Any]:
        """Processa uma mensagem do usuário"""
        try:
            agente_map = {
                "terapeuta": self.terapeuta,
                "genetograma": self.genetograma_expert,
                "ciclo_vida": self.ciclo_vida_analyzer,
                "padroes": self.padrao_analyzer,
                "reflexao": self.reflexao_facilitator
            }
            
            if agente_preferido not in agente_map:
                agente_preferido = "terapeuta"
            
            agente = agente_map[agente_preferido]
            
            # Processar mensagem baseado no agente
            if agente_preferido == "terapeuta":
                resposta = agente.processar_mensagem(
                    mensagem, 
                    self.session_state["historico"][-3:] if self.session_state["historico"] else []
                )
            elif agente_preferido == "genetograma":
                resposta = agente.iniciar_genetograma(mensagem)
            elif agente_preferido == "ciclo_vida":
                # Extrair idade se possível (implementação simples)
                idade = self._extrair_idade(mensagem)
                resposta = agente.identificar_estagio_atual(idade, mensagem)
            elif agente_preferido == "padroes":
                resposta = agente.analisar_conversa([{"conteudo": mensagem, "tipo": "user"}])
            else:  # reflexao
                quebra_gelo_tipo = self._identificar_tipo_quebra_gelo(mensagem)
                resposta = agente.aplicar_quebra_gelo(quebra_gelo_tipo, mensagem)
            
            # Adicionar ao histórico
            self.session_state["historico"].append({
                "tipo": "mensagem_usuario",
                "conteudo": mensagem,
                "agente_resposta": agente_preferido,
                "resposta": resposta
            })
            
            return {
                "success": True,
                "agente": agente_preferido.title(),
                "resposta": resposta,
                "session_id": len(self.session_state["historico"])
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro ao processar mensagem: {str(e)}",
                "agente": "Sistema"
            }
    
    def _extrair_idade(self, texto: str) -> int:
        """Extrai idade do texto (implementação simples)"""
        import re
        # Procura por padrões como "30 anos", "tenho 25", etc.
        patterns = [
            r'(\d+)\s*anos?',
            r'tenho\s*(\d+)',
            r'idade\s*(\d+)',
            r'sou\s*(\d+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, texto.lower())
            if match:
                return int(match.group(1))
        
        return 35  # Idade padrão se não encontrar
    
    def _identificar_tipo_quebra_gelo(self, texto: str) -> str:
        """Identifica tipo de quebra-gelo baseado no contexto"""
        texto_lower = texto.lower()
        
        if any(palavra in texto_lower for palavra in ["mudou", "diferente", "novo"]):
            return "transicoes_atuais"
        elif any(palavra in texto_lower for palavra in ["família", "pais", "herança"]):
            return "padroes_familiares"
        elif any(palavra in texto_lower for palavra in ["papel", "responsabilidade", "sempre"]):
            return "papeis_familiares"
        elif any(palavra in texto_lower for palavra in ["perda", "perdeu", "saudade"]):
            return "perdas_transformacoes"
        elif any(palavra in texto_lower for palavra in ["mapa", "árvore", "genealogia"]):
            return "genetograma_intro"
        else:
            return "transicoes_atuais"
    
    def obter_historico(self) -> List[Dict]:
        """Retorna o histórico da sessão"""
        return self.session_state["historico"]
    
    def limpar_sessao(self):
        """Limpa o estado da sessão"""
        self.session_state = {
            "historico": [],
            "contexto_familia": "",
            "estagio_identificado": None,
            "padroes_identificados": [],
            "genetograma_ativo": False
        }
    
    def obter_sugestoes_agente(self, mensagem: str) -> List[str]:
        """Sugere agentes baseado na mensagem"""
        texto_lower = mensagem.lower()
        sugestoes = []
        
        if any(palavra in texto_lower for palavra in ["família", "pais", "relacionamento"]):
            sugestoes.append("terapeuta")
        
        if any(palavra in texto_lower for palavra in ["árvore", "mapa", "gerações"]):
            sugestoes.append("genetograma")
        
        if any(palavra in texto_lower for palavra in ["idade", "fase", "estágio"]):
            sugestoes.append("ciclo_vida")
        
        if any(palavra in texto_lower for palavra in ["padrão", "repete", "sempre igual"]):
            sugestoes.append("padroes")
        
        if any(palavra in texto_lower for palavra in ["refletir", "pensar", "sentir"]):
            sugestoes.append("reflexao")
        
        # Se nenhuma sugestão específica, usar terapeuta principal
        if not sugestoes:
            sugestoes.append("terapeuta")
        
        return sugestoes
