import datos
import menu

def registro_empleados(): 
    menu.espacios()
    empleado = {}
    ID = input("Ingrese el ID del empleado: ")
    ID = ID.upper()
    if datos.data.get(ID, None) == None:
        empleado["nombre"] = input("Escriba el nombre del empleado: ")
    try:
        empleado["edad"] = int(input("Ingrese la edad del empleado: "))
    except Exception:
        print("Ingrese un valor válido!")
        return
    empleado["estatus"] = "contratado"
    datos.data[ID] = empleado
    datos.guardar_datos()

def mostrar_empleados(): 
    menu.espacios()
    print("Las empleados registrados son: ")
    for id, informacion in datos.data.items():
        print("ID:", id)
        print("- Nombre:", informacion["nombre"])
        print("- Edad:", informacion["edad"])
        print("- Estatus:", informacion["estatus"])
        print() 

def modificar_empleados(): 
    menu.espacios()
    ID = input("Ingrese el ID del empleado: ")
    ID = ID.upper()
    if datos.data.get(ID, None) == None:
        print("El ID ingresado no esta registrado en la base de datos")
    else: 
        while True: 
            opc = input("Ingrese el numero de la opción que desea cambiar: \n 1. Para cambiar el nombre. \n 2. Para cambiar la edad. \n 3. Para salir. \n")
            if opc == "1": 
                datos.data[ID]["nombre"] = input("Ingrese el nuevo nombre: ")
                datos.guardar_datos()
            elif opc == "2":
                try:
                    datos.data[ID]["edad"] = int(input("Ingrese la nueva edad: "))
                    datos.guardar_datos()
                except Exception: 
                    print("Ingrese un valor valido")
                    return
            elif opc == "3":
                print("Saliendo ...")
                break
            else: 
                print("Valor invalido, ingrese un valor valido")

def despedir_empleados(): 
    while True: 
        menu.espacios()
        ID = input("Ingrese el ID del empleado: ")
        ID = ID.upper()
        if datos.data.get(ID, None) == None:
            print("El ID no esta registrado en la base de datos")
            break
        else: 
            print("El empleado que desea despedir es: ")
            print("- ID:", ID)
            print("- Nombre:", datos.data[ID]["nombre"])
            print("- Edad:", datos.data[ID]["edad"])
            print("- Estatus:", datos.data[ID]["estatus"])
            while True:
                opc = input("Seleccione: \n 1. Para despedir al empleado. \n 2. Para buscar otro empleado. \n 3. Para salir ...\n")
                if opc == "1": 
                    datos.data[ID]["estatus"] = "despedido"
                    datos.guardar_datos()
                    return
                elif opc == "2": 
                    break
                elif opc == "3": 
                    print("Saliendo ...")
                    return
                else: 
                    print("Opcion invalida, ingrese una opcion valida")
