# Sistema de Inferência Nebulosa para Estimativa de Tempo de Manutenção

Este projeto implementa um **Sistema de Inferência Nebulosa (Fuzzy Inference System)** para estimar o tempo de manutenção de um equipamento com base na distância percorrida e no desgaste do equipamento.

## Requisitos

As bibliotecas necessárias para rodar o projeto estão listadas no arquivo `requirements.txt`. Para instalar as dependências, siga as instruções abaixo.

### Passos para Instalação:

1. Clone o repositório:

```bash
git clone https://github.com/IMNascimento/SIN.git
```

2. Crie um ambiente virtual:

```bash
# Para Linux/MacOS
python3 -m venv venv
source venv/bin/activate

# Para Windows
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execução
Para executar o código, basta rodar o script principal, que realiza a simulação e gera gráficos com as funções de pertinência e o resultado da defuzzificação:

```bash
python central_pecas.py
```

Após a execução, os gráficos serão exibidos mostrando as funções de pertinência e a estimativa de tempo de manutenção.

### Descrição das Variáveis

#### Variáveis de Entrada
1. distancia_percorrida (dp): Avalia a distância total percorrida pelo equipamento (intervalo de 0 a 100).

- Baixa
- Média
- Alta

2. desgaste_equipamento (de): Mede o nível de desgaste do equipamento (intervalo de 0 a 100).

- Baixa
- Média
- Alta
- Variável de Saída

3. tempo_estimado (te): Estima o tempo necessário para manutenção (intervalo de 0 a 10).
- Curto
- Médio
- Longo

#### Regras Fuzzy

- SE a distância percorrida é alta E o desgaste do equipamento é baixo, ENTÃO o tempo estimado é curto.

- SE a distância percorrida é média E o desgaste do equipamento é médio, ENTÃO o tempo estimado é médio.

- SE a distância percorrida é baixa E o desgaste do equipamento é alto, ENTÃO o tempo estimado é longo.