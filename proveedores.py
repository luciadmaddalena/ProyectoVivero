#revisar modificaciones de proveedores
#revisar que pasa cuando tiene el mismo nombre
#revisar la fecha que se carga 



from validaciones import pedir_string, pedir_entero, pedir_email , pedir_fecha, siguiente_id
import os, json


NOMBRE_ARCHIVO_PROVEEDORES = os.path.join('data', 'proveedores.json')


#ARCHIVOS
def leer_proveedores():
    if os.path.exists(NOMBRE_ARCHIVO_PROVEEDORES):
        with open(NOMBRE_ARCHIVO_PROVEEDORES, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return[]
    
def guardar_proveedores(datos):
    with open(NOMBRE_ARCHIVO_PROVEEDORES, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


#FUNCIONES
def alta_proveedor ():
    print("--- Cargar nuevo Proveedor ---")
    proveedores = leer_proveedores()
    nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
    telefono = pedir_entero('Ingresar teléfono: ')
    email = pedir_email('Ingresar email:')
    localidad = pedir_string('Ingresar localidad: ')
    producto_que_provee = pedir_string('Ingresar producto que provée: ')
    fecha_ultimo_pedido = pedir_fecha('Ingresar la fecha del último pedido: ')
    print("--------------------------------")
    
    proveedor = {
        "id": siguiente_id(proveedores),
        "nombre_proveedor": nombre_proveedor,
        "telefono": telefono, 
        "email": email,
        "localidad": localidad, 
        "producto_que_provee": producto_que_provee,
        "fecha_ultimo_pedido": str(fecha_ultimo_pedido)
    }
    proveedores.append(proveedor)
    guardar_proveedores(proveedores)

    print("--------------------------------")
    print(f"El proveedor '{nombre_proveedor}' ha sido agregado con ID {proveedor['id']}.")
    print("--------------------------------")

#listar los proveedores 
def listar_proveedores():
    print("--- Listado de proveedores ---")
    proveedores = leer_proveedores()

    if not proveedores:
        print("--------------------------------")
        print("No hay proveedores en el registro para mostrar.")
        print("--------------------------------")
        return 
    
    print("--------------------------------")
    print("Filtrar por:")
    print("1. Ver todos")
    print("2. Nombre del proveedor")
    print("3. Producto que provée")
    print("--------------------------------")

    opcion_filtro = input("Seleccione una opcion de filtro: ").strip()
       

    resultados = []
    if opcion_filtro == "2":
        nombre_buscado = pedir_string('Ingresar nombre: ')
        resultados = [proveedor for proveedor in proveedores if proveedor['nombre_proveedor'] == nombre_buscado]
    elif opcion_filtro == "3":
        producto_buscado = pedir_string('Ingresar producto: ')
        resultados = [proveedor for proveedor in proveedores if proveedor['producto_que_provee'] == producto_buscado]
    else:
        resultados = proveedores

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
        print(f"Producto que provée: {proveedor['producto_que_provee']}")
        print(f"Fecha del último pedido: {proveedor['fecha_ultimo_pedido']}")
        print("--------------------------------")

def buscar_proveedor():
    print("--- Buscar proveedor ---")
    proveedores = leer_proveedores()

    print("Buscar por:")
    print("1. Nombre del proveedor")
    print("2. Producto que provee")
    print("--------------------------------")
    opcion_busqueda = input("Seleccione una opción de busqueda: ").strip()
    
    resultados = []

    
    if opcion_busqueda == "1":
        nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
        for proveedor in proveedores:
            if nombre_proveedor in proveedor['nombre_proveedor'].strip():
                resultados.append(proveedor)
    elif opcion_busqueda == "2":
        producto_que_provee = pedir_string('Ingresar producto que provee: ')
        for proveedor in proveedores:
            if producto_que_provee in proveedor['producto_que_provee']:
                resultados.append(proveedor)
    else:
        print("--------------------------------")
        print("Opción de busqueda no valida.")
        print("--------------------------------")
        return
    
    if not resultados:
        print("--------------------------------")
        print("No se encontraron proveedores que coincidan.")
        print("--------------------------------")

    for proveedor in resultados:
        print("--------------------------------")
        print(f"ID: {proveedor['id']}")
        print(f"Nombre del proveedor: {proveedor['nombre_proveedor']}")
        print(f"Teléfono: {proveedor['telefono']}")
        print(f"Email: {proveedor['email']}")
        print(f"Localidad: {proveedor['localidad']}")
        print(f"Producto que provée: {proveedor['producto_que_provee']}")
        print(f"Fecha del último pedido: {proveedor['fecha_ultimo_pedido']}")
        print("--------------------------------")


def modificar_proveedor():
    print("--- Modificar Proveedor ---")
    proveedores = leer_proveedores()

    if not proveedores:
        print("--------------------------------")
        print("No hay proveedores registrados para modificar.")
        print("--------------------------------")
        return
    
    nombre_proveedor = pedir_string("Para modificar un proveedor, ingrese el nombre: ").lower().strip()
    for proveedor in proveedores: 
     if proveedor ["nombre_proveedor"].lower() == nombre_proveedor:
        print("--------------------------------")
        print("Ingrese los nuevos datos del proveedor")

        proveedor["telefono"] = pedir_entero("Ingrese el nuevo teléfono: ")
        proveedor["email"] = pedir_email("Ingrese el nuevo email:")
        proveedor["producto_que_provee"] = pedir_string("Ingrese o modifique el nuevo producto: ")

        print("--------------------------------")
        print(f"Los datos del proveedor se actualizaron")
        print("--------------------------------")
    guardar_proveedores(proveedores)
        

def baja_proveedor():
    print("--- Eliminar proveedor ---")
    proveedores = leer_proveedores()

    if not proveedores:
        print("--------------------------------")
        print("No hay proveedores registrados para eliminar.")
        print("--------------------------------")
        return
    
    nombre_proveedor =pedir_string("Para eliminar un proveedor, ingrese el nombre: ")

    proveedor_encontrado = None
    for proveedor in proveedores:
     if proveedor["nombre_proveedor"].lower() == nombre_proveedor.lower():
        proveedor_encontrado = proveedor
        break
     
     if not proveedor_encontrado:
        print("--------------------------------")
        print (f"No se encontró un proveedor con el nombre '{nombre_proveedor}'.")
        print("--------------------------------")
        return

    print(f"Proveedor a eliminar: {proveedor_encontrado["nombre_proveedor"]}")
    confirmar = input("Confirma que desea eliminar este proveedor? (s/n): ").lower().strip()


    if confirmar == 's':
        proveedores.remove(proveedor_encontrado)
        print("--------------------------------")
        print(f"El proveedor {proveedor_encontrado['nombre_proveedor']} ha sido eliminado.")
        print("--------------------------------")

    else:
        print("--------------------------------")
        print("La operación ha sido cancelada.")
        print("--------------------------------")
    guardar_proveedores(proveedores)

def menu_proveedores():
    while True:
        print("=" * 25)
        print("🌾 PROVEEDORES ")
        print("=" * 25)
        print("1. Cargar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedores por nombre o producto que provée")
        print("4. Actualizar datos de contacto")
        print("5. Eliminar proveedor")
        print("9. Volver al menú principal")
        print("=" * 25)

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
             print("--------------------------------")
             print("Opción no valida, intente de nuevo.")
             print("--------------------------------")


   