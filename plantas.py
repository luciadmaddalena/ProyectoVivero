def alta_planta ():
    print("--- Cargar nueva planta ---")
    nombre_comun = input('Ingresar nombre comun: ')
    nombre_cientifico = input('Ingresar nombre cientifico: ')
    categoria = input('Ingresar categoria: ')
    sector = input('Ingresar sector: ')
    stock = int(input('Ingresar stock: '))
    precio = float(input('Ingresar precio: '))
    cuidados = input('Ingresar cuidados: ')

    planta = {
         "id": len(stock_de_plantas) +1,
         "nombre_comun": nombre_comun,
         "nombre_cientifico": nombre_cientifico,
         "categoria": categoria,
         "sector": sector,
         "stock": stock,
         "precio": precio,
         "cuidados": cuidados
    }
    stock_de_plantas.append(planta)


def baja_planta ():
    nombre_comun = input('Para dar de baja ingrese en nombre_comun: ')
    for planta in stock_de_plantas:
        if nombre_comun == alta_planta ('nombre_comun'):
            stock_de_plantas.remove(planta)
            break

