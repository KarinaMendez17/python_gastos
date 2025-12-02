import os
import textwrap
import time
from services import sListar

def menuListar():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        menu = """
            =============================================
                            Listar Gastos
            =============================================
            1. Ver todos los gastos
            2. Filtrar por categoría
            3. Filtrar por rango de fechas
            4. Volver al menu principal
            =============================================
            """
        
        print(textwrap.dedent(menu))

        try:
            opcion = int(input("Seleccione una opcion para filtrar los gastos: "))
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

        match opcion:
            case 1:
                sListar.vTodo()
            case 2:
                sListar.filtrarCat()
            case 3:
                sListar.filtrarRango()
            case 4:
                return
            case _:
                print("Por favor elige una opción valida...")
                time.sleep(1)
                continue