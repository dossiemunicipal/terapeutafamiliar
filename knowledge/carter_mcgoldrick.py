"""
Base de conhecimento principal do livro Carter & McGoldrick
"As mudanças no ciclo de vida familiar" - IMPLEMENTAÇÃO COMPLETA
"""

CONCEITOS_FUNDAMENTAIS = {
    "ciclo_vida_familiar": {
        "definicao": "Estrutura para compreender o desenvolvimento familiar ao longo do tempo, considerando transições previsíveis e imprevisíveis",
        "principios": [
            "A família é mais do que a soma de suas partes",
            "O ciclo de vida individual acontece dentro do ciclo de vida familiar",
            "O contexto familiar é primário para o desenvolvimento humano",
            "Sintomas aparecem quando há interrupção no ciclo desenvolvimental",
            "Cada estágio tem tarefas específicas que devem ser completadas",
            "Transições são os momentos mais vulneráveis para problemas",
            "Questões não resolvidas de estágios anteriores afetam estágios posteriores",
            "A perspectiva multigeracional é essencial para compreensão familiar"
        ]
    },
    
    "eixos_ansiedade": {
        "vertical": {
            "descricao": "Padrões de relacionamento transmitidos através das gerações",
            "componentes": [
                "Atitudes familiares herdadas",
                "Tabus e expectativas",
                "Rótulos e questões opressivas", 
                "Triangulações emocionais",
                "Segredos familiares",
                "Traumas não resolvidos"
            ],
            "mecanismo": "Transmissão através de triangulação emocional (Bowen)"
        },
        "horizontal": {
            "descricao": "Ansiedade gerada por transições atuais do ciclo de vida",
            "componentes": [
                "Transições normativas (casamento, nascimento, morte)",
                "Crises inesperadas (doença, acidente, perda de emprego)",
                "Mudanças desenvolvimentais",
                "Estressores externos (econômicos, sociais)"
            ],
            "caracteristica": "Eventos que requerem reorganização familiar"
        },
        "intersecao": "Quando eixos vertical e horizontal se encontram, há aumento significativo da ansiedade familiar"
    },
    
    "estagios_ciclo_vida": {
        "1_jovem_adulto": {
            "tarefa_principal": "Diferenciação do self em relação à família de origem",
            "idade_tipica": "18-35 anos",
            "marcos_desenvolvimento": [
                "Independência financeira e emocional",
                "Relacionamentos íntimos fora da família",
                "Estabelecimento de carreira/identidade profissional",
                "Desenvolvimento da própria visão de mundo",
                "Capacidade de intimidade sem fusão"
            ],
            "desafios_comuns": [
                "Separação vs. conexão com família origem",
                "Identidade própria vs. expectativas familiares",
                "Intimidade vs. isolamento",
                "Estabelecimento de limites saudáveis",
                "Lidar com pressões para casar/ter filhos"
            ],
            "tarefas_especificas": [
                "Sair da casa dos pais (física e emocionalmente)",
                "Estabelecer relacionamentos de adulto com pais",
                "Desenvolver rede social própria",
                "Tomar decisões importantes independentemente",
                "Preparar-se para compromisso conjugal"
            ],
            "sinais_travamento": [
                "Dependência excessiva dos pais após os 25 anos",
                "Incapacidade de manter relacionamentos íntimos",
                "Decisões importantes sempre dependem de aprovação parental",
                "Dificuldade de estabelecer carreira",
                "Relacionamentos apenas casuais ou fusionais"
            ]
        },
        "2_formacao_casal": {
            "tarefa_principal": "Criação de um novo sistema conjugal",
            "idade_tipica": "25-35 anos",
            "marcos_desenvolvimento": [
                "Compromisso mútuo duradouro",
                "Integração harmoniosa de famílias de origem",
                "Estabelecimento de padrões conjugais únicos",
                "Sistema de tomada de decisão conjunto",
                "Identidade como casal"
            ],
            "desafios_comuns": [
                "Negociação de diferenças culturais/familiares",
                "Lealdades divididas entre cônjuge e família origem",
                "Expectativas irreais sobre casamento",
                "Questões de poder e controle",
                "Diferenças de gênero no relacionamento"
            ],
            "tarefas_especificas": [
                "Formar sistema conjugal diferenciado das famílias origem",
                "Realinhar relacionamentos com famílias estendidas",
                "Fazer relacionamento conjugal primário",
                "Estabelecer padrões de intimidade e autonomia",
                "Criar tradições e rituais próprios do casal"
            ],
            "sinais_travamento": [
                "Um dos cônjuges ainda muito dependente dos pais",
                "Conflitos constantes sobre famílias de origem",
                "Incapacidade de tomar decisões como casal",
                "Triangulação frequente com parentes",
                "Relacionamento conjugal sempre secundário"
            ]
        },
        "3_filhos_pequenos": {
            "tarefa_principal": "Abertura do sistema para incluir filhos",
            "idade_tipica": "25-40 anos dos pais",
            "marcos_desenvolvimento": [
                "Assumir papéis parentais competentemente",
                "Realinhamento do relacionamento conjugal",
                "Integração das gerações (avós/pais/filhos)",
                "Divisão funcional de responsabilidades parentais",
                "Manutenção da intimidade conjugal"
            ],
            "desafios_comuns": [
                "Divisão equitativa de responsabilidades parentais",
                "Manutenção do tempo e intimidade do casal",
                "Estabelecimento de padrões educativos consistentes",
                "Relacionamento com avós sobre netos",
                "Equilibrio trabalho-família"
            ],
            "tarefas_especificas": [
                "Fazer espaço para filhos no sistema conjugal",
                "Assumir responsabilidades parentais",
                "Renegociar relacionamento conjugal",
                "Estabelecer relacionamentos com avós como avós",
                "Desenvolver filosofia parental"
            ],
            "sinais_travamento": [
                "Filhos sempre vêm antes do relacionamento conjugal",
                "Incapacidade de estabelecer rotinas familiares",
                "Conflitos constantes sobre educação dos filhos",
                "Avós interferindo excessivamente na educação",
                "Perda completa da intimidade conjugal"
            ]
        },
        "4_filhos_adolescentes": {
            "tarefa_principal": "Aumento da flexibilidade para permitir independência dos filhos",
            "idade_tipica": "40-55 anos dos pais",
            "marcos_desenvolvimento": [
                "Renegociação de autoridade parental",
                "Preparação para eventual saída dos filhos",
                "Resolução de questões de meia-idade",
                "Relacionamento mais igualitário com filhos",
                "Renovação da intimidade conjugal"
            ],
            "desafios_comuns": [
                "Controle vs. liberdade para adolescentes",
                "Manutenção de relacionamento conjugal durante crise adolescente",
                "Questões de carreira vs. família na meia-idade",
                "Relacionamento com filhos que estão se diferenciando",
                "Preparação para mudanças futuras"
            ],
            "tarefas_especificas": [
                "Aumentar flexibilidade das fronteiras familiares",
                "Incluir interesse dos adolescentes em autonomia",
                "Refocalizar questões conjugais e de carreira",
                "Lidar com questões de relacionamento com avós envelhecendo",
                "Preparar-se para estágio de saída dos filhos"
            ],
            "sinais_travamento": [
                "Controle excessivo ou permissividade total",
                "Incapacidade de renegociar regras familiares",
                "Conflitos constantes sem resolução",
                "Triangulação com adolescentes em conflitos conjugais",
                "Recusa a aceitar crescimento dos filhos"
            ]
        },
        "5_saida_filhos": {
            "tarefa_principal": "Aceitação da entrada e saída de membros do sistema familiar",
            "idade_tipica": "45-65 anos dos pais",
            "marcos_desenvolvimento": [
                "Renegociação do sistema conjugal como díade",
                "Desenvolvimento de relacionamento adulto-adulto com filhos",
                "Inclusão de genros/noras e netos",
                "Reaproximação com questões de casal",
                "Relacionamento com próprios pais envelhecendo"
            ],
            "desafios_comuns": [
                "Síndrome do ninho vazio",
                "Redefinição de identidade parental",
                "Renovação ou deterioração do relacionamento conjugal",
                "Relacionamentos com filhos adultos e suas famílias",
                "Cuidado com pais idosos"
            ],
            "tarefas_especificas": [
                "Renegociar sistema conjugal como díade",
                "Manter conexões de apoio com filhos adultos",
                "Incluir genros/noras no sistema familiar",
                "Tornar-se avós quando apropriado",
                "Lidar com incapacidades e morte dos próprios pais"
            ],
            "sinais_travamento": [
                "Incapacidade de deixar filhos partirem",
                "Deterioração severa do relacionamento conjugal",
                "Interferência excessiva na vida dos filhos adultos",
                "Recusa a aceitar genros/noras",
                "Depressão severa por perda do papel parental"
            ]
        },
        "6_idade_tardia": {
            "tarefa_principal": "Aceitação da mudança de papéis geracionais",
            "idade_tipica": "65+ anos",
            "marcos_desenvolvimento": [
                "Manutenção de funcionamento e interesses individuais e do casal",
                "Apoio para papel mais central da geração do meio",
                "Criação de espaço para sabedoria e experiência dos idosos",
                "Lidar com perda de cônjuge, irmãos e outros pares",
                "Preparação para própria morte"
            ],
            "desafios_comuns": [
                "Perda de autonomia física/cognitiva",
                "Revisão de vida e aceitação de escolhas",
                "Relacionamento com filhos adultos agora cuidadores",
                "Perda de cônjuge e pares",
                "Questões de legado e transmissão"
            ],
            "tarefas_especificas": [
                "Manter interesses próprios face a declínio físico",
                "Apoiar funcionamento da geração do meio sem interferir",
                "Lidar com perda de cônjuge, irmãos e pares",
                "Fazer revisão de vida e transmitir legado",
                "Preparar-se para morte"
            ],
            "sinais_travamento": [
                "Recusa a aceitar limitações físicas",
                "Depressão severa por perdas múltiplas",
                "Interferência excessiva na vida dos filhos",
                "Incapacidade de lidar com dependência crescente",
            ]
        }
    },
    
    "variacoes_ciclo_vida": {
        "divorcio_recasamento": {
            "ciclo_divorcio": {
                "pre_divorcio": {
                    "tarefas": [
                        "Aceitar que o casamento tem problemas sérios",
                        "Tentar resolver problemas conjugais",
                        "Considerar todas as alternativas",
                        "Tomar decisão consciente sobre divórcio"
                    ],
                    "sinais_inicio": [
                        "Conflitos frequentes sem resolução",
                        "Perda de intimidade emocional/física",
                        "Consideração de separação",
                        "Busca por terapia conjugal"
                    ]
                },
                "decisao_divorcio": {
                    "tarefas": [
                        "Aceitar a incapacidade de resolver diferenças conjugais",
                        "Aceitar a decisão de se divorciar",
                        "Trabalhar cooperativamente em questões legais",
                        "Planejar custódia e finanças"
                    ],
                    "desafios": [
                        "Culpa e raiva sobre fracasso conjugal",
                        "Medo sobre futuro financeiro",
                        "Preocupação com impacto nos filhos",
                        "Pressão familiar e social"
                    ]
                },
                "pos_divorcio": {
                    "tarefas": [
                        "Elaborar luto pelo casamento e sonhos conjugais",
                        "Reconstruir identidade individual",
                        "Manter relacionamento cooperativo como co-pais",
                        "Lidar com questões familiares estendidas"
                    ],
                    "objetivos": [
                        "Estabelecer novo estilo de vida",
                        "Desenvolver rede de apoio",
                        "Resolver questões de custódia",
                        "Preparar-se para possível recasamento"
                    ]
                }
            },
            "ciclo_recasamento": {
                "namoro_pos_divorcio": {
                    "tarefas": [
                        "Completar recuperação emocional do divórcio",
                        "Desenvolver capacidade de confiar novamente",
                        "Trabalhar questões sobre impacto nos filhos",
                        "Preparar-se para complexidade da família reconstituída"
                    ]
                },
                "casamento_formacao_familia": {
                    "tarefas": [
                        "Formar novo casal comprometido com família reconstituída",
                        "Aceitar medos e fantasias sobre recasamento",
                        "Planejar integração de filhos de relacionamentos anteriores",
                        "Estabelecer novas tradições familiares"
                    ]
                },
                "familia_reconstituida": {
                    "tarefas": [
                        "Integrar membros de famílias anteriores",
                        "Estabelecer novas regras e papéis familiares",
                        "Manter relacionamentos cooperativos com ex-cônjuges",
                        "Desenvolver identidade como nova família"
                    ],
                    "desafios_especificos": [
                        "Lealdades conflitantes das crianças",
                        "Disciplina e autoridade com enteados",
                        "Relacionamentos com múltiplas famílias",
                        "Questões financeiras complexas"
                    ]
                }
            }
        },
        "doenca_cronica": {
            "tipologia_psicossocial": {
                "inicio": {
                    "agudo": "Sintomas aparecem rapidamente (infarto, acidente)",
                    "gradual": "Sintomas se desenvolvem lentamente (artrite, diabetes)"
                },
                "curso": {
                    "progressivo": "Piora contínua e irreversível (Alzheimer, ELA)",
                    "constante": "Estável após período inicial (paralisia)",
                    "episodico": "Períodos de crise alternados com estabilidade (epilepsia)"
                },
                "consequencias": {
                    "fatal": "Pode causar morte prematura (câncer, AIDS)",
                    "encurtamento_vida": "Reduz expectativa de vida (diabetes, cardiopatia)",
                    "nao_fatal": "Não afeta significativamente longevidade (artrite)"
                },
                "incapacitacao": {
                    "nenhuma": "Sem limitações funcionais significativas",
                    "leve": "Algumas limitações em atividades específicas",
                    "moderada": "Limitações importantes mas ainda independente",
                    "severa": "Dependência significativa para atividades diárias"
                }
            },
            "fases_temporais": {
                "fase_crise": {
                    "tarefas_familia": [
                        "Aprender a lidar com dor, incapacitação e sintomas",
                        "Aprender a lidar com ambiente hospitalar e procedimentos",
                        "Estabelecer relacionamento com equipe médica",
                        "Criar significado para a doença que preserve senso de domínio",
                        "Reorganizar temporariamente para acomodar doença"
                    ],
                    "duracao": "Período agudo inicial até estabilização"
                },
                "fase_cronica": {
                    "tarefas_familia": [
                        "Estabelecer rotina diária que acomode limitações",
                        "Manter intimidade e proximidade apesar da doença",
                        "Preservar autonomia de todos os membros familiares",
                        "Distribuir responsabilidades de cuidado",
                        "Manter relacionamento com mundo exterior"
                    ],
                    "duracao": "Período de adaptação de longo prazo"
                },
                "fase_terminal": {
                    "tarefas_familia": [
                        "Aceitar realidade da morte iminente",
                        "Completar questões inacabadas com pessoa morrendo",
                        "Preparar-se para período de luto",
                        "Apoiar pessoa doente em sua preparação para morte",
                        "Reorganizar-se para período pós-morte"
                    ],
                    "duracao": "Período de deterioração até morte"
                }
            },
            "interface_ciclo_vida": {
                "principios": [
                    "Timing da doença em relação ao estágio familiar é crucial",
                    "Doença crônica requer adaptação das tarefas desenvolvimentais",
                    "Família deve reorganizar-se para acomodar doença como 'novo membro'",
                    "Padrões de funcionamento familiar influenciam adaptação à doença",
                    "Doença pode tanto paralisar quanto catalisar desenvolvimento familiar"
                ],
                "adaptacoes_por_estagio": {
                    "jovem_adulto": "Doença pode interferir com diferenciação e intimidade",
                    "formacao_casal": "Teste prematuro dos votos 'na saúde e na doença'",
                    "filhos_pequenos": "Reorganização de papéis parentais e cuidado",
                    "filhos_adolescentes": "Conflito entre necessidades independência e cuidado",
                    "saida_filhos": "Filhos podem retardar saída para cuidar dos pais",
                    "idade_tardia": "Doença vista como parte natural do envelhecimento"
                }
            }
        },
        "familias_monoparentais": {
            "caracteristicas": [
                "Um genitor assume responsabilidade primária pelos filhos",
                "Necessidade de rede de apoio mais ampla",
                "Desafios específicos de disciplina e autoridade",
                "Questões econômicas frequentemente mais intensas"
            ],
            "tarefas_especificas": [
                "Estabelecer autoridade parental sem apoio de parceiro",
                "Criar rede de apoio substituta",
                "Lidar com próprias necessidades emocionais/sociais",
                "Proteger filhos de triangulação excessiva",
                "Manter esperança sobre relacionamentos futuros"
            ],
            "desafios_comuns": [
                "Sobrecarga do genitor responsável",
                "Filhos assumindo papéis adultos prematuramente",
                "Isolamento social da família",
                "Dificuldades financeiras",
                "Triangulação com filhos sobre questões adultas"
            ]
        },
        "familias_culturais_especificas": {
            "familias_negras_pobres": {
                "caracteristicas_ciclo": [
                    "Ciclo de vida truncado (eventos mais cedo)",
                    "Frequentemente chefiadas por mulheres",
                    "Estresse imprevisível constante",
                    "Dependência de apoio institucional"
                ],
                "adaptacoes_necessarias": [
                    "Reconhecer força na adaptação à adversidade",
                    "Valorizar papel da família estendida",
                    "Considerar impacto de fatores socioeconômicos",
                    "Adaptar expectativas de timing desenvolvimental"
                ]
            },
            "familias_profissionais": {
                "caracteristicas_ciclo": [
                    "Adiamento significativo de marcos (casamento, filhos)",
                    "Priorização de carreira sobre família inicialmente",
                    "Recursos econômicos facilitam transições",
                    "Expectativas altas sobre desempenho familiar"
                ],
                "desafios_especificos": [
                    "Conflito trabalho-família intensificado",
                    "Perfeccionismo nas transições familiares",
                    "Menor rede de apoio familiar tradicional",
                    "Pressão para otimizar desenvolvimento dos filhos"
                ]
            }
        }
    },
    
    "genero_ciclo_vida": {
        "diferencias_masculino_feminino": {
            "desenvolvimento_masculino": [
                "Enfase na autonomia e separação",
                "Identidade através do trabalho e conquistas",
                "Dificuldade com intimidade emocional",
                "Papel tradicional de provedor"
            ],
            "desenvolvimento_feminino": [
                "Identidade através de relacionamentos",
                "Capacidade de conexão e cuidado", 
                "Conflito trabalho vs. família",
                "Expectativas de cuidadora principal"
            ]
        },
        "impactos_familia": [
            "Mulheres frequentemente sobrecarregadas emocionalmente",
            "Homens podem ser periféricos nas relações familiares",
            "Necessidade de renegociar papéis tradicionais",
            "Importância de partnerships igualitários"
        ]
    }
}

