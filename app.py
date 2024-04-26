from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
import requests
import json

from model.frase import Frase
from schemas.error import ErrorSchema
from schemas.frase import FraseViewSchema, apresenta_frase

info = Info(title="API das frases aleatórias", version="0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapidDoc")
frases_tag = Tag(name="Frases", description="Frases aleatórias")

contador = 0

@app.get('/', tags=[home_tag])
def home():
  """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
  """
  return redirect('/openapi')

@app.get("/frases", tags=[frases_tag],
         responses={"200": FraseViewSchema, "404": ErrorSchema})
def pegaFrase():
  """Traz as frases de um dos servidores

  Returns:
      Frase: frase aleatória de um dos servidores
  """
  global contador
  print(contador)
  if (contador % 2) == 0:
    path = "https://geek-jokes.sameerkumar.website/api?format=json"
    r = requests.get(path)
    content = json.loads(r.content)
    texto = content.get("joke")
  else:
    path = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    r = requests.get(path)
    content = json.loads(r.content)
    texto = content.get("text")
  contador += 1
  frase = Frase(texto)
  return apresenta_frase(frase)

