import json
import os

RUTA = os.path.join(os.path.dirname(__file__), "..", "data", "gastos.json")
RUTA = os.path.abspath(RUTA)

def cargar():
    if not os.path.exists(RUTA):
        return {"gastos": []}
    
    try:
        with open(RUTA, "r", encoding="utf-8") as am:
            return json.load(am)
    except:
        return {"gastos": []}
    

def guardar(datos):
    with open(RUTA, "w", encoding="utf-8") as am:
        json.dump(datos, am, indent=4, ensure_ascii=False)