import logging

from entidades import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reservas import Reserva

from excepciones import (
    ClienteError,
    ServicioError,
    ReservaError
)

# ======================================
# CONFIGURACIÓN LOGS
# ======================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)

clientes = []
reservas = []

print("\n===== SOFTWARE FJ =====\n")

# ======================================
# OPERACIONES
# ======================================

operaciones = [

    ("cliente", 1, "Ana Blanco", "ana@gmail.com"),
    ("cliente", 2, "Carlos", "carlos@gmail.com"),

    # Cliente inválido
    ("cliente", 3, "", "correo"),

    # Reservas válidas
    ("reserva", 0, "sala", 3),
    ("reserva", 1, "equipo", 5),

    # Reserva inválida
    ("reserva", 0, "asesoria", -2)
]

# ======================================
# EJECUCIÓN
# ======================================

for operacion in operaciones:

    try:

        if operacion[0] == "cliente":

            _, id_cliente, nombre, correo = operacion

            cliente = Cliente(
                id_cliente,
                nombre,
                correo
            )

            clientes.append(cliente)

            print(
                cliente.mostrar()
            )

        elif operacion[0] == "reserva":

            (
                _,
                indice_cliente,
                tipo,
                horas
            ) = operacion

            cliente = clientes[indice_cliente]

            if tipo == "sala":

                servicio = ReservaSala(
                    "Sala Empresarial",
                    100
                )

            elif tipo == "equipo":

                servicio = AlquilerEquipo(
                    "Laptop",
                    80
                )

            else:

                servicio = AsesoriaEspecializada(
                    "IA",
                    200
                )

            reserva = Reserva(
                cliente,
                servicio,
                horas
            )

            print(
                reserva.confirmar()
            )

            print(
                reserva.procesar()
            )

            reservas.append(reserva)

    except (
        ClienteError,
        ServicioError,
        ReservaError
    ) as error:

        print(
            f"ERROR CONTROLADO: {error}"
        )

        logging.error(error)

    except Exception as error:

        print(
            f"ERROR GENERAL: {error}"
        )

        logging.error(error)

    finally:

        print(
            "\nOperación finalizada.\n"
        )

# ======================================
# RESUMEN
# ======================================

print("\n===== RESUMEN =====")

print(
    f"Clientes registrados: "
    f"{len(clientes)}"
)

print(
    f"Reservas realizadas: "
    f"{len(reservas)}"
)