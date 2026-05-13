# =========================================================
# ARCHIVO: reserva.py
# =========================================================

class ErrorReserva(Exception):

    pass

# =========================================================
# CLASE RESERVA
# =========================================================

class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        if duracion <= 0:

            raise ErrorReserva(
                "La duración de la reserva debe ser mayor a cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    # =====================================================

    def confirmar(self):

        self.estado = "Confirmada"

        print(
            "\nReserva confirmada correctamente."
        )

    # =====================================================

    def cancelar(self):

        self.estado = "Cancelada"

        print(
            "\nReserva cancelada."
        )

    # =====================================================

    def procesar(self):

        total = (
            self.servicio
            .calcular_costo()
        )

        print(
            f"\nCosto total: {total}"
        )
