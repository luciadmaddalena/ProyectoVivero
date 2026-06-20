import os, json
from datos import categorias, sectores
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
    plantas = leer_plantas()
    nombre_comun = pedir_string('Ingresar nombre común: ')
    nombre_cientifico = pedir_string('Ingresar nombre científico: ')
    categoria = pedir_opcion('Ingresar categoría: ', categorias)
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
    print("--------------------------------")
    print(f"La planta '{nombre_comun}' ha sido agregada al stock con ID {planta['id']}.")
    print("--------------------------------")

def listar_planta():
    print("--- Listado de plantas ---")
    plantas = leer_plantas()
    if not plantas:
        print("--------------------------------")
        print("No hay plantas en el vivero para mostrar.")
        print("--------------------------------")
        return
    
    print("-----------------------------")
    print("Filtrar por:")
    print("1. Ver todas")
    print("2. Categoría")
    print("3. Sector")
    opcion_filtro = pedir_string("Seleccione una opción de filtro: ")

    resultados = []
    if opcion_filtro == "2":
        categoria = pedir_opcion('Ingresar categoría: ', categorias)
        for planta in plantas:
            if planta['categoria'] == categoria:
                resultados.append(planta)
    elif opcion_filtro == "3":
        sector = pedir_opcion('Ingresar sector: ', sectores)
        for planta in plantas:
            if planta['sector'] == sector:
                resultados.append(planta)
    else:
        resultados = plantas

    if not resultados:
        print("--------------------------------")
        print("No se encontraron plantas que coincidan con el filtro seleccionado.")
        print("--------------------------------")
        return

    for planta in resultados:
        print("-----------------------------")
        print(f"ID: {planta['id']}")
        print(f"Nombre común: {planta['nombre_comun']}")
        print(f"Nombre científico: {planta['nombre_cientifico']}")
        print(f"Categoría: {planta['categoria']}")
        print(f"Sector: {planta['sector']}")
        print(f"Stock: {planta['stock']}")
        print(f"Precio: {planta['precio']}")
        print(f"Cuidados: {planta['cuidados']}")
        print("-----------------------------")



def buscar_planta ():
    print("--- Buscar planta ---")
    plantas = leer_plantas()
    if not plantas:
        print("--------------------------------")
        print("No hay plantas en el vivero para buscar.")
        print("--------------------------------")
        return


    termino = pedir_string('Ingrese el nombre común o científico de la planta a buscar: ')

    resultados = []
    for planta in plantas:
        if termino in planta['nombre_comun'].lower() or termino in planta['nombre_cientifico'].lower():
            resultados.append(planta)

    if not resultados:
        print("--------------------------------")
        print("No se encontraron plantas que coincidan con el nombre.")
        return
    
    for planta in resultados:
            print("-----------------------------")
            print(f"ID: {planta['id']}")
            print(f"Nombre común: {planta['nombre_comun']}")
            print(f"Nombre científico: {planta['nombre_cientifico']}")
            print(f"Categoría: {planta['categoria']}")
            print(f"Sector: {planta['sector']}")
            print(f"Stock: {planta['stock']}")
            print(f"Precio: {planta['precio']}")
            print(f"Cuidados: {planta['cuidados']}")
            print("-----------------------------")




def modificar_planta ():
    print("--- Modificar planta ---")
    plantas = leer_plantas()
    if not plantas:
        print("-------------------------------")
        print("No hay plantas en el vivero para modificar.")
        print("-------------------------------")
        return
    
    nombre_comun = pedir_string('Para modificar ingrese el nombre común: ').lower()
    for planta in plantas:
        if nombre_comun == planta['nombre_comun'].lower():
            print('Ingrese los nuevos datos de la planta')
            planta['sector'] = pedir_opcion('Ingresar sector: ', sectores)
            planta['stock'] = pedir_entero('Ingresar stock: ')
            planta['precio'] = pedir_float('Ingresar precio: ')
            planta['cuidados'] = pedir_string('Ingresar cuidados: ')
        else:
            print("-------------------------------")
            print("No se encontraron plantas con ese nombre.")
            print("-------------------------------")
    guardar_plantas(plantas)
    print("-------------------------------")
    print("Planta actualizada correctamente.")
    print("-------------------------------")


def baja_planta ():
    print("--- Dar de baja una planta ---")
    plantas = leer_plantas()
    if not plantas:
        print("No hay plantas en el vivero para dar de baja.")
        print("-------------------------------")
        return
    
    nombre_comun = pedir_string('Para dar de baja ingrese el nombre común: ')
    
    planta_encontrada = None
    for planta in plantas:
        if planta['nombre_comun'] == nombre_comun:
            planta_encontrada = planta
            break

    if not planta_encontrada:
        print("-------------------------------")
        print("No se encontró ninguna planta con ese nombre.")
        print("-------------------------------")
        return
    

    print(f"Planta a eliminar: {planta_encontrada['nombre_comun']}")
    confirmar = pedir_string("¿Confirma que desea eliminar esta planta? (s/n): ")
 

    if confirmar == "s":
        plantas.remove(planta_encontrada)
        guardar_plantas(plantas)
        print("-------------------------------")
        print(f"La planta '{planta_encontrada['nombre_comun']}' ha sido eliminada.")
        print("-------------------------------")
    else:
        print("-------------------------------")
        print("Operación cancelada. La planta no ha sido eliminada.")
        print("-------------------------------")
    



def menu_plantas():
    while True: 
        print("=" * 30)
        print(" 🪴 STOCK DE PLANTAS  ")
        print("=" * 30)
        print("1. Cargar una planta nueva")
        print("2. Ver listado de plantas")
        print("3. Buscar una planta")
        print("4. Actualizar stock o precio")
        print("5. Dar de baja una planta")
        print("9. Volver al menú principal")
        print("=" * 30)
        
        opcion = input("¿Qué querés hacer?")

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
            print("-------------------------------")
            print("Opción no valida, intente de nuevo")
            print("-------------------------------")