TRIANGULACOES_FAMILIARES = {
    "definicao": "Padrão relacional de três pessoas onde tensão entre duas é desviada através da terceira",
    "tipos_comuns": {
        "pai_mae_filho": {
            "descricao": "Conflito conjugal desviado através dos filhos",
            "dinamica": "Pais evitam conflitos diretos usando filho como foco",
            "sinais": [
                "Filho sempre envolvido em discussões dos pais",
                "Pais discutem sobre filho mas não sobre relacionamento",
                "Filho apresenta sintomas quando pais estão em conflito",
                "Um dos pais se alia ao filho contra o outro"
            ],
            "impacto_filho": [
                "Ansiedade excessiva sobre problemas familiares",
                "Dificuldade de separação na adolescência/idade adulta",
                "Problemas de intimidade em relacionamentos próprios",
                "Senso exagerado de responsabilidade pela família"
            ]
        },
        "sogra_genro_filha": {
            "descricao": "Lealdades conflitantes entre família origem e conjugal",
            "dinamica": "Conflito entre lealdade aos pais vs. lealdade ao cônjuge",
            "sinais": [
                "Cônjuge sempre criticado pela família de origem",
                "Pessoa no meio defendendo ora pais, ora cônjuge",
                "Visitas familiares sempre criam tensão no casal",
                "Decisões familiares sempre envolvem opinião dos pais"
            ],
            "impacto": [
                "Deterioração do relacionamento conjugal",
                "Ressentimento crescente de ambos os lados",
                "Filhos confusos sobre lealdades familiares",
                "Isolamento progressivo do casal"
            ]
        },
        "irmaos_pais": {
            "descricao": "Competição entre irmãos por aprovação parental",
            "dinamica": "Pais triangulam conflitos através de comparações entre filhos",
            "sinais": [
                "Pais sempre comparando filhos",
                "Um filho é 'bom', outro é 'problema'",
                "Irmãos competem por atenção ao invés de se aliarem",
                "Conflitos entre irmãos servem para distrair de problemas parentais"
            ],
            "impacto": [
                "Rivalidade fraterna que persiste na idade adulta",
                "Baixa autoestima no filho 'preterido'",
                "Sobrecarga de responsabilidade no filho 'preferido'",
                "Dificuldade de relacionamentos fraternos saudáveis"
            ]
        },
        "trabalho_familia": {
            "descricao": "Conflitos familiares expressos através de problemas profissionais",
            "dinamica": "Pessoa usa trabalho para evitar problemas familiares",
            "sinais": [
                "Workaholismo como fuga de conflitos domésticos",
                "Problemas no trabalho sempre coincidindo com crises familiares",
                "Família culpando trabalho por todos os problemas",
                "Cônjuge/filhos competindo com trabalho por atenção"
            ],
            "impacto": [
                "Deterioração tanto no trabalho quanto na família",
                "Problemas nunca são realmente resolvidos",
                "Pessoa se sente incompetente em ambas as áreas",
                "Família não desenvolve habilidades de resolução de conflitos"
            ]
        },
        "doenca_familia": {
            "descricao": "Membro doente é triangulado nos conflitos familiares",
            "dinamica": "Doença serve para estabilizar sistema familiar disfuncional",
            "sinais": [
                "Sintomas pioram quando há conflitos familiares",
                "Família se une apenas quando há crise médica",
                "Pessoa doente se sente culpada quando está melhor",
                "Conflitos familiares são evitados 'para não piorar' o doente"
            ],
            "impacto": [
                "Recuperação é inconscientemente sabotada",
                "Família não desenvolve outras formas de coesão",
                "Pessoa doente perde senso de identidade além da doença",
                "Outros problemas familiares nunca são abordados"
            ]
        },
        "avos_pais_netos": {
            "descricao": "Avós interferem na relação pais-filhos",
            "dinamica": "Conflitos intergeracionais expressos através dos netos",
            "sinais": [
                "Avós contradizem regras estabelecidas pelos pais",
                "Netos usam diferenças para manipular situações",
                "Pais se sentem desautorizados pelos próprios pais",
                "Crianças recebem mensagens conflitantes sobre comportamento"
            ],
            "impacto": [
                "Autoridade parental minada",
                "Confusão de valores e regras para as crianças",
                "Relacionamento pais-avós deteriora",
                "Crianças aprendem a manipular diferenças adultas"
            ]
        },
        "ex_conjuge_atual": {
            "descricao": "Ex-cônjuge triangulado em novo relacionamento",
            "dinamica": "Problemas do novo casal são canalizados através de questões com ex",
            "sinais": [
                "Conflitos sempre envolvem comparações com ex-cônjuge",
                "Questões financeiras/custódia dominam relacionamento atual",
                "Novo cônjuge sente-se em competição com ex",
                "Filhos usados como mensageiros entre casas"
            ],
            "impacto": [
                "Novo relacionamento não consegue se estabelecer",
                "Filhos se sentem leais divididas",
                "Recuperação emocional do divórcio é impedida",
                "Conflitos se perpetuam através das gerações"
            ]
        },
        "adicao_familia": {
            "descricao": "Vício funciona como terceiro membro do sistema familiar",
            "dinamica": "Família se organiza em torno da adição, evitando outros problemas",
            "sinais": [
                "Todos os problemas familiares são atribuídos à adição",
                "Família tem papéis rígidos (viciado, salvador, bode expiatório)",
                "Recuperação cria crise porque sistema precisa se reorganizar",
                "Recaídas coincidem com outras crises familiares"
            ],
            "impacto": [
                "Família não desenvolve habilidades de enfrentamento saudáveis",
                "Outros membros podem desenvolver co-dependência",
                "Recuperação é sabotada inconscientemente",
                "Problemas relacionais subjacentes não são abordados"
            ]
        },
        "genero_conflitos": {
            "descricao": "Conflitos são organizados em linhas de gênero",
            "dinamica": "Homens vs. mulheres ao invés de resolver questões específicas",
            "sinais": [
                "Conflitos sempre se tornam 'homens não entendem' vs. 'mulheres são complicadas'",
                "Alianças sempre seguem linhas de gênero",
                "Questões específicas são perdidas em generalizações sobre gênero",
                "Filhos aprendem estereótipos rígidos sobre papéis masculinos/femininos"
            ],
            "impacto": [
                "Questões reais nunca são abordadas",
                "Perpetuação de estereótipos de gênero",
                "Filhos desenvolvem expectativas irreais sobre relacionamentos",
                "Perdida oportunidade de desenvolvimento de empatia mútua"
            ]
        },
        "dinheiro_poder": {
            "descricao": "Questões financeiras mascarando conflitos de poder",
            "dinamica": "Conflitos sobre dinheiro evitam discussões sobre poder/controle",
            "sinais": [
                "Todas as discussões se tornam sobre dinheiro",
                "Quem ganha mais tem mais 'direitos' nas decisões",
                "Filhos aprendem que valor pessoal = valor financeiro",
                "Questões emocionais são traduzidas em termos monetários"
            ],
            "impacto": [
                "Questões de intimidade e poder não são resolvidas",
                "Relacionamentos se tornam transacionais",
                "Filhos desenvolvem valores materialísticos",
                "Família não desenvolve formas saudáveis de negociação"
            ]
        }
    },
    "sinais_triangulacao": [
        "Terceira pessoa sempre envolvida em conflitos de dois",
        "Dificuldade de relacionamento direto entre duas pessoas",
        "Sintomas em membro mais frágil do triângulo",
        "Segredos mantidos por coalições",
        "Alianças que excluem terceiros",
        "Pessoa no meio carregando mensagens entre outros dois",
        "Conflitos que se espalham ao invés de serem resolvidos",
        "Foco nos sintomas/comportamento ao invés de padrões relacionais"
    ],
    "estrategias_detriangulacao": {
        "reconhecimento": [
            "Identificar o padrão triangular específico",
            "Compreender a função que serve no sistema familiar",
            "Reconhecer como cada pessoa contribui para manter o triângulo",
            "Identificar benefícios secundários da triangulação"
        ],
        "intervencoes": [
            "Encorajar relacionamentos diretos entre duas pessoas",
            "Recusar-se a carregar mensagens entre outros",
            "Desenvolver posição pessoal clara em questões importantes",
            "Estabelecer limites apropriados nos relacionamentos",
            "Focar na própria parte no padrão ao invés de culpar outros"
        ],
        "manutencao": [
            "Praticar consistentemente comunicação direta",
            "Desenvolver tolerância à ansiedade dos outros sobre mudança",
            "Manter foco no que pode ser controlado (próprio comportamento)",
            "Criar rituais familiares que promovam relacionamentos diretos",
            "Buscar apoio para manter mudanças a longo prazo"
        ]
    }
}

