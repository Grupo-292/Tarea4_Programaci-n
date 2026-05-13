# ======================================================
# ARCHIVO: reserva.py
# Sistema de Gestión - Software FJ
# ======================================================

from datetime import datetime

# ======================================================
# EXCEPCIÓN PERSONALIZADA
# ======================================================

class ErrorReserva(Exception):

    pass


# ======================================================
# FUNCIÓN PARA LOGS
# ======================================================

def guardar_log(mensaje):

    with open(
        "logs.txt",
        "a",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            f"{datetime.now()} - "
            f"{mensaje}\n"
        )


# ======================================================
# CLASE RESERVA
# ======================================================

class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        tiempo
    ):

        if tiempo <= 0:

            raise ErrorReserva(
                "La duración de la reserva "
                "debe ser mayor a cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.tiempo = tiempo
        self.estado = "En espera"

    # --------------------------------------------------

    def confirmar_reserva(self):

        try:

            self.estado = "Confirmada"

            guardar_log(
                "Reserva confirmada."
            )

        except Exception as error:

            guardar_log(
                f"Error al confirmar: "
                f"{error}"
            )

    # --------------------------------------------------

    def cancelar_reserva(self):

        try:

            self.estado = "Cancelada"

            guardar_log(
                "Reserva cancelada."
            )

        finally:

            print(
                "Proceso terminado."
            )

    # --------------------------------------------------

    def procesar_reserva(self):

        try:

            total = (
                self.servicio
                .calcular_valor()
            )

            if total <= 0:

                raise ErrorReserva(
                    "El valor es inválido."
                )

        except Exception as error:

            guardar_log(
                f"Error de procesamiento: "
                f"{error}"
            )

            raise ErrorReserva(
                "No fue posible "
                "procesar la reserva."
            ) from error

        else:

            print(
                "\nReserva procesada "
                "correctamente."
            )

            print(
                f"Valor total: {total}"
            )
