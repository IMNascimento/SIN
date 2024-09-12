"""
1. Especificar o Problema e Definir as Variáveis Linguísticas
Objetivo do Sistema: O sistema deve ajudar o gerente da central de peças a manter o cliente satisfeito, reduzindo o tempo de espera ao mínimo possível.

Variáveis Linguísticas:

Entrada 1: Disponibilidade de Peças (DP)

Termos Linguísticos: Baixa, Média, Alta
Descrição: Representa a quantidade de peças disponíveis em perfeito estado.
Entrada 2: Demanda de Peças (DE)

Termos Linguísticos: Baixa, Média, Alta
Descrição: Representa a frequência de clientes solicitando peças.
Saída: Tempo de Espera (TE)

Termos Linguísticos: Curto, Médio, Longo
Descrição: Representa o tempo de espera do cliente por uma peça em perfeito estado.
2. Definir a Representação dos Termos Linguísticos
Você deve definir as funções de pertinência para cada termo linguístico. Estas funções podem ser representadas de diversas formas, como triangular, trapezoidal, etc.

Disponibilidade de Peças (DP):

Baixa: Função triangular com intervalo [0, 0, 50]
Média: Função triangular com intervalo [30, 50, 70]
Alta: Função triangular com intervalo [50, 100, 100]
Demanda de Peças (DE):

Baixa: Função triangular com intervalo [0, 0, 50]
Média: Função triangular com intervalo [30, 50, 70]
Alta: Função triangular com intervalo [50, 100, 100]
Tempo de Espera (TE):

Curto: Função triangular com intervalo [0, 0, 5]
Médio: Função triangular com intervalo [3, 5, 7]
Longo: Função triangular com intervalo [5, 10, 10]
3. Elicitar e Construir as Regras de Inferência
Agora, você precisa criar regras de inferência que determinam o tempo de espera baseado na disponibilidade e demanda de peças.

Exemplos de Regras:

Se DP é Alta e DE é Baixa, então TE é Curto.
Se DP é Média e DE é Média, então TE é Médio.
Se DP é Baixa e DE é Alta, então TE é Longo.
Você pode criar mais regras baseadas na lógica de negócio.

4. Codificar os Conjuntos e Regras de Inferência
Para implementar o sistema, você pode usar ferramentas como Python com bibliotecas especializadas em lógica fuzzy, como scikit-fuzzy.
"""
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Definir variáveis linguísticas
distancia_percorrida = ctrl.Antecedent(np.arange(0, 101, 1), 'distancia_percorrida')
desgaste_equipamento = ctrl.Antecedent(np.arange(0, 101, 1), 'desgaste_equipamento')
tempo_estimado = ctrl.Consequent(np.arange(0, 11, 1), 'tempo_estimado')

# Funções de pertinência para distancia_percorrida (dp)
distancia_percorrida['baixa'] = fuzz.trimf(distancia_percorrida.universe, [0, 0, 50])
distancia_percorrida['media'] = fuzz.trimf(distancia_percorrida.universe, [30, 50, 70])
distancia_percorrida['alta'] = fuzz.trimf(distancia_percorrida.universe, [50, 100, 100])

# Funções de pertinência para desgaste_equipamento (de)
desgaste_equipamento['baixa'] = fuzz.trimf(desgaste_equipamento.universe, [0, 0, 50])
desgaste_equipamento['media'] = fuzz.trimf(desgaste_equipamento.universe, [30, 50, 70])
desgaste_equipamento['alta'] = fuzz.trimf(desgaste_equipamento.universe, [50, 100, 100])

# Funções de pertinência para tempo_estimado (te)
tempo_estimado['curto'] = fuzz.trimf(tempo_estimado.universe, [0, 0, 5])
tempo_estimado['medio'] = fuzz.trimf(tempo_estimado.universe, [3, 5, 7])
tempo_estimado['longo'] = fuzz.trimf(tempo_estimado.universe, [5, 10, 10])

# Definir as regras fuzzy
rule1 = ctrl.Rule(distancia_percorrida['alta'] & desgaste_equipamento['baixa'], tempo_estimado['curto'])
rule2 = ctrl.Rule(distancia_percorrida['media'] & desgaste_equipamento['media'], tempo_estimado['medio'])
rule3 = ctrl.Rule(distancia_percorrida['baixa'] & desgaste_equipamento['alta'], tempo_estimado['longo'])

# Criar o sistema de controle fuzzy
tempo_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tempo_simulation = ctrl.ControlSystemSimulation(tempo_ctrl)

# Definir os valores de entrada
tempo_simulation.input['distancia_percorrida'] = 60
tempo_simulation.input['desgaste_equipamento'] = 40

# Computar a saída
tempo_simulation.compute()

# Exibir resultado da defuzzificação
print(f"Tempo estimado para manutenção: {tempo_simulation.output['tempo_estimado']:.2f}")

# Função para plotar as funções de pertinência e resultado da defuzzificação
def plot_fuzzy_variables():
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    # Gráfico para distancia_percorrida
    axs[0].plot(distancia_percorrida.universe, distancia_percorrida['baixa'].mf, label='Baixa')
    axs[0].plot(distancia_percorrida.universe, distancia_percorrida['media'].mf, label='Média')
    axs[0].plot(distancia_percorrida.universe, distancia_percorrida['alta'].mf, label='Alta')
    axs[0].set_title('Função de Pertinência - Distância Percorrida')
    axs[0].legend()

    # Gráfico para desgaste_equipamento
    axs[1].plot(desgaste_equipamento.universe, desgaste_equipamento['baixa'].mf, label='Baixa')
    axs[1].plot(desgaste_equipamento.universe, desgaste_equipamento['media'].mf, label='Média')
    axs[1].plot(desgaste_equipamento.universe, desgaste_equipamento['alta'].mf, label='Alta')
    axs[1].set_title('Função de Pertinência - Desgaste do Equipamento')
    axs[1].legend()

    # Gráfico para tempo_estimado
    axs[2].plot(tempo_estimado.universe, tempo_estimado['curto'].mf, label='Curto')
    axs[2].plot(tempo_estimado.universe, tempo_estimado['medio'].mf, label='Médio')
    axs[2].plot(tempo_estimado.universe, tempo_estimado['longo'].mf, label='Longo')
    axs[2].axvline(tempo_simulation.output['tempo_estimado'], color='r', linestyle='--', label=f'Resultado: {tempo_simulation.output["tempo_estimado"]:.2f}')
    axs[2].set_title('Função de Pertinência - Tempo Estimado')
    axs[2].legend()

    # Exibir gráficos
    plt.tight_layout()
    plt.show()

# Plotar os gráficos
plot_fuzzy_variables()