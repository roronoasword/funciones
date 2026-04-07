# principal.py
import funciones_super

def ejecutar_simulador():
    # Datos iniciales
    productos = ["Poción", "Antídoto", "Superball", "Revivir", "Caramelo Raro"]
    precios = [15.50, 10.0, 25.75, 40.0, 100.25]
    carrito = []

    funciones_super.mostrar_bienvenida()
    presupuesto = funciones_super.obtener_presupuesto()

    # Bucle principal de opciones
    while True:
        print(f"\nSaldo actual: ${round(presupuesto, 2)}")
        print("1. Comprar")
        print("2. Salir")
        
        opcion = input("¿Qué deseas hacer? (1/2): ")

        if opcion == "1":
            funciones_super.mostrar_productos(productos, precios)
            # Uso de int() para la selección del usuario
            try:
                seleccion = int(input("Selecciona el número del producto: "))
                presupuesto = funciones_super.procesar_compra(seleccion, productos, precios, presupuesto, carrito)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        elif opcion == "2":
            break
        else:
            print("Opción no reconocida.")

    # Resultado final
    funciones_super.mostrar_resumen(carrito, presupuesto)

if __name__ == "__main__":
    ejecutar_simulador()