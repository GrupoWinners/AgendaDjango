
# Agenda de Eventos - Django

## Sobre o projeto

Projeto desenvolvido para o Trabalho Final da disciplina
Tópicos Especiais em Análise e Desenvolvimento de Sistemas,
do curso de Análise e Desenvolvimento de Sistemas (ADS)
do IMEPAC.

O objetivo é desenvolver uma aplicação utilizando o
framework Django, demonstrando seus principais recursos
por meio de um sistema de gerenciamento de eventos.

## Integrantes

- Samela Maria da Silva Ferreira
- Nadiny da Silva Martins
- João Vitor Santos de Souza

## Tecnologias utilizadas

- Python
- Django
- SQLite
- Postman
- Git e GitHub

## Funcionalidades

O sistema permite realizar as operações básicas de CRUD:

- Cadastrar eventos (Create)
- Listar eventos por ordem de data (Read)
- Consultar um evento pelo ID (Read)
- Atualizar eventos (Update)
- Excluir eventos (Delete)

Também possui validações para impedir o cadastro de
eventos com campos obrigatórios vazios ou datas inválidas.

## Estrutura do evento

Cada evento possui os seguintes campos:

- ID: identificador do evento
- Título: nome do evento
- Descrição: informações adicionais
- Data: data de realização
- Local: local do evento

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/GrupoWinners/AgendaDjango.git
cd AgendaDjango
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

### 4. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Preparar o banco de dados

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

O servidor estará disponível em:

http://127.0.0.1:8000/

## Endpoints da API

| Método | Endpoint | Funcionalidade |
|--------|----------|----------------|
| GET | /eventos | Listar eventos |
| GET | /eventos/{id} | Consultar evento |
| POST | /eventos | Cadastrar evento |
| PUT | /eventos/{id} | Atualizar evento |
| DELETE | /eventos/{id} | Excluir evento |

## Exemplo de cadastro

Para cadastrar um evento, utilizar o método POST
no Postman, com a URL:

http://127.0.0.1:8000/eventos

No Body, selecionar raw e JSON e enviar:

```json
{
  "titulo": "Apresentação de Django",
  "descricao": "Trabalho final de ADS",
  "data": "2026-11-23",
  "local": "IMEPAC"
}
```

## Testes realizados

A aplicação foi testada utilizando o Postman,
com requisições HTTP para verificar o funcionamento
dos métodos GET, POST, PUT e DELETE.

Também foram realizados testes de validação de
campos obrigatórios e datas inválidas.

## Considerações finais

O desenvolvimento do projeto permitiu compreender
o funcionamento básico do framework Django,
a criação de rotas, a manipulação de dados com ORM,
a utilização do SQLite e a implementação de uma
API com operações CRUD.

O projeto foi desenvolvido para fins acadêmicos.
