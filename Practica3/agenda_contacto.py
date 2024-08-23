
def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto: ")
    telefono = input("Ingrese el telefono de contacto: ")
    email = input("Ingrese el email de contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto '{nombre}' fue eliminado.")
    else: 
        print(f"No existe un contacto llamado '{nombre}'")
    
def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print("\n")
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else: 
        print(f"No existe el contacto llamado '{nombre}'")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print("_" * 50)
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info['telefono']}")
            print(f"Email: {info['email']}")            
    else:
        print("La agenda está vacia.")


def agenda_contacto():
    agenda = {}   

    while True:
        print("_" *100)
        print("        Agenda de contactos: \
        \n\t1. Agregar contacto.\
        \n\t2. Eliminar contacto.\
        \n\t3. Buscar contacto.\
        \n\t4. Lista de contactos.\
        \n\t5. Salir del programa.")
        print("_" * 100)
        opcion = input("Por favor ingrese una opcion: ")
        print("_" * 100)
        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de conmtactos ¡Hasta pronto!")
            break
        else: 
            print("Ingrese una opcion valida (del 1 al 5)")
        
agenda_contacto()


