# Projeto de Gestão de Comissões e Validação de Pagamentos

Este projeto é uma ferramenta desenvolvida como parte do Desafio técnico AAWZ - Automação, com o objetivo de calcular comissões de vendas, validar pagamentos e extrair informações de clientes a partir de arquivos Excel e textos estruturados.

## Funcionalidades

- **Cálculo de Comissões**: Calcula a comissão inicial e final para vendedores com base nos dados de vendas. O cálculo considera descontos para vendas online e comissões adicionais para gerentes.
- **Validação de Pagamentos**: Compara os valores de comissão pagos aos vendedores com os valores calculados para identificar discrepâncias.
- **Extração de Informações de Clientes**: Extrai o nome e a quantidade de cotas de clientes a partir de textos estruturados.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado. As bibliotecas necessárias estão listadas no arquivo `requirements.txt`.

### Recomendação: Uso de Ambientes Virtuais

Recomendo o uso de ambientes virtuais para gerenciar as dependências do projeto. Para criar e ativar um ambiente virtual, siga os passos abaixo:

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
    ```
2. Ative o ambiente virtual:
  - Windows:
    ```bash
    venv\Scripts\activate
    ```
  - Linux:
    ```bash
    source venv/bin/activate
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Comandos Disponíveis

1. **Cálculo de Comissões**
   ```bash
   python main.py calculate-commission <arquivo_excel> [--sheet <nome_da_aba>]
   ```
   - `<arquivo_excel>`: Arquivo Excel contendo os dados de vendas.
   - `--sheet <nome_da_aba>`: (Opcional) Nome da aba contendo os dados de vendas. O padrão é "Vendas".

2. **Validação de Pagamentos**
   ```bash
   python main.py validate-payments <arquivo_excel> [--sales-sheet <nome_da_aba_vendas>] [--payments-sheet <nome_da_aba_pagamentos>]
   ```
   - `<arquivo_excel>`: Arquivo Excel contendo os dados de vendas e pagamentos.
   - `--sales-sheet <nome_da_aba_vendas>`: (Opcional) Nome da aba contendo os dados de vendas. O padrão é "Vendas".
   - `--payments-sheet <nome_da_aba_pagamentos>`: (Opcional) Nome da aba contendo os dados de pagamentos. O padrão é "Pagamentos".

3. **Extração de Informações de Clientes**
   ```bash
   python main.py extract-client-info <arquivo_texto>
   ```
   - `<arquivo_texto>`: Arquivo de texto contendo as informações dos clientes.

### Exemplos de Uso

Os exemplos abaixo utilizam os arquivos de amostra fornecidos na pasta `sample/`.

- **Cálculo de Comissões**:
  ```bash
  python main.py calculate-commission .\sample\Vendas.xlsx
  ```

- **Validação de Pagamentos**:
  ```bash
  python main.py validate-payments .\sample\Vendas.xlsx
  ```

- **Extração de Informações de Clientes**:
  ```bash
  python main.py extract-client-info .\sample\Partnership.txt
  ```

### Resultados

Os resultados serão salvos em novos arquivos Excel na pasta `results/`, com nomes de acordo com a operação executada.

### Notas

Inicialmente, o projeto utilizava a biblioteca `sys` para receber os argumentos da linha de comando, mas os nomes das abas eram codificados diretamente no código, com base nos arquivos de amostra fornecidos. Para tornar o projeto mais flexível, foi feita a migração para a biblioteca `click`. Com `click`, é possível passar os nomes das abas como parâmetros opcionais na linha de comando, permitindo que o usuário especifique diferentes nomes de abas conforme necessário. Se os nomes das abas não forem fornecidos, os valores padrão serão utilizados.