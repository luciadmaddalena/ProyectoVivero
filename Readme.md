# 🌿 VIVERO "EL JACARANDÁ" — Sistema de Gestión

Trabajo Práctico Integrador — **Programación I**
Tecnicatura en Desarrollo Web — Facultad de Ciencias de la Administración (FCAD), Universidad Nacional de Entre Ríos (UNER)

## Integrantes

- Lucía Della Maddalena
- Damaris Abinzano
- Gabriela López

---

##  Descripción del proyecto

El sistema gestiona la operación diaria de un vivero: stock de plantas, clientes, ventas, proveedores y encargos especiales.
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
- Actualizar stock o precio.
- Dar de baja una planta

**Datos que se guardan por planta:** id, nombre común, nombre científico, categoría, sector, cantidad en stock, precio unitario, cuidados básicos.

---

##  Módulo: Clientes

- Registrar un cliente nuevo
- Listar todos los clientes
- Buscar por DNI o por nombre
- Actualizar datos de contacto
- Eliminar un cliente

**Datos que se guardan por cliente:** id, DNI, nombre completo, teléfono, email, tipo de cliente (particular, paisajista, empresa, vivero amigo), notas.

---

##  Módulo: Ventas

- Registrar una venta nueva
- Listar todas las ventas
- Buscar una venta
- Modificar una venta
- Eliminar una venta 

 **Importante:** al registrar una venta, el stock de cada planta vendida se descuenta automáticamente.

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
---

##  Cómo ejecutar el programa

```bash
python main.py
```

El programa se mantiene abierto hasta que el usuario elige la opción **"0. Salir"** desde el menú principal.
