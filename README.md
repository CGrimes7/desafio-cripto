## Desafio Técnico: Coleta e Armazenamento de Dados de Criptomoedas - Cadastra ##

Este projeto em Python coleta dados da API CoinCap e os armazena em um banco de dados PostgreSQL.

## Pré-requisitos ##

- Python 3.x instalado;
- Pip;
- PostgreSQL instalado.

## Configuração ##

1.  Clone este repositório.
2.  Instale as dependências: "pip install -r requirements.txt"
3.  Crie um arquivo ".env" com suas configurações de API e banco de dados (renomeie ".env_test" para ".env").
4.  Execute o script "database.sql" para criar as tabelas no seu banco de dados PostgreSQL.

## Execução ##

Execute o script "main.py": "python main.py"

## Power BI ##

Utilize os dados no banco de dados para criar um dashboard no Power BI. O arquivo "crypto_data" contém dados de exemplo em CSV para você experimentar no Power BI Desktop.