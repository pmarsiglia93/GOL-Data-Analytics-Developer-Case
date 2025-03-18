# GOL Data Analytics | Developer Case (GDADC)

## Requisitos

- Python 3.13.2


<br>


## Ferramentas

- FastAPI 0.115.11


<br>


## Execução

Para executar a **API**, você precisará instalar as dependências do projeto.

Sugerimos usar o [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html), pois fornecemos um arquivo **environment.yml**.

<br>

Para criar o ambiente a partir do arquivo, execute os seguintes comandos:

```sh
# Primeiro, crie o ambiente
$ conda env create -f environment.yml

# Depois, ative-o
$ conda activate gdadc
```

<br>

Para iniciar a **API**, execute o seguinte comando:

```sh
$ ./run.sh
```

<br>

É possível executar a **API** utilizando Docker, através do seguinte comando:

```sh
$ docker compose up
```

No entanto, através do Docker, a **API** requer autenticação.


<br>


## Documentação

Ao executar a **API**, você pode consultar a documentação em [http://localhost:8000/docs](http://localhost:8000/docs).


<br>


# API

A **API** faz parte de um sistema de acompanhamento e cadastramento de reservas de voos.

<br>

## Autenticação

A **API** só requer autenticação no modo `PRD`:

```sh
# ./.env
export ENV="PRD"
```

A autenticação é feita através do envio de um token no cabeçalho das requisições.

Mais detalhes sobre o cabeçalho das requisições e o token na raíz do projeto em `README.md`.

<br>

## Gráficos

A **API** possui 3 endpoints para construção de gráficos:

| Elemento | Descrição                                          | API                                |
|----------|----------------------------------------------------|------------------------------------|
| Gráfico  | Partidas de passageiros por data                   | GET /api/v1/dashboard/chart/data/1 |
| Gráfico  | Chegadas de passageiros por data                   | GET /api/v1/dashboard/chart/data/2 |
| Gráfico  | Número de passageiros por rota                     | GET /api/v1/dashboard/chart/data/3 |

Os endpoints já entregam os dados do eixo X (category) e Y (value):

```json
{
    "category": "2025-03-14",
    "value": 27
}
```

<br>

## Testes

A **API** possui um endpoint para o upload do arquivo de teste:

| Descrição             | API                                |
|-----------------------|------------------------------------|
| Upload das reservas   | POST /api/v1/booking/file/upload   |

Fornecemos um arquivo de teste em `./test/booking.xlsx`.

Exemplo:

```json
{
    "first_name": "Isabela",
    "last_name": "Rocha",
    "birthday": "1987-01-16",
    "document": "16287453044",
    "departure_date": "2025-04-04",
    "departure_iata": "GRU",
    "arrival_iata": "BSB",
    "arrival_date": "2025-04-09",
}
```

Reserva:

```plaintext
Nome              : Isabela
Sobrenome         : Rocha
Aniversário       : 1987-01-16 (YYYY-MM-DD)
Documento         : 162.874.530-44 (CPF)
Data da Partida   : 2025-04-04 (YYYY-MM-DD)
Origem da Partida : GRU (Guarulhos - SP)
Origem da Chegada : BSB (Brasília - DF)
Data da Chegada   : 2025-04-09 (YYYY-MM-DD)
```
