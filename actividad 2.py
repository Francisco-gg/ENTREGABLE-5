class EstudiantesTable:
    def __init__(self):
        self.estudiantes = []
        self.id_counter = 1  
    def insertar_estudiante(self, nombre, edad, ciudad):
        estudiante = {
            "id": self.id_counter,
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }
        self.estudiantes.append(estudiante)
        self.id_counter += 1
    def consultar_todos(self):
        return self.estudiantes
    def filtrar_por_ciudad(self, ciudad):
        return [est for est in self.estudiantes if est["ciudad"] == ciudad]
    def consultar_mayores_de_20(self):
        return [est for est in self.estudiantes if est["edad"] > 20]

tabla = EstudiantesTable()

tabla.insertar_estudiante("Ana", 22, "Bogotá")
tabla.insertar_estudiante("Luis", 19, "Medellín")
tabla.insertar_estudiante("Camila", 23, "Bogotá")
tabla.insertar_estudiante("Pedro", 20, "Cali")
tabla.insertar_estudiante("Carlitos", 18, "Medellín")
tabla.insertar_estudiante("Diana", 23, "Cali")

print("Todos los registros:")
for estudiante in tabla.consultar_todos():
    print(estudiante)

ciudad = "Bogotá"
print(f"\nEstudiantes en {ciudad}:")
for estudiante in tabla.filtrar_por_ciudad(ciudad):
    print(estudiante)

ciudad = "Cali"
print(f"\nEstudiantes en {ciudad}:")
for estudiante in tabla.filtrar_por_ciudad(ciudad):
    print(estudiante)    

ciudad = "Medellín"
print(f"\nEstudiantes en {ciudad}:")
for estudiante in tabla.filtrar_por_ciudad(ciudad):
    print(estudiante)    

print("\nEstudiantes mayores de 20 años:")
for estudiante in tabla.consultar_mayores_de_20():
    print(estudiante)
