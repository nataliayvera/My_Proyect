from database import Database  
from database import Coleccion  
from document import Documento   
from str2dic import Str2Dic 
import os

# Función para importar una colección desde un archivo CSV
def import_collection(nombre_archivo):
    coleccion = Coleccion("Personas") # Crear una nueva colección llamada 'Personas'
    with open(nombre_archivo, "r", encoding="utf-8") as file:
        schema = file.readline().strip()  # Leer el esquema
        str2dic = Str2Dic(schema)
        linea = file.readline()
        while linea:
            data = str2dic.convert(linea)  # Convertir línea a diccionario
            documento = Documento(coleccion.next_id, data)  # Crear documento
            coleccion.añadir_documento(documento)  # Añadir a la colección
            coleccion.next_id += 1
            linea = file.readline()  # Leer la siguiente línea
    return coleccion


def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion.isdigit() and 1 <= int(opcion) <= 6:
        return int(opcion)
    print("Opción no válida. Intente nuevamente.")
    return None


# Función principal que maneja la ejecución del programa
def main():
    db = Database()  # Crear una instancia de la base de datos

    while True:
        opcion = mostrar_menu() # Mostrar el menú y obtener la opción seleccionada
        if opcion is None:   # Si la opción no es válida, continuar con el ciclo
            continue

       # Opción 1: Crear una nueva colección 
        if opcion == 1 :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.crear_coleccion(nombre_coleccion)   # Crear la colección en la base de datos
            print(f"Colección '{nombre_coleccion}' creada.")
        
        # Opción 2: Importar datos desde un archivo CSV
        elif opcion == 2  :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)    # Obtener la colección de la base de datos
            if coleccion:
                ruta_csv = input("Ingrese la ruta del archivo CSV: ")
                # Verificar si el archivo existe
                if os.path.exists(ruta_csv):
                    coleccion.importar_csv(ruta_csv) 
                    print(f"Datos importados en la colección '{nombre_coleccion}'.")
                else:
                    print("El archivo no existe.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        # Opción 3: Consultar un documento por su ID
        elif opcion == 3 :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion) 
            if coleccion:
                try:
                    doc_id = int(input("Ingrese el ID del documento: ")) 
                    documento = coleccion.buscar_documento(doc_id)  # Buscar el documento por su ID 
                    if documento:
                        print("Documento encontrado:") #si se encuentra el documento
                        print(documento)
                    else:
                        print("Documento no encontrado.") #si no se encuentra
                except ValueError:
                    print ("El ID debe ser un número.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        # Opción 4: Eliminar un documento por su ID
        elif opcion == 4:
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion) 
            if coleccion:
                try:
                    doc_id = int(input("Ingrese el ID del documento a eliminar: "))  
                    coleccion.eliminar_documento(doc_id) 
                    print(f"Documento con ID {doc_id} eliminado.")
                except ValueError:
                    print ("El ID debe ser un número.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        # Opción 5: Listar todos los documentos de la colección
        elif opcion == 5:
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)
            if coleccion:
                documentos = coleccion.listar_documentos()  
                if documentos:
                    print("\n--- Lista de Documentos ---")
                    for doc in documentos:
                        print(doc)
                        print("-----------")
                else:
                    print("No hay documentos en la colección.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        # Opción 6: Salir del programa
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()