#main menu

import os
import time
import textwrap

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        menu = """
        =============================================
                Simulador de Gasto Diario
        =============================================
        Seleccione una opcion:
        1. Registrar nuevo gasto
        2. Listar gastos
        3. Calcular total de gastos
        4. Generar reporte de gastos
        5. Salir
        ============================================="""

        print(textwrap.dedent(menu))

        try:
            opcion = int(input("Elige una opcion: "))
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
                pass
            case 5:
                break
            case _:
                print("Por favor elige una opción valida...")
                time.sleep(1)
                continue

if __name__ == "__main__":
    main()



