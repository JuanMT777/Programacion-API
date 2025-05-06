class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):  
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
            
# Crear objetos
p1 = Persona("Juan", 23)
p1.saludar()
