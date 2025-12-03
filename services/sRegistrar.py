import time
from services import utilities
from datetime import datetime
import os

CATEGORIAS_PREDEFINIDAS = ["Comida", "Transporte", "Entretenimiento", "Otros"]

def registrarGasto():
    while True:
        try:
            monto = float(input("Ingresa el monto: "))
            if monto <= 0:
                print("No puedes registrar montos negativos o iguales a cero.")
                time.sleep(1)
                continue

            confirmar = input(f"¿El monto {monto} es correcto? (s/n): ").strip().lower()
            if confirmar == "s":
                return monto
            elif confirmar == "n":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                print("Responde con 's' o 'n'.")
                time.sleep(1)
                continue
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

def rDescripcion():
    descripcion = input("Ingresa una descripción del gasto (Opcional): ")
    descripcion = descripcion.strip().lower()

    return descripcion if descripcion else "sin descripción"


def guardarGasto(categoria):
    datos = utilities.cargar()

    if "gastos" not in datos or not isinstance(datos["gastos"], list):
        datos["gastos"] = []

    monto = registrarGasto()
    descripcion = rDescripcion()
    fecha = datetime.now().strftime("%Y-%m-%d")

    nuevo_gasto = {
        "categoria": categoria,
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha
    }

    datos["gastos"].append(nuevo_gasto)
    utilities.guardar(datos)

    print("Gasto registrado correctamente.")
    time.sleep(1)


def registrarCategoria(categoria):
    print(f"\n--- Registro de gasto: {categoria} ---")
    guardarGasto(categoria)

def crear():
    while True:
        try:
            print("\n--- Crear nueva categoría ---")
            nombre = input("Nombre de la nueva categoría: ").strip()

            if not nombre:
                print("No puedes crear una categoría vacía.")
                time.sleep(1)
                return
            
            nombre_normalizado = nombre.capitalize()

            if nombre_normalizado in CATEGORIAS_PREDEFINIDAS:
                print("Esa categoría ya existe entre las predefinidas.")
                time.sleep(1)
                return
            
            confirmar = input(f"¿La categoría '{nombre_normalizado}' es correcta? (s/n): ").strip().lower()
            if confirmar == "s":
                registrarCategoria(nombre_normalizado)
                return
            elif confirmar == "n":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            else:
                print("Responde con 's' o 'n'.")
                time.sleep(1)
                continue
        
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue