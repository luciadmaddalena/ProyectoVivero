#PROVEEDORES (dama)

#       id
#       nombre o razon social
#       telefono
#       email
#       localidad
#       que provee (lista de strings - ej: [“semillas de tomate”, “tierra negra”])
#       fecha del ultimo pedido que le hicimos

#/ listar todos los proveedores
#/ buscar un proveedor por nombre o por lo que provee
#/actualizar los datos de contacto o lo que provee
# / dar de baja un proveedor con el que se dejo de trabajar.
from validaciones import pedir_string, pedir_entero, pedir_email , pedir_fecha, pedir_opcion 
from datos import total_de_proveedores, siguiente_id

#registrar proveedor nuevo
def alta_proveedor ():
    print("--- Cargar nuevo Proveedor ---")
    nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
    telefono = pedir_entero('Ingresar teléfono: ')
    email = pedir_email('Ingresar email:')
    localidad = pedir_string('Ingresar localidad: ')
    producto_que_provee = pedir_string('Ingresar producto que provee: ')
    fecha_ultimo_pedido = pedir_fecha('Ingresar la fecha del ultimo pedido: ')
    print("--------------------------------")
    
    proveedor = {
        "id": siguiente_id(total_de_proveedores),
        "nombre_proveedor": nombre_proveedor,
        "teléfono": telefono, 
        "email": email,
        "localidad": localidad, 
        "producto_que_provee": producto_que_provee,
        "fecha_ultimo_pedido": fecha_ultimo_pedido
    }
    total_de_proveedores.append(proveedor)
    print(f"El proveedor '{nombre_proveedor}' ha sido agregado con ID {proveedor['id']}.")

#listar los proveedores 
def listar_proveedores():
    print("--- Listado de proveedores ---")
    if not total_de_proveedores:
        print("No hay proveedores en el registro para mostrar.")
        return # return para salir de la funcion si no encuentra proveedores 
    
    print("Filtrar por:")
    print("1. Ver todos")
    print("2. Nombre del proveedor")
    print("3. Producto que provee")

    opcion_filtro = input("Seleccione una opcion de filtro: ").strip()
       

    resultados = []
    if opcion_filtro == "2":
        nombre_proveedor = pedir_opcion('Ingresar nombre: ', nombre_proveedor)
        resultados = [proveedor for proveedor in total_de_proveedores if proveedor['nombre_proveedor'] == nombre_proveedor]
    elif opcion_filtro == "3":
        producto_que_provee = pedir_opcion('Ingresar producto: ', producto_que_provee)
        resultados = [proveedor for proveedor in total_de_proveedores if proveedor['producto_que_provee'] == producto_que_provee]
    else:
        resultados = total_de_proveedores

        if not resultados:
         print("No se encontraron proveedores que coincidan con el filtro seleccionado.")
        return
    
    for proveedor in resultados:
        print(f"ID: {proveedor['id']}")
        print(f"Nombre del proveedor: {proveedor['nombre_proveedor']}")
        print(f"Telefono: {proveedor['telefono']}")
        print(f"Email: {proveedor['email']}")
        print(f"Localidad: {proveedor['Localidad']}")
        print(f"Producto que provee: {proveedor['producto_que_provee']}")
        print(f"Fecha del ultimo pedido: {proveedor['fecha_ultimo_pedido']}")



