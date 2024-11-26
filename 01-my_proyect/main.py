from database import Database  
from database import Coleccion  
from document import Documento   
from str2dic import Str2Dic 
import os

def import_collection(nombre_archivo):
    coleccion = Coleccion("Personas")
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



def main():
    db = Database()  

    while True:
        opcion = mostrar_menu()
        if opcion is None:  
            continue
        
        if opcion == 1 :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            db.crear_coleccion(nombre_coleccion)  
            print(f"Colección '{nombre_coleccion}' creada.")
        
        elif opcion == 2  :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion)  
            if coleccion:
                ruta_csv = input("Ingrese la ruta del archivo CSV: ")
                if os.path.exists(ruta_csv):
                    coleccion.importar_csv(ruta_csv) 
                    print(f"Datos importados en la colección '{nombre_coleccion}'.")
                else:
                    print("El archivo no existe.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
        elif opcion == 3 :
            nombre_coleccion = input("Ingrese el nombre de la colección: ")
            coleccion = db.obtener_coleccion(nombre_coleccion) 
            if coleccion:
                try:
                    doc_id = int(input("Ingrese el ID del documento: ")) 
                    documento = coleccion.buscar_documento(doc_id)  
                    if documento:
                        print("Documento encontrado:")
                        print(documento)
                    else:
                        print("Documento no encontrado.")
                except ValueError:
                    print ("El ID debe ser un número.")
            else:
                print(f"Colección '{nombre_coleccion}' no encontrada.")
        
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
        
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()