INTERVENCOES_TERAPEUTICAS = {
    "genetograma": {
        "objetivo": "Mapear padrões familiares multigeracionais",
        "tecnica": "Representação gráfica de pelo menos três gerações",
        "beneficios": ["Visualização de padrões", "Identificação de recursos", "Compreensão histórica"],
        "aplicacao_por_estagio": {
            "jovem_adulto": "Identificar padrões familiares que podem interferir com diferenciação",
            "formacao_casal": "Compreender heranças familiares que ambos trazem para o relacionamento",
            "filhos_pequenos": "Mapear estilos parentais transmitidos através das gerações",
            "filhos_adolescentes": "Identificar padrões de separação/individualização na família",
            "saida_filhos": "Compreender como gerações anteriores lidaram com esta transição",
            "idade_tardia": "Revisar vida familiar e identificar legado a ser transmitido"
        }
    },
    "detriangulacao": {
        "objetivo": "Quebrar padrões triangulares disfuncionais",
        "tecnica": "Encorajar relacionamentos diretos entre duas pessoas",
        "etapas": ["Identificar triângulo", "Compreender função", "Criar relacionamentos diretos"],
        "estrategias_especificas": {
            "posicao_eu": "Desenvolver posições claras sem atacar ou se defender",
            "relacionamentos_diretos": "Comunicar-se diretamente com pessoa envolvida",
            "recusa_mensageiro": "Não carregar mensagens entre outros dois membros",
            "limites_claros": "Estabelecer o que se está disposto ou não a fazer",
            "foco_proprio": "Mudar próprio comportamento ao invés de tentar mudar outros"
        }
    },
    "rituais_transicao": {
        "objetivo": "Facilitar passagem entre estágios do ciclo de vida",
        "tipos": ["Rituais de separação", "Rituais de iniciação", "Rituais de integração"],
        "componentes": ["Reconhecimento da mudança", "Simbolismo", "Participação familiar"],
        "exemplos_por_transicao": {
            "saida_casa": "Cerimônia de 'lançamento' reconhecendo maturidade",
            "casamento": "Ritual que integra duas famílias de origem",
            "nascimento_filho": "Celebração que reconhece novos papéis parentais",
            "divorcio": "Ritual de finalização que honra o que foi bom no casamento",
            "morte": "Funeral que permite elaboração do luto e continuidade familiar"
        }
    },
    "trabalho_genero": {
        "objetivo": "Abordar diferenças de gênero no desenvolvimento familiar",
        "areas_foco": [
            "Expectativas diferentes para homens e mulheres",
            "Padrões de comunicação específicos de gênero",
            "Conflitos trabalho-família diferenciados por gênero",
            "Modelos de relacionamento baseados em estereótipos"
        ],
        "intervencoes": [
            "Questionar papéis de gênero rígidos",
            "Promover desenvolvimento de empatia entre gêneros",
            "Encorajar comunicação direta sobre expectativas",
            "Desenvolver modelos relacionais mais flexíveis"
        ]
    },
    "terapia_multigeracional": {
        "objetivo": "Trabalhar questões que atravessam múltiplas gerações",
        "tecnicas": [
            "Entrevistas com múltiplas gerações",
            "Exploração de segredos familiares",
            "Identificação de padrões repetitivos",
            "Trabalho com lealdades invisíveis"
        ],
        "aplicacoes": [
            "Traumas não resolvidos transmitidos através de gerações",
            "Padrões de doença mental/física familiares",
            "Conflitos não resolvidos entre gerações",
            "Recursos familiares não utilizados"
        ]
    },
    "coaching_ciclo_vida": {
        "objetivo": "Auxiliar famílias a navegar transições específicas",
        "metodologia": [
            "Educação sobre tarefas desenvolvimentais normais",
            "Identificação de recursos familiares existentes",
            "Desenvolvimento de habilidades específicas para estágio",
            "Preparação para próximas transições"
        ],
        "areas_especializacao": {
            "preparacao_casamento": "Preparar casais para desafios específicos do casamento",
            "educacao_parental": "Desenvolver habilidades parentais apropriadas por estágio",
            "preparacao_aposentadoria": "Ajudar casais a se preparar para mudanças da aposentadoria",
            "cuidado_idosos": "Auxiliar famílias no cuidado de membros idosos"
        }
    }
}

