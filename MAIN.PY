import random
random.seed()
def random_birth_country():
    countries = [
        "Índia", "China", "Estados Unidos", "Indonésia", "Paquistão", "Nigéria", "Brasil", "Bangladesh", "Rússia", "Etiópia",
        "México", "Japão", "Egito", "Filipinas", "Rep. Dem. do Congo", "Vietnã", "Irã", "Turquia", "Alemanha", "Tailândia",
        "Tanzânia", "Reino Unido", "França", "África do Sul", "Itália", "Quênia", "Mianmar", "Colômbia", "Coreia do Sul", "Espanha",
        "Sudão", "Ucrânia", "Argentina", "Argélia", "Iraque", "Afeganistão", "Uganda", "Polônia", "Canadá", "Marrocos",
        "Arábia Saudita", "Uzbequistão", "Malásia", "Moçambique", "Gana", "Nepal", "Venezuela", "Iémen", "Costa do Marfim", "Camarões"
    ]
    
    # Populações relativas em milhões
    populations = [
        1463.87, 1416.10, 347.28, 285.72, 255.22, 237.53, 212.81, 175.69, 143.99, 135.47,
        131.95, 123.10, 118.37, 116.79, 112.83, 101.60, 92.42, 87.69, 84.08, 71.62,
        70.55, 67.86, 67.29, 64.75, 58.68, 57.53, 55.82, 52.56, 51.76, 47.33,
        51.66, 37.52, 46.85, 47.44, 45.70, 43.33, 51.38, 37.54, 40.20, 38.43,
        37.78, 36.81, 35.32, 35.63, 35.06, 31.96, 29.66, 34.00, 32.71, 29.27
    ]
    
    total = sum(populations)
    weights = [pop / total for pop in populations]
    
    return random.choices(countries, weights=weights, k=1)[0]

import random

def random_eye_color():
    colors = [
        "Castanho",     # Brown
        "Azul",         # Blue
        "Mel",          # Amber
        "Avelã",        # Hazel
        "Verde",        # Green
        "Cinza",        # Gray
        "Outro/Raro"    # Albino, heterocromia, etc.
    ]
    
    # Probabilidades aproximadas (%)
    weights = [
        70,  # Castanho
        10,  # Azul
        5,   # Mel
        5,   # Avelã
        2,   # Verde
        1,   # Cinza
        2    # Outros/raros
    ]
    
    return random.choices(colors, weights=weights, k=1)[0]
def random_sex():
    # Aproximadamente 50,5% masculino e 49,5% feminino globalmente
    return random.choices(["masculino", "feminino"], weights=[50.5, 49.5], k=1)[0]

def random_height():
    sexo = random_sex()
    
    # Médias e desvios por sexo
    if sexo == "masculino":
        media = 171
        desvio = 10
    else:  # feminino
        media = 159
        desvio = 8
    
    # Gera altura com distribuição normal
    altura = random.gauss(media, desvio)

    # Limita a altura a valores humanos realistas
    altura = max(altura, 130)  # mínimo
    altura = min(altura, 210)  # máximo

    return sexo, round(altura, 1)

sexo, altura = random_height()

def random_penis_size():
    # Média e desvio padrão em centímetros (ereção)
    media = 13.2
    desvio = 3

    # Gera valor com distribuição normal
    tamanho = random.gauss(media, desvio)

    # Limita a valores realistas (muito fora da curva são raros)
    tamanho = max(tamanho, 7.0)   # mínimo fisiológico
    tamanho = min(tamanho, 25.0)  # máximo raro observado

    return round(tamanho, 1)

def random_breast_size():
    # Média da circunferência do busto (em cm)
    media_busto = 93
    desvio_busto = 7

    # Gera medida com distribuição normal
    busto = random.gauss(media_busto, desvio_busto)

    # Limita a medidas razoáveis
    busto = max(busto, 75)   # mínimo
    busto = min(busto, 120)  # máximo

    return round(busto, 1)

def random_foot_size(sexo):
    if sexo is None:
        # Sorteia sexo com base estatística
        sexo = random.choices(["masculino", "feminino"], weights=[50.5, 49.5], k=1)[0]
    
    if sexo == "masculino":
        media = 41.5
        desvio = 1.5
        min_tam, max_tam = 37, 47
    elif sexo == "feminino":
        media = 37.5
        desvio = 1.5
        min_tam, max_tam = 33, 43
    else:
        raise ValueError("Sexo inválido. Use 'masculino' ou 'feminino'.")

    # Gera tamanho com distribuição normal
    tam_pe = random.gauss(media, desvio)
    tam_pe = max(min_tam, min(max_tam, round(tam_pe, 1)))  # limita e arredonda

    return tam_pe

# Teste
tamanho = random_foot_size(sexo)

def random_iq():
    media = 100
    desvio = 15

    iq = random.gauss(media, desvio)

    # Limita valores entre 40 e 160 (extremos muito raros)
    iq = max(40, min(160, round(iq)))

    return iq


def random_baldness(sexo):
    if sexo == "masculino":
        chance_bald = 0.8  # 80% chance de algum grau de calvície
        if random.random() > chance_bald:
            return False, None  # Não fica careca
        
        # Idade de início (distribuição aproximada)
        # 25% antes dos 30, 50% até 50, e o resto depois dos 50
        age_start = random.choices(
            population=[25, 35, 50, 60],
            weights=[0.25, 0.35, 0.30, 0.10],
            k=1
        )[0]
        return True, age_start
    
    else:  # feminino
        chance_bald = 0.20  # 20% chance
        if random.random() > chance_bald:
            return False, None
        
        # Idade de início mais tardia em mulheres
        age_start = random.choices(
            population=[40, 50, 60, 70],
            weights=[0.20, 0.30, 0.30, 0.20],
            k=1
        )[0]
        return True, age_start


