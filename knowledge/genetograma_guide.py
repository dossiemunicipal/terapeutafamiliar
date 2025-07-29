"""
Guia completo para criação de Genetograma
Baseado na metodologia de Carter & McGoldrick
"""

GENETOGRAMA_GUIDE = {
    "introducao": {
        "titulo": "Como montar seu Genetograma (com profundidade emocional)",
        "descricao": "Este guia orienta a criação de um genetograma clínico conforme a abordagem de Carter & McGoldrick.",
        "objetivo": "Mapear o impacto emocional, não apenas a cronologia familiar."
    },
    
    "etapa_1": {
        "titulo": "Estrutura básica (família de origem e atual)",
        "instrucoes": [
            "Desenhe você mesmo ao centro (quadrado se homem, círculo se mulher)",
            "Adicione seus pais acima, conectados com uma linha de casal",
            "Inclua seus irmãos, se houver, da esquerda para a direita (mais velho à esquerda)",
            "Coloque filhos abaixo de você, caso tenha",
            "Adicione parceiros atuais e antigos, se houver, com data de início e fim da relação"
        ],
        "simbolos": {
            "homem": "□ Quadrado",
            "mulher": "○ Círculo", 
            "falecido": "X sobre o símbolo",
            "casamento_forte": "Dupla linha",
            "uniao_informal": "Linha tracejada",
            "separacao": "Linha com corte",
            "relacao_conflituosa": "Zigzag ou raio"
        }
    },
    
    "etapa_2": {
        "titulo": "Informações vitais",
        "dados_necessarios": [
            "Nome completo",
            "Ano de nascimento e falecimento (se aplicável)", 
            "Profissão (ou papel predominante na família)",
            "Escolaridade",
            "Religião / crenças centrais",
            "Diagnóstico médico/psicológico (se houver e for relevante)",
            "Cidade onde viveu ou vive atualmente"
        ]
    },
    
    "etapa_3": {
        "titulo": "Eventos marcantes",
        "eventos_importantes": [
            "Casamentos e divórcios",
            "Adoções", 
            "Perdas (falecimentos importantes)",
            "Acidentes, traumas, mudanças drásticas (ex: migração)",
            "Doenças crônicas (físicas ou emocionais)",
            "Situações de dependência, violência, abuso ou abandono"
        ],
        "lembrete": "🧠 Lembre-se: você está mapeando o impacto emocional, não apenas a cronologia."
    },
    
    "etapa_4": {
        "titulo": "Padrões e vínculos emocionais",
        "perguntas_norteadoras": [
            "Quais relações eram muito próximas, simbióticas ou 'coladas'?",
            "Quais relações foram cortadas ou distantes?", 
            "Quem sempre resolvia os conflitos?",
            "Há padrões repetitivos (ex: mulheres cuidando de todos, homens ausentes, filhos que repetem o destino dos pais)?",
            "Há triangulações? (Ex: pai distante, mãe próxima demais do filho)"
        ],
        "exemplo": "🌀 Você pode marcar com uma linha grossa a relação mais intensa (positiva ou negativa). Ou setas para mostrar alianças ou conflitos."
    },
    
    "etapa_5": {
        "titulo": "Eixos verticais e horizontais",
        "eixo_vertical": {
            "nome": "Herança emocional",
            "pergunta": "Que padrões, segredos, traumas ou papéis parecem ter sido passados de geração para geração?"
        },
        "eixo_horizontal": {
            "nome": "Momento atual", 
            "pergunta": "O que está em crise agora? Quais transições estão ocorrendo na sua família (morte, nascimento, separação, mudança, aposentadoria)?"
        },
        "sintese": "✍️ Combine os dois para entender onde as emoções atuais estão conectadas ao passado familiar."
    },
    
    "etapa_6": {
        "titulo": "Reflexão final guiada",
        "perguntas_reflexivas": [
            "O que você descobriu que nunca tinha percebido?",
            "Há padrões que você quer manter? Quais precisa romper?",
            "Que emoções aparecem quando você olha esse mapa?",
            "Que lealdades invisíveis você pode estar carregando?"
        ]
    }
}

TRIANGULACOES_COMUNS = {
    "pai_mae_filho": {
        "descricao": "Pai distante, mãe próxima demais do filho",
        "impacto": "Filho pode ter dificuldades em relacionamentos íntimos",
        "sinais": ["Mãe confidenciando problemas conjugais ao filho", "Pai ausente emocionalmente", "Filho assumindo papel de 'marido emocional'"]
    },
    "avos_netos": {
        "descricao": "Avós interferindo na educação dos netos",
        "impacto": "Conflitos entre gerações, autoridade parental comprometida",
        "sinais": ["Regras diferentes entre casa dos pais e avós", "Criança manipulando diferenças", "Pais se sentindo desautorizados"]
    },
    "irmaos_pais": {
        "descricao": "Um irmão sendo o 'preferido' dos pais",
        "impacto": "Rivalidade fraterna, baixa autoestima no 'preterido'",
        "sinais": ["Comparações constantes", "Recursos emocionais/financeiros desiguais", "Papéis fixos (responsável vs irresponsável)"]
    }
}

def get_etapa_genetograma(etapa_numero: int) -> dict:
    """Retorna as instruções de uma etapa específica do genetograma"""
    etapa_key = f"etapa_{etapa_numero}"
    return GENETOGRAMA_GUIDE.get(etapa_key, {})

def get_all_etapas() -> dict:
    """Retorna todas as etapas do genetograma"""
    return GENETOGRAMA_GUIDE
