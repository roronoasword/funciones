def mostrar_bienvenida():
    print("--Bienvenido al poke-mart--")

def obtener_presupuesto():

    dato = input("Ingresa tu sueldo: ")
    return float(dato)

def mostrar_productos(nombres, precios):
    print("\n Lista de productos: ")

    inventario = list(zip(nombres, precios))
    for i, (prod, precio) in enumerate(inventario, 1):
        print(f"{i}. {prod} -${precio}")

def procesar_compra(seleccion, nombres, precios, saldo, carrito):
    # Uso de len() para validar
    if 1 <= seleccion <= len(nombres):
        # Uso de int() para asegurar el índice
        indice = int(seleccion) - 1
        precio_item = precios[indice]
        nombre_item = nombres[indice]

        if saldo >= precio_item:
            saldo -= precio_item
            carrito.append(precio_item)
            print(f"¡Has comprado {nombre_item}!")
        else:
            print("¡Saldo insuficiente! Necesitas más entrenamiento.")
    else:
        print("Opción no válida.")
    return saldo

def mostrar_resumen(carrito, saldo_final):
    print("\n" + "="*30)
    print("RESUMEN DE TU COMPRA")
    
    # Uso de len() para verificar si hay elementos
    if len(carrito) > 0:
        # Uso de sum(), sorted(), max(), min() y round()
        total = sum(carrito)
        precios_ordenados = sorted(carrito)
        
        print(f"Total de productos: {len(carrito)}")
        print(f"Precios pagados (ordenados): {precios_ordenados}")
        print(f"Producto más caro: ${max(carrito)}")
        print(f"Producto más barato: ${min(carrito)}")
        print(f"Gasto total: ${round(total, 2)}")
    else:
        print("No compraste nada hoy.")

    print(f"Saldo restante: ${round(saldo_final, 2)}")
    print("¡Gracias por visitar el Poké-Mart!")
    print("="*30)
