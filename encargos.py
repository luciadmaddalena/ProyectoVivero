import os, json
from datetime import date
from validaciones import siguiente_id, pedir_string, pedir_float, pedir_opcion, pedir_fecha, pedir_entero, buscar_por_id
from datos import estado_encargo


NOMBRE_ARCHIVO_ENCARGOS = os.path.join('data', 'encargos.json')
NOMBRE_ARCHIVO_CLIENTES = os.path.join('data', 'clientes.json')
NOMBRE_ARCHIVO_PLANTAS = os.path.join('data', 'plantas.json')
NOMBRE_ARCHIVO_PROVEEDORES = os.path.join('data', 'proveedores.json')


#ARCHIVOS
def leer_encargos():
    ##para ver si un archivo existe
    if os.path.exists(NOMBRE_ARCHIVO_ENCARGOS):
        with open(NOMBRE_ARCHIVO_ENCARGOS, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return[]
    
def guardar_encargos(datos):
    with open(NOMBRE_ARCHIVO_ENCARGOS, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

def leer_clientes():
    if os.path.exists(NOMBRE_ARCHIVO_CLIENTES):
        with open(NOMBRE_ARCHIVO_CLIENTES, 'rt', encoding='UTF-8') as archivo:
            return json.load(archivo)
    return []

def leer_plantas():
    if os.path.exists(NOMBRE_ARCHIVO_PLANTAS):
        with open(NOMBRE_ARCHIVO_PLANTAS, 'rt', encoding='UTF-8') as archivo:
            return json.load(archivo)
    return []

def leer_proveedores():
    if os.path.exists(NOMBRE_ARCHIVO_PROVEEDORES):
        with open(NOMBRE_ARCHIVO_PROVEEDORES, 'rt', encoding='utf-8') as archivo:
            return json.load(archivo)
    return []




#FUNCIONES
def alta_encargo():
    print("--- Cargar Encargo especial nuevo---")
    encargos = leer_encargos()
    clientes = leer_clientes()
    plantas = leer_plantas()
    proveedores = leer_proveedores()

    #validamos si hay clientes, plantas y proveedores para seguir con la carga
    if not clientes:
        print("No hay clientes registrados. Registra un cliente primero")
        return
    if not plantas:
        print("No hay plantas registrados. Registra una planta primero")
        return
    if not proveedores:
        print("No hay proveedores registrados. Registra un proveedor primero")
        return


    #revisar a que cliente corresponde el encargo
    cliente_encargo = pedir_string("A que cliente corresponde? Escriba nombre completo: ")

    resultados_clientes = []
    for cliente in clientes:
        if cliente_encargo == cliente["nombre_completo"].lower():
            resultados_clientes.append(cliente)
    
    if not resultados_clientes:
        print("No existe ningun cliente con ese nombre.")
        return
    
    print("Cliente encontrado:", resultados_clientes[0]["nombre_completo"], "ID: ", resultados_clientes[0]["id"])

    #revisar a que proveedor corresponde el pedido
    proveedor_encargo = pedir_string("A que proveedor le pedimos? Escriba nombre o razon social: ")
    
    resultados_proveedores = []
    for proveedor in proveedores:
        if proveedor_encargo == proveedor["nombre_proveedor"].lower():
            resultados_proveedores.append(proveedor)
    
    if not resultados_proveedores:
        print("No existe ningun proveedor con ese nombre.")
        return
    
    print("Proveedor encontrado:", resultados_proveedores[0]["nombre_proveedor"], "ID: ", resultados_proveedores[0]["id"])

    #que planta corresponde el encargo
    planta_encargo = pedir_string("Que planta esta pidiendo? Escriba nombre comun: ")

    resultados_plantas = []
    for planta in plantas:
        if planta_encargo == planta["nombre_comun"].lower():
            resultados_plantas.append(planta)
    
    if not resultados_plantas:
        print("No existe ninguna planta con ese nombre.")
        return
    
    print("Planta encontrada:", resultados_plantas[0]["nombre_comun"], "ID: ", resultados_plantas[0]["id"])




    descripcion = pedir_string("Descripción libre: ")
    fecha_pedido = pedir_fecha("Fecha de pedido: ")
    fecha_llegada = pedir_fecha("Fecha estimada de llegada: ")
    estado = pedir_opcion("Estado de pedido: ", estado_encargo)
    senia = pedir_float("Seña recibida: ")

    encargo = {
        "id": siguiente_id(encargos),
        "id_cliente": resultados_clientes[0]["id"],
        "cliente_encargo": cliente_encargo,
        "proveedor_encargo": proveedor_encargo,
        "id_proveedor": resultados_proveedores[0]["id"],
        "planta_encargo": planta_encargo,
        "descripcion": descripcion,
        "fecha_pedido": str(fecha_pedido),
        "fecha_llegada": str(fecha_llegada),
        "estado": estado,
        "senia": senia,
    }

    encargos.append(encargo)
    guardar_encargos(encargos)
    print(f"El encargo ha sido agregada al stock con ID {encargo['id']}.")


def listar_encargos_activos():
    encargos = leer_encargos()
    clientes = leer_clientes()
    proveedores = leer_proveedores()

    activos = []
    for encargo in encargos:
        if encargo["estado"] not in ("entregado", "cancelado"):
            activos.append(encargo)
    
    if not activos:
        print("No hay encargos activos.")
        return
    
    for encargo in activos:
        cliente = buscar_por_id(clientes, encargo["id_cliente"])
        proveedor = buscar_por_id(proveedores, encargo["id_proveedor"])
        print("--------------------------------")
        print(f"ID: {encargo['id']}")
        print(f"Cliente: {cliente['nombre_completo']}")
        print(f"Proveedor: {proveedor['nombre_proveedor']}")
        print(f"Descripción: {encargo['descripcion']}")
        print(f"Estado: {encargo['estado']}")
        print(f"Llega: {encargo['fecha_llegada']}")
        print("--------------------------------")


def buscar_encargo():
    print("--- Buscar encargo---")
    encargos = leer_encargos()


    if not encargos:
        print("No hay encargos registrados")
        return
    
    print("Buscar por:")
    print("1. Cliente")
    print("2. Proveedor")
    print("3. Fecha de pedido")
    opcion = input("Opcion: ").strip()

    resultados = []

    if opcion == "1":
        nombre_cliente = pedir_string("Nombre del cliente: ")
        clientes = leer_clientes()

        for encargo in encargos:
            cliente_encontrado = None
            for cliente in clientes:
                if cliente["id"] == encargo["id_cliente"]:
                    cliente_encontrado = cliente
                    break
            if cliente_encontrado and nombre_cliente in cliente["nombre_completo"].lower():
                resultados.append(encargo)
    
    elif opcion == "2":
        nombre_proveedor = pedir_string("Nombre o razon social de proveedor: ")
        proveedores = leer_proveedores()

        for encargo in encargos:
            proveedor_encontrado = None
            for proveedor in proveedores:
                if proveedor["id"] == encargo["id_proveedor"]:
                    proveedor_encontrado = proveedor
                    break
            if proveedor_encontrado and nombre_proveedor in proveedor["nombre_proveedor"]:
                resultados.append(encargo)
    
    elif opcion == "3":
        fecha = str(pedir_fecha("Fecha del pedido: "))
        for encargo in encargos:
            if fecha == encargo["fecha_pedido"]:
                resultados.append(encargo)
    else:
        print("Opcion no valida")
        return
    
    if not resultados:
        print("No se encontraron encargos")
        return
    
    for encargo in resultados:
        print(f"ID: {encargo['id']}") 
        print(f"Cliente encargo: {encargo['cliente_encargo']}")
        print(f"Proveedor encargo: {encargo['proveedor_encargo']}")
        print(f"Planta encargo: {encargo['planta_encargo']}")
        print(f"Descripción: {encargo['descripcion']}")
        print(f"Fecha pedido: {encargo['fecha_pedido']}")
        print(f"Fecha llegada: {encargo['fecha_llegada']}")
        print(f"Estado del pedido: {encargo['estado']}")
        print(f"Seña: {encargo['senia']}")
        print("---------------------------------------")
        

def actualizar_estado_encargo():
    print("--- Actualizar estado de encargo ---")
    encargos = leer_encargos()
    clientes = leer_clientes()

    if not encargos:
        print("No hay encargos registrados")
        return

    id_encargo = pedir_entero("ID del encargo a actualizar: ")
    encargo = buscar_por_id(encargos, id_encargo)

    if not encargo:
        print("No existe ningún encargo con ese ID.")
        return

    print("Estado actual: ", encargo["estado"])
    nuevo_estado = pedir_opcion("Nuevo estado: ", estado_encargo)
    encargo["estado"] = nuevo_estado
    guardar_encargos(encargos)
    print("Estado actualizado a: ", nuevo_estado)

    if nuevo_estado == "llegó":
        cliente = buscar_por_id(clientes, encargo["id_cliente"])
        if cliente:
            print(" ¡El encargo llegó! Datos del cliente para avisar:")
            print("   Nombre:", cliente["nombre_completo"])
            print("   Teléfono:", cliente["telefono"])



    


def baja_encargo():
    print("--- Cancelar encargo ---")
    encargos = leer_encargos()
    if not encargos:
        print("No hay encargos registrados para dar de baja.")
        return

    id_encargo = pedir_entero('Para dar de baja ingrese el ID del encargo: ')
    encargo_encontrado = buscar_por_id(encargos, id_encargo)

    if not encargo_encontrado:
        print("--------------------------------")
        print("No se encontró ningún encargo con ese ID.")
        print("--------------------------------")
        return

    print(f"Encargo a eliminar: {encargo_encontrado['descripcion']}")
    confirmar = pedir_string("¿Confirma que desea eliminar este encargo? (s/n): ")

    if confirmar == "s":
        encargos.remove(encargo_encontrado)
        guardar_encargos(encargos)
        print("--------------------------------")
        print(f"El encargo '{encargo_encontrado['descripcion']}' ha sido eliminado.")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("Operación cancelada. El encargo no ha sido eliminado.")
        print("--------------------------------")


def menu_encargos():
    while True: 
        print("=" * 25)
        print("📋 ENCARGOS ESPECIALES 📋")
        print("=" * 25)
        print("1. Cargar una encargo nuevo")
        print("2. Listar encargos activos")
        print("3. Buscar encargo")
        print("4. Actualizar estado de encargo")
        print("5. Dar de baja un encargo")
        print("9. Volver al menu principal")
        print("=" * 25)
        
        opcion = input("Que queres hacer?")

        if opcion == "1":
            alta_encargo()
        elif opcion == "2":
            listar_encargos_activos()
        elif opcion == "3":
            buscar_encargo()
        elif opcion == "4":
            actualizar_estado_encargo()
        elif opcion == "5":
            baja_encargo()
        elif opcion == "9":
            break
        else:
            print("Opcion no valida, intente de nuevo")
