from src.inference import *

def sistema_nebuloso(sujeira, manchas):
    regras = inferencia(sujeira, manchas)
    tempo_mp = media_ponderada(regras)
    tempo_cg = centro_gravidade(regras)
    return tempo_mp, tempo_cg

# Exemplo de uso:
sujeira = 7  # Grau de sujeira
manchas = 3  # Quantidade de manchas

tempo_mp, tempo_cg = sistema_nebuloso(sujeira, manchas)
print(f"Tempo de lavagem (Média Ponderada): {tempo_mp:.2f} minutos")
print(f"Tempo de lavagem (Centro de Gravidade): {tempo_cg:.2f} minutos")