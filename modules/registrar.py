import os
import textwrap
import time

def menuRegistrar():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu = """
            =============================================
                        Registrar Nuevo Gasto
            =============================================
            1. Comida
            2. Transporte
            3. Crear nueva categoria
            4. Volver al menu principal
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
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                return
            case _:
                print("Por favor elige una opción valida...")
                time.sleep(1)
                continue