

from datos import total_de_ventas , formas_pago, total_de_plantas
from validaciones import pedir_entero, pedir_float, pedir_string, pedir_opcion, buscar_por_id, siguiente_id, pedir_fecha 

def alta_venta():
    print("--- Registrar nueva venta ---")
    id_cliente = pedir_entero('Ingresar ID del cliente: ')
    fecha = pedir_string('Ingresar fecha: ')
    forma_pago = pedir_opcion('Ingresar forma de pago: ', formas_pago)

    id_planta = pedir_entero('Ingresar ID de planta: ')
    cantidad = pedir_entero('Ingresar cantidad: ')
    precio_unit = pedir_float('Ingresar precio unitario: ')

    items = [
        {
            'id_planta': id_planta,
            'cantidad': cantidad,
            'precio_unit': precio_unit
        }
    ] 
    total = cantidad * precio_unit  

    venta = {
         "id": siguiente_id(total_de_ventas),
         "id_cliente": id_cliente,
         "fecha": fecha,
         "items": items,
         "total": total,
         "forma_pago": forma_pago
    }
        
    total_de_ventas.append(venta)
    descontar_stock(items)
    print(f"La venta N° {venta['id']} ha sido registrada.")

#cuando se registra una venta, el stock de cada planta vendida tiene que
#descontarse automáticamente.

def descontar_stock(items):
    for item in items:
        id_planta = item["id_planta"]
        cantidad = item["cantidad"]

        for planta in total_de_plantas:
            if planta["id"] == id_planta:
                planta["stock"] -= cantidad
                break
                

def consultar_ventas():
    print ("--- Lista de ventas ---")
    if not total_de_ventas:
        print("No hay ventas registradas.")
        return

    for venta in total_de_ventas:
            print(f"ID: {venta['id']}")
            print(f"ID Cliente: {venta['id_cliente']}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Items: {venta['items']}")
            print(f"Total: {venta['total']}")
            print(f"Forma de pago: {venta['forma_pago']}")
            print("-----------------------------")

from clientes import clientes
def buscar_venta_por_dni():
    print ('--- Buscar ventas por DNI ---')

    dni = input('Ingrese DNI del cliente: ')

    # buscar id_cliente

    id_cliente = None

    for cliente in cliente:
        if cliente['dni'] == dni:
            id_cliente = cliente['id']
            break

    if not id_cliente:
        print("No se encontro ningun cliente con ese DNI.")
        return

    # buscar ventas

    resultados = []
    for venta in total_de_ventas:
        if venta['id_cliente'] == id_cliente:
            resultados.append(venta)

    if not resultados:
       print ('No hay ventas para ese cliente.')
       return
    # mostrar los resultados
    
    for venta in resultados:
            print(f"ID venta: {venta['id']}")
            print(f"Fecha: {venta['fecha']}")
            print(f"Total: {venta['total']}")
            print(f"Forma de pago: {venta['forma_pago']}")
            print("-----------------------------")

def modificar_venta ():
    print("--- Modificar venta ---")
    id_venta = int(input('Para modificar ingrese el ID de venta: '))
    for venta in total_de_ventas:
        if venta['id'] == id_venta:
            print('Venta encontrada:')
            print(venta)
            print('¿QUé desea modificar?')
            print("1 - Forma de pago")
            print("2 - Total")
            print("3 - Cliente")

            opcion = input('Seleccione una opcion de venta: ').strip()
            if opcion == "1":
                
               venta['forma_pago'] = input('Ingresar nueva forma de pago: ')

            elif opcion == '2':
            
                 total = 0

                 for item in venta["items"]:
                    total += item["cantidad"] * item["precio_unit"]

                 venta["total"] = total
                 print("Total recalculado.")
            
            elif opcion == "3":
                 venta["id_cliente"] = int(input("Nuevo ID de cliente: "))

            else:
                 print("Opción inválida.")
                 return

            print("Venta modificada correctamente.")
            return
print("No se encontró una venta con ese ID.")
        


def baja_venta ():
    print("--- Dar de baja una venta ---")
    if not total_de_ventas:
        print("No hay ventas en el vivero para dar de baja.")
        return
    
    id_venta = int(input('Para dar de baja ingrese el ID de la venta: '))
    
    venta_encontrada = None
    for venta in total_de_ventas:
        if venta['id'] == id_venta:
            venta_encontrada = venta
            break

    if not venta_encontrada:
        print("No se encontro ninguna venta con ese ID.")
        return
    

    print(f"Venta a eliminar: {venta_encontrada['id']}")
    confirmar = input ("¿Confirma que desea eliminar esta venta? (s/n): ").lower() .strip()
 

    if confirmar == "s":
        total_de_ventas.remove(venta_encontrada)
        print(f"La venta '{venta_encontrada['id']}' ha sido eliminada.")
    else:
        print("Operacion cancelada. La venta no ha sido eliminada.")

def menu_ventas():
    while True:
        print("===== Menú de ventas ====")
        print("1. Cargar venta")
        print("2. Consultar ventas")
        print("3. Buscar venta por DNI")
        print("4. Modificar datos de venta")
        print("5. Eliminar venta")
        print("9. Volver al menu principal")

        opcion = input("Que queres hacer?").strip()

        if opcion == "1":
            alta_venta()
        elif opcion == "2":
            consultar_ventas()
        elif opcion == "3":
             buscar_venta_por_dni()
        elif opcion == "4":
             modificar_venta()
        elif opcion == "5":
             baja_venta()
        elif opcion == "9":
             print("Volviendo al menú principal...")
             break
        else:
             print("Opcion no valida, intente de nuevo")











    
        
