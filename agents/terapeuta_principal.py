"""
Agente Terapeuta Principal
Especializado em conduzir sessões terapêuticas empáticas baseadas no modelo Carter & McGoldrick
"""

from crewai import Agent, Task, Crew
from typing import Dict, Any, List
import os
from config import Config
from knowledge.carter_mcgoldrick import (
    CONCEITOS_FUNDAMENTAIS,
    get_estagio_ciclo_vida,
    identificar_triangulacoes_ativas,
    sugerir_intervencoes_por_estagio
)
from knowledge.quebra_gelos import QUEBRA_GELOS, get_quebra_gelo_by_context
from knowledge.genetograma_guide import GENETOGRAMA_GUIDE

class TerapeutaPrincipal:
    def __init__(self):
        self.llm = Config.get_llm()
        
        # Configurar agente CrewAI
        self.agent = Agent(
            role="Terapeuta Familiar Principal",
            goal="""Conduzir sessões terapêuticas familiares eficazes usando a teoria completa 
                    de Carter & McGoldrick, facilitando insights transformadores e promovendo 
                    mudanças positivas nas dinâmicas familiares.""",
            backstory="""Você é um terapeuta familiar experiente especializado na abordagem 
                        sistêmica de Carter & McGoldrick, com profundo conhecimento do ciclo de vida familiar.
                        
                        Sua expertise inclui:
                        
                        TEORIA DO CICLO DE VIDA:
                        - Domínio completo dos 6 estágios do ciclo de vida familiar
                        - Identificação precisa de tarefas desenvolvimentais por estágio
                        - Reconhecimento de sinais de travamento em transições
                        - Compreensão das variações: divórcio, doença crônica, famílias monoparentais
                        - Sensibilidade a diferenças culturais e socioeconômicas
                        
                        PADRÕES RELACIONAIS:
                        - Identificação de triangulações familiares complexas
                        - Análise de padrões multigeracionais de funcionamento
                        - Compreensão de lealdades invisíveis e segredos familiares
                        - Reconhecimento de fronteiras difusas ou rígidas
                        - Avaliação de sistemas de poder e tomada de decisão
                        
                        INTERVENÇÕES ESPECIALIZADAS:
                        - Intervenções específicas para cada estágio do ciclo de vida
                        - Técnicas de detriangulação para diferentes padrões
                        - Estratégias para facilitar transições travadas
                        - Abordagens adaptadas para variações familiares especiais
                        - Integração de perspectivas individuais e sistêmicas
                        
                        ABORDAGEM TERAPÊUTICA:
                        - Empático mas direto quando necessário
                        - Foco em recursos e competências familiares
                        - Respeito pela autonomia e valores da família
                        - Colaborativo na definição de objetivos terapêuticos
                        - Atento a questões de diversidade e inclusão
                        
                        Você inicia conversas de forma acolhedora mas mantém foco terapêutico claro,
                        sempre considerando o estágio do ciclo de vida e padrões sistêmicos únicos
                        de cada família.""",
            tools=[],
            llm=self.llm,  # Usar o objeto LLM do Config
            verbose=Config.VERBOSE,
            memory=Config.ENABLE_MEMORY,
            allow_delegation=True  # Necessário para processo hierárquico no CrewAI
        )
    
    def iniciar_sessao(self, contexto_inicial: str = None) -> Dict[str, Any]:
        """Inicia uma nova sessão terapêutica"""
        
        quebra_gelo = get_quebra_gelo_by_context(contexto_inicial or "")
        
        prompt = f"""
        Você está iniciando uma nova sessão de apoio emocional. 
        
        Contexto inicial: {contexto_inicial or 'Primeira sessão'}
        
        Quebra-gelo sugerido: {quebra_gelo['pergunta']}
        
        Instruções:
        1. Faça uma abertura acolhedora e empática
        2. Explique brevemente como você pode ajudar (sem ser didático)
        3. Use o quebra-gelo de forma natural na conversa
        4. Mantenha tom conversacional, não formal
        5. Demonstre genuíno interesse pela pessoa
        
        Lembre-se: Você está aqui para ouvir, acolher e apoiar. Não é uma consulta médica,
        mas um espaço seguro para reflexão sobre dinâmicas familiares.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "quebra_gelo_usado": quebra_gelo,
            "agente": "terapeuta_principal"
        }
    
    def _executar_task(self, prompt: str) -> str:
        """Executa uma task com o agente"""
        task = Task(
            description=prompt,
            agent=self.agent,
            expected_output="Resposta empática e terapêutica em formato de texto"
        )
        
        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=False
        )
        
        result = crew.kickoff()
        return str(result)
    
    def avaliar_familia_inicial(self, informacoes_familia: str, 
                               contexto_inicial: str = None) -> Dict[str, Any]:
        """Conduz avaliação inicial da família baseada na teoria completa de Carter & McGoldrick"""
        
        quebra_gelo = get_quebra_gelo_by_context(contexto_inicial or "")
        
        prompt = f"""
        {quebra_gelo['pergunta']}
        
        Como terapeuta familiar especializado na abordagem de Carter & McGoldrick,
        faça uma avaliação inicial abrangente desta família:
        
        INFORMAÇÕES DA FAMÍLIA:
        {informacoes_familia}
        
        Contexto inicial: {contexto_inicial or 'Não fornecido'}
        
        Realize uma avaliação estruturada seguindo rigorosamente a teoria completa
        de Carter & McGoldrick:
        
        1. IDENTIFICAÇÃO DO ESTÁGIO DO CICLO DE VIDA:
        - Baseado nas informações, identifique o estágio atual do ciclo de vida
        - Justifique sua identificação usando os marcos específicos de cada estágio
        - Considere se há sobreposição entre estágios ou transições em andamento
        - Verifique se há variações especiais aplicáveis (divórcio, doença crônica, etc.)
        
        2. AVALIAÇÃO DE TAREFAS DESENVOLVIMENTAIS:
        - Liste as tarefas específicas que esta família deveria estar cumprindo
        - Identifique quais tarefas parecem estar sendo realizadas adequadamente
        - Identifique quais tarefas estão em atraso, evitadas ou sendo resistidas
        - Avalie se há travamentos em tarefas de estágios anteriores
        
        3. ANÁLISE DE PADRÕES RELACIONAIS:
        - Identifique padrões de triangulação presentes na família
        - Avalie qualidade das fronteiras entre subsistemas familiares
        - Examine padrões de comunicação e resolução de conflitos
        - Identifique lealdades invisíveis ou segredos familiares aparentes
        
        4. AVALIAÇÃO MULTIGERACIONAL:
        - Como padrões das famílias de origem influenciam funcionamento atual?
        - Há repetição de padrões problemáticos através das gerações?
        - Questões não resolvidas dos pais afetam capacidade de cumprir tarefas atuais?
        - Que recursos multigeracionais podem ser mobilizados?
        
        5. FATORES CONTEXTUAIS:
        - Considere influências culturais, socioeconômicas e ambientais
        - Avalie impacto de estressores externos no funcionamento familiar
        - Identifique recursos e suportes externos disponíveis
        - Considere questões de diversidade e inclusão relevantes
        
        6. SÍNTESE E HIPÓTESES INICIAIS:
        - Qual sua hipótese principal sobre os desafios desta família?
        - Como os problemas apresentados se relacionam com o estágio do ciclo?
        - Que mudanças sistêmicas seriam mais impactantes?
        - Qual o prognóstico inicial baseado em recursos identificados?
        
        7. DIREÇÕES TERAPÊUTICAS PRELIMINARES:
        - Que áreas precisam de foco terapêutico prioritário?
        - Que intervenções seriam mais apropriadas para este estágio?
        - Como engajar a família no processo terapêutico?
        - Que recursos precisam ser desenvolvidos ou mobilizados?
        
        Mantenha tom empático e acolhedor, mas seja específico e teoricamente fundamentado.
        Base toda análise rigorosamente nos conceitos completos de Carter & McGoldrick.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "avaliacao_inicial": resposta,
            "quebra_gelo": quebra_gelo,
            "tipo": "avaliacao_inicial",
            "agente": "terapeuta_principal"
        }
    
    def analisar_padrao_intergeracional(self, historico_familiar: str, 
                                       problema_atual: str) -> Dict[str, Any]:
        """Analisa padrões que se repetem através das gerações"""
        
        prompt = f"""
        Como terapeuta familiar especialista em padrões multigeracionais:
        
        HISTÓRICO FAMILIAR:
        {historico_familiar}
        
        PROBLEMA ATUAL:
        {problema_atual}
        
        Analise os padrões multigeracionais seguindo os conceitos de Carter & McGoldrick:
        
        1. IDENTIFICAÇÃO DE PADRÕES REPETITIVOS:
        - Que padrões de funcionamento se repetem através das gerações?
        - Como os mesmos problemas aparecem em formas diferentes?
        - Que temas não resolvidos passam de geração para geração?
        
        2. ANÁLISE DE TRIANGULAÇÕES MULTIGERACIONAIS:
        - Como triangulações se estabelecem através das gerações?
        - Que alianças/coalizões cruzam fronteiras geracionais?
        - Como conflitos não resolvidos criam triangulações atuais?
        
        3. LEALDADES INVISÍVEIS:
        - Que lealdades não expressas influenciam comportamento atual?
        - Como membros "protegem" gerações anteriores inconscientemente?
        - Que segredos familiares ainda impactam funcionamento atual?
        
        4. MISSÕES FAMILIARES TRANSMITIDAS:
        - Que "missões" ou expectativas são passadas entre gerações?
        - Como membros tentam "reparar" feridas de gerações anteriores?
        - Que papéis rígidos são transmitidos através das gerações?
        
        5. RECURSOS MULTIGERACIONAIS:
        - Que forças e competências existem na linhagem familiar?
        - Como recursos de gerações anteriores podem ser mobilizados?
        - Que tradições positivas podem ser resgatadas?
        
        6. INTERVENÇÕES ESPECÍFICAS:
        - Como interromper padrões problemáticos multigeracionais?
        - Que conversas precisam acontecer entre gerações?
        - Como honrar o passado enquanto permite mudança?
        
        Base sua análise nos conceitos específicos de Carter & McGoldrick sobre 
        transmissão multigeracional e dinâmicas familiares.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise_multigeracional": resposta,
            "tipo": "analise_multigeracional",
            "agente": "terapeuta_principal"
        }
    
    def facilitar_transicao_ciclo_vida(self, estagio_atual: str, 
                                      desafios_transicao: str) -> Dict[str, Any]:
        """Facilita transições entre estágios do ciclo de vida"""
        
        estagio_info = get_estagio_ciclo_vida(estagio_atual)
        intervencoes = sugerir_intervencoes_por_estagio(estagio_atual)
        
        prompt = f"""
        Como terapeuta especialista em transições do ciclo de vida familiar:
        
        ESTÁGIO ATUAL: {estagio_atual}
        
        INFORMAÇÕES DO ESTÁGIO:
        {estagio_info}
        
        DESAFIOS NA TRANSIÇÃO:
        {desafios_transicao}
        
        INTERVENÇÕES RECOMENDADAS:
        {intervencoes}
        
        Desenvolva estratégias específicas para facilitar esta transição:
        
        1. NORMALIZAÇÃO DA TRANSIÇÃO:
        - Como normalizar os desafios que a família está enfrentando?
        - Que aspectos da transição são universais vs. únicos desta família?
        - Como reduzir ansiedade sobre mudanças normais do desenvolvimento?
        
        2. IDENTIFICAÇÃO DE TRAVAMENTOS:
        - Que aspectos da transição estão sendo evitados ou resistidos?
        - Como medos ou lealdades passadas impedem movimento?
        - Que recursos internos da família não estão sendo utilizados?
        
        3. ESTRATÉGIAS DE FACILITAÇÃO:
        - Que passos concretos podem facilitar o movimento para próximo estágio?
        - Como usar rituais ou marcos para marcar transições?
        - Que conversas específicas precisam acontecer?
        
        4. MOBILIZAÇÃO DE RECURSOS:
        - Como mobilizar recursos familiares existentes?
        - Que apoios externos podem facilitar a transição?
        - Como construir sobre forças familiares identificadas?
        
        5. PREVENÇÃO DE RECAÍDAS:
        - Como prevenir retorno a padrões anteriores?
        - Que sinais indicariam necessidade de apoio adicional?
        - Como criar sistemas de apoio duradouros?
        
        6. INTERVENÇÕES ESPECÍFICAS:
        - Que técnicas específicas são mais apropriadas para esta transição?
        - Como adaptar intervenções para o contexto único desta família?
        - Que sequência de intervenções seria mais efetiva?
        
        Mantenha foco na capacidade da família de navegar mudanças com suporte apropriado.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "estrategias_transicao": resposta,
            "estagio_foco": estagio_atual,
            "tipo": "facilitacao_transicao",
            "agente": "terapeuta_principal"
        }
    
    def processar_mensagem(self, mensagem: str, contexto_sessao: List[Dict] = None) -> Dict[str, Any]:
        """Processa uma mensagem durante a sessão"""
        
        historico = "\n".join([
            f"{msg.get('tipo', 'user')}: {msg.get('conteudo', '')}" 
            for msg in (contexto_sessao or [])
        ])
        
        prompt = f"""
        Histórico da conversa:
        {historico}
        
        Nova mensagem do usuário: {mensagem}
        
        Como terapeuta familiar sistêmico, responda considerando:
        
        1. ESCUTA EMPÁTICA:
        - Valide os sentimentos expressos
        - Reflita de volta o que você ouviu
        - Demonstre compreensão genuína
        
        2. PERSPECTIVA SISTÊMICA:
        - Identifique possíveis padrões familiares mencionados
        - Note conexões entre gerações se houver
        - Observe triangulações ou dinâmicas relacionais
        
        3. PERGUNTAS TERAPÊUTICAS:
        - Faça perguntas abertas que promovam reflexão
        - Explore contexto familiar quando apropriado
        - Ajude a pessoa a fazer suas próprias conexões
        
        4. APOIO EMOCIONAL:
        - Normalize sentimentos difíceis
        - Ofereça perspectivas esperançosas quando apropriado
        - Mantenha foco na capacidade de crescimento da pessoa
        
        Evite:
        - Dar conselhos diretos ou soluções prontas
        - Interpretações profundas sem convite
        - Linguagem técnica excessiva
        - Assumir conhecimento sobre a situação familiar
        
        Sua resposta deve ser calorosa, reflexiva e que convide à continuidade da conversa.
        """
        
        resposta = self._executar_task(prompt)
        
        # Analisar se é momento para sugerir genetograma ou quebra-gelos específicos
        insights = self._analisar_insights(mensagem, resposta)
        
        return {
            "resposta": resposta,
            "agente": "terapeuta_principal",
            "insights_detectados": insights.get("insights", []),
            "quebra_gelo_sugerido": insights.get("quebra_gelo"),
            "proximos_passos": insights.get("proximos_passos", [])
        }
    
    def _analisar_insights(self, mensagem_usuario: str, resposta_agente: str) -> Dict[str, Any]:
        """Analisa a conversa para identificar insights e próximos passos"""
        
        prompt = f"""
        Analise esta interação terapêutica:
        
        Usuário: {mensagem_usuario}
        Terapeuta: {resposta_agente}
        
        Identifique:
        1. Insights sobre padrões familiares mencionados ou implícitos
        2. Se seria apropriado sugerir criação de genetograma
        3. Que quebra-gelo específico poderia ser útil na próxima conversa
        4. Próximos passos terapêuticos naturais
        
        Retorne em formato:
        INSIGHTS: [lista de insights identificados]
        GENETOGRAMA: [sim/não e por quê]
        QUEBRA_GELO: [tipo recomendado ou nenhum]
        PROXIMOS_PASSOS: [lista de próximos passos naturais]
        """
        
        analise = self._executar_task(prompt)
        
        # Processar a resposta estruturada (implementação simplificada)
        insights = {
            "insights": [],
            "quebra_gelo": None, 
            "proximos_passos": []
        }
        
        # Aqui você implementaria parsing mais sofisticado da análise
        if "genetograma" in analise.lower():
            insights["quebra_gelo"] = QUEBRA_GELOS["genetograma_intro"]
        
        return insights
    
    def finalizar_sessao(self, resumo_sessao: str) -> Dict[str, Any]:
        """Finaliza a sessão com um fechamento empático"""
        
        prompt = f"""
        Você está finalizando uma sessão de apoio emocional.
        
        Resumo da sessão: {resumo_sessao}
        
        Crie um fechamento que:
        1. Reconheça o que a pessoa compartilhou
        2. Destaque forças e recursos identificados
        3. Ofereça validação e encorajamento
        4. Deixe a porta aberta para futuras conversas
        5. Seja genuinamente empático e esperançoso
        
        Evite resumos técnicos ou interpretações - foque no aspecto humano e relacional.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "resposta": resposta,
            "agente": "terapeuta_principal",
            "tipo": "finalizacao"
        }
    
    def get_agent(self):
        """Retorna o agente CrewAI para uso no orquestrador"""
        return self.agent
