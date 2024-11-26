from document import Documento
from str2dic import Str2Dic 

class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
        self.next_id = 1  

    def añadir_documento(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def listar_documentos(self):
        return list(self.documentos.values())

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento)
    
    def importar_csv(self, ruta_csv):
        try:
            with open(ruta_csv, "r", encoding="utf-8") as file:
                schema = file.readline().strip().split(",")  # Leer la primera línea como esquema
                if not schema or any(not col for col in schema):
                    raise ValueError("El esquema del archivo CSV está vacío o mal formado.")
                
                for idx, row in enumerate(file, start=1):
                    values = row.strip().split(",")  # Separar valores
                    if len(values) == len(schema):  # Validar que coincidan con el esquema
                        data = {schema[i]: values[i] for i in range(len(schema))}  # Crear diccionario
                        documento = Documento(self.next_id, data)  # Crear documento
                        self.añadir_documento(documento)  # Añadir a la colección
                        self.next_id += 1  # Incrementar ID
                    else:
                        print(f"Advertencia: La fila {idx} no coincide con el esquema y será omitida.")
        except FileNotFoundError:
            print(f"Error: El archivo '{ruta_csv}' no existe.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado al importar CSV: {e}")

    def __str__(self):
        return f"Colección '{self.nombre}' con {len(self.documentos)} documentos."

class Database:
    def __init__(self):
        self.colecciones = {}

    def crear_coleccion (self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones [nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self,nombre_coleccion):
        return self.colecciones.get(nombre_coleccion)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} colecciones"
    
    
