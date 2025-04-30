import pyodbc

# Mostrar drivers disponibles (opcional)
print(pyodbc.drivers())

# Conexión a SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=MT;'
    'DATABASE=GestionEstudiantesCursos;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Funciones del sistema
def agregar_estudiante():
    id_estudiante = input("ID del estudiante: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    cursor.execute(
        "INSERT INTO Estudiantes (id_estudiante, nombre_completo, correo) VALUES (?, ?, ?)",
        (id_estudiante, nombre, correo)
    )
    conn.commit()
    print("✅ Estudiante agregado.\n")

def agregar_curso():
    id_curso = input("ID del curso: ")
    nombre = input("Nombre del curso: ")
    descripcion = input("Descripción: ")
    
    while True:
        try:
            creditos = int(input("Créditos: "))
            break
        except ValueError:
            print("❌ Por favor, ingresa un número válido para los créditos.")
    
    cursor.execute(
        "INSERT INTO Cursos (id_curso, nombre, descripcion, creditos) VALUES (?, ?, ?, ?)",
        (id_curso, nombre, descripcion, creditos)
    )
    conn.commit()
    print("✅ Curso agregado.\n")


def inscribir_estudiante():
    id_estudiante = input("ID del estudiante: ")
    id_curso = input("ID del curso: ")
    cursor.execute(
        "INSERT INTO Inscripciones (id_estudiante, id_curso) VALUES (?, ?)",
        (id_estudiante, id_curso)
    )
    conn.commit()
    print("✅ Inscripción completada.\n")

def listar_cursos_de_estudiante():
    id_estudiante = input("ID del estudiante: ")
    cursor.execute('''
        SELECT c.nombre, c.descripcion, c.creditos
        FROM Inscripciones i
        JOIN Cursos c ON i.id_curso = c.id_curso
        WHERE i.id_estudiante = ?
    ''', (id_estudiante,))
    cursos = cursor.fetchall()
    if cursos:
        print("📚 Cursos del estudiante:")
        for curso in cursos:
            print(f"- {curso.nombre} ({curso.creditos} créditos): {curso.descripcion}")
    else:
        print("❌ No hay cursos inscritos.\n")

def eliminar_inscripcion():
    id_estudiante = input("ID del estudiante: ")
    id_curso = input("ID del curso a eliminar: ")
    cursor.execute(
        "DELETE FROM Inscripciones WHERE id_estudiante = ? AND id_curso = ?",
        (id_estudiante, id_curso)
    )
    conn.commit()
    print("🗑️ Inscripción eliminada.\n")

# Menú interactivo
def menu():
    while True:
        print("\n--- Sistema de Gestión de Estudiantes y Cursos ---")
        print("1. Agregar estudiante")
        print("2. Agregar curso")
        print("3. Inscribir estudiante en curso")
        print("4. Listar cursos de un estudiante")
        print("5. Eliminar inscripción")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            agregar_curso()
        elif opcion == '3':
            inscribir_estudiante()
        elif opcion == '4':
            listar_cursos_de_estudiante()
        elif opcion == '5':
            eliminar_inscripcion()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

menu()
