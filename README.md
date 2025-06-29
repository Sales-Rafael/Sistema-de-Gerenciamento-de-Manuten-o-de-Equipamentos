#Sistema de Gerenciamento de Manutenção de Equipamentos

## 1) Tema/Nome do Sistema
Sistema de Gerenciamento de Manutenção de Equipamentos

## 2) Finalidade/Objetivo
O sistema tem como objetivo registrar e organizar as manutenções realizadas em equipamentos de forma simples e eficiente. A necessidade surge da dificuldade de controlar manutenções em ambientes como oficinas, setores industriais, escolas técnicas ou empresas que utilizam equipamentos regularmente. O sistema permite o cadastro, consulta, edição e remoção de registros de manutenção, facilitando o histórico e o acompanhamento das ações realizadas.

## 3) Principais Funcionalidades
- Cadastro de uma nova manutenção com geração automática de ID
- Consulta do histórico de manutenções registradas
- Edição de manutenções existentes, com atualização dos dados
- Remoção de manutenções por meio do ID
- Validação de entrada de dados, principalmente a data no formato correto

## 4) Recursos da Linguagem Python Utilizados
Durante o desenvolvimento do sistema, foram aplicados diversos conceitos da disciplina:

**Entrada e saída de dados:**
- Utilização das funções `input()` e `print()` para interação com o usuário

**Estrutura condicional:**
- Uso de `if`, `elif` e `else` para validação de opções e dados, como o formato da data

**Estrutura de repetição:**
- Uso de `while` para manter o menu funcionando até o usuário optar por sair
- Para repetição de entrada de dados inválidos

**Listas:**
- A lista `lista_de_manutenção` armazena todos os registros de manutenção como dicionários

**Dicionários:**
- Cada manutenção é representada por um dicionário contendo os campos ID, mecânico, data e maquinário

**Funções:**
- O código foi modularizado com funções como:
  - `adicionar_manutenção()`
  - `remover_manutenção()`
  - `consultando_lista_de_manutenções()`
  - `alterar_manutenção()`
- Para organização e reuso de código

**Biblioteca random:**
- A função `random.randint()` foi usada para gerar IDs automáticos e únicos para cada manutenção

**Tratamento de tipos e validações:**
- Conversão de strings para inteiros com `int()`
- Validação com `.isdigit()`
- Controle de formato de data com `split()`

## 5) Desenvolvimento
**O que foi feito:**
Foi desenvolvido um sistema em linguagem Python com interface textual simples para gerenciamento de manutenções de equipamentos.

**Como foi feito:**
- Executado diretamente no terminal ou IDEs como VS Code
- O código foi estruturado em funções para facilitar a manutenção e a leitura
- Os dados são mantidos em memória durante a execução utilizando listas e dicionários

**Recursos técnicos utilizados:**
- Python 3.12.6
- VS Code como ambiente de desenvolvimento
- Execução em ambiente local
- Biblioteca padrão random

## 6) Conclusão/Resultados
O sistema desenvolvido atende plenamente às necessidades básicas de registro e consulta de manutenções de equipamentos. Ele é simples, leve, e pode ser facilmente expandido.

**Pontos positivos:**
- Facilidade de uso e entendimento
- Validação das entradas
- Organização por funções e separação lógica do código

**Pontos negativos:**
- Os dados não são salvos após o fechamento do programa
- A interface é limitada ao modo texto no terminal

## 7) Trabalhos Futuros
Possibilidades de melhorias e novos caminhos:
- Adição de salvamento de dados em arquivos .txt, .csv ou .json
- Criação de uma interface gráfica
- Controle de login e permissões de usuários
- Filtros por data, mecânico ou equipamento
- Integração com banco de dados para maior robustez e persistência dos dados
