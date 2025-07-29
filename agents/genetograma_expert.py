"""
Agente Especialista em Genetograma
Especializado em orientar a criação e análise de genetogramas familiares
"""

from crewai import Agent, Task, Crew
from typing import Dict, Any, List
import os
from config import Config
from knowledge.genetograma_guide import GENETOGRAMA_GUIDE, get_etapa_genetograma, TRIANGULACOES_COMUNS
from knowledge.carter_mcgoldrick import (
    CONCEITOS_FUNDAMENTAIS,
    identificar_triangulacoes_ativas,
    analisar_padroes_multigeracionais
)

class GenetogramaExpert:
    def __init__(self):
        self.llm = Config.get_llm()
        
        self.agent = Agent(
            role="Especialista em Genetograma e Mapeamento Familiar",
            goal="""Orientar usuários na criação de genetogramas emocionalmente significativos, 
                    ajudando-os a mapear padrões familiares multigeracionais de acordo com a 
                    metodologia de Carter & McGoldrick.""",
            backstory="""Você é um especialista altamente qualificado em genetogramas familiares
                        com profundo conhecimento da teoria sistêmica de Carter & McGoldrick.
                        
                        Sua expertise especializada inclui:
                        
                        TÉCNICA DE GENETOGRAMA:
                        - Domínio completo de símbolos, convenções e notações padronizadas
                        - Capacidade de mapear 3-4 gerações com precisão e clareza
                        - Técnicas para coleta de informações familiares sensíveis
                        - Métodos para revelar padrões ocultos através do mapeamento visual
                        - Adaptação de técnicas para diferentes culturas e contextos
                        
                        ANÁLISE DE PADRÕES MULTIGERACIONAIS:
                        - Identificação de padrões repetitivos através das gerações
                        - Reconhecimento de temas familiares não resolvidos
                        - Análise de transmissão de traumas e recursos através do tempo
                        - Identificação de missões familiares e lealdades invisíveis
                        - Compreensão de como eventos históicos impactam gerações futuras
                        
                        TRIANGULAÇÕES COMPLEXAS:
                        - Identificação de triangulações que cruzam fronteiras geracionais
                        - Análise de alianças secretas e coalizões rígidas
                        - Reconhecimento de padrões de triangulação múltipla
                        - Compreensão de como segredos familiares criam triangulações
                        - Estratégias para mapear visualmente relacionamentos triangulados
                        
                        INTERPRETAÇÃO SISTÊMICA:
                        - Conexão de padrões visuais com teoria do ciclo de vida familiar
                        - Análise de como estrutura familiar impacta funcionamento atual
                        - Identificação de recursos familiares ocultos ou subutilizados
                        - Compreensão de como mudanças em uma parte afetam todo o sistema
                        - Integração de perspectivas individuais e sistêmicas no genetograma
                        
                        ABORDAGEM COLABORATIVA:
                        - Engajamento respeitoso na coleta de informações familiares
                        - Sensibilidade a questões de privacidade e confidencialidade
                        - Capacidade de facilitar descobertas sem ser invasivo
                        - Apoio emocional durante revelações difíceis
                        - Empoderamento da família através da compreensão de sua própria história
                        
                        Você conduz o processo de genetograma como uma exploração colaborativa,
                        ajudando famílias a descobrirem sua própria sabedoria através da 
                        visualização de seus padrões únicos.""",
            tools=[],
            llm=self.llm,
            verbose=Config.VERBOSE,
            memory=Config.ENABLE_MEMORY,
            allow_delegation=False
        )
    
    def iniciar_genetograma(self, contexto_familiar: str = None) -> Dict[str, Any]:
        """Inicia o processo de criação do genetograma"""
        
        etapa_1 = get_etapa_genetograma(1)
        
        prompt = f"""
        Você está ajudando alguém a começar seu genetograma - um mapa emocional da família.
        
        Contexto familiar mencionado: {contexto_familiar or 'Primeira vez criando genetograma'}
        
        Use o quebra-gelo especial: "Se você pudesse desenhar sua família como um mapa emocional, 
        o que seria impossível deixar de fora?"
        
        Depois explique de forma acolhedora:
        1. O que é um genetograma e por que é útil
        2. Que vamos começar com a estrutura básica (você no centro)
        3. Como os símbolos funcionam (quadrado=homem, círculo=mulher)
        4. Que o foco é no impacto emocional, não só cronologia
        
        Seja encorajador - muitas pessoas ficam intimidadas no início. Explique que 
        vamos construir juntos, passo a passo, e que não precisa ser perfeito.
        
        Termine perguntando por onde eles gostariam de começar: com eles mesmos no centro,
        ou se já têm em mente alguém da família que foi muito marcante.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "etapa_atual": 1,
            "proximos_passos": [
                "Posicionar usuário no centro do genetograma",
                "Adicionar pais acima",
                "Incluir irmãos se houver",
                "Definir símbolos básicos"
            ],
            "agente": "genetograma_expert"
        }
    
    def orientar_etapa(self, etapa_numero: int, contexto_atual: str = None) -> Dict[str, Any]:
        """Orienta uma etapa específica do genetograma"""
        
        etapa_info = get_etapa_genetograma(etapa_numero)
        
        if not etapa_info:
            return {"erro": "Etapa não encontrada"}
        
        prompt = f"""
        Você está orientando a Etapa {etapa_numero}: {etapa_info.get('titulo', '')}
        
        Contexto atual: {contexto_atual or 'Continuando o genetograma'}
        
        Informações da etapa: {etapa_info}
        
        Instruções:
        1. Explique o objetivo desta etapa de forma clara e motivadora
        2. Dê as orientações práticas de forma didática mas não mecânica
        3. Use exemplos quando ajudar na compreensão
        4. Sempre conecte com o aspecto emocional - por que isso importa?
        5. Termine com uma pergunta que ajude a pessoa a começar esta etapa
        
        Lembre-se: estamos mapeando emoções, não apenas fazendo um organograma familiar.
        Seja empático sobre como pode ser difícil ou emocionante explorar certas memórias.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "etapa_atual": etapa_numero,
            "titulo_etapa": etapa_info.get('titulo', ''),
            "agente": "genetograma_expert"
        }
    
    def analisar_padroes(self, informacoes_genetograma: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa o genetograma para identificar padrões familiares"""
        
        prompt = f"""
        Analise estas informações do genetograma familiar:
        
        {informacoes_genetograma}
        
        Como especialista em padrões familiares, identifique:
        
        1. PADRÕES REPETITIVOS:
        - Há papéis que se repetem entre gerações?
        - Padrões de relacionamento similares?
        - Profissões, problemas ou características recorrentes?
        
        2. TRIANGULAÇÕES:
        - Há sinais de triangulações familiares?
        - Alguém sempre no meio de conflitos?
        - Alianças que excluem terceiros?
        
        3. EIXOS VERTICAIS E HORIZONTAIS:
        - Que heranças emocionais você identifica?
        - Há crises atuais conectadas ao passado familiar?
        
        4. RECURSOS E FORÇAS:
        - Que recursos familiares estão disponíveis?
        - Há padrões positivos para serem fortalecidos?
        
        Apresente suas observações de forma cuidadosa e construtiva, sempre 
        perguntando se a pessoa reconhece esses padrões em sua experiência.
        """
        
        resposta = self._executar_task(prompt)
        
        # Identificar triangulações específicas
        triangulacoes_detectadas = self._identificar_triangulacoes(informacoes_genetograma)
        
        return {
            "resposta": resposta,
            "triangulacoes_detectadas": triangulacoes_detectadas,
            "agente": "genetograma_expert",
            "tipo": "analise_padroes"
        }
    
    def _identificar_triangulacoes(self, info_genetograma: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica possíveis triangulações no genetograma"""
        
        triangulacoes = []
        
        # Lógica simplificada - em implementação real seria mais sofisticada
        relacionamentos = info_genetograma.get("relacionamentos", [])
        
        for tipo, triangulacao in TRIANGULACOES_COMUNS.items():
            # Aqui você implementaria lógica para detectar padrões específicos
            # baseado nos relacionamentos descritos
            pass
        
        return triangulacoes
    
    def orientar_reflexao_final(self, genetograma_completo: Dict[str, Any]) -> Dict[str, Any]:
        """Orienta a reflexão final sobre o genetograma completado"""
        
        etapa_6 = get_etapa_genetograma(6)
        
        prompt = f"""
        O genetograma está praticamente pronto! Agora é hora da reflexão mais profunda.
        
        Genetograma criado: {genetograma_completo}
        
        Perguntas reflexivas da Etapa 6:
        {etapa_6.get('perguntas_reflexivas', [])}
        
        Como especialista, conduza uma reflexão empática e profunda:
        
        1. Reconheça o trabalho corajoso que a pessoa fez ao mapear sua família
        2. Faça as perguntas reflexivas de forma gentil e espaçada
        3. Dê tempo para que a pessoa processe suas descobertas
        4. Destaque insights positivos e recursos identificados
        5. Seja sensível a emoções que podem surgir
        
        O objetivo é que a pessoa saia com:
        - Maior compreensão sobre padrões familiares
        - Clareza sobre o que quer manter ou mudar
        - Senso de agência sobre sua própria história
        
        Termine perguntando qual foi a descoberta mais significativa para ela.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "etapa_atual": 6,
            "tipo": "reflexao_final",
            "agente": "genetograma_expert"
        }
    
    
    def _executar_task(self, prompt: str) -> str:
        """Executa uma task com o agente"""
        task = Task(
            description=prompt,
            agent=self.agent,
            expected_output="Resposta especializada em formato de texto"
        )
        
        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=False
        )
        
        result = crew.kickoff()
        return str(result)

    def responder_duvida(self, duvida: str, contexto_etapa: int = None) -> Dict[str, Any]:
        """Responde dúvidas específicas sobre o genetograma"""
        
        prompt = f"""
        Dúvida sobre genetograma: {duvida}
        Etapa atual: {contexto_etapa or 'Não especificada'}
        
        Como especialista em genetogramas, responda de forma:
        1. Clara e prática
        2. Conectada ao propósito emocional do genetograma
        3. Encorajadora se a pessoa estiver hesitante
        4. Com exemplos concretos quando útil
        
        Se for uma dúvida técnica (símbolos, estrutura), seja didático.
        Se for dúvida emocional (como lidar com memórias difíceis), seja empático.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "agente": "genetograma_expert",
            "tipo": "esclarecimento"
        }
    
    def get_agent(self):
        """Retorna o agente CrewAI para uso no orquestrador"""
        return self.agent
