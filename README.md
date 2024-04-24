# frases-aleatorias-api
API que provê frases aleatórias.

Ela utiliza outras duas APIs externas para buscar as frases em inglês e uma para traduzir para o português.

Ele vai contar com um serviço:
- GET /frase - retornando uma frase aleatória de um dos serviços em português.

API externa:
- https://uselessfacts.jsph.pl/ - fatos inúteis aleatórios
- https://github.com/sameerkumar18/geek-joke-api - permite que você busque uma piada aleatória relacionada a geeks/programação para uso em todos os tipos de aplicativos.
- https://libretranslate.com/docs/ - api que para traduzir as frases

Estas APIs não precisam de autenticação.

Será disponibilizado o swagger com a documentação no seguinte endereço: /openapi

---

## Como executar em modo de desenvolvimento

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```shell
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```shell
(env)$ flask run --host 127.0.0.1 --port 5010
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```shell
(env)$ flask run --host 127.0.0.1 --port 5010 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5010/#/) no navegador para verificar o status da API em execução.

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```shell
$ docker build -t nome_da_sua_imagem .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```shell
$ docker run -d -p 8080:80 nome_da_sua_imagem
```

Uma vez executando, para acessar o front-end, basta abrir o [http://localhost:8080/#/](http://localhost:8080/#/) no navegador.
