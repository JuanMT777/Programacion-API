#Programacion estructurada en PY
from datetime import data, datetime, timedelta

# Mensaje de variables
nombre = "Juan"
edad = 23
estatura = 1.85

print(f"{nombre} tiene {edad} años y mide {estatura} metros.") #La f sirve para interpolar variables con texto

# Conversion de tipos

edad_str = "30"
edad_int = int(edad_str)

print(edad_int + 5)

# manejo de fechas
fecha_hoy = data.today()
fecha_hora = datetime.now()
cumpleaños = data(1990, 4, 15)
mañana = data.today() + timedelta(days=1)
dias_transcurridos = (fecha_hoy - data(2025, 1, 1)).days

print(cumpleaños)

#Manejo de boleans e if - else con Y
es_mayor_de_edad = True
Tien_Licencia = False

if es_mayor_de_edad and Tien_Licencia:
    print("Puedes conducir")
else: 
    print("No puedes conducir")
        
#Manejo de rangos con if-elif-else
nota = 85
if nota >= 5:
    print("Excelente")
elif nota >= 3:
    print("Aprobado")
else:
    print("Reprobado")        
    
#Simulacion de casos
opcion = 2

if opcion == 1:
    print("Opcion 1")
elif opcion == 2:
    print("Opcion 2")
else:
    print("Opcion no valido")       
    
 #Simulaciones de casos con diccionario   
def opcion_1():
    return "Opcion 1"
def opcion_2():
    return "Opcion 2"

switch = {1: opcion_1, 2: opcion_2}
resultado = switch.get(2, lambda: "Opcion no valid")()
print("resultado")

#bucles for y while
#For
for i in range(1, 6):
    print(i)

#While
contador = 3
while contador > 0:
    print(contador)
    cont -= 1 

#Simulacion de bucle con while:
while True:
    numero = int(input("Ingresa un numero mayor que 0 para inciar y 10 para terminar"))
    if numero > 0:
        continue
    elif numero == 10:
        break
    
#Bucle tipo foreach con lista y diccionario
animales = ["gato", "perro", "loro"]
for animal in animales:
    print(animal)
    
persona = {"Nombre": "Juan", "Edad": 30}
for clave, valor in persona.items():
    print(f"{clave}: {valor}") 
       
