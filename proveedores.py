#PROVEEDORES (dama)
#PROVEEDORES (dama)


from validaciones import pedir_string, pedir_entero, pedir_email , pedir_fecha, siguiente_id
from datos import total_de_proveedores

#registrar proveedor nuevo
def alta_proveedor ():
    print("--- Cargar nuevo Proveedor ---")
    nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
    telefono = pedir_entero('Ingresar teléfono: ')
    email = pedir_email('Ingresar email:')
    localidad = pedir_string('Ingresar localidad: ')
    producto_que_provee = pedir_string('Ingresar producto que provee: ')
    fecha_ultimo_pedido = pedir_fecha('Ingresar la fecha del último pedido: ')
    print("--------------------------------")
    
    proveedor = {
        "id": siguiente_id(total_de_proveedores),
        "nombre_proveedor": nombre_proveedor,
        "telefono": telefono, 
        "email": email,
        "localidad": localidad, 
        "producto_que_provee": producto_que_provee,
        "fecha_ultimo_pedido": fecha_ultimo_pedido
    }
    total_de_proveedores.append(proveedor)

    print("--------------------------------")
    print(f"El proveedor '{nombre_proveedor}' ha sido agregado con ID {proveedor['id']}.")
    print("--------------------------------")

#listar los proveedores 
def listar_proveedores():
    print("--- Listado de proveedores ---")
    if not total_de_proveedores:
        print("--------------------------------")
        print("No hay proveedores en el registro para mostrar.")
        print("--------------------------------")
        return # return para salir de la funcion si no encuentra proveedores 
    
    print("--------------------------------")
    print("Filtrar por:")
    print("1. Ver todos")
    print("2. Nombre del proveedor")
    print("3. Producto que provee")
    print("--------------------------------")

    opcion_filtro = input("Seleccione una opcion de filtro: ").strip()
       

    resultados = []
    if opcion_filtro == "2":
        nombre_proveedor = pedir_string('Ingresar nombre: ', nombre_proveedor)
        resultados = [proveedor for proveedor in total_de_proveedores if proveedor['nombre_proveedor'] == nombre_proveedor]
    elif opcion_filtro == "3":
        producto_que_provee = pedir_string('Ingresar producto: ', producto_que_provee)
        resultados = [proveedor for proveedor in total_de_proveedores if proveedor['producto_que_provee'] == producto_que_provee]
    else:
        resultados = total_de_proveedores

    if not resultados:
         print("--------------------------------")
         print("No se encontraron proveedores que coincidan con el filtro seleccionado.")
         print("--------------------------------")
         return
    
    for proveedor in resultados:
        print("--------------------------------")
        print(f"ID: {proveedor['id']}")
        print(f"Nombre del proveedor: {proveedor['nombre_proveedor']}")
        print(f"Teléfono: {proveedor['telefono']}")
        print(f"Email: {proveedor['email']}")
        print(f"Localidad: {proveedor['localidad']}")
        print(f"Producto que provee: {proveedor['producto_que_provee']}")
        print(f"Fecha del último pedido: {proveedor['fecha_ultimo_pedido']}")
        print("--------------------------------")

def buscar_proveedor():
    print("--- Buscar proveedor ---")
    print("Buscar por:")
    print("1. Nombre del proveedor")
    print("2. Producto que provee")
    print("--------------------------------")
    opcion_busqueda = input("Seleccione una opción de busqueda: ").strip()
    
    resultados = []

    
    if opcion_busqueda == "1":
        nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
        for proveedor in total_de_proveedores:
            if nombre_proveedor in proveedor['nombre_proveedor'].strip():
                resultados.append(proveedor)
    elif opcion_busqueda == "2":
        producto_que_provee = pedir_string('Ingresar producto que provee: ')
        for proveedor in total_de_proveedores:
            if producto_que_provee in proveedor['producto_que_provee']:
                resultados.append(proveedor)
    else:
        print("--------------------------------")
        print("Opción de busqueda no valida.")
        print("--------------------------------")
        return
    
    if not resultados:
        print("--------------------------------")
        print("No se encontraron proveedores que coincidan con el filtro seleccionado.")
        print("--------------------------------")

    for proveedor in resultados:
        print("--------------------------------")
        print(f"ID: {proveedor['id']}")
        print(f"Nombre del proveedor: {proveedor['nombre_proveedor']}")
        print(f"Producto que provee: {proveedor['producto_que_provee']}")
        print("--------------------------------")


def modificar_proveedor():
    print("--- Modificar Proveedor ---")
    if not total_de_proveedores:
        print("--------------------------------")
        print("No hay proveedores registrados para modificar.")
        print("--------------------------------")
        return
    
    nombre_proveedor = pedir_string("Para modificar un proveedor, ingrese el nombre: ")
    for proveedor in total_de_proveedores: 
     if proveedor ["nombre_proveedor"] == nombre_proveedor:
        print("--------------------------------")
        print("Ingrese los nuevos datos del proveedor")
#sumar la validacion para modificar de a uno 
        proveedor["telefono"] = pedir_entero("Ingrese el nuevo teléfono: ")
        proveedor["email"] = pedir_email("Ingrese el nuevo email:")
        proveedor["Producto que provee"] = pedir_string("Ingrese o modifique el nuevo producto: ")
#sumar mensaje de confirmacion de que se modifico el proveedor 


def baja_proveedor():
    print("--- Eliminar proveedor ---")
    if not total_de_proveedores:
        print("--------------------------------")
        print("No hay proveedores registrados para eliminar.")
        print("--------------------------------")
        return
    
    nombre_proveedor =pedir_string("Para eliminar un proveedor, ingrese el nombre: ")

    proveedor_encontrado = None
    for proveedor in total_de_proveedores:
     if proveedor["nombre_proveedor"] == nombre_proveedor:
        proveedor_encontrado = proveedor
        break
     
     if not proveedor_encontrado:
        print("--------------------------------")
        print (f"No se encontró un proveedor con el nombre '{nombre_proveedor}'.")
        print("--------------------------------")

    print(f"Proveedor a eliminar: {proveedor_encontrado["nombre_proveedor"]}")
    confirmar = input("Confirma que desea eliminar este proveedor? (s/n): ").lower().strip()


    if confirmar == 's':
        total_de_proveedores.remove(proveedor_encontrado)
        print("--------------------------------")
        print(f"El proveedor {proveedor_encontrado['nombre_proveedor']} ha sido eliminado.")
        print("--------------------------------")

    else:
        print("La operación ha sido cancelada.")

def menu_proveedores():
    while True:
        print("=====  Proveedores  ====")
        print("1. Cargar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedores por nombre o producto que provée")
        print("4. Actualizar datos de contacto")
        print("5. Eliminar proveedor")
        print("9. Volver al menú principal")
        print("--------------------------------")

        opcion = input("Que querés hacer?")

        if opcion == "1":
            alta_proveedor()
        elif opcion == "2":
            listar_proveedores()
        elif opcion == "3":
             buscar_proveedor()
        elif opcion == "4":
             modificar_proveedor()
        elif opcion == "5":
             baja_proveedor()
        elif opcion == "9":
             break
        else:
             print("Opción no valida, intente de nuevo.")


   