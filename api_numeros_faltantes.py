from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="API para encontrar número faltante")

class NumeroInput(BaseModel):
    numeros: List[int]

class Conjunto100:
    def __init__(self):
        self.todos = set(range(1, 101))  # Conjunto original del 1 al 100

    def extraer(self, numeros: List[int]) -> int:
        if not all(1 <= n <= 100 for n in numeros):
            raise ValueError("Todos los números deben estar entre 1 y 100")
        if len(numeros) != 99:
            raise ValueError("La lista debe contener exactamente 99 números")

        ingresados = set(numeros)
        faltantes = self.todos - ingresados

        if len(faltantes) != 1:
            raise ValueError("No se pudo determinar un único número faltante")

        return faltantes.pop()

@app.post("/numero_faltante")
def encontrar_numero_faltante(input_data: NumeroInput):
    try:
        conjunto = Conjunto100()
        faltante = conjunto.extraer(input_data.numeros)
        return {"numero_faltante": faltante}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Ejecutar con: uvicorn api_numeros_faltantes:app --reload
