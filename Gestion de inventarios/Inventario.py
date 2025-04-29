class Producto:
    def __init__(self, identificador, nombre, descripcion, precio, cantidad):
        self.id = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad 

    def __str__(self):
        return (f"ID: {self.id} | Nombre: {self.nombre} | Descripción: {self.descripcion} | "
                f"Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, identificador):
        original_len = len(self.productos)
        self.productos = [p for p in self.productos if p.id != identificador]
        if len(self.productos) < original_len:
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, identificador):
        for producto in self.productos:
            if producto.id == identificador:
                producto.nombre = input("Nuevo nombre (dejar vacío para mantener): ") or producto.nombre
                producto.descripcion = input("Nueva descripción: ") or producto.descripcion
                try:
                    nuevo_precio = input("Nuevo precio: ")
                    if nuevo_precio:
                        producto.precio = float(nuevo_precio)
                except ValueError:
                    print("⚠️ Precio no válido. No se actualizó.")
                try:
                    nueva_cantidad = input("Nueva cantidad: ")
                    if nueva_cantidad:
                        producto.cantidad = int(nueva_cantidad)
                except ValueError:
                    print("⚠️ Cantidad no válida. No se actualizó.")
                print("✅ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    def listar_productos(self):
        if not self.productos:
            print("📦 No hay productos en el inventario.")
        else:
            print("\n📋 Lista de productos:")
            for p in self.productos:
                print(p)

    def filtrar_producto(self, criterio):
        encontrados = [
            p for p in self.productos if criterio.lower() in p.nombre.lower() or criterio == p.id
        ]
        if encontrados:
            print("\n🔎 Resultados encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese criterio.")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Listar productos")
        print("5. Buscar producto (por ID o nombre)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_ = input("ID del producto: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(Producto(id_, nombre, descripcion, precio, cantidad))
            except ValueError:
                print("⚠️ Error: precio o cantidad inválidos.")
        elif opcion == "2":
            id_ = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_)
        elif opcion == "3":
            id_ = input("ID del producto a actualizar: ")
            inventario.actualizar_producto(id_)
        elif opcion == "4":
            inventario.listar_productos()
        elif opcion == "5":
            criterio = input("Buscar por ID o nombre: ")
            inventario.filtrar_producto(criterio)
        elif opcion == "6":
            print("👋 Saliendo del inventario...")
            break
        else:
            print("❌ Numero validos del 1 al 6. Intentalo de nuevo")


if __name__ == "__main__":
    menu()
