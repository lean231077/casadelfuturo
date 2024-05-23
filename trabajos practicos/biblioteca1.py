import json

class Libro:
    def __init__(self, titulo, autor, año_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True
        self.unidades = unidades

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_disponibles = []

    def agregar_libro(self, libro):
        self.libros_disponibles.append(libro)
        
    #def agregar(productos):
      # while True:
    #     titulo=input("Ingrese el nombre del libro: ")
    #     autor=input("Ingrese el autor: ")
    #     añp=int(input("Ingrese el año: "))
    #     cantidad=int(input("Ingrese la cantidad: "))
    #     libros_disponibles.update({"titulo":titulo,"autor":autor, "año": año, "cantidad":cantidad})
    #     libros_disponibles.append(libro)
    #     pregunta=input("desea agregar otro libro? S/N ")
    #     print("--------------------------------------")
    #     pregunta=pregunta.lower()
    #     if pregunta=="n":
    #         break

    def mostrar_libros_disponibles(self):
        print(f"Libros disponibles en la biblioteca '{self.nombre}':")
        for libro in self.libros_disponibles:
            print(f"- {libro.titulo} ({libro.autor})")

    def prestar_libro(self, titulo_libro):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo_libro and libro.disponible:
                libro.disponible = False
                print(f"Se ha prestado el libro '{libro.titulo}'")
                return
        print(f"No se encontró el libro '{titulo_libro}' o no está disponible en la biblioteca '{self.nombre}'")

    def recibir_libro(self, titulo_libro):
        for libro in self.libros_disponibles:
            if libro.titulo == titulo_libro and not libro.disponible:
                libro.disponible = True
                print(f"Se ha recibido el libro '{libro.titulo}'")
                return
        print(f"No se encontró el libro '{titulo_libro}' o ya está disponible en la biblioteca '{self.nombre}'")



# libro1 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, 5)
# libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, 3)
# libro3 = Libro ("Matrix", "Hermanos",2007,43)

biblioteca1 = Biblioteca("Biblioteca Central")
# biblioteca1.agregar_libro(libro1)
# biblioteca1.agregar_libro(libro2)
# biblioteca1.agregar_libro(libro3)
biblioteca3 = Biblioteca ("Biblioteca Sur")
# biblioteca3.agregar_libro(libro3)



print (biblioteca1.libros_disponibles)
#biblioteca1.prestar_libro("Matrix")
#biblioteca1.recibir_libro("Matrix")
#biblioteca3.mostrar_libros_disponibles()
biblioteca1.mostrar_libros_disponibles()
# while True:
#     print ("ingrese la opcion deseada:")
#     seleccion= int(input ("Seleccione la opcion deseada: 1-Agregar libro 2-Mostrar libros en biblioteca 3-Prestar libro 4-Recibir libro"))
#    
        
   