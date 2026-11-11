# main.py
from exceptions import UsuarioNoEncontrado
from biblioteca import Biblioteca

biblioteca = Biblioteca()
# Asignar datos iniciales creados previamente
# biblioteca.usuarios = [...]
# biblioteca.libros = [...]

print("Bienvenido a Platzi Biblioteca.")
print("Libros disponibles:")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")
print()

cedula = input("Digite el número de cédula: ")

try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"Cédula: {usuario.cedula}, Nombre: {usuario.nombre}")
except UsuarioNoEncontrado:
    print("El usuario que estás buscando no existe.")