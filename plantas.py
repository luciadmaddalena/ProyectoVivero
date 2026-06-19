import os, json
from datos import total_de_plantas , categorias, sectores
from validaciones import pedir_entero, pedir_float, pedir_string, pedir_opcion, siguiente_id


NOMBRE_ARCHIVO_PLANTAS = os.path.join('data', 'plantas.json')


#ARCHIVOS
def leer_plantas():
    #leer datos de un json
    ##para ver si un archivo existe
    if os.path.exists(NOMBRE_ARCHIVO_PLANTAS):
        with open(NOMBRE_ARCHIVO_PLANTAS, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return[]
    
def guardar_plantas(datos):
    #guardar datos en un json
    with open(NOMBRE_ARCHIVO_PLANTAS, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

#FUNCIONES
def alta_planta ():
    print("--- Cargar nueva planta ---")
    plantas = leer_plantas
    nombre_comun = pedir_string('Ingresar nombre comun: ')
    nombre_cientifico = pedir_string('Ingresar nombre cientifico: ')
    categoria = pedir_opcion('Ingresar categoria: ', categorias)
    sector = pedir_opcion('Ingresar sector: ', sectores)
    stock = pedir_entero('Ingresar stock: ')
    precio = pedir_float('Ingresar precio: ')
    cuidados = pedir_string('Ingresar cuidados: ')

    planta = {
         "id": siguiente_id(plantas),
         "nombre_comun": nombre_comun,
         "nombre_cientifico": nombre_cientifico,
         "categoria": categoria,
         "sector": sector,
         "stock": stock,
         "precio": precio,
         "cuidados": cuidados
    }
    plantas.append(planta)
    guardar_plantas(plantas)
    print(f"La planta '{nombre_comun}' ha sido agregada al stock con ID {planta['id']}.")

def listar_planta():
    print("--- Listado de plantas ---")
    plantas = leer_plantas
    if not plantas:
        print("No hay plantas en el vivero para mostrar.")
        return
    
    print("Filtrar por:")
    print("1. ver todas")
    print("2. Categoria")
    print("3. Sector")
    opcion_filtro = input("Seleccione una opcion de filtro: ").strip()

    resultados = []
    if opcion_filtro == "2":
        categoria = pedir_opcion('Ingresar categoria: ', categorias)
        resultados = [planta for planta in plantas if planta['categoria'] == categoria]
    elif opcion_filtro == "3":
        sector = pedir_opcion('Ingresar sector: ', sectores)
        resultados = [planta for planta in plantas if planta['sector'] == sector]
    else:
        resultados = plantas

    if not resultados:
        print("No se encontraron plantas que coincidan con el filtro seleccionado.")
        return

    for planta in resultados:
        print(f"ID: {planta['id']}")
        print(f"Nombre comun: {planta['nombre_comun']}")
        print(f"Nombre cientifico: {planta['nombre_cientifico']}")
        print(f"Categoria: {planta['categoria']}")
        print(f"Sector: {planta['sector']}")
        print(f"Stock: {planta['stock']}")
        print(f"Precio: {planta['precio']}")
        print(f"Cuidados: {planta['cuidados']}")
        print("-----------------------------")



def buscar_planta ():
    print("--- Buscar planta ---")
    plantas = leer_plantas
    if not plantas:
        print("No hay plantas en el vivero para buscar.")
        return


    termino = input('Ingrese el nombre comun o cientifico de la planta a buscar: ').lower()

    resultados = []
    for planta in plantas:
        if termino in planta['nombre_comun'].lower() or termino in planta['nombre_cientifico'].lower():
            resultados.append(planta)

    if not resultados:
        return
    
    for planta in resultados:
            print(f"ID: {planta['id']}")
            print(f"Nombre comun: {planta['nombre_comun']}")
            print(f"Nombre cientifico: {planta['nombre_cientifico']}")
            print(f"Categoria: {planta['categoria']}")
            print(f"Sector: {planta['sector']}")
            print(f"Stock: {planta['stock']}")
            print(f"Precio: {planta['precio']}")
            print(f"Cuidados: {planta['cuidados']}")
            print("-----------------------------")




def modificar_planta ():
    print("--- Modificar planta ---")
    plantas = leer_plantas
    nombre_comun = input('Para modificar ingrese el nombre comun: ') .lower()
    for planta in plantas:
        if nombre_comun == planta['nombre_comun']:
            print('Ingrese los nuevos datos de la planta')
            planta['sector'] = input('Ingresar sector: ')
            planta['stock'] = int(input('Ingresar stock: '))
            planta['precio'] = float(input('Ingresar precio: '))
            planta['cuidados'] = input('Ingresar cuidados: ')
    #falta guardar cambios en plantas


def baja_planta ():
    print("--- Dar de baja una planta ---")
    if not total_de_plantas:
        print("No hay plantas en el vivero para dar de baja.")
        return
    
    nombre_comun = input('Para dar de baja ingrese el nombre comun: ') .lower()
    
    planta_encontrada = None
    for planta in total_de_plantas:
        if planta['nombre_comun'] == nombre_comun:
            planta_encontrada = planta
            break

    if not planta_encontrada:
        print("No se encontro ninguna planta con ese nombre.")
        return
    

    print(f"Planta a eliminar: {planta_encontrada['nombre_comun']}")
    confirmar = input ("¿Confirma que desea eliminar esta planta? (s/n): ").lower() .strip()
 

    if confirmar == "s":
        total_de_plantas.remove(planta_encontrada)
        print(f"La planta '{planta_encontrada['nombre_comun']}' ha sido eliminada.")
    else:
        print("Operacion cancelada. La planta no ha sido eliminada.")



def menu_plantas():
    while True: 
        print("==== STOCK DE PLANTAS ====")
        print("1. Cargar una planta nueva")
        print("2. Ver listado de plantas")
        print("3. Buscar una planta")
        print("4. Actualizar stock o precio")
        print("5. Dar de baja una planta")
        print("9. Volver al menu principal")
        
        opcion = input("Que queres hacer?")

        if opcion == "1":
            alta_planta()
        elif opcion == "2":
            listar_planta()
        elif opcion == "3":
            buscar_planta()
        elif opcion == "4":
            modificar_planta()
        elif opcion == "5":
            baja_planta()
        elif opcion == "9":
            break
        else:
            print("Opcion no valida, intente de nuevo")

