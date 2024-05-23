"""
Crea una clase llamada **`Libro`** con los siguientes atributos:

- **`titulo`**
- **`autor`**
- **`año_publicacion`**
- **`disponible`** (inicializado en True)
- `**unidades**`

Pueden crear el JSON de libros utilizando: [JSON Data AI](https://www.jsondataai.com/)

Crea otra clase llamada **`Biblioteca`** que tenga una lista de libros disponibles. Implementa métodos para:

- Mostrar todos los libros disponibles.
- Prestar un libro (cambia el estado de **`disponible`** a False).
- Recibir un libro (cambia el estado de **`disponible`** a True).

Por último, crear un sistema que permita seleccionar entre bibliotecas (crear al menos 2) y 
agregar o quitar libros de las mismas. El sistema debe permitir guardar la base de libros de 
la biblioteca en un archivo **JSON**, o crear nuevas bibliotecas a partir de un archivo **JSON**. 
"""

class Libro:
    def __init__(self, titulo, autor, año, disponible, unidades):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
        self.unidades = unidades
        
    def agregar(libros):
    
        while True:
            autor=input("Ingrese el nombre del autor: ")
            titulo=input("Ingrese el titulo: ")
            año=int(input("Ingrese el año: "))
            cantidad=int(input("Ingrese la cantidad: "))
            unidades = int (input ("ingrese las unidades:"))
            libros={}
            libros.update({"autor":autor,"titulo":titulo, "año": año, "cantidad":cantidad, "unidades": unidades})
            pregunta=input("desea agregar otro libro? S/N ")
            print("--------------------------------------")
            pregunta=pregunta.lower()
            if pregunta=="n":
                break


class Biblioteca:
    def __init__ (self,disponible):
        self.disponible =True
        
    
    
    