"""
Base de conhecimento dos quebra-gelos terapêuticos
Baseado no trabalho desenvolvido para o GPT de Apoio Emocional
"""

QUEBRA_GELOS = {
    "transicoes_atuais": {
        "pergunta": "O que mudou recentemente na sua família que parece ter mudado tudo dentro de você também?",
        "foco": "Transições normativas ou inesperadas (nascimento, morte, separação, aposentadoria)",
        "base_teorica": "Estressores horizontais e momentos de ruptura nos ciclos",
        "objetivo": "Investigar o ponto de transição atual do usuário",
        "followup_questions": [
            "Como essa mudança tem afetado seu dia a dia?",
            "Que sentimentos têm surgido com mais frequência?",
            "Há algo que você gostaria que voltasse a ser como antes?"
        ]
    },
    
    "padroes_familiares": {
        "pergunta": "Você sente que está repetindo alguma história ou padrão que vem da sua família de origem?",
        "foco": "Heranças emocionais, triangulações, padrões verticais",
        "base_teorica": "Eixo vertical de ansiedade emocional e legado multigeracional",
        "objetivo": "Explorar padrões herdados e contexto histórico familiar",
        "followup_questions": [
            "Que semelhanças você vê entre sua vida e a de seus pais/avós?",
            "Há algo que você jurou que nunca faria, mas se vê fazendo?",
            "Que histórias da sua família você conhece que podem estar se repetindo?"
        ]
    },
    
    "papeis_familiares": {
        "pergunta": "Qual papel você sempre teve na sua família — e ainda está tentando manter, mesmo que esteja te fazendo mal?",
        "foco": "Papéis rígidos, expectativas invisíveis, lealdades familiares",
        "base_teorica": "Desconforto entre papéis esperados e identidade real",
        "objetivo": "Trazer à tona as amarras emocionais e as disfunções sutis",
        "followup_questions": [
            "Como você se sente quando não consegue cumprir esse papel?",
            "O que aconteceria se você parasse de fazer isso?",
            "Quem mais na família desempenha papéis similares?"
        ]
    },
    
    "perdas_transformacoes": {
        "pergunta": "Você sente que está perdendo alguém ou alguma parte de si mesmo nessa fase da vida?",
        "foco": "Lutos simbólicos, redefinição de identidade, ninho vazio, separações",
        "base_teorica": "Tarefas emocionais ligadas à perda e reorganização",
        "objetivo": "Trabalhar o impacto emocional das perdas e transformações",
        "followup_questions": [
            "O que você mais sente falta de como era antes?",
            "Há algo novo em você que está emergindo?",
            "Como você está lidando com essa transformação?"
        ]
    },
    
    "genetograma_intro": {
        "pergunta": "Se você pudesse desenhar sua família como um mapa emocional, o que seria impossível deixar de fora?",
        "foco": "Ativação da memória emocional e afetiva para início do genetograma",
        "base_teorica": "Mapeamento sistêmico multigeracional de Carter & McGoldrick",
        "objetivo": "Ajudar o usuário a sair da paralisia de 'por onde começo?' e ativar a memória emocional",
        "followup_questions": [
            "Quem mais impactou sua vida emocionalmente - positiva ou negativamente?",
            "Que relações familiares você considera mais intensas?",
            "Há segredos familiares que ainda influenciam as relações hoje?"
        ]
    }
}

def get_quebra_gelo_by_context(context: str) -> dict:
    """Retorna o quebra-gelo mais apropriado baseado no contexto da conversa"""
    context_mapping = {
        "transicao": "transicoes_atuais",
        "mudanca": "transicoes_atuais", 
        "padrao": "padroes_familiares",
        "repeticao": "padroes_familiares",
        "papel": "papeis_familiares",
        "responsabilidade": "papeis_familiares",
        "perda": "perdas_transformacoes",
        "luto": "perdas_transformacoes",
        "genetograma": "genetograma_intro",
        "mapa": "genetograma_intro"
    }
    
    for key, quebra_gelo_key in context_mapping.items():
        if key in context.lower():
            return QUEBRA_GELOS[quebra_gelo_key]
    
    # Default: retorna o quebra-gelo de transições atuais
    return QUEBRA_GELOS["transicoes_atuais"]

def get_all_quebra_gelos() -> dict:
    """Retorna todos os quebra-gelos disponíveis"""
    return QUEBRA_GELOS
