"""
Agente Analisador de Padrões
Especializado em identificar padrões transgeracionais e triangulações familiares
"""

from crewai import Agent, Task, Crew
from typing import Dict, Any, List
import os
from config import Config
from knowledge.carter_mcgoldrick import (
    CONCEITOS_FUNDAMENTAIS,
    identificar_triangulacoes_ativas,
    analisar_padroes_multigeracionais,
    sugerir_detriangulacao
)
from knowledge.genetograma_guide import TRIANGULACOES_COMUNS

class PadraoAnalyzer:
    def __init__(self):
        self.llm = Config.get_llm()
        
        self.agent = Agent(
            role="Analista de Padrões Familiares Transgeracionais",
            goal="""Identificar padrões repetitivos, triangulações e dinâmicas familiares 
                    que se perpetuam através das gerações, oferecendo insights terapêuticos 
                    baseados na teoria sistêmica.""",
            backstory="""Você é um especialista de elite em análise de padrões familiares sistêmicos
                        com maestria completa na teoria de Carter & McGoldrick e Bowen.
                        
                        Sua expertise altamente especializada inclui:
                        
                        ANÁLISE DE PADRÕES TRANSGERACIONAIS:
                        - Identificação precisa de padrões que se repetem através de 3-4 gerações
                        - Reconhecimento de temas familiares não resolvidos e sua transmissão
                        - Análise de como traumas e sucessos se propagam através do tempo
                        - Compreensão de missões familiares e mandatos inconscientes
                        - Identificação de padrões de relacionamento que atravessam gerações
                        
                        TRIANGULAÇÕES COMPLEXAS:
                        - Mapeamento de todos os tipos de triangulação (pai-mãe-filho, conflitual, fusão, etc.)
                        - Identificação de triangulações múltiplas e sobrepostas
                        - Análise de triangulações que cruzam fronteiras geracionais
                        - Reconhecimento de alianças secretas e coalizões rígidas
                        - Compreensão de como segredos familiares mantêm triangulações
                        
                        DINÂMICAS DE PODER E FRONTEIRAS:
                        - Análise de hierarquias familiares e distribuição de poder
                        - Identificação de fronteiras difusas, rígidas ou apropriadas
                        - Compreensão de subsistemas familiares e suas interações
                        - Reconhecimento de papéis rígidos e pseudocomplementaridade
                        - Análise de padrões de inclusão/exclusão familiar
                        
                        DIFERENCIAÇÃO E FUSÃO:
                        - Avaliação de níveis de diferenciação em membros familiares
                        - Identificação de padrões de fusão emocional
                        - Reconhecimento de cut-offs emocionais e suas funções
                        - Compreensão de como ansiedade se propaga através do sistema
                        - Análise de equilíbrio entre autonomia e conexão
                        
                        RECURSOS E COMPETÊNCIAS FAMILIARES:
                        - Identificação de forças e recursos ocultos ou subutilizados
                        - Reconhecimento de padrões de resiliência através das gerações
                        - Análise de tradições positivas e valores centrais da família
                        - Compreensão de como mobilizar competências existentes
                        - Identificação de aliados naturais dentro do sistema familiar
                        
                        INTEGRAÇÃO CONTEXTUAL:
                        - Consideração de fatores culturais, socioeconômicos e históricos
                        - Análise do impacto de eventos traumáticos na formação de padrões
                        - Compreensão de como mudanças sociais afetam padrões familiares
                        - Sensibilidade a questões de diversidade e inclusão
                        - Integração de perspectivas individuais e sistêmicas
                        
                        Sua abordagem é simultaneamente analítica e empática, apresentando insights
                        complexos de forma acessível e sempre focando no empoderamento da família
                        através da compreensão consciente de seus próprios padrões únicos.""",
            tools=[],
            llm=self.llm,
            verbose=Config.VERBOSE,
            memory=Config.ENABLE_MEMORY,
            allow_delegation=False
        )
    
    def analisar_conversa(self, historico_conversa: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa uma conversa para identificar padrões familiares mencionados"""
        
        conversa_texto = "\n".join([
            f"{msg.get('tipo', 'user')}: {msg.get('conteudo', '')}" 
            for msg in historico_conversa
        ])
        
        prompt = f"""
        Analise esta conversa terapêutica para identificar padrões familiares mencionados 
        ou implícitos:
        
        {conversa_texto}
        
        Como especialista em padrões familiares, identifique:
        
        1. PADRÕES TRANSGERACIONAIS:
        - Há comportamentos/papéis que parecem se repetir entre gerações?
        - Semelhanças entre a pessoa e seus familiares?
        - Heranças emocionais aparentes?
        
        2. TRIANGULAÇÕES:
        - A pessoa menciona estar no meio de conflitos?
        - Há alianças que excluem terceiros?
        - Padrões de "dois contra um"?
        
        3. PAPÉIS FAMILIARES:
        - Que papel a pessoa parece ter na família?
        - Há expectativas rígidas ou lealdades invisíveis?
        - Papéis que limitam o crescimento pessoal?
        
        4. EIXOS VERTICAL E HORIZONTAL:
        - Que herança do passado está influenciando o presente?
        - Há crises atuais conectadas com padrões antigos?
        
        5. RECURSOS E FORÇAS:
        - Que recursos familiares positivos foram mencionados?
        - Há padrões saudáveis a serem fortalecidos?
        
        Apresente suas observações de forma empática e construtiva, sempre como 
        hipóteses para exploração, não como verdades absolutas.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise": resposta,
            "padroes_identificados": self._extrair_padroes(resposta),
            "agente": "padrao_analyzer",
            "tipo": "analise_conversa"
        }
    
    def analisar_genetograma(self, dados_genetograma: Dict[str, Any]) -> Dict[str, Any]:
        """Analisa um genetograma para identificar padrões específicos"""
        
        prompt = f"""
        Analise este genetograma familiar em profundidade:
        
        {dados_genetograma}
        
        Como especialista em análise familiar sistêmica, forneça uma análise detalhada:
        
        1. PADRÕES REPETITIVOS IDENTIFICADOS:
        - Que comportamentos/características se repetem entre gerações?
        - Há padrões de relacionamento similares?
        - Profissões, problemas de saúde ou traços que se repetem?
        
        2. TRIANGULAÇÕES E DINÂMICAS:
        - Identifique triangulações presentes (pai-mãe-filho, etc.)
        - Há coalições que persistem através do tempo?
        - Quem são os "portadores de sintoma" em cada geração?
        
        3. ANÁLISE DE GÊNERO:
        - Como homens e mulheres são tratados diferentemente na família?
        - Há papéis de gênero rígidos?
        - Que expectativas diferentes existem para cada gênero?
        
        4. EIXOS VERTICAIS (HERANÇA):
        - Que segredos familiares atravessam gerações?
        - Que traumas não resolvidos estão sendo transmitidos?
        - Quais valores/crenças passam de geração em geração?
        
        5. EIXOS HORIZONTAIS (ATUAL):
        - Que transições atuais estão criando estresse?
        - Como os padrões antigos estão sendo ativados agora?
        
        6. RECURSOS E FORTALEZAS:
        - Que recursos a família possui?
        - Há padrões positivos a serem fortalecidos?
        - Quem são os membros mais resilientes?
        
        7. SUGESTÕES TERAPÊUTICAS:
        - Que intervenções poderiam ajudar a quebrar padrões disfuncionais?
        - Como fortalecer recursos existentes?
        - Que triangulações precisam ser abordadas prioritariamente?
        
        Organize sua análise de forma clara e construtiva, sempre considerando a 
        perspectiva da pessoa que criou o genetograma.
        """
        
        resposta = self._executar_task(prompt)
        
        triangulacoes = self._identificar_triangulacoes_detalhadas(dados_genetograma)
        recursos = self._identificar_recursos(dados_genetograma)
        
        return {
            "analise_completa": resposta,
            "triangulacoes_detectadas": triangulacoes,
            "recursos_familiares": recursos,
            "padroes_prioritarios": self._priorizar_padroes(resposta),
            "agente": "padrao_analyzer",
            "tipo": "analise_genetograma"
        }
    
    def sugerir_intervencoes(self, padroes_identificados: List[str], contexto_pessoa: str) -> Dict[str, Any]:
        """Sugere intervenções terapêuticas baseadas nos padrões identificados"""
        
        prompt = f"""
        Baseado nestes padrões familiares identificados:
        {padroes_identificados}
        
        Contexto da pessoa: {contexto_pessoa}
        
        Sugira intervenções terapêuticas sistêmicas apropriadas:
        
        1. INTERVENÇÕES PARA TRIANGULAÇÕES:
        - Como a pessoa pode sair de triangulações disfuncionais?
        - Que relacionamentos diretos precisam ser desenvolvidos?
        
        2. QUEBRA DE PADRÕES REPETITIVOS:
        - Que comportamentos alternativos podem ser experimentados?
        - Como conscientemente escolher diferentes caminhos?
        
        3. FORTALECIMENTO DE RECURSOS:
        - Como utilizar melhor os recursos familiares existentes?
        - Que relacionamentos positivos podem ser fortalecidos?
        
        4. TRABALHO COM DIFERENCIAÇÃO:
        - Como a pessoa pode se diferenciar sem se desconectar?
        - Que limites saudáveis podem ser estabelecidos?
        
        5. RITUAIS E PRÁTICAS:
        - Há rituais familiares que poderiam ser modificados?
        - Que novas tradições poderiam ser criadas?
        
        Apresente as sugestões como possibilidades para reflexão, não como 
        obrigações. Seja sensível ao ritmo e capacidade da pessoa.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "intervencoes_sugeridas": resposta,
            "agente": "padrao_analyzer",
            "tipo": "sugestoes_intervencao"
        }
    
    def _extrair_padroes(self, analise_texto: str) -> List[str]:
        """Extrai padrões específicos do texto de análise"""
        # Implementação simplificada - em produção seria mais sofisticada
        padroes = []
        
        keywords_padroes = [
            "triangulação", "coalição", "papéis rígidos", "lealdade invisível",
            "padrão repetitivo", "herança emocional", "segredo familiar"
        ]
        
        for keyword in keywords_padroes:
            if keyword in analise_texto.lower():
                padroes.append(keyword)
        
        return padroes
    
    def _identificar_triangulacoes_detalhadas(self, dados_genetograma: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identifica triangulações específicas no genetograma"""
        triangulacoes = []
        
        # Lógica para identificar padrões triangulares
        # Em implementação real, seria baseada nos relacionamentos mapeados
        
        return triangulacoes
    
    def _identificar_recursos(self, dados_genetograma: Dict[str, Any]) -> List[str]:
        """Identifica recursos e forças na família"""
        recursos = []
        
        # Lógica para identificar relacionamentos positivos, 
        # membros resilientes, tradições saudáveis, etc.
        
        return recursos
    
    def _priorizar_padroes(self, analise_texto: str) -> List[str]:
        """Prioriza os padrões mais importantes para trabalhar"""
        # Lógica para identificar quais padrões têm maior impacto atual
        return []
    
    def comparar_com_ciclo_vida(self, idade_pessoa: int, situacao_atual: str) -> Dict[str, Any]:
        """Compara a situação atual com tarefas esperadas do ciclo de vida"""
        
        # Determinar estágio do ciclo de vida baseado na idade e situação
        estagio_esperado = self._determinar_estagio_ciclo_vida(idade_pessoa, situacao_atual)
        
        prompt = f"""
        Pessoa com {idade_pessoa} anos, situação atual: {situacao_atual}
        
        Estágio esperado do ciclo de vida: {estagio_esperado}
        
        Analise:
        1. A pessoa está alinhada com as tarefas desenvolvimentais esperadas?
        2. Há descompasso entre idade cronológica e emocional?
        3. Que tarefas do ciclo de vida podem estar sendo evitadas?
        4. Como padrões familiares podem estar interferindo no desenvolvimento?
        5. Que apoio é necessário para avançar desenvolimentalmente?
        
        Base sua análise na teoria do ciclo de vida familiar de Carter & McGoldrick.
        """
        
        resposta = self._executar_task(prompt)
        
        return {
            "analise_ciclo_vida": resposta,
            "estagio_atual": estagio_esperado,
            "agente": "padrao_analyzer",
            "tipo": "comparacao_ciclo_vida"
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

    def _determinar_estagio_ciclo_vida(self, idade: int, situacao: str) -> str:
        """Determina o estágio do ciclo de vida baseado em idade e situação"""
        
        estagios = CONCEITOS_FUNDAMENTAIS.get("estagios_ciclo_vida", {})
        
        if idade < 25:
            return "1_jovem_adulto"
        elif idade < 35 and "casamento" in situacao.lower():
            return "2_formacao_casal"
        elif "filhos pequenos" in situacao.lower():
            return "3_filhos_pequenos"
        elif "adolescentes" in situacao.lower():
            return "4_filhos_adolescentes"
        elif idade > 45 and "filhos saindo" in situacao.lower():
            return "5_saida_filhos"
        elif idade > 60:
            return "6_idade_tardia"
        else:
            return "transicao"  # Entre estágios
    
    def get_agent(self):
        """Retorna o agente CrewAI para uso no orquestrador"""
        return self.agent
