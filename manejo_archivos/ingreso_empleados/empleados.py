import datos

def registro_empleados(): 
    empleado = {}
    ID = input("Ingrese el ID del empleado: ")
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
    print("Las empleados registrados son: ")
    for id, informacion in datos.data.items():
        print("ID:", id)
        print("- Nombre:", informacion["nombre"])
        print("- Edad:", informacion["edad"])
        print("- Estatus:", informacion["estatus"])
        print() 