careca, idade_inicio = random_baldness(sexo)


def random_beauty_score():
    media = 50
    desvio = 15

    score = random.gauss(media, desvio)
    score = max(0, min(100, round(score)))

    return score

def random_weight(sexo):
    if sexo == "masculino":
        media = 70
        desvio = 15
    elif sexo == "feminino":
        media = 60
        desvio = 15
    else:
        raise ValueError("Sexo inválido. Use 'masculino' ou 'feminino'.")

    peso = random.gauss(media, desvio)
    peso = max(40, min(150, round(peso, 1)))  # Limita entre 40 e 150 kg

    return  peso


peso = random_weight(sexo)

def random_skin_color():
    cores_pele = ["Parda", "Negra", "Branca", "Amarelada"]
    pesos_pele = [40, 40, 15, 5]

    cor = random.choices(cores_pele, weights=pesos_pele, k=1)[0]
    return cor

def random_profession_expanded():
    profissoes = [
        # Agricultura / Agropecuária
        "Agricultor", "Pecuarista", "Técnico agrícola", "Agrônomo", "Veterinário",
        # Serviços
        "Vendedor", "Atendente", "Recepcionista", "Motorista", "Auxiliar administrativo", "Segurança", "Garçom", "Cabeleireiro", "Caixa", "Faxineiro",
        # Indústria / Fabricação
        "Operador de máquina", "Técnico de manutenção", "Eletricista", "Soldador", "Montador", "Mecânico",
        # Tecnologia / TI
        "Programador", "Analista de sistemas", "Técnico em informática", "Engenheiro de software", "Suporte técnico", "Cientista de dados",
        # Educação / Saúde
        "Professor", "Enfermeiro", "Médico", "Psicólogo", "Fisioterapeuta", "Técnico em enfermagem",
        # Administração / Financeiro
        "Contador", "Assistente financeiro", "Gerente", "Auxiliar administrativo", "Auditor",
        # Artes / Comunicação
        "Jornalista", "Designer gráfico", "Fotógrafo", "Publicitário", "Ator", "Músico",
        # Comércio / Varejo
        "Operador de caixa", "Estoquista", "Gerente de loja", "Comprador", "Merchandiser"
    ]

    pesos = [
        # Agricultura / Agropecuária (total 15%)
        4, 3, 2, 3, 3,
        # Serviços (total 30%)
        6, 4, 3, 3, 3, 3, 2, 2, 2, 2,
        # Indústria / Fabricação (total 15%)
        5, 3, 3, 2, 1, 1,
        # Tecnologia / TI (total 10%)
        3, 2, 1, 2, 1, 1,
        # Educação / Saúde (total 15%)
        4, 3, 3, 2, 2, 1,
        # Administração / Financeiro (total 7%)
        2, 1, 2, 1, 1,
        # Artes / Comunicação (total 5%)
        1, 1, 1, 1, 1, 1,
        # Comércio / Varejo (total 3%)
        1, 1, 1, 1, 1
    ]

    profissao = random.choices(profissoes, weights=pesos, k=1)[0]
    return profissao


def random_vices():
    vicios = {
        "Fuma": 0.10,      
        "Bebe álcool regularmente": 0.15,
        "Usa drogas ilícitas": 0.01,
        "Consome café diariamente": 0.18,
        "Joga jogos de azar": 0.05,     
        "Uso excessivo de redes sociais": 0.15, 
        "Masturba-se frequentemente": 0.10,     
        "Assiste TV/streaming excessivamente": 0.12, 
        "Comida fast food em excesso": 0.10,   
        "Uso frequente de smartphone": 0.20,     
        "Roer unhas": 0.06,                 
        "Compra compulsiva": 0.08,      
        "Dormir pouco (<6h)": 0.08,                  
        "Café em excesso (>5 xícaras)": 0.08,      
        "Mastigar gelo": 0.04,                       
        "Roer lápis/caneta": 0.05,             
        "Falar sozinho": 0.06,
        "Coçar a cabeça excessivamente": 0.035,
        "Roer cutícula": 0.08,
        "Brincar com o cabelo": 0.05,
        "Mexer no celular no banheiro": 0.18,
        "Assistir vídeos de gatos excessivamente": 0.10,
        "Repetir palavras mentalmente": 0.03,
        "Apertar espinhas": 0.06,
        "Colecionar coisas inúteis": 0.025,
        "Roer canudo ou palito de dente": 0.035
    }

    result = []
    for vicio, chance in vicios.items():
        if random.random() < chance:
            result.append(vicio)
    
    if not result:
        result.append("Nenhum vício/hábito relevante")

    return result





print(f"Sexo: {sexo.capitalize()}, Altura: {altura} cm")
print(f"Peso: {peso} kg")
print("Cor da pele:", random_skin_color())
print("Profissão:", random_profession_expanded())
print("QI", random_iq())
print("Você nasceu no(a):", random_birth_country())
print("Cor dos olhos:", random_eye_color())
if careca:
    print(f"ficará careca a partir dos {idade_inicio} anos.")
else:
    print(f"não ficará careca.")
print(f"Tamanho do pé (BR): {tamanho}")
if sexo == "masculino":
    print("Tamanho do piu-piu:", random_penis_size(), "cm")
else:
    print("Tamanho das peitchola:", random_breast_size(), "cm")
print("Beleza (0 a 100):", random_beauty_score())
print("Vícios/hábitos:", random_vices())