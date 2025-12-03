import os
import textwrap
import time
from services import sReporte

def menuReporte():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        menu = """
            =============================================
                    Generar Reporte de Gastos
            =============================================
            1. Reporte diario
            2. Reporte semanal
            3. Reporte mensual
            4. Regresar al menú principal
            =============================================
            """
        
        
        print(textwrap.dedent(menu))

        try:
            opcion = int(input("Seleccione el tipo de reporte: "))
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

        match opcion:
            case 1:
                sReporte.totalDiario()
            case 2:
                sReporte.totalSemanal()
            case 3:
                sReporte.totalMensual()
            case 4:
                return
            case _:
                print("Por favor elige una opción valida...")
                time.sleep(1)
                continue