from datos import total_de_clientes , tipos_clientes
from validaciones import pedir_email, pedir_string, pedir_opcion, siguiente_id


def alta_cliente():
    print("--- Cargar nuevo cliente ---")
    dni = pedir_string('Ingresar DNI: ')
    nombre_completo = pedir_string('Ingresar nombre completo: ')
    telefono = pedir_string('Ingresar telefono: ')
    email = pedir_email('Ingresar email: ')
    tipo_cliente = pedir_opcion('Ingresar tipo de cliente: ', tipos_clientes)
    notas = pedir_string('Ingresar notas adicionales, a que se dedica, que le suele interesar, etc: ')

    id = 1
    if (len(total_de_clientes)>0):
        ultimo_id = total_de_clientes[-1]
        id = ultimo_id["id"]+1

    cliente = {
            "id": id,
            "dni": dni,
            "nombre_completo": nombre_completo,
            "telefono": telefono,
            "email": email,
            "tipo_cliente": tipo_cliente,
            "notas": notas
    }
    total_de_clientes.append(cliente)
    print(f"El cliente '{nombre_completo}' ha sido agregado con ID {cliente['id']}.")


def listar_clientes():
    print("--- Listado de clientes ---")
    if not total_de_clientes:
        print("No hay clientes registrados para mostrar.")
        return
    
    for cliente in total_de_clientes:
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
    print("Buscar por:")
    print("1. DNI")
    print("2. Nombre completo")
    opcion_busqueda = input("Seleccione una opcion de busqueda: ").strip()
    
    resultados = []
    
    if opcion_busqueda == "1":
        dni = pedir_string('Ingresar DNI: ')
        for cliente in total_de_clientes:
            if dni in cliente['dni'].strip():
                resultados.append(cliente)
    elif opcion_busqueda == "2":
        nombre_completo = pedir_string('Ingresar nombre completo: ')
        for cliente in total_de_clientes:
            if nombre_completo in cliente['nombre_completo']:
                resultados.append(cliente)
    else:
        print("Opcion de busqueda no valida.")
        return
    
    if not resultados:
        print("No se encontraron clientes que coincidan con el filtro seleccionado")

    for cliente in resultados:
        print(f"ID: {cliente['id']}")
        print(f"DNI: {cliente['dni']}")
        print(f"Nombre completo: {cliente['nombre_completo']}")
        print(f"Telefono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print(f"Tipo de cliente: {cliente['tipo_cliente']}")
        print(f"Notas: {cliente['notas']}")
        print("-------------------------------")


def modificar_cliente():
    print("--- Modificar cliente ---")
    if not total_de_clientes:
        print("No hay clientes registrados para modificar.")
        return
        
    nombre_completo = pedir_string('Para modificar un cliente, ingrese su nombre completo: ')
    for cliente in total_de_clientes:
        if cliente ['nombre_completo'] == nombre_completo:
            print("Ingrese los nuevos datos del cliente: ")
            cliente['telefono'] = pedir_string('Ingresar nuevo telefono: ')
            cliente['email'] = pedir_email('Ingresar nuevo email: ')
    

def baja_cliente():
    print("--- Eliminar cliente ---")
    if not total_de_clientes:
        print("No hay clientes registrados para eliminar.")
        return
    
    nombre_completo = pedir_string('Para eliminar un cliente, ingrese su nombre completo: ')

    cliente_encontrado = None
    for cliente in total_de_clientes:
        if cliente['nombre_completo'] == nombre_completo:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print(f"No se econtro cliente con el nombre '{nombre_completo}'.")
        return
    

    print(f"Cliente a eliminar: {cliente_encontrado['nombre_completo']}")
    confirmar = input("Confirma que desea eliminar este cliente? (s/n): ").lower().strip()

    if confirmar == 's':
        total_de_clientes.remove(cliente_encontrado)
        print(f"El cliente {cliente_encontrado['nombre_completo']} ha sido eliminado.")
    else:
        print("La operacion ha sido cancelada.")

def menu_clientes():
    while True:
        print("=====  Clientes  ====")
        print("1. Cargar cliente")
        print("2. Listar clientes")
        print("3. Buscar cientes por DNI o nombre")
        print("4. Actualizar datos de contacto")
        print("5. Eliminar cliente")
        print("9. Volver al menu principal")

        opcion = input("Que queres hacer?")

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
             print("Opcion no valida, intente de nuevo")



    