# Funções auxiliares expandidas
def get_conceito(nome_conceito: str) -> dict:
    """Retorna informações sobre um conceito específico"""
    return CONCEITOS_FUNDAMENTAIS.get(nome_conceito, {})

def get_estagio_ciclo_vida(estagio: str) -> dict:
    """Retorna informações sobre um estágio específico do ciclo de vida"""
    estagios = CONCEITOS_FUNDAMENTAIS.get("estagios_ciclo_vida", {})
    return estagios.get(estagio, {})

def get_triangulacao_info() -> dict:
    """Retorna informações sobre triangulações familiares"""
    return TRIANGULACOES_FAMILIARES

def determinar_estagio_por_idade_situacao(idade: int, situacao_familiar: str) -> dict:
    """Determina estágio do ciclo de vida baseado em idade e situação familiar"""
    estagio_identificado = None
    
    # Lógica básica de identificação
    if idade < 25:
        estagio_identificado = "1_jovem_adulto"
    elif 25 <= idade < 35:
        if any(palavra in situacao_familiar.lower() for palavra in ["casado", "casamento", "casal", "esposo", "esposa"]):
            if any(palavra in situacao_familiar.lower() for palavra in ["filho", "filha", "bebê", "criança"]):
                estagio_identificado = "3_filhos_pequenos"
            else:
                estagio_identificado = "2_formacao_casal"
        else:
            estagio_identificado = "1_jovem_adulto"
    elif 35 <= idade < 50:
        if any(palavra in situacao_familiar.lower() for palavra in ["adolescente", "teenager", "ensino médio"]):
            estagio_identificado = "4_filhos_adolescentes"
        elif any(palavra in situacao_familiar.lower() for palavra in ["filho", "filha", "criança"]):
            estagio_identificado = "3_filhos_pequenos"
        else:
            estagio_identificado = "2_formacao_casal"
    elif 50 <= idade < 65:
        if any(palavra in situacao_familiar.lower() for palavra in ["saindo", "faculdade", "independente", "ninho vazio"]):
            estagio_identificado = "5_saida_filhos"
        else:
            estagio_identificado = "4_filhos_adolescentes"
    else:
        estagio_identificado = "6_idade_tardia"
    
    if estagio_identificado:
        return {
            "estagio": estagio_identificado,
            "detalhes": get_estagio_ciclo_vida(estagio_identificado),
            "idade_pessoa": idade,
            "situacao_descrita": situacao_familiar
        }
    
    return {"erro": "Não foi possível determinar estágio"}

