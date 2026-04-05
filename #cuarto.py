def calcular_valor_inventario():
    inventario = []
    cantidad_productos = int(input("cuantos productos hay en el inventario: "))

    for i in range(cantidad_productos):
        print(f"producto {i+1} ")
        nombre = input(" nombre: ")
        precio = float(input( f"precio de {nombre}: "))
        cantidad = int(input( f"cantidad de stock: "))
        inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad })

    total = sum(p['precio'] * p['cantidad'] for p in inventario)
    print(f"\n el valor del inventario es: ${total:,.2f}")

calcular_valor_inventario()