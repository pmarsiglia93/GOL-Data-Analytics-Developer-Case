# GOL Data Analytics | Developer Case (GDADC)

Olá,

Seja bem-vindo ao desafio técnico para desenvolvedor do time de Data Analytics da GOL.

O seu desafio é desenvolver uma UI em Angular (JavaScript) com base em uma API em FastAPI (Python).


<br>


# Telas

A API faz parte de um sistema de acompanhamento e cadastramento de reservas de voos.

<br>

## Tela 1

Deve conter os seguintes elementos:

| Elemento | Descrição             | API                                |
|----------|-----------------------|------------------------------------|
| Botão    | Cadastrar uma reserva | POST /api/v1/booking               |
| Botão    | Download das reservas | GET  /api/v1/booking/file/download |
| Botão    | Upload das reservas   | POST /api/v1/booking/file/upload   |
| Tabela   | Reservas              | GET  /api/v1/booking               |

**Objetivo:** Gerenciar e visualizar passageiros e reservas.

<br>

## Tela 2

Deve conter os seguintes elementos:

| Elemento | Descrição                                          | API                                |
|----------|----------------------------------------------------|------------------------------------|
| Gráfico  | Partidas de passageiros por data                   | GET /api/v1/dashboard/chart/data/1 |
| Gráfico  | Chegadas de passageiros por data                   | GET /api/v1/dashboard/chart/data/2 |
| Gráfico  | Número de passageiros por rota                     | GET /api/v1/dashboard/chart/data/3 |
| Tabela   | Partidas e chegadas de passageiros por data e rota | GET /api/v1/dashboard/data         |

**Objetivo:** Gerenciar e visualizar KPIs e métricas.

<br>

## Tabelas

As tabelas devem conter filtros e ordenações nas colunas que fazem sentido.

<br>

## Gráficos

Os gráficos devem ser de barras verticais.

Podem ser usadas bibliotecas de sua escolha.

Se não conseguir, não deixe de fazer os demais elementos.

<br>

## Datas

A API entrega datas no formato `YYYY-MM-DD`.

As tabelas devem apresentar as datas no formato `DD-MM-YYYY`.

Os gráficos devem apresentar as datas no formato `DD-MM`.

Podem ser usadas barras (`/`) no lugar de traços (`-`).

<br>

## Autenticação

A API requer autenticação com o envio de um token no cabeçalho das requisições:

```javascript
const headers = new HttpHeaders({
    Authorization: `Bearer ${encryptedToken}`
});
```

O token deve ser gerado da seguinte forma:

```javascript
const authTokenPass = environment.authTokenPass;

const authTokenKey = CryptoJS.enc.Base64.parse(environment.authTokenKey);
const authTokenIv = CryptoJS.enc.Utf8.parse(environment.authTokenIv);

const encryptedToken = CryptoJS.AES.encrypt(
    authTokenPass,
    authTokenKey,
    {
        iv: authTokenIv,
        mode: CryptoJS.mode.CBC
    }
).toString();
```


<br>


# API

A API em FastAPI (Python) está no diretório `back/`, onde há um `README.md`.

Após a execução, é possível acessar a documentação em [http://localhost:8000/docs](http://localhost:8000/docs).

Essa documentação será seu guia para o desenvolvimento das telas na UI em Angular (JavaScript).


<br>


# UI

A criatividade e o design serão parte dos critérios de avaliação.

A UI deve ser desenvolvida no diretório `front/`, onde fornecemos alguns arquivos.

A UI deve ser minimalista, porém, deve apresentar **consistência** e **boas práticas de UX**.

<br>

## Ambiente

Dentre os arquivos fornecidos temos:

- environments/environment.ts

As variáveis de ambiente presentes no arquivo devem ser usadas na UI.

Caso necessário, você pode incluir novas variáveis de ambiente.

Caso necessário, você pode criar um arquivo para produção.

Mantenha os valores das variáveis, exceto `production`.

<br>

## Execução

O comando `npm start` deverá executar a UI da seguinte forma:

```sh
ng serve --host 0.0.0.0 --disable-host-check
```

O avaliador deverá ser capaz de executar a UI com os seguintes comandos:

```sh
$ npm install
$ npm start
```

O avaliador deverá ser capaz de acessar a UI em [http://localhost:4200](http://localhost:4200).

<br>

## Requisitos

- Node.js=18.19.1

<br>

- Angular=19.2.x
- [crypto-js](https://www.npmjs.com/package/crypto-js)=4.2.0

<br>

- Material Design 3
- Material Symbols & Icons


<br>


# Bônus

Desafios que contam como bônus na avaliação:

- Docker
- Notificações

<br>

## Docker

Dentre os arquivos fornecidos temos:

- Dockerfile
- nginx.conf

O arquivo Dockerfile deverá ser ajustado, se necessário.

O avaliador deverá ser capaz de executar a UI com os seguintes comandos:

```sh
$ docker build -t gdadc-ui .
$ docker run -d --name gdadc-ui -p 4200:80 gdadc-ui
```

O avaliador deverá ser capaz de acessar a UI em [http://localhost:4200](http://localhost:4200).

<br>

## Notificações

A UI deverá contar com notificações do tipo *toast* para as ações do usuário ou erros da API.


<br>


# Entrega

Entregue o desafio em até **7 dias**.

Faça um *fork* do repositório original no GitHub.

Abra um *pull request* para o repositório original no GitHub.
