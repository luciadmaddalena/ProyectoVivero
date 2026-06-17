
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
            print("Mostrando stock de plantas...")
        elif opcion == "2":
             print("Mostrando clientes...")
        elif opcion == "3":
                print("Mostrando ventas...")
        elif opcion == "4":
                print("Mostrando proveedores...")
        elif opcion == "5":
                print("Mostrando encargos especiales...")
        elif opcion == "0":
            print("Hasta luego, esperamos que vuelvas pronto")
            break
        else:
            print("Opcion no valida, intente de nuevo")

main()





