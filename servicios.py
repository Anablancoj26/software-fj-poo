from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre, tarifa_base):

        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError(
                "Horas inválidas."
            )

        return self.tarifa_base * horas

    def descripcion(self):

        return (
            "Servicio de reserva de salas."
        )


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError(
                "Horas inválidas."
            )

        return (self.tarifa_base * horas) + 50

    def descripcion(self):

        return (
            "Servicio de alquiler de equipos."
        )


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):

        if horas <= 0:
            raise ServicioError(
                "Horas inválidas."
            )

        return (self.tarifa_base * horas) * 1.2

    def descripcion(self):

        return (
            "Servicio de asesoría especializada."
        )