import os
import textwrap
from services import utilities


def vTodo():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    datos = utilities.cargar()
    lista = datos.get("gastos", [])

    print(textwrap.dedent("""
        =============================================
                    LISTADO DE TODOS LOS GASTOS
        =============================================
    """))

    if not lista:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    for i, gasto in enumerate(lista, start=1):
        print(f"{i}. Categoría : {gasto.get('categoria', 'N/A')}")
        print(f"   Monto     : {gasto.get('monto', 0)}")
        print(f"   Descripción: {gasto.get('descripcion', 'Sin descripción')}")
        print(f"   Fecha     : {gasto.get('fecha', 'Sin fecha')}")
        print("-" * 50)

    input("\nPresiona Enter para volver...")

def filtrarCat():
    pass

def filtrarRango():
    pass
