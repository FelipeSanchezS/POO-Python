class Libro:
    ##pass
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

#Llamamos la función
milibro = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156012195", True)
milibro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0156012196", True)
milibro3 = Libro("Rayuela", "Julio Cortázar", "978-0156012197", True)

#print(f"Mi primer libro es '{milibro.titulo}' y fue escrito por {milibro.autor}.")
#print(f"Mi segundo libro es '{milibro2.titulo}' y fue escrito por {milibro2.autor}.")
#print(f"Mi tercer libro es '{milibro3.titulo}' y fue escrito por {milibro3.autor}.")

#cremaos catalogo para recorrer todos los libros
catalogo = [milibro, milibro2, milibro3]

for libro in catalogo:
    print(f"El libro '{libro.titulo}' fue escrito por {libro.autor}.")