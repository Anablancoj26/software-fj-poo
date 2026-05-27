from excepciones import ReservaError


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        horas
    ):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        try:

            if self.horas <= 0:

                raise ReservaError(
                    "La reserva debe tener horas válidas."
                )

            self.estado = "Confirmada"

            return (
                f"Reserva confirmada para "
                f"{self.cliente.nombre}"
            )

        except ReservaError:
            raise

    def cancelar(self):

        self.estado = "Cancelada"

        return "Reserva cancelada."

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo(
                self.horas
            )

            return (
                f"Costo total: ${costo}"
            )

        except Exception as error:

            raise ReservaError(
                "Error procesando reserva."
            ) from error