def identificar_variacoes_aplicaveis(situacao_familiar: str) -> list:
    """Identifica variações do ciclo de vida aplicáveis à situação"""
    variacoes = []
    situacao_lower = situacao_familiar.lower()
    
    if any(palavra in situacao_lower for palavra in ["divórcio", "divorcio", "separação", "separacao", "ex-"]):
        variacoes.append("divorcio_recasamento")
    
    if any(palavra in situacao_lower for palavra in ["doença", "doenca", "câncer", "cancer", "diabetes", "depressão"]):
        variacoes.append("doenca_cronica")
    
    if any(palavra in situacao_lower for palavra in ["mãe solteira", "pai solteiro", "monoparental"]):
        variacoes.append("familias_monoparentais")
    
    if any(palavra in situacao_lower for palavra in ["pobre", "baixa renda", "assistência", "desemprego"]):
        variacoes.append("familias_negras_pobres")
    
    if any(palavra in situacao_lower for palavra in ["médico", "advogado", "professor", "engenheiro", "pós-graduação"]):
        variacoes.append("familias_profissionais")
    
    return variacoes

def avaliar_cumprimento_tarefas_estagio(estagio: str, situacao_atual: str) -> dict:
    """Avalia se as tarefas do estágio estão sendo cumpridas adequadamente"""
    detalhes_estagio = get_estagio_ciclo_vida(estagio)
    if not detalhes_estagio:
        return {"erro": "Estágio não encontrado"}
    
    tarefas = detalhes_estagio.get("tarefas_especificas", [])
    sinais_travamento = detalhes_estagio.get("sinais_travamento", [])
    
    # Análise básica baseada em palavras-chave
    tarefas_cumpridas = []
    possivel_travamento = []
    
    for tarefa in tarefas:
        # Lógica simplificada - em implementação real seria mais sofisticada
        if "independência" in tarefa.lower() and "independente" in situacao_atual.lower():
            tarefas_cumpridas.append(tarefa)
    
    for sinal in sinais_travamento:
        # Lógica simplificada para detectar sinais de travamento
        if "dependência" in sinal.lower() and "dependente" in situacao_atual.lower():
            possivel_travamento.append(sinal)
    
    return {
        "estagio": estagio,
        "tarefas_identificadas_cumpridas": tarefas_cumpridas,
        "sinais_travamento_detectados": possivel_travamento,
        "recomendacoes": f"Focar nas tarefas específicas do estágio {estagio} e abordar possíveis travamentos identificados"
    }

