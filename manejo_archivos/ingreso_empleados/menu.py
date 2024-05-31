import datos
import empleados

opc_menu = ("1. Para registrar un empleado", "2. Para mostrar todos los empleados", "3. Para modificar información de un empleado", "4. Para despedir un empleado", "5. Para registrar el ingreso o salida de un empleado", "6. Para mostrar los registros", "7. Para salir")

def recorrer_menu():
    global opc_menu
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def espacios(): 
    print("*******************************************")

def menu_principal():
    datos.cargar_datos()
    while True:
        espacios()
        opc = 0
        try:
            opc = recorrer_menu()
        except Exception:
            print("Valor incorrecto!!")            
        if opc == 1:
            empleados.registro_empleados()
        elif opc == 2:
            empleados.mostrar_empleados()
        elif opc == 3:
            empleados.modificar_empleados()
        elif opc == 4: 
            empleados.despedir_empleados()
        elif opc == 5: 
            print("registros")
        elif opc == 6: 
            print("mostrar_registros")
        elif opc == 7:
            print("Saliendo...")
            break
        else:
            print("La opción no es válida!")