# Aqui se impoortan las expresiones regulares
import re

# Aqui se valida que se ingresen numeros
def ingresaFloat(mensaje):
  while True:
    try:
      return float(input(mensaje))
    except ValueError:
        print("Ingresa un Numero !")

# Aqui se valida que se ingresen numeros
def ingresaEntero(mensaje):
  while True:
    try:
      return int(input(mensaje))
    except ValueError:
        print("Ingresa un Entero !")


# Aqui se pone una expresion regular para validar el texto
def ingresaTexto(mensaje):
  patron = r'^[a-zA-Z0-9\s]+$'
  while True:
    try:
      texto = input(mensaje)
      if re.match(patron, texto):
        return texto
      else:        
          raise ValueError
    except ValueError:
      print("Ingresa un Texto !")

      # Menu de usuario:
# Este metodo  le permite al usuario acceder a un menu interactivo,
# entregando una lista de opciones seleccionables listadas con numeros del 1-6 
def menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por ID")
    print("5. Listar todos los productos")
    print("6. Salir")
    opcion = ingresaEntero("Seleccione una opción: ")
    return opcion

# Clase de excepciones cubriendo errores para: Producto No Encontrado, Cantidad y Precio no Valido
class InventarioException(Exception):
    pass

class ProductoNoEncontradoException(InventarioException):
    def __init__(self, id):
        self.id = id
        super().__init__(f"El producto con ID {id} no fue encontrado en el inventario.")

class CantidadNoValidaException(InventarioException):
    def __init__(self, cantidad):
        self.cantidad = cantidad
        super().__init__(f"La cantidad '{cantidad}' no es válida. Debe ser un número entero mayor o igual a cero.")

class PrecioNoValidoException(InventarioException):
    def __init__(self, precio):
        self.precio = precio
        super().__init__(f"El precio '{precio}' no es válido. Debe ser un número mayor que cero.")

#  creacion de clase Producto con sus respectivos atributos 

class Producto:
    def __init__(self, id, nombre, descripcion, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

# Devuelve una cadena formateada con los atributos de la instancia 
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}"




# Creacion de un diccionario para la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

# Permite agregar productos a la clase Producto
    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

# Permite eliminar un producto de la clase Producto, si el producto no es encontrado dentro de la clase se lansa una excepcion
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            raise ProductoNoEncontradoException(id)

# Permite actualizar un producto de la clase Producto, si encuentra el ID del producto y la cantidad o precio
# es menor o igual a 0 se llama a las clases de excepción correspondiente. Si el ID no se encuentra, se llamada
# a la clase ProductoNoEncontradoException(id) 
    def actualizar_producto(self, id, nombre, descripcion, cantidad, precio):
        if id in self.productos:
            if cantidad < 0:
                raise CantidadNoValidaException(cantidad)
            if precio <= 0:
                raise PrecioNoValidoException(precio)

            self.productos[id].nombre = nombre
            self.productos[id].descripcion = descripcion
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
        else:
            raise ProductoNoEncontradoException(id)

# Metodo que crea una funcion para buscar si el producto pertenece
# dentro de la clase Producto 
    def buscar_producto(self, id):
        if id in self.productos:
            return self.productos[id]
        else:
            raise ProductoNoEncontradoException(id)

# Este metodo informa al usuario la cantidad total de productos dentro del inventario
# y ademas realiza el calculo del valor de venta total del inventario. 
    def listar_productos(self):
        total_cantidad = sum(producto.cantidad for producto in self.productos.values())
        total_valor = sum(producto.cantidad * producto.precio for producto in self.productos.values())
        print("Inventario:")
        for producto in self.productos.values():
            print(producto)
        print(f"Total de productos: {total_cantidad}, Valor total del inventario: {total_valor}")


# Este metodo establece cuales son las acciones a realizar dentro de mi clase
# inventario posterior a que el usuario  seleccione un argumento del menu. 
def main():
    inventario = Inventario()

    while True:
        opcion = menu()

        if opcion == 1:
            id = ingresaEntero("Ingrese el ID del producto: ")
            nombre = ingresaEntero("Ingrese el nombre del producto: ")
            descripcion = ingresaTexto("Ingrese la descripción del producto: ")
            cantidad = ingresaEntero("Ingrese la cantidad del producto: ")
            precio = ingresaFloat("Ingrese el precio del producto: ")
            producto = Producto(id, nombre, descripcion, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado al inventario.")

        elif opcion == 2:
            id = ingresaEntero("Ingrese el ID del producto a eliminar: ")
            try:
                inventario.eliminar_producto(id)
            except ProductoNoEncontradoException as e:
                print(e)

        elif opcion == 3:
            id = ingresaEntero("Ingrese el ID del producto a actualizar: ")
            nombre = ingresaEntero("Ingrese el nuevo nombre del producto: ")
            descripcion = ingresaTexto("Ingrese la nueva descripción del producto: ")
            cantidad = ingresaEntero("Ingrese la nueva cantidad del producto: ")
            precio = ingresaFloat("Ingrese el nuevo precio del producto: ")
            try:
                inventario.actualizar_producto(id, nombre, descripcion, cantidad, precio)
            except (ProductoNoEncontradoException) as e:
                print(e)

        elif opcion == 4:
            id = ingresaEntero("Ingrese el ID del producto a buscar: ")
            try:
                producto = inventario.buscar_producto(id)
                print(producto)
            except ProductoNoEncontradoException as e:
                print(e)

        elif opcion == 5:
            inventario.listar_productos()

        elif opcion == 6:
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Clase por defecto para llamar al main
if __name__ == "__main__":
    main()


