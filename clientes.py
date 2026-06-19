from datos import tipos_clientes
from validaciones import pedir_email, pedir_string, pedir_opcion, siguiente_id
import os, json

NOMBRE_ARCHIVO_CLIENTES = os.path.join('data', 'clientes.json')

#ARCHIVOS
def leer_clientes():
    if os.path.exists(NOMBRE_ARCHIVO_CLIENTES):
        with open(NOMBRE_ARCHIVO_CLIENTES, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return[]
    
def guardar_clientes(datos):
    with open(NOMBRE_ARCHIVO_CLIENTES, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

def alta_cliente():
    print("--- Cargar nuevo cliente ---")
    clientes = leer_clientes()
    dni = pedir_string('Ingresar DNI: ')
    nombre_completo = pedir_string('Ingresar nombre completo: ')
    telefono = pedir_string('Ingresar telefono: ')
    email = pedir_email('Ingresar email: ')
    tipo_cliente = pedir_opcion('Ingresar tipo de cliente: ', tipos_clientes)
    notas = pedir_string('Ingresar notas adicionales, a qué se dedica, qué le suele interesar, etc: ')

    cliente = {
            "id": siguiente_id(clientes),
            "dni": dni,
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "email": email,
            "tipo_cliente": tipo_cliente,
            "notas": notas
    }
    clientes.append(cliente)
    guardar_clientes(clientes)
    print("--------------------------------")
    print(f"El cliente '{nombre_completo}' ha sido agregado con ID {cliente['id']}.")
    print("--------------------------------")


def listar_clientes():
    print("--- Listado de clientes ---")
    clientes = leer_clientes()
    if not clientes:
        print("--------------------------------")
        print("No hay clientes registrados para mostrar.")
        print("--------------------------------")
        return
    
    for cliente in clientes:
        print("-------------------------------")
        print(f"ID: {cliente['id']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Nombre completo: {cliente['nombre_completo']}")
        print(f"Telefono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print(f"Tipo de cliente: {cliente['tipo_cliente']}")
        print(f"Notas: {cliente['notas']}")
        print("-------------------------------")

def buscar_cliente():
    print("--- Buscar cliente ---")
    clientes = leer_clientes()
    print("Buscar por: ")
    print("1. DNI")
    print("2. Nombre completo")
    print("-------------------------------")
    opcion_busqueda = pedir_string("Seleccione una opción de busqueda: ")
    
    resultados = []
    
    if opcion_busqueda == "1":
        dni = pedir_string('Ingresar DNI: ')
        for cliente in clientes:
            if dni in cliente['dni'].strip():
                resultados.append(cliente)
    elif opcion_busqueda == "2":
        nombre_completo = pedir_string('Ingresar nombre completo: ')
        for cliente in clientes:
            if nombre_completo in cliente['nombre_completo']:
                resultados.append(cliente)
    else:
        print("-------------------------------")
        print("Opción de busqueda no valida.")
        print("-------------------------------")
        return
    
    if not resultados:
        print("-------------------------------")
        print("No se encontraron clientes que coincidan con el filtro seleccionado")
        print("-------------------------------")

    for cliente in resultados:
        print("-------------------------------")
        print(f"ID: {cliente['id']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Nombre completo: {cliente['nombre_completo']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print(f"Tipo de cliente: {cliente['tipo_cliente']}")
        print(f"Notas: {cliente['notas']}")
        print("-------------------------------")


def modificar_cliente():
    print("--- Modificar cliente ---")
    clientes = leer_clientes()
    if not clientes:
        print("-------------------------------")
        print("No hay clientes registrados para modificar.")
        print("-------------------------------")
        return
        
    nombre_completo = pedir_string('Para modificar un cliente, ingrese su nombre completo: ')
    for cliente in clientes:
        if cliente ['nombre_completo'] == nombre_completo:
            print("Ingrese los nuevos datos del cliente: ")
            cliente['telefono'] = pedir_string('Ingresar nuevo teléfono: ')
            cliente['email'] = pedir_email('Ingresar nuevo email: ')
    guardar_clientes(clientes)
    

def baja_cliente():
    print("--- Eliminar cliente ---")
    clientes = leer_clientes()
    if not clientes:
        print("-------------------------------")
        print("No hay clientes registrados para eliminar.")
        print("-------------------------------")
        return
    
    nombre_completo = pedir_string('Para eliminar un cliente, ingrese su nombre completo: ')

    cliente_encontrado = None
    for cliente in clientes:
        if cliente['nombre_completo'] == nombre_completo:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("-------------------------------")
        print(f"No se encontró cliente con el nombre '{nombre_completo}'.")
        print("-------------------------------")
        return
    

    print(f"Cliente a eliminar: {cliente_encontrado['nombre_completo']}")
    confirmar = pedir_string("Confirma que desea eliminar este cliente? (s/n): ")

    if confirmar == 's':
        clientes.remove(cliente_encontrado)
        print("--------------------------------")
        print(f"El cliente {cliente_encontrado['nombre_completo']} ha sido eliminado.")
        print("-------------------------------")
    else:
        print("-------------------------------")
        print("La operación ha sido cancelada.")
        print("-------------------------------")
    guardar_clientes(clientes)

def menu_clientes():
    while True:
        print("=====  Clientes  ====")
        print("1. Cargar cliente")
        print("2. Listar clientes")
        print("3. Buscar cientes por DNI o nombre")
        print("4. Actualizar datos de contacto")
        print("5. Eliminar cliente")
        print("9. Volver al menú principal")

        opcion = input("Qué querés hacer?")

        if opcion == "1":
            alta_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
             buscar_cliente()
        elif opcion == "4":
             modificar_cliente()
        elif opcion == "5":
             baja_cliente()
        elif opcion == "9":
             break
        else:
             print("-------------------------------")
             print("Opción no válida, intente de nuevo.")
             print("-------------------------------")



    

