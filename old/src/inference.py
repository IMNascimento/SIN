from src.dirt import *
from src.stains import *

def inferencia(x1, x2):
    regras = []
    # Regras de inferência
    regras.append(min(ps(x1), sm(x2)) * 15)   # R1
    regras.append(min(ps(x1), mm(x2)) * 30)   # R2
    regras.append(min(ps(x1), gm(x2)) * 45)   # R3
    regras.append(min(ms(x1), sm(x2)) * 30)   # R4
    regras.append(min(ms(x1), mm(x2)) * 45)   # R5
    regras.append(min(ms(x1), gm(x2)) * 60)   # R6
    regras.append(min(gs(x1), sm(x2)) * 45)   # R7
    regras.append(min(gs(x1), mm(x2)) * 60)   # R8
    regras.append(min(gs(x1), gm(x2)) * 60)   # R9
    return regras

def media_ponderada(regras):
    soma_ponderada = sum(regras)
    soma_graus = sum([grau for grau in regras if grau > 0])
    return soma_ponderada / soma_graus if soma_graus != 0 else 0

def centro_gravidade(regras):
    y_values = [i for i in range(0, 61)]
    numerador = sum([grau * y for grau, y in zip(regras, y_values)])
    denominador = sum(regras)
    return numerador / denominador if denominador != 0 else 0