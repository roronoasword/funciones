def gestionar_agenda():
    agenda = {}
    cantidad = int(input("cuantos contactos desea agregar: "))

    for _ in range(cantidad):
        nombre = input("Nombre del contacto: ")
        telefono = input(f"Telefono de {nombre}: ")
        agenda[nombre] = telefono
    print("\n eliminacion \n")
    eliminar = input(" a quien desea eliminar: ")
    if eliminar in agenda:
        del agenda[eliminar]
        print(f"contacto {eliminar} eliminado")
    else:
        print("el contacto no existe")
gestionar_agenda()
