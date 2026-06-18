from datetime import datetime 

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("por favor, ingrese un numero entero valido.")
            continue
        numero = int(entrada)
        return numero

def pedir_float(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if not entrada.isdigit():
            print("Por favor, ingrese un numero valido.")
            continue
        numero = float(entrada)
        return numero

def pedir_string(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("Por favor, ingrese un valor valido.")
            continue
        return entrada
    
def pedir_email(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if "@" not in entrada or "." not in entrada:
            print("Por favor, ingrese un email valido.")
            continue
        return entrada
    
def pedir_opcion(mensaje, opciones_validas):
    print (f"Opciones validas: {', ' .join(opciones_validas)}")
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada not in opciones_validas:
            print(f"Por favor, ingrese una opcion valida: {', '.join(opciones_validas)}")
            continue
        return entrada

def buscar_por_id (lista, id):
    for item in lista:
        if item['id'] == id:
            return item
    return None

def siguiente_id (lista):
    if not lista:
        return 1
    return max(item['id'] for item in lista) + 1

#agregue la validacion para fecha con su formato de dd/mm/aaaa

def pedir_fecha(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            fecha = datetime.strptime(entrada, "%d/%m/%Y") #metodo para que se pueda convertir a fecha
            return fecha
        except ValueError:
            print("Por favor, ingrese una fecha valida en formato DD/MM/AAAA.")