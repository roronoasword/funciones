#segundo

def filtrar_estudiantes():
    estudiantes = []
    cantidad = int(input("ingrese la cantidad de estudiantes: "))

    for i in range(cantidad):
        nombre = input(f"--nombre del estudiante {i+1}--: ")
        nota = float(input(f"--nota de {nombre}--: "))
        estudiantes.append((nombre, nota))
    aprovados = [nombre for nombre, nota in estudiantes if nota >= 3.0]
    print(f"\nLos estudiantes que aprovaron: {', '.join(aprovados)if aprovados else'nadie aprobo'}")

filtrar_estudiantes()