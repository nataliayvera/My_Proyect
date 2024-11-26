schema= "Nombre,Apellido,Edad,Mail"
row= "Natalia,Vera,25,nataliayvera17@gmail.com"

class Str2Dic (object):
    def __init__(self, schemaStr, separator =","):
        self.schema = schemaStr.strip().split(separator)
        self.separator = separator

    def convert(self, row):
        tmp = row.strip().split(self.separator)
        if len(tmp) == len(self.schema):
            return {self.schema[i]: tmp[i] for i in range(len(self.schema))}
        else:
            raise ValueError("La fila no coincide con el esquema.")
    
o = Str2Dic(schema)
d= o.convert(row)
print (d)