def identificar_triangulacoes_ativas(situacao_familiar: str) -> list:
    """Identifica possíveis triangulações ativas baseadas na descrição familiar"""
    triangulacoes_detectadas = []
    
    situacao_lower = situacao_familiar.lower()
    
    # Buscar padrões de triangulação
    padroes_triangulacao = {
        "pai_mae_filho": ["conflito casal", "criança meio", "brigas pais"],
        "sogra_casal": ["sogra interfere", "familia origem", "conflito sogra"],
        "irmao_do_meio": ["irmão meio", "mediador família", "sempre no meio"],
        "trabalho_familia": ["trabalho demais", "nunca em casa", "carreira vs família"],
        "ex_parceiro": ["ex-marido", "ex-esposa", "pai biológico", "mãe biológica"],
        "doenca_familia": ["doente família", "cuidador único", "toda responsabilidade"],
        "filho_adulto_dependente": ["filho não sai", "depende pais", "não trabalha"],
        "segredo_familiar": ["segredo", "ninguém fala", "todos sabem mas"],
        "alcool_drogas": ["bebe demais", "problema bebida", "usa drogas"],
        "dinheiro_poder": ["questões dinheiro", "controla financeiro", "quem decide"]
    }
    
    for tipo_triangulacao, palavras_chave in padroes_triangulacao.items():
        if any(palavra in situacao_lower for palavra in palavras_chave):
            triangulacoes_detectadas.append(tipo_triangulacao)
    
    return triangulacoes_detectadas

