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
from skfuzzy import control as ctrl

# Definir variáveis
dp = ctrl.Antecedent(np.arange(0, 101, 1), 'dp')
de = ctrl.Antecedent(np.arange(0, 101, 1), 'de')
te = ctrl.Consequent(np.arange(0, 11, 1), 'te')

# Funções de pertinência
dp['baixa'] = fuzz.trimf(dp.universe, [0, 0, 50])
dp['media'] = fuzz.trimf(dp.universe, [30, 50, 70])
dp['alta'] = fuzz.trimf(dp.universe, [50, 100, 100])

de['baixa'] = fuzz.trimf(de.universe, [0, 0, 50])
de['media'] = fuzz.trimf(de.universe, [30, 50, 70])
de['alta'] = fuzz.trimf(de.universe, [50, 100, 100])

te['curto'] = fuzz.trimf(te.universe, [0, 0, 5])
te['medio'] = fuzz.trimf(te.universe, [3, 5, 7])
te['longo'] = fuzz.trimf(te.universe, [5, 10, 10])

# Regras
rule1 = ctrl.Rule(dp['alta'] & de['baixa'], te['curto'])
rule2 = ctrl.Rule(dp['media'] & de['media'], te['medio'])
rule3 = ctrl.Rule(dp['baixa'] & de['alta'], te['longo'])

# Sistema de controle
te_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
te_simulation = ctrl.ControlSystemSimulation(te_ctrl)

# Simulação
te_simulation.input['dp'] = 60
te_simulation.input['de'] = 40
te_simulation.compute()

print(te_simulation.output['te'])