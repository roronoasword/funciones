#primer ejercicio
def calcular_estats():
    notas = []
    cantidad = int(input("cuantas notas va a ingresar?: "))

    for i in range(cantidad):
        nota = float(input(f"ingrese la nota {i + 1}: "))
        notas.append(nota)
    
    if notas:
        promedio = sum(notas) / len(notas)
        print("\n resultados \n")
        print(f"promdeio: {promedio:.2f}")
        print(f"nota mas alta: {max(notas)}")
        print(f"nota mas baja: {min(notas)}")
calcular_estats()
