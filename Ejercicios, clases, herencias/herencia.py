class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo

    def presentar(self):
        print(f"{self.nombre}, {self.edad} años, trabaja como {self.cargo}.")
