total_de_plantas = []

def alta_planta ():
    print("--- Cargar nueva planta ---")
    nombre_comun = input('Ingresar nombre comun: ') .lower()
    nombre_cientifico = input('Ingresar nombre cientifico: ') .lower()
    categoria = input('Ingresar categoria: ') .lower()
    sector = input('Ingresar sector: ') .lower()
    stock = int(input('Ingresar stock: '))
    precio = float(input('Ingresar precio: '))
    cuidados = input('Ingresar cuidados: ') .lower()

    planta = {
         "id": len(total_de_plantas) +1,
         "nombre_comun": nombre_comun,
         "nombre_cientifico": nombre_cientifico,
         "categoria": categoria,
         "sector": sector,
         "stock": stock,
         "precio": precio,
         "cuidados": cuidados
    }
    total_de_plantas.append(planta)


def mostrar_planta ():
    print("--- Mostrar plantas ---")
    for planta in total_de_plantas:
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
    termino = input('Ingrese el nombre comun o cientifico de la planta a buscar: ').lower()

    resultados = []
    for planta in total_de_plantas:
        if termino in planta['nombre_comun'].lower() or termino in planta['nombre_cientifico'].lower():
            resultados.append(planta)

        if not resultados:
            print("No se encontraron plantas que coincidan con el termino de busqueda.")
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
    nombre_comun = input('Para modificar ingrese el nombre_comun: ') .lower()
    for planta in total_de_plantas:
        if nombre_comun == planta['nombre_comun']:
            print('Ingrese los nuevos datos de la planta')
            planta['sector'] = input('Ingresar sector: ')
            planta['stock'] = int(input('Ingresar stock: '))
            planta['precio'] = float(input('Ingresar precio: '))
            planta['cuidados'] = input('Ingresar cuidados: ')


def baja_planta ():
    print("--- Dar de baja una planta ---")
    if not total_de_plantas:
        print("No hay plantas en el vivero para dar de baja.")
        return
    
    nombre_comun = input('Para dar de baja ingrese el nombre_comun: ') .lower()
    confirmar = input ("¿Confirma que desea eliminar esta planta? (s/n): ").lower() .strip()
 
    print(f"Planta a eliminar: {nombre_comun}")

    if confirmar == "s":
        total_de_plantas.remove(nombre_comun)
        print(f"La planta '{nombre_comun}' ha sido eliminada.")
    else:
        print("Operacion cancelada. La planta no ha sido eliminada.")
    

    


    
    #nombre_comun = input('Para dar de baja ingrese en #nombre_comun: ')
    #for planta in total_de_plantas:
    #    if nombre_comun == alta_planta ('nombre_comun'):
    #        total_de_plantas.remove(planta)
    #        break




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
            mostrar_planta()
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

menu_plantas()