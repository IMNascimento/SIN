from src.vehicle_over_system import VehicleOvertakeSystem

# Criando o sistema de controle de ultrapassagem
sistema_ultrapassagem = VehicleOvertakeSystem()

# Simulando uma entrada
inputs = {
    'distancia': 3,
    'velocidade_relativa': 7,
    'permissao': 1,
    'pista': 1,
    'visibilidade': 1
}

# Realizando a simulação
resultado = sistema_ultrapassagem.simulate(inputs)
print(f"Decisão de ultrapassagem: {resultado:.2f}")

# Gerando e salvando gráficos das variáveis como PNG
sistema_ultrapassagem.distancia.plot(input_value=inputs['distancia'])
sistema_ultrapassagem.velocidade_relativa.plot(input_value=inputs['velocidade_relativa'])
sistema_ultrapassagem.permissao.plot(input_value=inputs['permissao'])
sistema_ultrapassagem.pista.plot(input_value=inputs['pista'])
sistema_ultrapassagem.visibilidade.plot(input_value=inputs['visibilidade'])