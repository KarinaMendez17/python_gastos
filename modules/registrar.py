import os
import textwrap
import time
from services import sRegistrar

def menuRegistrar():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu = """
            =============================================
                        Registrar Nuevo Gasto
            =============================================
            1. Comida
            2. Transporte
            3. Entretenimiento
            4. Otros/Sin Categoria
            5. Crear nueva categoria
            6. Volver al menu principal
            =============================================
            """

        print(textwrap.dedent(menu))

        try:
            opcion = int(input("Seleccione el tipo de gasto: "))
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

        match opcion:
            case 1:
                sRegistrar.registrarCategoria("Comida")
            case 2:
                sRegistrar.registrarCategoria("Transporte")
            case 3:
                sRegistrar.registrarCategoria("Entretenimiento")
            case 4:
                sRegistrar.registrarCategoria("Otros")
            case 5:
                sRegistrar.crear()
            case 6:
                return
            case _:
                print("Por favor elige una opción valida...")
                time.sleep(1)
                continue