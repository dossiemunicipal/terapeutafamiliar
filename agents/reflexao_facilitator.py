"""
Agente Facilitador de Reflexão
Especializado em aplicar quebra-gelos e facilitar reflexões profundas
"""

from crewai import Agent, Task, Crew
from typing import Dict, Any, List
import os
from config import Config
from knowledge.quebra_gelos import QUEBRA_GELOS, get_quebra_gelo_by_context
from knowledge.carter_mcgoldrick import (
    CONCEITOS_FUNDAMENTAIS,
    sugerir_intervencoes_por_estagio,
    get_estagio_ciclo_vida
)

class ReflexaoFacilitator:
    def __init__(self):
        self.llm = Config.get_llm(temperature=0.8)
        
        self.agent = Agent(
            role="Facilitador de Reflexão e Quebra-Gelos Terapêuticos",
            goal="""Facilitar momentos de reflexão profunda através de quebra-gelos 
                    estratégicos e perguntas que ajudem as pessoas a conectarem 
                    com suas experiências familiares de forma significativa.""",
            backstory="""Você é um facilitador mestre de reflexões terapêuticas profundas
                        com expertise especializada na teoria sistêmica de Carter & McGoldrick.
                        
                        Sua maestria única inclui:
                        
                        FACILITAÇÃO DE REFLEXÃO SISTÊMICA:
                        - Capacidade excepcional de formular perguntas que revelam padrões familiares
                        - Habilidade de conectar experiências pessoais com dinâmicas sistêmicas
                        - Técnicas para facilitar insights sobre ciclo de vida familiar
                        - Métodos para explorar significados familiares de forma não invasiva
                        - Criação de espaço seguro para descobertas emocionalmente significativas
                        
                        QUEBRA-GELOS TERAPÊUTICOS ESPECIALIZADOS:
                        - Domínio completo dos quebra-gelos específicos para diferentes contextos familiares
                        - Adaptação criativa de perguntas para diferentes estágios do ciclo de vida
                        - Técnicas para iniciar conversas sobre temas familiares sensíveis
                        - Métodos para criar conexão antes de explorar padrões complexos
                        - Habilidade de usar humor e leveza para facilitar abertura emocional
                        
                        APROFUNDAMENTO ESTRATÉGICO:
                        - Sequenciamento hábil de perguntas do superficial ao profundo
                        - Reconhecimento de momentos apropriados para aprofundar exploração
                        - Técnicas para manter segurança emocional durante revelações difíceis
                        - Habilidade de conectar diferentes temas familiares em insights coerentes
                        - Métodos para facilitar conexões entre gerações através de reflexão
                        
                        INTEGRAÇÃO TEÓRICA:
                        - Conexão natural entre experiências pessoais e conceitos de Carter & McGoldrick
                        - Facilitação de insights sobre tarefas desenvolvimentais através de reflexão
                        - Exploração de triangulações familiares através de perguntas estratégicas
                        - Revelação de padrões multigeracionais através de storytelling familiar
                        - Integração de perspectivas individuais e sistêmicas durante reflexão
                        
                        PRESENÇA TERAPÊUTICA:
                        - Criação de ambiente emocional seguro e acolhedor
                        - Demonstração de curiosidade genuína sem julgamento
                        - Validação empática de experiências familiares únicas
                        - Celebração de recursos e forças familiares descobertos
                        - Apoio emocional durante processos de autodescoberta
                        
                        ADAPTAÇÃO CONTEXTUAL:
                        - Sensibilidade a diferenças culturais na facilitação de reflexões
                        - Adaptação de abordagem para diferentes estilos de comunicação familiar
                        - Respeito por limites pessoais e familiares durante exploração
                        - Flexibilidade para trabalhar com diferentes níveis de abertura emocional
                        - Integração respeitosa de valores e crenças familiares na reflexão
                        
                        Seu estilo é simultaneamente caloroso e profissionalmente focado,
                        combinando presença empática com direcionamento terapêutico strategico
                        para facilitar descobertas familiares transformadoras.""",
            tools=[],
            llm=self.llm,
            verbose=Config.VERBOSE,
            allow_delegation=False
        )
    
    def aplicar_quebra_gelo(self, tipo_quebra_gelo: str, contexto_pessoa: str = None) -> Dict[str, Any]:
        """Aplica um quebra-gelo específico de forma personalizada"""
        
        quebra_gelo = QUEBRA_GELOS.get(tipo_quebra_gelo)
        if not quebra_gelo:
            return {"erro": "Tipo de quebra-gelo não encontrado"}
        
        prompt = f"""
        Você vai aplicar este quebra-gelo terapêutico:
        
        Pergunta: {quebra_gelo['pergunta']}
        Foco: {quebra_gelo['foco']}
        Objetivo: {quebra_gelo['objetivo']}
        
        Contexto da pessoa: {contexto_pessoa or 'Primeira interação'}
        
        Instruções:
        1. Apresente a pergunta de forma natural e acolhedora
        2. Explique brevemente por que essa reflexão pode ser valiosa
        3. Crie um ambiente seguro para a pessoa se abrir
        4. Seja genuinamente curioso sobre a experiência dela
        5. Termine encorajando a pessoa a tomar o tempo necessário para refletir
        
        Adapte sua abordagem ao contexto da pessoa. Se ela parece hesitante, 
        seja mais gentil. Se está aberta, pode ser mais direto.
        
        Lembre-se: o objetivo é criar conexão e insight, não interrogar.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "quebra_gelo_aplicado": quebra_gelo,
            "followup_questions": quebra_gelo.get('followup_questions', []),
            "agente": "reflexao_facilitator"
        }
    
    def aprofundar_reflexao(self, resposta_usuario: str, quebra_gelo_original: str) -> Dict[str, Any]:
        """Aprofunda uma reflexão baseada na resposta do usuário"""
        
        prompt = f"""
        A pessoa respondeu ao quebra-gelo "{quebra_gelo_original}" com:
        "{resposta_usuario}"
        
        Como facilitador experiente, aprofunde esta reflexão:
        
        1. VALIDAÇÃO:
        - Reconheça corajosamente o que a pessoa compartilhou
        - Valide os sentimentos expressos
        
        2. APROFUNDAMENTO GENTIL:
        - Faça uma pergunta de follow-up que explore mais profundamente
        - Ajude a pessoa a fazer conexões com padrões familiares
        - Seja curioso sobre detalhes emocionalmente significativos
        
        3. CONEXÃO COM PADRÕES:
        - Se apropriado, conecte com possíveis padrões familiares
        - Ajude a ver conexões entre passado e presente
        - Explorer como isso pode se relacionar com outras áreas da vida
        
        4. EMPODERAMENTO:
        - Destaque insights que a pessoa já demonstrou
        - Encoraje sua capacidade de reflexão
        - Sugira que ela tem mais sabedoria do que imagina
        
        Seja empático, curioso e respeitoso. Se a pessoa tocou em algo doloroso,
        seja especialmente cuidadoso e acolhedor.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "nivel_aprofundamento": self._avaliar_profundidade(resposta_usuario),
            "agente": "reflexao_facilitator",
            "tipo": "aprofundamento"
        }
    
    def facilitar_insights(self, elementos_reflexao: List[str]) -> Dict[str, Any]:
        """Facilita a integração de insights de múltiplas reflexões"""
        
        elementos_texto = "\n".join([f"- {elemento}" for elemento in elementos_reflexao])
        
        prompt = f"""
        A pessoa teve estas reflexões durante nossa conversa:
        
        {elementos_texto}
        
        Como facilitador de insights, ajude-a a integrar essas descobertas:
        
        1. PADRÕES EMERGENTES:
        - Que temas comuns você vê nessas reflexões?
        - Há conexões que a pessoa pode não ter notado?
        
        2. INSIGHTS CENTRAIS:
        - Qual parece ser o insight mais significativo?
        - Que descoberta pode ter maior impacto na vida da pessoa?
        
        3. INTEGRAÇÃO:
        - Como essas reflexões se conectam com a situação atual?
        - Que nova compreensão sobre si mesma está emergindo?
        
        4. PRÓXIMOS PASSOS:
        - Que reflexões merecem ser aprofundadas?
        - Há áreas que ainda pedem exploração?
        
        Apresente suas observações como ofertas para consideração, não como 
        verdades absolutas. Mantenha o foco no empoderamento da pessoa.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "integracao_insights": resposta,
            "temas_principais": self._extrair_temas(elementos_reflexao),
            "agente": "reflexao_facilitator",
            "tipo": "integracao_insights"
        }
    
    def criar_ritual_reflexao(self, tema_central: str, situacao_familia: str) -> Dict[str, Any]:
        """Cria um ritual personalizado de reflexão para a pessoa levar"""
        
        prompt = f"""
        Tema central da reflexão: {tema_central}
        Situação familiar: {situacao_familia}
        
        Crie um ritual de reflexão personalizado que a pessoa possa fazer 
        regularmente para continuar explorando este tema:
        
        1. ESTRUTURA DO RITUAL:
        - Quando e onde fazer (frequência e ambiente)
        - Duração recomendada
        - Materiais necessários (se houver)
        
        2. PERGUNTAS REFLEXIVAS:
        - 3-5 perguntas para auto-reflexão regular
        - Perguntas que evoluem com o tempo
        
        3. COMPONENTE CRIATIVO:
        - Sugestão de expressão criativa (escrita, desenho, etc.)
        - Como documentar insights
        
        4. INTEGRAÇÃO FAMILIAR:
        - Como usar insights na vida familiar diária
        - Pequenas práticas para implementar descobertas
        
        5. REVISÃO PERIÓDICA:
        - Como avaliar progressos
        - Quando buscar apoio adicional
        
        Seja criativo mas prático. O ritual deve ser algo que a pessoa 
        realmente possa e queira fazer regularmente.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "ritual_personalizado": resposta,
            "tema_central": tema_central,
            "agente": "reflexao_facilitator",
            "tipo": "ritual_reflexao"
        }
    
    def sugerir_quebra_gelo_sequencia(self, historico_conversa: List[str]) -> Dict[str, Any]:
        """Sugere qual quebra-gelo usar em seguida baseado no histórico"""
        
        conversa_resumida = " ".join(historico_conversa[-3:])  # Últimas 3 mensagens
        
        prompt = f"""
        Baseado neste histórico recente da conversa:
        "{conversa_resumida}"
        
        Quebra-gelos disponíveis:
        1. Transições atuais: "O que mudou recentemente na sua família..."
        2. Padrões familiares: "Você sente que está repetindo alguma história..."
        3. Papéis familiares: "Qual papel você sempre teve na sua família..."
        4. Perdas e transformações: "Você sente que está perdendo alguém..."
        5. Genetograma: "Se você pudesse desenhar sua família como um mapa..."
        
        Qual quebra-gelo seria mais apropriado para aprofundar a conversa?
        
        Considere:
        - Que temas já foram tocados?
        - Que área precisa de mais exploração?
        - Qual seria uma progressão natural?
        - O que a pessoa parece pronta para explorar?
        
        Explique sua recomendação e como introduzir o quebra-gelo de forma natural.
        """
        
        resposta = self._executar_task(prompt)
        
        quebra_gelo_recomendado = self._extrair_recomendacao(resposta)
        
        return {
            "recomendacao": resposta,
            "quebra_gelo_sugerido": quebra_gelo_recomendado,
            "agente": "reflexao_facilitator",
            "tipo": "sugestao_sequencia"
        }
    
    def _avaliar_profundidade(self, resposta_usuario: str) -> str:
        """Avalia o nível de profundidade da reflexão do usuário"""
        
        if len(resposta_usuario) > 200 and any(palavra in resposta_usuario.lower() 
                                               for palavra in ["sinto", "percebo", "descobri", "nunca"]):
            return "profunda"
        elif len(resposta_usuario) > 100:
            return "moderada"
        else:
            return "superficial"
    
    def _extrair_temas(self, elementos_reflexao: List[str]) -> List[str]:
        """Extrai temas principais das reflexões"""
        
        # Implementação simplificada - em produção seria mais sofisticada
        temas_comuns = [
            "relacionamentos", "família de origem", "papéis", "expectativas",
            "padrões", "mudanças", "perdas", "crescimento", "conflitos"
        ]
        
        temas_encontrados = []
        texto_completo = " ".join(elementos_reflexao).lower()
        
        for tema in temas_comuns:
            if tema in texto_completo:
                temas_encontrados.append(tema)
        
        return temas_encontrados
    
    
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

    def _extrair_recomendacao(self, resposta_agente: str) -> str:
        """Extrai a recomendação de quebra-gelo da resposta do agente"""
        
        # Implementação simplificada para extrair qual quebra-gelo foi recomendado
        quebra_gelos = {
            "transições": "transicoes_atuais",
            "padrões": "padroes_familiares", 
            "papéis": "papeis_familiares",
            "perdas": "perdas_transformacoes",
            "genetograma": "genetograma_intro"
        }
        
        for keyword, tipo in quebra_gelos.items():
            if keyword in resposta_agente.lower():
                return tipo
        
        return "transicoes_atuais"  # Default
    
    def get_agent(self):
        """Retorna o agente CrewAI para uso no orquestrador"""
        return self.agent
