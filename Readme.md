# 🌿 Vivero "El Jacarandá" — Sistema de Gestión

Trabajo Práctico Integrador — **Programación I**
Tecnicatura en Desarrollo Web — Facultad de Ciencias de la Administración (FCAD), Universidad Nacional de Entre Ríos (UNER)

## Integrantes

- Lucía Della Maddalena
- Damaris Abinzano
- Gabriela López

---

##  Descripción del proyecto

El sistema gestiona la operación diaria de un vivero: stock de plantas, clientes, ventas, proveedores y encargos especiales. Está pensado para uso local, sin conexión a internet, con persistencia de datos en archivos JSON.

El programa se organiza en un **menú principal** con cinco áreas de trabajo. Cada área es un módulo independiente con su propio archivo `.py`, y todas comparten funciones de validación reutilizables.

```
═══════════════════════════════════════
  VIVERO EL JACARANDÁ — Sistema v1.0
═══════════════════════════════════════
  1. Stock de plantas
  2. Clientes
  3. Ventas
  4. Proveedores
  5. Encargos especiales
  0. Salir
═══════════════════════════════════════
```

Cada módulo tiene su propio submenú con las operaciones de alta, listado, búsqueda, modificación y baja correspondientes.

---

##  Módulo: Stock de plantas

- Cargar una planta nueva
- Ver listado completo, con filtro por **sector** (interior, exterior, invernadero, huerta) o por **categoría** (árbol, arbusto, suculenta, aromática, frutal, ornamental)
- Buscar una planta por nombre común o nombre científico
- Actualizar stock o precio (por venta, reproducción, o pérdida de la planta)
- Dar de baja una variedad que ya no se comercializa

**Datos que se guardan por planta:** id, nombre común, nombre científico, categoría, sector, cantidad en stock, precio unitario, cuidados básicos.

---

##  Módulo: Clientes

- Registrar un cliente nuevo
- Listar todos los clientes
- Buscar por DNI o por nombre
- Actualizar datos de contacto
- Eliminar un cliente

Al consultar un cliente, también se muestran sus **compras anteriores** y sus **encargos activos**.

**Datos que se guardan por cliente:** id, DNI, nombre completo, teléfono, email, tipo de cliente (particular, paisajista, empresa, vivero amigo), notas.

---

##  Módulo: Ventas

- Registrar una venta nueva (cliente, plantas vendidas, cantidades, forma de pago)
- Listar todas las ventas
- Buscar una venta por DNI del cliente o por fecha
- Modificar una venta cargada con errores
- Eliminar una venta anulada

 **Importante:** al registrar una venta, el stock de cada planta vendida se descuenta automáticamente. Al eliminar una venta, el stock se restaura.

**Datos que se guardan por venta:** id, id del cliente, fecha, ítems vendidos (planta + cantidad + precio al momento de la venta), total, forma de pago.

---

##  Módulo: Proveedores

- Registrar un proveedor nuevo
- Listar todos los proveedores
- Buscar por nombre o por lo que provee
- Actualizar datos de contacto o productos que ofrece
- Dar de baja un proveedor

**Datos que se guardan por proveedor:** id, nombre o razón social, teléfono, email, localidad, productos que provee, fecha del último pedido.

---

##  Módulo: Encargos especiales

- Registrar un encargo especial (cliente, proveedor, planta pedida, cantidad, fechas)
- Listar todos los encargos activos
- Buscar encargos por cliente, proveedor o fecha
- Actualizar el estado del encargo (pedido → llegó → entregado)
- Cancelar un encargo

 Cuando el estado de un encargo cambia a **"llegó"**, el sistema muestra automáticamente los datos de contacto del cliente para avisarle.

**Datos que se guardan por encargo:** id, id del cliente, id del proveedor, descripción libre, cantidad, fecha de pedido, fecha estimada de llegada, estado, seña recibida.

---

##  Aspectos técnicos

- **Persistencia:** cada módulo guarda su información en un archivo `.json` dentro de la carpeta `data/`, usando las librerías `os` y `json`.
- **Estructura de datos:** cada área se maneja como una lista de diccionarios. Cada registro individual es un diccionario.
- **IDs únicos y autoincrementales:** se calculan a partir del ID más alto existente en cada lista, evitando duplicados aunque se eliminen registros.
- **Validaciones:** se verifica que los campos numéricos sean números válidos, que los emails contengan `@`, y que las búsquedas sin resultados se informen sin interrumpir el programa.
- **Organización del código:** el proyecto está dividido en módulos (`plantas.py`, `clientes.py`, `ventas.py`, `proveedores.py`, `encargos.py`, `validaciones.py`), conectados entre sí mediante `import`, con `main.py` como punto de entrada único.

---

##  Cómo ejecutar el programa

```bash
python main.py
```

El programa se mantiene abierto hasta que el usuario elige la opción **"0. Salir"** desde el menú principal.