class EstudiantesColeccion:
    def __init__(self):
        self.estudiantes = []
    def insertar_documento(self, nombre, edad, ciudad):
        documento = {
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }
        self.estudiantes.append(documento)
    def consultar_todos(self):
        return self.estudiantes
    def filtrar_por_ciudad(self, ciudad):
        return [doc for doc in self.estudiantes if doc["ciudad"] == ciudad]
    def consultar_mayores_de_20(self):
        return [doc for doc in self.estudiantes if doc["edad"] > 20]

coleccion = EstudiantesColeccion()

coleccion.insertar_documento("Juan", 20, "Bogotá")
coleccion.insertar_documento("Ana", 22, "Medellín")
coleccion.insertar_documento("Luis", 19, "Cali")

print("Todos los documentos:")
for estudiante in coleccion.consultar_todos():
    print(estudiante)

ciudad = "Bogotá"
print(f"\nEstudiantes en {ciudad}:")
for estudiante in coleccion.filtrar_por_ciudad(ciudad):
    print(estudiante)

print("\nEstudiantes mayores de 20 años:")
for estudiante in coleccion.consultar_mayores_de_20():
    print(estudiante)
