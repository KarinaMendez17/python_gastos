import os
import textwrap
import time
from datetime import datetime
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
    os.system('cls' if os.name == 'nt' else 'clear')

    datos = utilities.cargar()
    lista = datos.get("gastos", [])

    print(textwrap.dedent("""
        =============================================
                 FILTRAR GASTOS POR CATEGORÍA
        =============================================
    """))

    if not lista:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    categorias = sorted({catLista.get("categoria", "Sin categoria") for catLista in lista})

    print("Categorías disponibles:\n")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")

    opcion = input("\nEscribe el NÚMERO de la categoría o el nombre exacto: ").strip()
    if not opcion:
        print("Entrada vacía. Cancelando filtro...")
        time.sleep(1)
        return

    categoria_elegida = None

    if opcion.isdigit():
        idx = int(opcion)
        if 1 <= idx <= len(categorias):
            categoria_elegida = categorias[idx - 1]
    else:
        opcion_norm = opcion.lower()
        for cat in categorias:
            if cat.lower() == opcion_norm:
                categoria_elegida = cat
                break

    if categoria_elegida is None:
        print("Categoría no encontrada.")
        input("\nPresiona Enter para volver...")
        return

    filtrados = [
        catLista for catLista in lista
        if catLista.get("categoria", "").lower() == categoria_elegida.lower()
    ]

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"GASTOS EN LA CATEGORÍA: {categoria_elegida}\n")

    if not filtrados:
        print("No hay gastos registrados en esta categoría.")
        input("\nPresiona Enter para volver...")
        return

    for i, gasto in enumerate(filtrados, start=1):
        print(f"{i}. Monto       : {gasto.get('monto', 0)}")
        print(f"   Descripción: {gasto.get('descripcion', 'Sin descripción')}")
        print(f"   Fecha      : {gasto.get('fecha', 'Sin fecha')}")
        print("-" * 50)

    input("\nPresiona Enter para volver...")


def filtrarRango():
    os.system('cls' if os.name == 'nt' else 'clear')

    datos = utilities.cargar()
    lista = datos.get("gastos", [])

    print(textwrap.dedent("""
        =============================================
                 FILTRAR POR RANGO DE FECHAS
        =============================================
        Formato esperado: YYYY-MM-DD
    """))

    if not lista:
        print("No hay gastos registrados aún.")
        input("\nPresiona Enter para volver...")
        return

    while True:
        inicio = input("Ingresa la FECHA INICIAL (YYYY-MM-DD): ").strip()
        try:
            fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato inválido. Intenta de nuevo.\n")
            continue

    while True:
        fin = input("Ingresa la FECHA FINAL (YYYY-MM-DD): ").strip()
        try:
            fecha_fin = datetime.strptime(fin, "%Y-%m-%d")
            if fecha_fin < fecha_inicio:
                print("La fecha final NO puede ser menor que la inicial.\n")
                continue
            break
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

    filtrados = []
    for gasto in lista:
        try:
            fecha_gasto = datetime.strptime(gasto.get("fecha", ""), "%Y-%m-%d")
        except(ValueError, KeyboardInterrupt) as sixth:
            print(f"ERROR: {sixth}. Ingresa un caracter valido...")
            input("Presione 'Enter' para continuar...")
            continue

        if fecha_inicio <= fecha_gasto <= fecha_fin:
            filtrados.append(gasto)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"GASTOS ENTRE {inicio} Y {fin}\n")

    if not filtrados:
        print("No se encontraron gastos en ese rango.")
        input("\nPresiona Enter para volver...")
        return

    for i, g in enumerate(filtrados, start=1):
        print(f"{i}. Categoría : {g.get('categoria', 'N/A')}")
        print(f"   Monto     : {g.get('monto', 0)}")
        print(f"   Descripción: {g.get('descripcion', 'Sin descripción')}")
        print(f"   Fecha     : {g.get('fecha', 'Sin fecha')}")
        print("-" * 50)

    input("\nPresiona Enter para volver...")
