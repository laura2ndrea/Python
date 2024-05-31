import json
import csv

data = []
columnas = ['tipo_registro', 'id', 'nombre', 'fecha/hora', 'advertencia']

RUTA_ARCHIVO_JSON = "manejo_archivos/ingreso_empleados/empleados.json"
RUTA_ARCHIVO_CSV = "manejo_archivos/ingreso_empleados/registros.csv"

def guardar_datos(formato = "json"):
    global data
    global columnas
    global RUTA_ARCHIVO_JSON
    global RUTA_ARCHIVO_CSV
    
    try:
        if formato == "json":
            contenido = json.dumps(data, indent = 4)
            with open(RUTA_ARCHIVO_JSON, "w") as file:
                file.write(contenido)
            print("Datos guardados exitosamente :)")
        elif formato == "csv":
            with open(RUTA_ARCHIVO_CSV, "w", newline="") as file: 
                writer = csv.DictWriter(file, fieldnames=columnas)
                writer.writeheader()
                for fila in data:
                    writer.writerow(fila)
            print("Datos guardados exitosamente :)")
        else: 
            print("Formato de arhivo no compatible")
    except Exception: 
        print("Error al guardar los datos :(")
        
def cargar_datos(formato = "json"):
    global data
    global RUTA_ARCHIVO_JSON
    global RUTA_ARCHIVO_CSV
    
    try: 
        if formato == "json": 
            with open(RUTA_ARCHIVO_JSON, "r") as file:
                data = json.load(file)
            print("Datos cargados exitosamente :)")
        elif formato == "csv": 
            with open(RUTA_ARCHIVO_CSV, "r") as file:
                lector = csv.DictReader(file)
                data = list(lector)
            print("Datos cargados exitosamente :)")
        else: 
            print("Formato de arhivo no compatible")
    except Exception:
        print("Error al cargar los datos :()")




         
    
        

