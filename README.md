# frases-aleatorias-api
API que provê frases aleatórias.

Ela utiliza outras duas APIs externas para buscar as frases em inglês.

Ele vai contar com um serviço:
- GET /frase - retornando uma frase aleatória de um dos serviços em português.

API externa:
- https://uselessfacts.jsph.pl/ - fatos inúteis aleatórios
- https://github.com/sameerkumar18/geek-joke-api - permite que você busque uma piada aleatória relacionada a geeks/programação para uso em todos os tipos de aplicativos.

Estas APIs não precisam de autenticação.

Será disponibilizado o swagger com a documentação no seguinte endereço: /openapi

Desenho esquemático do Sistema:

[![Orçamento Doméstico](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVEJcbiAgc3ViZ3JhcGggRnJvbnRlbmRcbiAgICBXRUIoT3LDp2FtZW50byBEb23DqXN0aWNvIFdlYilcbiAgZW5kXG4gIHN1YmdyYXBoIEJhY2tlbmRcbiAgICBBUEkoT3LDp2FtZW50byBEb23DqXN0aWNvIC0gQVBJKVxuICAgIEdhdGV3YXkoRnJhc2VzIC0gQVBJKVxuICAgIEJEKEJhbmNvIGRlIERhZG9zIGVtIFNRTGl0ZSlcbiAgZW5kXG4gIHN1YmdyYXBoIEFQSXMgRXh0ZXJuYXNcbiAgICBHSihHZWVrLUpva2VzKSAgXG4gICAgUlVGKFJhbmRvbSBVc2VsZXNzIEZhY3RzKVxuICBlbmRcbiAgXG4gIFdFQi0tPkFQSVxuICBXRUItLT5HYXRld2F5XG4gIEdhdGV3YXktLS0tPkdKXG4gIEdhdGV3YXktLS0tPlJVRlxuICBBUEktLT5CRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://workflow.jace.pro/#/edit/eyJjb2RlIjoiZ3JhcGggVEJcbiAgc3ViZ3JhcGggRnJvbnRlbmRcbiAgICBXRUIoT3LDp2FtZW50byBEb23DqXN0aWNvIFdlYilcbiAgZW5kXG4gIHN1YmdyYXBoIEJhY2tlbmRcbiAgICBBUEkoT3LDp2FtZW50byBEb23DqXN0aWNvIC0gQVBJKVxuICAgIEdhdGV3YXkoRnJhc2VzIC0gQVBJKVxuICAgIEJEKEJhbmNvIGRlIERhZG9zIGVtIFNRTGl0ZSlcbiAgZW5kXG4gIHN1YmdyYXBoIEFQSXMgRXh0ZXJuYXNcbiAgICBHSihHZWVrLUpva2VzKSAgXG4gICAgUlVGKFJhbmRvbSBVc2VsZXNzIEZhY3RzKVxuICBlbmRcbiAgXG4gIFdFQi0tPkFQSVxuICBXRUItLT5HYXRld2F5XG4gIEdhdGV3YXktLS0tPkdKXG4gIEdhdGV3YXktLS0tPlJVRlxuICBBUEktLT5CRCIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

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

Abra o [http://localhost:5010/#/](http://localhost:5010/#/) no navegador para verificar o status da API em execução.

## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```shell
$ docker build -t frases-aleatorias-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, o seguinte comando:

```shell
$ docker run -d -p 5010:5000 frases-aleatorias-api
```

Uma vez executando, para acessar o swagger desta api, basta abrir o [http://localhost:5010/#/](http://localhost:5010/#/) no navegador.
