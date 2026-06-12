

GITHUB

github desktop

que pide hacer el programa?

PRIMER PASO - menu principal
que tiene que hacer el menu?
mostrar las opciones
esperar que el usuario escriba algo
hacer algo segun lo que escribio
repetir esto hasta que el usuario elija la opcion “salir”

LISTA DE OPCIONES 
1. Stock de plantas
2. Clientes
3. Ventas
4. Proveedores
5. Encargos especiales
0. Salir



funcion mostrar menu solo con prints

funcion main con while true llamando a mostrar menu() adentro


items del menu:
PLANTAS
     / cargar planta nueva   
                  (id -
                   nombre comun (str) - 
                  nombre cientifico (str) - 
                  categoria (arbol, arbusto suculenta, aromatica, frutal, ornamental, otro) - 
                  sector (interior, exterior, invernadero, huerta) - 
                  cantida de stock (int) - 
                  precio unitario (float) - 
                  cuidados basicos (un breve texto) (str)
                / ver listado completo y filtrar por sector (interior, exterior, invernadero, huerta) o por categoria (arbol, arbusto, suculentas, aromaticas, frutales, ornamentales)
     / buscar una planta por nombre comun o por nombre cientifico
     / actualizar stock cuando hay una venta, cuando muere una planta o cuando se reproduce
     / dar de baja una variedad que ya no se va a vender.

CLIENTES
    /   registrar a un cliente cuando viene por primera vez 
           (id)
           (dni)
           (nombre completo)
           (telefono)
           (e-mail)
           (tipo de cliente: particular, paisajista, empresa, vivero amigo)
           (notas: a que se dedica, que le suele interesar)
    / listar todos los clientes
    / buscar clientes por DNI o nombre
   / actualizar sus datos de contacto
    / eliminar a un cliente que pidio no figurar mas
tambien le gustaria poder ver cuando consulta a un cliente, que compro antes y que encargos tiene activos
VENTAS
/ registrar venta nueva
      id
       a que cliente corresponde
      fecha de la venta
      items vendidos (codigo de planta + cantidad + precio al momento de la venta) 
      total de la venta
      forma de pago (efectivo, transferencia, tarjeta)
 / ver todas las ventas hechas
 / buscar una venta por dni del cliente o por fecha
 / modificar una venta si se equivoco al cargarla
 / eliminar una venta anulada

     cuando se registra una venta, el stock de cada planta vendida tiene que descontarse automaticamente.


PROVEEDORES
/ registrar un proveedor nuevo
       id
       nombre o razon social
       telefono
       email
       localidad
       que provee (lista de strings - ej: [“semillas de tomate”, “tierra negra”])
       fecha del ultimo pedido que le hicimos
/ listar todos los proveedores
/ buscar un proveedor por nombre o por lo que provee
/actualizar los datos de contacto o lo que provee
 / dar de baja un proveedor con el que se dejo de trabajar.

ENCARGOS ESPECIALES
            / registrar un encargo especial
                       id
                       a que cliente corresponde
                       a que proveedor le pedimos
                       que planta esta pidiendo ( descripcion libre, ej. limonero de 4 patas , 1.5 mts
                       cantidad
                       fecha de pedido
                       fecha estimada de llegada
                       estado de pedido (pedido, llego, entregado, cancelado)
                       senia recibida (si el cliente dejo algo)
            / listar todos los encargos activos
            / buscar encargos por cliente, por proveedor o por fecha
           / actualizar estado del encargo (pedido, llego, entregado)
           / cancelar un encargo si el cliente se arrepiente
cando llega un encargo quiere ver los datos del cliente.

cada item del menu, deberia llamar una funcion aparte. ej menu plantas, menu clientes, menu ventas…. etc

estas funciones serian los modulos. - estos se definen siempre antes de ser llamados, es decir antes del main

Validaciones que necesito sí o sí Cuando ingreso un número (cantidad, precio, código), que verifique que sea un número. Cuando ingreso un email, que al menos chequee que tenga @ . Cuando busco algo y no existe, que me lo diga sin romperse. Los códigos de planta, cliente, venta, proveedor y encargo tienen que ser únicos y autoincrementales. 
