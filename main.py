from plantas import menu_plantas
from clientes import menu_clientes
from ventas import menu_ventas
from proveedores import menu_proveedores
from encargos import menu_encargos


def mostrar_menu():
    print("==== VIVERO EL JACARANDA ====")
    print("1. Stock de plantas")
    print("2. Clientes")
    print("3. Ventas")
    print("4. Proveedores")
    print("5. Encargos especiales")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Que queres hacer?")

        if opcion == "1":
            menu_plantas()
        elif opcion == "2":
             menu_clientes()
        elif opcion == "3":
             menu_ventas()
        elif opcion == "4":
             menu_proveedores()
        elif opcion == "5":
            menu_encargos()
        elif opcion == "0":
            print("Hasta luego, esperamos que vuelvas pronto")
            break
        else:
            print("Opcion no valida, intente de nuevo")

if __name__ == "__main__":
     main()






