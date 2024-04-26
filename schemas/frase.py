from pydantic import BaseModel
from model.frase import Frase

class FraseViewSchema(BaseModel):
  """Define como uma frase será retornada
  """
  frase: str = "Ser ou não ser, eis a questão!"
  proximoServidor: int

class FrasePathSchema(BaseModel):
  """Define o pathParam numeroServidor
  """
  numeroServidor: int

def apresenta_frase(frase: Frase):
  """Retorna a representação da Frase

  Args:
      frase (Frase): frase que será retornada
  """
  return {
    "proximoServidor": frase.numeroServidor,
    "frase": frase.texto
  }
