stock_de_plantas = []

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


def menu_plantas():
    while True: 
        print("==== STOCK DE PLANTAS ====")
        print("1. Cargar una planta nueva")
        print("2. Ver listado de plantas")
        print("3. Buscar una planta")
        print("4. Actualizar stock o precio")
        print("5. Dar de baja una planta")
        print("9. Volver al menu principal")
        
        opcion = input("Que queres hacer?")

        if opcion == "1":
            alta_planta()
        elif opcion == "2":
            ver_listado_plantas()
        elif opcion == "3":
            buscar_planta()
        elif opcion == "4":
            actualizar_stock_o_precio()
        elif opcion == "5":
            baja_planta()
        elif opcion == "9":
            break
        else:
            print("Opcion no valida, intente de nuevo")

    
def menu_clientes ():
     while True:
          print("==== CLIENTES ====")
          print("1. Cargar un cliente nuevo")
          print("2. Listar todos lo clientes")
          print("3. Buscar un cliente")
          print("4. Actualizar datos de contacto")
          print("5. Dar de baja un cliente")
          print("9. Volver al menu principal")

          opcion = input("Que queres hacer?")

          if opcion == "1":
            alta_cliente()
          elif opcion == "2":
               ver_listado_clientes()

main()