def analisar_padroes_multigeracionais(historico_familiar: str) -> dict:
    """Analisa padrões que se repetem através das gerações"""
    padroes_identificados = []
    
    historico_lower = historico_familiar.lower()
    
    # Padrões comuns multigeracionais
    padroes_geracionais = {
        "divorcio_repetitivo": ["pais divorciados", "avós divorciados", "separações família"],
        "alcoolismo_familiar": ["pai bebia", "avô alcoólatra", "problema bebida família"],
        "violencia_domestica": ["pai batia", "violência casa", "agressivo família"],
        "doenca_mental": ["depressão família", "ansiedade gerações", "problema mental"],
        "segredos_familia": ["nunca falavam", "segredos família", "ninguém conta"],
        "abandono_emocional": ["pai ausente", "mãe fria", "não demonstravam afeto"],
        "conflitos_dinheiro": ["problemas financeiros", "brigas por dinheiro", "questões herança"],
        "papeis_rigidos": ["homem provedor", "mulher casa", "papéis definidos"],
        "triangulacoes_cronicas": ["sempre no meio", "mediador conflitos", "nunca direto"],
        "lealdades_cegas": ["família primeiro", "nunca questionar", "sempre obedecer"]
    }
    
    for padrao, indicadores in padroes_geracionais.items():
        if any(indicador in historico_lower for indicador in indicadores):
            padroes_identificados.append(padrao)
    
    return {
        "padroes_identificados": padroes_identificados,
        "analise": "Análise preliminar baseada em indicadores comuns",
        "recomendacao": "Explorar mais profundamente cada padrão identificado"
    }

