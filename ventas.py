import os, json
from datos import formas_pago
from validaciones import pedir_entero, pedir_float, pedir_string, pedir_opcion, siguiente_id, pedir_fecha 

NOMBRE_ARCHIVO_VENTAS = os.path.join('data', 'ventas.json')
NOMBRE_ARCHIVO_CLIENTES = os.path.join('data', 'clientes.json')
NOMBRE_ARCHIVO_PLANTAS = os.path.join('data', 'plantas.json')


#ARCHIVOS
def leer_ventas():
    if os.path.exists(NOMBRE_ARCHIVO_VENTAS):
        with open(NOMBRE_ARCHIVO_VENTAS, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return[]
    
def guardar_ventas(datos):
    #guardar datos en un json
    with open(NOMBRE_ARCHIVO_VENTAS, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

#para relacionarlo con el json de clientes
def leer_clientes():
    if os.path.exists(NOMBRE_ARCHIVO_CLIENTES):
        with open(NOMBRE_ARCHIVO_CLIENTES, 'rt', encoding='UTF-8') as archivo:
            return json.load(archivo)
    return []
#para relacionarlo con el json de plantas
def leer_plantas():
    if os.path.exists(NOMBRE_ARCHIVO_PLANTAS):
        with open(NOMBRE_ARCHIVO_PLANTAS, 'rt', encoding='UTF-8') as archivo:
            return json.load(archivo)
    return []
#para modificar el stock de plantas en json
def guardar_plantas(datos):
    with open(NOMBRE_ARCHIVO_PLANTAS, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


#FUNCIONES
def alta_venta():
    print("--- Registrar nueva venta ---")
    ventas = leer_ventas()
    clientes = leer_clientes()
    plantas = leer_plantas()

    #se pide el nombre del cliente relacionado con la venta
    cliente_venta = pedir_string("A qué cliente corresponde? Escriba nombre completo: ")
    
    cliente_elegido = None
    for cliente in clientes:
        if cliente_venta == cliente["nombre_completo"].lower():
            cliente_elegido = cliente 
            break
    
    if not cliente_elegido:
        print("--------------------------------")
        print("No existe ningún cliente con ese nombre.")
        print("--------------------------------")
        return
    print("--------------------------------")
    print("Cliente encontrado:", cliente_elegido["nombre_completo"], "ID: ", cliente_elegido["id"], "DNI: ", cliente_elegido["dni"])
    print("--------------------------------")

    
    fecha = pedir_fecha('Ingresar fecha: ')
    
    
    #se pide el nombre de la planta relacionada con la venta
    planta_venta = pedir_string("Qué planta compro? Escriba nombre común: ")
    resultado_planta = []
    for planta in plantas:
        if planta_venta == planta["nombre_comun"].lower():
            resultado_planta.append(planta)
    
    if not resultado_planta:
        print("No existe ninguna planta con ese nombre.")
        print("--------------------------------")
        return
    
    print("Planta encontrada:", resultado_planta[0]["nombre_comun"], "ID: ", resultado_planta[0]["id"], "Stock: ", resultado_planta[0]["stock"])


    cantidad = pedir_entero("Ingrese cantidad comprada: ")
    precio_unit = pedir_float("Ingresar precio unitario: ")
    total = cantidad * precio_unit
    items = [
        {"id_planta": resultado_planta[0]["id"], "cantidad": cantidad , "precio_unit": precio_unit}
    ]
    
    forma_pago = pedir_opcion('Ingresar forma de pago: ', formas_pago)

    
    venta = {
         "id": siguiente_id(ventas),
         "id_cliente": cliente_elegido["id"],#agrego cliente_elegido para buscar por dni 
         "cliente_venta": cliente_elegido["nombre_completo"], #
         "fecha": str(fecha),
         "items": items,
         "total": total,
         "forma_pago": forma_pago
    }
        
    ventas.append(venta)
    guardar_ventas(ventas)
    print("--------------------------------")
    print(f"La venta N° {venta['id']} ha sido registrada.")
    print("--------------------------------")

    #cuando se registra una venta, el stock de cada planta vendida tiene que
    #descontarse automáticamente.

    def descontar_stock(items, plantas):
        for item in items:
            id_planta = item["id_planta"]
            cantidad = item["cantidad"]

            for planta in plantas:
              if planta["id"] == id_planta:
                 planta["stock"] -= cantidad
                 break
        guardar_plantas(plantas)

    descontar_stock(items, plantas)
                


def listar_ventas():
    print ("--- Lista de ventas ---")
    ventas = leer_ventas()
    if not ventas:
        print("--------------------------------")
        print("No hay ventas registradas.")
        print("--------------------------------")
        return

    for venta in ventas:
            print(f"ID: {venta['id']}")
            print(f"ID Cliente: {venta['cliente_venta']}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Items: {venta['items']}")
            print(f"Total: {venta['total']}")
            print(f"Forma de pago: {venta['forma_pago']}")
            print("-----------------------------")


def buscar_venta():
    print ('--- Buscar ventas ---')
    ventas = leer_ventas()
    clientes = leer_clientes()
   
    print("Buscar por DNI:")
    dni = pedir_string('Ingresar DNI: ')

    id_cliente = None
    for cliente in clientes:
        if dni == cliente['dni'].strip():
            id_cliente = cliente["id"]
            break
        
    if not id_cliente:
        print("--------------------------------")
        print("No se encontró ningún cliente con ese DNI.")
        print("--------------------------------")
        return
        
    resultados = []
    for venta in ventas:
        if id_cliente == venta['id_cliente']:
            resultados.append(venta)
    if not resultados:
        print("--------------------------------")
        print("No hay ventas para ese cliente.")
        print("--------------------------------")
        return
        
    for venta in resultados:
            print("--------------------------------")
            print(f"ID venta: {venta['id']}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Total: {venta['total']}")
            print(f"Forma de pago: {venta['forma_pago']}")
            print("-----------------------------")
            



def modificar_venta ():
    print("--- Modificar venta ---")
    ventas = leer_ventas()

    nombre_cliente = pedir_string('Para modificar, ingrese el nombre del cliente: ').lower()
    for venta in ventas:
        if venta['cliente_venta'].lower() == nombre_cliente.lower():
            print("--------------------------------")
            print('Venta encontrada. Ingrese los nuevos datos a modificar de la venta')
            venta['items'][0]['cantidad'] = pedir_entero('Ingrese nueva cantidad: ')
            venta['items'][0]['precio_unit'] = pedir_float('Ingresar nuevo precio: ')
            venta['forma_pago'] = pedir_opcion('Ingresar nueva forma de pago: ', formas_pago)
            break
    else:
        print("--------------------------------")
        print("No se encontraron ventas con ese nombre.")
        print("--------------------------------")
    guardar_ventas(ventas)
    print("--------------------------------")
    print("Venta actualizada correctamente.")
    print("--------------------------------")

        


def baja_venta ():
    print("--- Dar de baja una venta ---")
    ventas = leer_ventas()

    if not ventas:
        print("--------------------------------")
        print("No hay ventas en el vivero para dar de baja.")
        print("--------------------------------")
        return
    
    id_venta = int(input('Para dar de baja ingrese el ID de la venta: '))
    
    venta_encontrada = None
    for venta in ventas:#ventas? / estaba total_de_ventas 
        if venta['id'] == id_venta:
            venta_encontrada = venta
            break

    if not venta_encontrada:
        print("--------------------------------")
        print("No se encontró ninguna venta con ese ID.")
        print("--------------------------------")
        return
    

    print(f"Venta a eliminar: {venta_encontrada['id']}")
    confirmar = input ("¿Confirma que desea eliminar esta venta? (s/n): ").lower() .strip()
 

    if confirmar == "s":
        ventas.remove(venta_encontrada)
        guardar_ventas(ventas)
        print("--------------------------------")
        print(f"La venta '{venta_encontrada['id']}' ha sido eliminada.")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("Operación cancelada. La venta no ha sido eliminada.")
        print("--------------------------------")
    

def menu_ventas():
    while True:
        print("=" * 25)
        print("💰 VENTAS  ")
        print("=" * 25)
        print("1. Cargar venta")
        print("2. Consultar ventas")
        print("3. Buscar venta por DNI")
        print("4. Modificar datos de venta")
        print("5. Eliminar venta")
        print("9. Volver al menú principal")

        opcion = input("Qué querés hacer?").strip()

        if opcion == "1":
            alta_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
             buscar_venta()
        elif opcion == "4":
             modificar_venta()
        elif opcion == "5":
             baja_venta()
        elif opcion == "9":
             print("Volviendo al menú principal...")
             break
        else:
             print("--------------------------------")
             print("Opción no válida, intente de nuevo.")
             print("--------------------------------")











    
        
