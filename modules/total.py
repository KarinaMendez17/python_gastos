import os
import textwrap
import time

def menuTotal():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        menu = """
            =============================================
                    Calcular Total de Gastos
            =============================================
            1. Calcular total diario
            2. Calcular total semanal
            3. Calcular total mensual
            4. Regresar al menú principal
            =============================================
            """
        
        print(textwrap.dedent(menu))

        try:
            opcion = int(input("Seleccione el periodo de calculo: "))
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