def sugerir_intervencoes_por_estagio(estagio: str) -> dict:
    """Sugere intervenções específicas baseadas no estágio do ciclo de vida"""
    
    intervencoes_por_estagio = {
        "jovem_adulto_solteiro": {
            "foco_principal": "Diferenciação da família de origem",
            "intervencoes": [
                "Explorar padrões familiares internalizados",
                "Desenvolver identidade independente",
                "Trabalhar questões de autonomia vs. conexão",
                "Abordar medos de intimidade ou compromisso",
                "Facilitar conversas com pais sobre mudanças de papel"
            ],
            "tecnicas": ["Genograma focado em diferenciação", "Roleplay de conversas difíceis", "Cartas não enviadas"]
        },
        
        "novo_casal": {
            "foco_principal": "Criação de nova unidade familiar",
            "intervencoes": [
                "Negociar diferenças de origem familiar",
                "Estabelecer tradições próprias do casal",
                "Trabalhar conflitos de lealdade com famílias de origem",
                "Desenvolver padrões de comunicação saudáveis",
                "Integrar diferentes estilos familiares"
            ],
            "tecnicas": ["Mapeamento de tradições familiares", "Exercícios de negociação", "Rituais de união"]
        },
        
        "familia_filhos_pequenos": {
            "foco_principal": "Adaptação aos papéis parentais",
            "intervencoes": [
                "Renegociar papéis e responsabilidades",
                "Manter conexão conjugal",
                "Estabelecer limites com gerações anteriores",
                "Desenvolver estilos parentais cooperativos",
                "Gerenciar estresse e mudanças de rotina"
            ],
            "tecnicas": ["Esculturas familiares", "Planejamento conjunto", "Rituais familiares"]
        },
        
        "familia_adolescentes": {
            "foco_principal": "Flexibilização de fronteiras familiares",
            "intervencoes": [
                "Renegociar regras e autonomia",
                "Lidar com conflitos de autoridade",
                "Preparar para eventual saída dos filhos",
                "Abordar questões de identidade familiar",
                "Facilitar comunicação entre gerações"
            ],
            "tecnicas": ["Contratos familiares", "Mediação de conflitos", "Círculos de diálogo"]
        },
        
        "lancamento_filhos": {
            "foco_principal": "Redefinição da família nuclear",
            "intervencoes": [
                "Renegociar relacionamento conjugal",
                "Desenvolver novos papéis para pais",
                "Facilitar saída saudável dos filhos",
                "Explorar novos interesses e propósitos",
                "Lidar com sentimentos de perda e vazio"
            ],
            "tecnicas": ["Rituais de transição", "Exploração de novos papéis", "Redefinição de espaços"]
        },
        
        "familia_vida_tardia": {
            "foco_principal": "Aceitação de mudanças e legado",
            "intervencoes": [
                "Lidar com perdas e limitações",
                "Transmitir sabedoria familiar",
                "Renegociar papéis de cuidado",
                "Preparar questões de fim de vida",
                "Celebrar contribuições e legado"
            ],
            "tecnicas": ["Narrativas de vida", "Rituais de legado", "Círculos de sabedoria"]
        }
    }
    
    return intervencoes_por_estagio.get(estagio, {
        "foco_principal": "Avaliação contextual necessária",
        "intervencoes": ["Identificar estágio específico", "Adaptar abordagem"],
        "tecnicas": ["Avaliação aprofundada"]
    })

def sugerir_detriangulacao(tipo_triangulacao: str) -> dict:
    """Sugere estratégias de detriangulação baseadas no tipo identificado"""
    
    estrategias_detriangulacao = {
        "pai_mae_filho": {
            "objetivo": "Devolver conflito conjugal ao casal",
            "estrategias": [
                "Orientar pais a resolverem conflitos diretamente",
                "Ajudar filho a sair do papel de mediador",
                "Estabelecer limites claros entre subsistemas",
                "Desenvolver comunicação direta entre cônjuges"
            ],
            "tecnicas": ["Coaching conjugal", "Estabelecimento de regras", "Roleplay de comunicação direta"]
        },
        
        "sogra_casal": {
            "objetivo": "Fortalecer fronteira do casal",
            "estrategias": [
                "Estabelecer limites claros com família estendida",
                "Fortalecer unidade conjugal",
                "Negociar envolvimento apropriado de sogros",
                "Desenvolver autonomia do casal"
            ],
            "tecnicas": ["Contratos de limites", "Exercícios de união", "Comunicação assertiva"]
        },
        
        "trabalho_familia": {
            "objetivo": "Equilibrar prioridades e compromissos",
            "estrategias": [
                "Renegociar prioridades familiares",
                "Estabelecer limites trabalho-casa",
                "Desenvolver apoio mútuo",
                "Criar rituais de conexão familiar"
            ],
            "tecnicas": ["Planejamento de tempo", "Rituais familiares", "Comunicação de necessidades"]
        },
        
        "doenca_familia": {
            "objetivo": "Distribuir responsabilidades de cuidado",
            "estrategias": [
                "Dividir responsabilidades entre membros",
                "Evitar sobrecarga de um cuidador",
                "Manter funcionamento familiar normal",
                "Incluir pessoa doente nas decisões quando possível"
            ],
            "tecnicas": ["Planejamento de cuidados", "Rodízio de responsabilidades", "Reuniões familiares"]
        }
    }
    
    return estrategias_detriangulacao.get(tipo_triangulacao, {
        "objetivo": "Análise específica necessária",
        "estrategias": ["Identificar dinâmica específica", "Adaptar intervenção"],
        "tecnicas": ["Avaliação detalhada da triangulação"]
    })
