import json

data = []

RUTA_ARCHIVO = "manejo_archivos/ingreso_empleados/empleados.json"

def guardar_datos():
    global data
    global RUTA_ARCHIVO
    
    try:
        contenido = json.dumps(data, indent = 4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente :)")
    except Exception: 
        print("Error al guardar los datos :(")
        
def cargar_datos():
    global data
    global RUTA_ARCHIVO
    
    try: 
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente :)")
    except Exception:
        print("Error al cargar los datos :()")

