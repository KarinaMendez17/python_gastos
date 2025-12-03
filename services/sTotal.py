import os
import textwrap
import time
from datetime import datetime, timedelta
from services import utilities

def cargarGastos():
    datos = utilities.cargar()
    return datos.get("gastos", [])

def totalDiario():
    os.system('cls' if os.name == 'nt' else 'clear')

    gastos = cargarGastos()

    print(textwrap.dedent("""
        =============================================
                    TOTAL DIARIO DE GASTOS
        =============================================
        Formato de fecha: YYYY-MM-DD
    """))

    if not gastos:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    fecha_str = input("Ingresa la fecha (YYYY-MM-DD): ").strip()
    try:
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except(ValueError, KeyboardInterrupt) as sixth:
        print(f"ERROR: {sixth}. Ingresa un caracter valido...")
        time.sleep(1)
        return

    total = 0
    for g in gastos:
        try:
            f_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d").date()
        except:
            continue

        if f_gasto == fecha_obj:
            total += float(g.get("monto", 0))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"TOTAL DEL {fecha_str}: {total:.2f}")
    input("\nPresiona Enter para volver...")

def totalSemanal():
    os.system('cls' if os.name == 'nt' else 'clear')

    gastos = cargarGastos()

    print(textwrap.dedent("""
        =============================================
                    TOTAL SEMANAL DE GASTOS
        =============================================
        Ingresa una fecha y se calculará la semana.
        Semana: lunes → domingo
        Formato: YYYY-MM-DD
    """))

    if not gastos:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    fecha_str = input("Ingresa una fecha dentro de la semana: ").strip()
    try:
        fecha_base = datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except(ValueError, KeyboardInterrupt) as sixth:
        print(f"ERROR: {sixth}. Ingresa un caracter valido...")
        time.sleep(1)
        return

    lunes = fecha_base - timedelta(days=fecha_base.weekday())
    domingo = lunes + timedelta(days=6)

    total = 0
    for g in gastos:
        try:
            f_gasto = datetime.strptime(g["fecha"], "%Y-%m-%d").date()
        except:
            continue

        if lunes <= f_gasto <= domingo:
            total += float(g.get("monto", 0))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"TOTAL DEL {lunes} AL {domingo}: {total:.2f}")
    input("\nPresiona Enter para volver...")

def totalMensual():
    os.system('cls' if os.name == 'nt' else 'clear')

    gastos = cargarGastos()

    print(textwrap.dedent("""
        =============================================
                    TOTAL MENSUAL DE GASTOS
        =============================================
        Formato esperado: YYYY-MM
    """))

    if not gastos:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    mes_str = input("Ingresa el mes (YYYY-MM): ").strip()

    try:
        datetime.strptime(mes_str + "-01", "%Y-%m-%d")
    except(ValueError, KeyboardInterrupt) as sixth:
        print(f"ERROR: {sixth}. Ingresa un caracter valido...")
        time.sleep(1)
        return

    total = 0
    for g in gastos:
        fecha_g = g.get("fecha", "")
        if fecha_g.startswith(mes_str):
            try:
                total += float(g.get("monto", 0))
            except(ValueError, KeyboardInterrupt) as sixth:
                print(f"ERROR: {sixth}. Ingresa un caracter valido...")
                input("Presione 'Enter' para continuar...")
                continue

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"TOTAL DEL MES {mes_str}: {total:.2f}")
    input("\nPresiona Enter para volver...")

