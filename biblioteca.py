from exceptions import UsuarioNoEncontrado

class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.libros = []

    def buscar_usuario(self, cedula: str):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontrado(f"El usuario con la cédula {cedula} no fue encontrado.")