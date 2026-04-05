def contar_frecuencias():
    entrada = input("Ingrese una frase separada por espacios: ")

    lista = entrada.lower().split()

    frecuencias = {}

    for palabra in lista:
        frecuencias[palabra] = frecuencias.get(palabra, 0 ) + 1
    print("\n conteo: ")
    for palabra, cantidad in frecuencias.items():
        print(f"-{palabra}: {cantidad} vez/veces")
contar_frecuencias()