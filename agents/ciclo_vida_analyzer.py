"""
Agente Analisador de Ciclo de Vida Familiar
Especializado em identificar estágios, avaliar tarefas desenvolvimentais e detectar travamentos
"""

from crewai import Agent, Task, Crew
from typing import Dict, Any, List
import os
from config import Config
from knowledge.carter_mcgoldrick import (
    CONCEITOS_FUNDAMENTAIS, 
    get_estagio_ciclo_vida, 
    determinar_estagio_por_idade_situacao,
    identificar_variacoes_aplicaveis,
    avaliar_cumprimento_tarefas_estagio
)

class CicloVidaAnalyzer:
    def __init__(self):
        self.llm = Config.get_llm()
        
        self.agent = Agent(
            role="Especialista em Ciclo de Vida Familiar",
            goal="""Identificar precisamente o estágio atual do ciclo de vida familiar, 
                    avaliar cumprimento de tarefas desenvolvimentais e detectar travamentos 
                    ou descompassos no desenvolvimento familiar baseado na teoria completa 
                    de Carter & McGoldrick.""",
            backstory="""Você é um especialista altamente treinado na teoria do ciclo de vida 
                        familiar de Carter & McGoldrick com conhecimento profundo sobre:
                        
                        - Os 6 estágios específicos do ciclo de vida familiar
                        - Tarefas desenvolvimentais específicas de cada estágio
                        - Sinais de travamento em transições
                        - Variações especiais: divórcio, doença crônica, famílias monoparentais
                        - Diferenças culturais e socioeconômicas nos padrões de ciclo
                        - Interface entre estágios individuais e familiares de desenvolvimento
                        - Impacto de eventos imprevisíveis no ciclo familiar
                        
                        Sua expertise permite identificar não apenas ONDE a família está no ciclo,
                        mas também avaliar se estão cumprindo adequadamente as tarefas daquele 
                        estágio e que intervenções podem facilitar transições saudáveis.
                        
                        Você é preciso, analítico mas empático, sempre considerando o contexto 
                        único de cada família.""",
            tools=[],
            llm=self.llm,
            verbose=Config.VERBOSE,
            allow_delegation=False
        )
    
    def identificar_estagio_atual(self, idade_pessoa: int, situacao_familiar: str, 
                                 contexto_adicional: str = None) -> Dict[str, Any]:
        """Identifica o estágio atual do ciclo de vida familiar"""
        
        # Usar função auxiliar para determinação inicial
        estagio_base = determinar_estagio_por_idade_situacao(idade_pessoa, situacao_familiar)
        variacoes = identificar_variacoes_aplicaveis(situacao_familiar)
        
        prompt = f"""
        Como especialista em ciclo de vida familiar, analise esta situação:
        
        Idade da pessoa: {idade_pessoa} anos
        Situação familiar: {situacao_familiar}
        Contexto adicional: {contexto_adicional or 'Não fornecido'}
        
        Análise preliminar automática:
        - Estágio base identificado: {estagio_base.get('estagio', 'Não identificado')}
        - Variações possivelmente aplicáveis: {variacoes}
        
        Baseado na teoria completa de Carter & McGoldrick, forneça análise detalhada:
        
        1. IDENTIFICAÇÃO DO ESTÁGIO:
        - Confirme ou corrija o estágio identificado automaticamente
        - Justifique sua identificação baseada nos marcos descritos
        - Considere se há sobreposição entre estágios
        
        2. TAREFAS DESENVOLVIMENTAIS:
        - Liste as tarefas específicas que a família deveria estar cumprindo
        - Identifique quais parecem estar sendo cumpridas adequadamente
        - Identifique quais parecem estar em atraso ou sendo evitadas
        
        3. AVALIAÇÃO DE TRANSIÇÕES:
        - A família está navegando alguma transição atualmente?
        - Há sinais de travamento em transições anteriores?
        - Que desafios específicos do estágio atual são evidentes?
        
        4. VARIAÇÕES ESPECIAIS:
        - Alguma das variações (divórcio, doença, monoparental, etc.) se aplica?
        - Como isso modifica as tarefas desenvolvimentais normais?
        - Que adaptações são necessárias na abordagem terapêutica?
        
        5. RECOMENDAÇÕES IMEDIATAS:
        - Que áreas precisam de foco terapêutico prioritário?
        - Que recursos familiares podem ser mobilizados?
        - Que intervenções específicas são mais apropriadas para este estágio?
        
        Seja específico e baseie-se rigorosamente na teoria de Carter & McGoldrick.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise_detalhada": resposta,
            "estagio_identificado": estagio_base.get("estagio"),
            "variacoes_aplicaveis": variacoes,
            "idade_pessoa": idade_pessoa,
            "agente": "ciclo_vida_analyzer",
            "tipo": "identificacao_estagio"
        }
    
    def avaliar_travamentos(self, estagio_atual: str, historico_familiar: str, 
                           sintomas_apresentados: List[str] = None) -> Dict[str, Any]:
        """Avalia travamentos específicos no desenvolvimento familiar"""
        
        detalhes_estagio = get_estagio_ciclo_vida(estagio_atual)
        
        prompt = f"""
        Analise possíveis travamentos no desenvolvimento familiar:
        
        Estágio atual: {estagio_atual}
        Histórico familiar: {historico_familiar}
        Sintomas/problemas apresentados: {sintomas_apresentados or ['Não especificados']}
        
        Informações do estágio atual:
        {detalhes_estagio}
        
        Como especialista em ciclo de vida familiar, identifique:
        
        1. TRAVAMENTOS IDENTIFICADOS:
        - Há sinais de que a família está "travada" neste estágio?
        - Que tarefas desenvolvimentais não estão sendo cumpridas?
        - Há evidências de travamentos em estágios anteriores não resolvidos?
        
        2. PADRÕES DE EVITAÇÃO:
        - A família está evitando transições necessárias?
        - Há resistência a mudanças apropriadas para a idade/estágio?
        - Que medos podem estar impedindo o progresso?
        
        3. IMPACTO DOS TRAVAMENTOS:
        - Como os travamentos estão se manifestando em sintomas?
        - Que membros da família estão mais afetados?
        - Como isso interfere com o funcionamento familiar geral?
        
        4. QUESTÕES MULTIGERACIONAIS:
        - Há padrões de travamento que se repetem através das gerações?
        - Questões não resolvidas dos pais estão impactando o estágio atual?
        - Que lealdades invisíveis podem estar mantendo travamentos?
        
        5. FATORES CONTRIBUINTES:
        - Que fatores externos (culturais, econômicos, sociais) contribuem?
        - Há eventos traumáticos que complicaram transições normais?
        - Recursos familiares insuficientes para navegar transições?
        
        6. PROGNÓSTICO E INTERVENÇÕES:
        - Qual é a capacidade da família para superar travamentos?
        - Que intervenções específicas podem facilitar desbloqueio?
        - Que sequência de mudanças seria mais efetiva?
        
        Base sua análise rigorosamente na teoria de Carter & McGoldrick sobre 
        travamentos em transições do ciclo de vida familiar.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise_travamentos": resposta,
            "estagio_analisado": estagio_atual,
            "agente": "ciclo_vida_analyzer",
            "tipo": "avaliacao_travamentos"
        }
    
    def planejar_transicao(self, estagio_atual: str, proximo_estagio: str, 
                          situacao_familia: str) -> Dict[str, Any]:
        """Planeja estratégias para facilitar transição para próximo estágio"""
        
        detalhes_atual = get_estagio_ciclo_vida(estagio_atual)
        detalhes_proximo = get_estagio_ciclo_vida(proximo_estagio)
        
        prompt = f"""
        Desenvolva plano de transição entre estágios do ciclo de vida:
        
        Estágio atual: {estagio_atual}
        Próximo estágio: {proximo_estagio}
        Situação da família: {situacao_familia}
        
        Detalhes do estágio atual:
        {detalhes_atual}
        
        Detalhes do próximo estágio:
        {detalhes_proximo}
        
        Como especialista, desenvolva plano estruturado:
        
        1. PREPARAÇÃO PARA TRANSIÇÃO:
        - Que tarefas do estágio atual ainda precisam ser completadas?
        - Como preparar a família emocionalmente para próximo estágio?
        - Que recursos precisam ser desenvolvidos antes da transição?
        
        2. DESAFIOS ESPECÍFICOS DA TRANSIÇÃO:
        - Que desafios únicos esta família enfrentará na transição?
        - Baseado na situação atual, que obstáculos são previsíveis?
        - Que padrões familiares podem dificultar a transição?
        
        3. ESTRATÉGIAS DE FACILITAÇÃO:
        - Que intervenções específicas podem facilitar a transição?
        - Como mobilizar recursos familiares existentes?
        - Que rituais de transição seriam apropriados?
        
        4. CRONOGRAMA REALÍSTICO:
        - Qual seria um cronograma realístico para esta transição?
        - Que marcos intermediários podem ser estabelecidos?
        - Como monitorar progresso na transição?
        
        5. PREVENÇÃO DE TRAVAMENTOS:
        - Que sinais de alerta indicariam travamento na transição?
        - Como prevenir regressões para estágios anteriores?
        - Que sistemas de apoio são necessários durante transição?
        
        6. ADAPTAÇÕES ESPECIAIS:
        - Esta família precisa de adaptações especiais na transição?
        - Fatores culturais, econômicos ou de saúde a considerar?
        - Como adaptar expectativas normativas para esta família específica?
        
        Baseie todas as recomendações na teoria específica de Carter & McGoldrick 
        sobre transições do ciclo de vida familiar.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "plano_transicao": resposta,
            "estagio_origem": estagio_atual,
            "estagio_destino": proximo_estagio,
            "agente": "ciclo_vida_analyzer",
            "tipo": "planejamento_transicao"
        }
    
    def analisar_descompasso_desenvolvimental(self, idade_cronologica: int, 
                                            comportamento_descrito: str,
                                            situacao_familiar: str) -> Dict[str, Any]:
        """Analisa descompassos entre idade cronológica e desenvolvimento emocional"""
        
        prompt = f"""
        Analise possível descompasso desenvolvimental:
        
        Idade cronológica: {idade_cronologica} anos
        Comportamento/funcionamento descrito: {comportamento_descrito}
        Situação familiar: {situacao_familiar}
        
        Como especialista em desenvolvimento familiar, avalie:
        
        1. ALINHAMENTO DESENVOLVIMENTAL:
        - O funcionamento emocional está alinhado com a idade cronológica?
        - Há sinais de funcionamento mais jovem ou mais velho que a idade?
        - Que áreas específicas mostram descompasso?
        
        2. FATORES CONTRIBUINTES:
        - Que fatores familiares podem ter contribuído para descompasso?
        - Há história de trauma, perda ou estresse que explique o descompasso?
        - Padrões familiares incentivaram desenvolvimento acelerado ou retardado?
        
        3. IMPACTO NO CICLO FAMILIAR:
        - Como o descompasso afeta as transições familiares normais?
        - Outros membros da família compensam o descompasso?
        - A família se organizou em torno do descompasso?
        
        4. NECESSIDADES DESENVOLVIMENTAIS:
        - Que experiências de desenvolvimento foram perdidas?
        - Como criar oportunidades para desenvolvimento apropriado à idade?
        - Que apoios são necessários para realinhamento desenvolvimental?
        
        5. PROGNÓSTICO:
        - Qual é o potencial para realinhamento desenvolvimental?
        - Que fatores facilitariam ou impediriam o progresso?
        - Intervenções mais apropriadas para esta situação específica?
        
        6. RECOMENDAÇÕES:
        - Estratégias para apoiar desenvolvimento apropriado à idade
        - Como ajudar família a adaptar expectativas
        - Que recursos externos podem ser necessários
        
        Use a perspectiva de Carter & McGoldrick sobre desenvolvimento individual 
        dentro do contexto do ciclo de vida familiar.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise_descompasso": resposta,
            "idade_analisada": idade_cronologica,
            "agente": "ciclo_vida_analyzer",
            "tipo": "analise_descompasso"
        }
    
    def recomendar_intervencoes_especificas(self, estagio_identificado: str, 
                                          travamentos_detectados: List[str],
                                          recursos_familiares: List[str]) -> Dict[str, Any]:
        """Recomenda intervenções específicas baseadas no estágio e travamentos"""
        
        prompt = f"""
        Desenvolva recomendações de intervenção específicas:
        
        Estágio do ciclo de vida: {estagio_identificado}
        Travamentos detectados: {travamentos_detectados}
        Recursos familiares disponíveis: {recursos_familiares}
        
        Como especialista em intervenções familiares baseadas no ciclo de vida:
        
        1. INTERVENÇÕES PRIORITÁRIAS:
        - Que intervenções têm maior potencial de impacto?
        - Qual seria a sequência mais efetiva de intervenções?
        - Como priorizar baseado na capacidade atual da família?
        
        2. ESTRATÉGIAS POR ESTÁGIO:
        - Que técnicas são mais efetivas para este estágio específico?
        - Como adaptar abordagens gerais para necessidades do estágio?
        - Que armadilhas evitar ao trabalhar com famílias neste estágio?
        
        3. ABORDAGEM DOS TRAVAMENTOS:
        - Como abordar especificamente cada travamento identificado?
        - Que ordem de trabalho seria mais efetiva?
        - Como usar recursos familiares para superar travamentos?
        
        4. MOBILIZAÇÃO DE RECURSOS:
        - Como maximizar uso dos recursos familiares existentes?
        - Que recursos adicionais precisam ser desenvolvidos?
        - Como conectar família com recursos externos apropriados?
        
        5. PREVENÇÃO DE RECIDIVAS:
        - Como prevenir retorno aos padrões problemáticos?
        - Que habilidades a família precisa desenvolver para autocontrole?
        - Como criar sistemas de apoio duradouros?
        
        6. CRONOGRAMA E MARCOS:
        - Cronograma realístico para implementação das intervenções
        - Marcos intermediários para avaliar progresso
        - Sinais de que intervenções estão funcionando
        
        7. ADAPTAÇÕES CULTURAIS/CONTEXTUAIS:
        - Como adaptar intervenções para contexto específico da família?
        - Fatores culturais, econômicos ou sociais a considerar?
        - Como respeitar valores familiares enquanto promove mudança?
        
        Base todas as recomendações na teoria e práticas específicas de 
        Carter & McGoldrick para intervenção em diferentes estágios do ciclo familiar.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "recomendacoes_intervencao": resposta,
            "estagio_base": estagio_identificado,
            "travamentos_abordados": travamentos_detectados,
            "agente": "ciclo_vida_analyzer",
            "tipo": "recomendacoes_intervencao"
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
    
    def get_agent(self):
        """Retorna o agente CrewAI para uso no orquestrador"""
        return self.agent
