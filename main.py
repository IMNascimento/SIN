def pertinencia_ps(x):
    if 0 <= x <= 50:
        return 1 - (x / 50)
    else:
        return 0

def pertinencia_ms(x):
    if 0 <= x <= 50:
        return x / 50
    elif 50 < x <= 100:
        return 1 - (x - 50) / 50
    else:
        return 0

def pertinencia_gs(x):
    if 50 < x <= 100:
        return (x - 50) / 50
    elif x > 100:
        return 1
    else:
        return 0

def pertinencia_sm(x):
    if 0 <= x <= 50:
        return 1 - (x / 50)
    else:
        return 0

def pertinencia_mm(x):
    if 0 <= x <= 50:
        return x / 50
    elif 50 < x <= 100:
        return 1 - (x - 50) / 50
    else:
        return 0

def pertinencia_gm(x):
    if 50 < x <= 100:
        return (x - 50) / 50
    elif x > 100:
        return 1
    else:
        return 0

def pertinencia_mc(y):
    if 0 <= y <= 10:
        return 1 - (y / 10)
    else:
        return 0

def pertinencia_c(y):
    if 0 <= y <= 10:
        return y / 10
    elif 10 < y <= 25:
        return 1 - (y - 10) / 15
    else:
        return 0

def pertinencia_m(y):
    if 10 <= y <= 25:
        return (y - 10) / 15
    elif 25 < y <= 40:
        return 1 - (y - 25) / 15
    else:
        return 0

def pertinencia_l(y):
    if 25 <= y <= 40:
        return (y - 25) / 15
    elif 40 < y <= 60:
        return 1 - (y - 40) / 20
    else:
        return 0

def pertinencia_ml(y):
    if 40 <= y <= 60:
        return (y - 40) / 20
    elif y > 60:
        return 1
    else:
        return 0

# Tabela de regras (MAF)
regras = {
    ("PS", "SM"): "MC",
    ("PS", "MM"): "M",
    ("PS", "GM"): "L",
    ("MS", "SM"): "C",
    ("MS", "MM"): "M",
    ("MS", "GM"): "L",
    ("GS", "SM"): "M",
    ("GS", "MM"): "L",
    ("GS", "GM"): "ML"
}

def inferencia(sujeira, manchas):
    # Calcula os graus de pertinência para as entradas
    pertinencia_sujeira = {
        "PS": pertinencia_ps(sujeira),
        "MS": pertinencia_ms(sujeira),
        "GS": pertinencia_gs(sujeira)
    }
    pertinencia_manchas = {
        "SM": pertinencia_sm(manchas),
        "MM": pertinencia_mm(manchas),
        "GM": pertinencia_gm(manchas)
    }
    print(f"Pertinência de Sujeira: {pertinencia_sujeira}")
    print(f"Pertinência de Manchas: {pertinencia_manchas}")
    # Inicializa um dicionário para acumular os resultados das regras
    resultados = {
        "MC": 0,
        "C": 0,
        "M": 0,
        "L": 0,
        "ML": 0
    }

    # Aplica cada regra e calcula o grau de ativação
    for (entrada_sujeira, entrada_manchas), saida_tempo in regras.items():
        grau_ativacao = min(pertinencia_sujeira[entrada_sujeira], pertinencia_manchas[entrada_manchas])
        resultados[saida_tempo] = max(resultados[saida_tempo], grau_ativacao)

    return resultados

def defuzzificacao_media_ponderada(resultados):
    # Define os valores centrais dos conjuntos nebulosos para a saída
    valores_centrais = {
        "MC": 5,
        "C": 17.5,
        "M": 32.5,
        "L": 50,
        "ML": 60
    }
    
    # Calcula a soma ponderada
    numerador = sum(resultados[chave] * valor for chave, valor in valores_centrais.items())
    denominador = sum(resultados[chave] for chave in valores_centrais.keys())
    
    if denominador == 0:
        return 0  # Evita divisão por zero
    
    return numerador / denominador

def defuzzificacao_centro_gravidade(resultados):
    # Define os valores centrais dos conjuntos nebulosos para a saída
    valores_centrais = {
        "MC": 5,
        "C": 17.5,
        "M": 32.5,
        "L": 50,
        "ML": 60
    }
    
    # Calcula a soma ponderada
    numerador = sum(resultados[chave] * valor for chave, valor in valores_centrais.items())
    denominador = sum(resultados[chave] for chave in valores_centrais.keys())
    
    if denominador == 0:
        return 0  # Evita divisão por zero
    
    return numerador / denominador

def main():
    # Entradas
    #sujeira = 50
    #manchas = 40
    sujeira = 25
    manchas = 50
    
    # Realiza a inferência
    resultados = inferencia(sujeira, manchas)
    
    # Realiza a defuzzificação
    tempo_lavagem_mp = defuzzificacao_media_ponderada(resultados)
    tempo_lavagem_cg = defuzzificacao_centro_gravidade(resultados)
    
    print(f"Resultados da Inferência: {resultados}")
    print(f"Tempo de Lavagem (Média Ponderada): {tempo_lavagem_mp} minutos")
    print(f"Tempo de Lavagem (Centro de Gravidade): {tempo_lavagem_cg} minutos")


    print("\n------------------------------------------------------------")
    # Valores de teste
    valores_sujeira = [0, 25, 50, 75, 100]
    valores_manchas = [0, 25, 50, 75, 100]
    valores_tempo = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

    print("Pertinência de Pequeno Grau de Sujeira (PS):")
    for x in valores_sujeira:
        print(f"Sujeira {x}: {pertinencia_ps(x)}")

    print("\nPertinência de Médio Grau de Sujeira (MS):")
    for x in valores_sujeira:
        print(f"Sujeira {x}: {pertinencia_ms(x)}")

    print("\nPertinência de Grande Grau de Sujeira (GS):")
    for x in valores_sujeira:
        print(f"Sujeira {x}: {pertinencia_gs(x)}")

    print("\nPertinência de Sem Mancha (SM):")
    for x in valores_manchas:
        print(f"Manchas {x}: {pertinencia_sm(x)}")

    print("\nPertinência de Média Quantidade de Manchas (MM):")
    for x in valores_manchas:
        print(f"Manchas {x}: {pertinencia_mm(x)}")

    print("\nPertinência de Grande Quantidade de Manchas (GM):")
    for x in valores_manchas:
        print(f"Manchas {x}: {pertinencia_gm(x)}")

    print("\nPertinência de Tempo Muito Curto (MC):")
    for y in valores_tempo:
        print(f"Tempo {y}: {pertinencia_mc(y)}")

    print("\nPertinência de Tempo Curto (C):")
    for y in valores_tempo:
        print(f"Tempo {y}: {pertinencia_c(y)}")

    print("\nPertinência de Tempo Médio (M):")
    for y in valores_tempo:
        print(f"Tempo {y}: {pertinencia_m(y)}")

    print("\nPertinência de Tempo Longo (L):")
    for y in valores_tempo:
        print(f"Tempo {y}: {pertinencia_l(y)}")

    print("\nPertinência de Tempo Muito Longo (ML):")
    for y in valores_tempo:
        print(f"Tempo {y}: {pertinencia_ml(y)}")

   

if __name__ == "__main__":
    main()

