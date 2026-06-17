#PROVEEDORES (dama)
#/registrar un proveedor nuevo
#
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
from validaciones import pedir_string, pedir_entero, pedir_email , pedir_fecha 
from datos import total_de_proveedores, siguiente_id

def alta_proveedor ():
    print("--- Cargar nuevo Proveedor ---")
    nombre_proveedor = pedir_string('Ingresar nombre del proveedor: ')
    telefono = pedir_entero('Ingresar teléfono: ')
    email = pedir_email('Ingresar email:')
    localidad = pedir_string('Ingresar localidad: ')
    producto_que_provee = pedir_string('Ingresar producto que provee: ')
    fecha_ultimo_pedido = pedir_fecha('Ingresar la fecha del ultimo pedido: ')
    
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
    print(f"El proveedor '{nombre_proveedor}' ha sido agregado con ID {proveedor['id']}")