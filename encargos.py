import os, json
from datetime import date
from validaciones import siguiente_id, pedir_string, pedir_float, pedir_opcion, pedir_fecha, pedir_entero
from datos import estado_encargo


NOMBRE_ARCHIVO_ENCARGOS = os.path.join('data', 'encargos.json')
NOMBRE_ARCHIVO_CLIENTES = os.path.join('data', 'clientes.json')
NOMBRE_ARCHIVO_PLANTAS = os.path.join('data', 'plantas.json')
NOMBRE_ARCHIVO_PROVEEDORES = os.path.join('data', 'proveedores.json')


#archivos
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




#funciones encargos
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
    
    print("Cliente encontrado:", cliente["nombre_completo"], "ID: ", cliente["id"])

    #revisar a que proveedor corresponde el pedido
    proveedor_encargo = pedir_string("A que proveedor le pedimos? Escriba nombre o razon social: ")
    
    resultados_proveedores = []
    for proveedor in proveedores:
        if proveedor_encargo == proveedor["nombre_proveedor"].lower():
            resultados_proveedores.append(proveedor)
    
    if not resultados_proveedores:
        print("No existe ningun proveedor con ese nombre.")
        return
    
    print("Proveedor encontrado:", proveedor["nombre_proveedor"], "ID: ", proveedor["id"])

    #que planta corresponde el encargo
    planta_encargo = pedir_string("Que planta esta pidiendo? Escriba nombre comun: ")

    resultados_plantas = []
    for planta in plantas:
        if planta_encargo == planta["nombre_comun"].lower():
            resultados_plantas.append(planta)
    
    if not resultados_plantas:
        print("No existe ninguna planta con ese nombre.")
        return
    
    print("Planta encontrada:", planta["nombre_comun"], "ID: ", planta["id"])




    descripcion = pedir_string("Descripcion libre: ")
    fecha_pedido = pedir_fecha("fecha de pedido: ")
    fecha_llegada = pedir_fecha("Fecha estimada de llegada: ")
    estado = pedir_opcion("Estado de pedido: ", estado_encargo)
    senia = pedir_float("Se;a recibida: ")

    encargo = {
        "id": siguiente_id(encargos),
        "cliente_encargo": cliente_encargo,
        "proveedor_encargo": proveedor_encargo,
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
    #clientes = leer_clientes()
    #proveedores = leer_proveedores()

    activos = []
    for encargo in encargos:
        if encargo["estado"] not in ("entregado", "cancelado"):
            activos.append(encargo)
    
    if not activos:
        print("No hay encargos activos.")
        return
    
    print(f"Encargos activos: {[activos]}")

def buscar_encargo():
    print("--- Buscar encargo---")
    encargos = leer_encargos()
    #clientes = leer_clientes()
    #proveedores = leer_proveedores()

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
        for encargo in encargos:
            if nombre_cliente == encargo["cliente_encargo"]:
                resultados.append(encargo)
    elif opcion == "2":
        nombre_proveedor = pedir_string("Nombre o razon social de proveedor: ")
        for encargo in encargos:
            if nombre_proveedor == encargo["proveedor_encargo"]:
                resultados.append(encargo)
    elif opcion == "3":
        fecha = pedir_fecha("Fecha del pedido: ")
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
        print(f"cliente encargo: {encargo['cliente_encargo']}")
        print(f"proveedor encargo: {encargo['proveedor_encargo']}")
        print(f"planta encargo: {encargo['planta_encargo']}")
        print(f"descripcion: {encargo['descripcion']}")
        print(f"fecha pedido: {encargo['fecha_pedido']}")
        print(f"fecha llegada: {encargo['fecha_llegada']}")
        print(f"estado: {encargo['estado']}")
        print(f"senia: {encargo['senia']}")
        

def actualizar_estado_encargo():
    print("--- Actualizar estado de encargo ---")
    encargos = leer_encargos()
    clientes = leer_clientes()

    if not encargos:
        print("No hay encargos registrados")
        return
    
    
    id_encargo = pedir_entero("ID del encargo a actualizar: ")
    resultado = []
    for encargo in encargos:
        if id_encargo == encargo["id"]:
            resultado.append(encargo)
    
    print("Estado actual: ", encargo["estado"])
    nuevo_estado = pedir_opcion("Nuevo estado: ", estado_encargo)
    encargo["estado"] = nuevo_estado
    guardar_encargos(encargos)
    print("Estado actualizado a: ", nuevo_estado)


    


def baja_encargo():
    encargos = leer_encargos()
    nombre_cliente = input("Para dar de baja ingrese el nombre del cliente: ")
    for encargo in encargos:
        if nombre_cliente == encargo["cliente_encargo"]:
            encargos.remove(encargo)
            break
    guardar_encargos(encargos)
    #falta confirmacion


def menu_encargos():
    while True: 
        print("==== ENCARGOS ESPECIALES ====")
        print("1. Cargar una encargo nuevo")
        print("2. Listar encargos activos")
        print("3. Buscar encargo")
        print("4. Actualizar estado de encargo")
        print("5. Dar de baja un encargo")
        print("9. Volver al menu principal")
        
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
