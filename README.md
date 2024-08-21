# Senai-Flask

Este é um projeto Flask que implementa um sistema de gerenciamento para estudantes, cursos e inscrições, incluindo a definição de tabelas e relacionamentos em um banco de dados MySQL.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

- `app/`: Contém o código principal da aplicação.
  - `__init__.py`: Inicializa o aplicativo Flask e configura o banco de dados.
  - `models.py`: Define os modelos de dados e os relacionamentos entre eles.
  - `routes.py`: Define as rotas da aplicação (não incluído neste exemplo, mas tipicamente presente).

- `migrations/`: Contém scripts de migração para o banco de dados gerados pelo Flask-Migrate.

- `requirements.txt`: Lista de dependências do projeto.

- `config.py`: Arquivo de configuração (não incluído neste exemplo, mas tipicamente presente).

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalá-las, use o seguinte comando:

```bash
pip install -r requirements.txt
