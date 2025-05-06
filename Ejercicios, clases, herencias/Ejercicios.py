#01. Si puede votar o no
nombre = str(input("Ingresa tu nombre: "))
edad = int(input("Ingresa tu edad: "))
 
if edad >= 18:
    print(f"{nombre}, Puedes votar, tienes {edad} años")
else:
    print(f"{nombre}, No puedes votar, tienes {edad} años")    
    
    
#02. Cajero automatico 
# Simulación de un cajero automático
saldo = 1000  # Saldo inicial del usuario

print("Bienvenido al Cajero Automático")
print(f"Tu saldo inicial es: ${saldo}\n")

while saldo > 0:
    try:  # Es para permitir que el programa no se rompa en ocacion de un error
        retiro = float(input("Ingresa la cantidad que deseas retirar: $"))

        if retiro <= 0:
            print("Ingresa un monto válido mayor a 0.\n")
            continue

        if retiro > saldo:
            print(f"No tienes suficiente saldo. Tu saldo actual es: ${saldo}\n")
        else:
            saldo -= retiro
            print(f"Has retirado ${retiro}. Saldo restante: ${saldo}\n")

    except ValueError: #Se ejecuta si ocurre un error del tipo ValueError
        print("Por favor, ingresa un número válido.\n")

print("Tu saldo es 0. No puedes retirar más dinero.")
print("Gracias por usar el cajero. ¡Hasta pronto!")

#Almacen de frutas
# Lista de frutas
frutas = ["manzana", "banana", "naranja", "sandía", "pera", "mango"]

# Mostrar lista de frutas disponibles
print("Lista de frutas disponibles:")
print(", ".join(frutas))

# Solicitar búsqueda
busqueda = input("\n Ingresa el nombre de la fruta que deseas buscar: ").lower()

# Verificar si la fruta está en la lista
if busqueda in frutas:
    print(f"¡Sí! La fruta '{busqueda}' está en la lista.")
else:
    print(f"La fruta '{busqueda}' no se encuentra en la lista.")




    