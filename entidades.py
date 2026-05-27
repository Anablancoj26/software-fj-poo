from abc import ABC
from excepciones import ClienteError


class Entidad(ABC):

    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad


class Cliente(Entidad):

    def __init__(self, id_entidad, nombre, correo):

        super().__init__(id_entidad)

        self.nombre = nombre
        self.correo = correo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():
            raise ClienteError(
                "El nombre no puede estar vacío."
            )

        self._nombre = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):

        if "@" not in valor:
            raise ClienteError(
                "Correo inválido."
            )

        self._correo = valor

    def mostrar(self):

        return (
            f"Cliente: {self.nombre} "
            f"| Correo: {self.correo}"
        )