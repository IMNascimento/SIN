# Repositório de Exercícios de Sistema de Inferência Nebulosa (SIN)

Este repositório contém vários exercícios práticos relacionados à implementação de **Sistemas de Inferência Nebulosa (SIN)**. Cada pasta no repositório representa um exercício, e dentro de cada pasta, você encontrará o **enunciado** do problema e o código correspondente para rodar o sistema.

## Estrutura do Repositório

### 1. `central_pecas/`
Este diretório contém um exercício de **Sistema de Inferência Nebulosa para Central de Peças**. O objetivo do sistema é calcular o número de peças extras recomendadas para uma central de reparo, com base em variáveis como tempo de espera, fator de utilização e número de funcionários.

- **Subpasta `problema/`**: Contém o enunciado do problema.
- **Execução**: Para testar, basta executar o código `central_pecas.py`.

### 2. `maquina_lavar/`
Esta pasta contém um exercício de **Sistema de Inferência Nebulosa para Máquina de Lavar Roupas**. O sistema calcula o tempo de lavagem com base na quantidade de roupas e o nível de sujeira.

- **Subpasta `problema/`**: Contém o enunciado do problema.
- **Execução**: Para testar, basta executar o código `maquina_lavar.py`.

### 3. `ultrapassagem/`
Este diretório contém um exercício de **Sistema de Inferência Nebulosa para Controle de Ultrapassagem de Veículos**. O sistema avalia a segurança para iniciar uma ultrapassagem com base na distância até o veículo à frente, a visibilidade, a velocidade e a permissão de ultrapassagem.

- **Subpasta `problema/`**: Contém o enunciado do problema.
- **Execução**: Para testar, basta executar o código `main.py`.

## Como Executar

1. **Clone o Repositório**:

```bash
git clone https://github.com/IMNascimento/SIN.git
```

Navegue até a pasta correspondente ao exercício que deseja testar:

```bash
cd nome_da_pasta_exercicio
```

Instale as dependências (se necessário, você pode usar um ambiente virtual):
```bash
pip install -r requirements.txt
```

Execute o código:

```bash
python nome_do_arquivo.py
```

Cada exercício é autônomo e possui seu próprio código e enunciado do problema. Ao executar o código, os resultados e gráficos serão exibidos.