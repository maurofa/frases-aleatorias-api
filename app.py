from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
import requests
import json

from model.frase import Frase
from schemas.error import ErrorSchema
from schemas.frase import FrasePathSchema, FraseViewSchema, apresenta_frase

info = Info(title="API das frases aleatórias", version="0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapidDoc")
frases_tag = Tag(name="Frases", description="Frases aleatórias")

@app.get('/', tags=[home_tag])
def home():
  """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
  """
  return redirect('/openapi')

@app.get("/frases/<int:numeroServidor>", tags=[frases_tag],
         responses={"200": FraseViewSchema, "404": ErrorSchema})
def pegaFrase(path: FrasePathSchema):
  """Traz as frases de um dos servidores

  Returns:
      Frase: frase aleatória de um dos servidores
  """

  if path.numeroServidor == 0:
    proximoServidor = 1
    path = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    r = requests.get(path)
    content = json.loads(r.content)
    texto = content.get("text")
  else:
    proximoServidor = 0
    path = "https://geek-jokes.sameerkumar.website/api?format=json"
    r = requests.get(path)
    content = json.loads(r.content)
    texto = content.get("joke")
  frase = Frase(texto, proximoServidor)
  return apresenta_frase(frase)

