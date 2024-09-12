from src.linguistic_variable import LinguisticVariable
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class VehicleOvertakeSystem:
    def __init__(self):
        # Definindo as variáveis linguísticas
        self.distancia = LinguisticVariable('distancia', np.arange(0, 10, 0.1), {
            'pequena': fuzz.trapmf(np.arange(0, 10, 0.1), [0, 0, 2, 4]),
            'media': fuzz.trimf(np.arange(0, 10, 0.1), [2, 5, 7]),
            'grande': fuzz.trapmf(np.arange(0, 10, 0.1), [6, 8, 10, 10])
        })

        self.permissao = LinguisticVariable('permissao', np.arange(0, 1.1, 0.1), {
            'nao_permitido': fuzz.trimf(np.arange(0, 1.1, 0.1), [0, 0, 0.5]),
            'permitido': fuzz.trimf(np.arange(0, 1.1, 0.1), [0.5, 1, 1])
        })

        self.pista = LinguisticVariable('pista', np.arange(0, 1.1, 0.1), {
            'obstruida': fuzz.trimf(np.arange(0, 1.1, 0.1), [0, 0, 0.5]),
            'livre': fuzz.trimf(np.arange(0, 1.1, 0.1), [0.5, 1, 1])
        })

        self.velocidade_relativa = LinguisticVariable('velocidade_relativa', np.arange(0, 10, 0.1), {
            'baixa': fuzz.trapmf(np.arange(0, 10, 0.1), [0, 0, 2, 4]),
            'media': fuzz.trimf(np.arange(0, 10, 0.1), [3, 5, 7]),
            'alta': fuzz.trapmf(np.arange(0, 10, 0.1), [6, 8, 10, 10])
        })

        self.visibilidade = LinguisticVariable('visibilidade', np.arange(0, 1.1, 0.1), {
            'ruim': fuzz.trimf(np.arange(0, 1.1, 0.1), [0, 0, 0.5]),
            'boa': fuzz.trimf(np.arange(0, 1.1, 0.1), [0.5, 1, 1])
        })

        self.iniciar_ultrapassagem = LinguisticVariable('iniciar_ultrapassagem', np.arange(0, 1.1, 0.1), {
            'nao': fuzz.trimf(np.arange(0, 1.1, 0.1), [0, 0, 0.5]),
            'sim': fuzz.trimf(np.arange(0, 1.1, 0.1), [0.5, 1, 1])
        })

    def create_rules(self):
        # Definindo as quatro regras
        rule1 = ctrl.Rule(
            self.distancia.variable['pequena'] & self.velocidade_relativa.variable['alta'] &
            self.permissao.variable['permitido'] & self.pista.variable['livre'] &
            self.visibilidade.variable['boa'], self.iniciar_ultrapassagem.variable['sim']
        )

        rule2 = ctrl.Rule(
            self.distancia.variable['pequena'] & self.velocidade_relativa.variable['media'] &
            self.permissao.variable['permitido'] & self.pista.variable['livre'] &
            self.visibilidade.variable['boa'], self.iniciar_ultrapassagem.variable['sim']
        )

        rule3 = ctrl.Rule(
            self.distancia.variable['grande'] | self.velocidade_relativa.variable['baixa'] |
            self.pista.variable['obstruida'], self.iniciar_ultrapassagem.variable['nao']
        )

        rule4 = ctrl.Rule(
            self.distancia.variable['media'] & self.velocidade_relativa.variable['alta'] &
            self.permissao.variable['permitido'] & self.pista.variable['livre'],
            self.iniciar_ultrapassagem.variable['sim']
        )

        return [rule1, rule2, rule3, rule4]

    def simulate(self, inputs):
        # Cria o sistema de controle e a simulação
        rules = self.create_rules()
        ultrapassagem_ctrl = ctrl.ControlSystem(rules)
        ultrapassagem_sim = ctrl.ControlSystemSimulation(ultrapassagem_ctrl)

        # Passa as entradas
        ultrapassagem_sim.input['distancia'] = inputs['distancia']
        ultrapassagem_sim.input['velocidade_relativa'] = inputs['velocidade_relativa']
        ultrapassagem_sim.input['permissao'] = inputs['permissao']
        ultrapassagem_sim.input['pista'] = inputs['pista']
        ultrapassagem_sim.input['visibilidade'] = inputs['visibilidade']

        # Realiza a computação
        ultrapassagem_sim.compute()
        return ultrapassagem_sim.output['iniciar_ultrapassagem']