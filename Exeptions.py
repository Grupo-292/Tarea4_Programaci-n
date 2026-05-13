# =========================================================
# ARCHIVO: exceptions.py
# Sistema Integral de Gestión - Software FJ
# Manejo de excepciones personalizadas
# =========================================================


# =========================================================
# CLASE BASE DE EXCEPCIONES
# =========================================================

class SistemaError(Exception):

    """
    Clase principal de excepciones del sistema.

    Todas las excepciones personalizadas
    heredarán de esta clase.
    """

    def __init__(self, mensaje):

        self.mensaje = mensaje

        super().__init__(self.mensaje)

    # -----------------------------------------------------

    def __str__(self):

        return (
            f"[ERROR DEL SISTEMA]: "
            f"{self.mensaje}"
        )


# =========================================================
# EXCEPCIONES RELACIONADAS CON CLIENTES
# =========================================================

class ErrorCliente(SistemaError):

    """
    Maneja errores relacionados
    con los clientes.
    """

    pass


# ---------------------------------------------------------

class NombreClienteError(ErrorCliente):

    """
    Error generado cuando el nombre
    del cliente es inválido.
    """

    def __init__(self):

        super().__init__(
            "El nombre del cliente "
            "no cumple con los requisitos."
        )


# ---------------------------------------------------------

class CorreoClienteError(ErrorCliente):

    """
    Error generado cuando el correo
    electrónico es inválido.
    """

    def __init__(self):

        super().__init__(
            "El correo electrónico "
            "ingresado no es válido."
        )


# ---------------------------------------------------------

class TelefonoClienteError(ErrorCliente):

    """
    Error generado cuando el teléfono
    del cliente es incorrecto.
    """

    def __init__(self):

        super().__init__(
            "El teléfono debe contener "
            "únicamente números válidos."
        )


# =========================================================
# EXCEPCIONES RELACIONADAS CON SERVICIOS
# =========================================================

class ErrorServicio(SistemaError):

    """
    Maneja errores relacionados
    con los servicios.
    """

    pass


# ---------------------------------------------------------

class CostoServicioError(ErrorServicio):

    """
    Error cuando el costo
    del servicio es inválido.
    """

    def __init__(self):

        super().__init__(
            "El costo del servicio "
            "debe ser mayor a cero."
        )


# ---------------------------------------------------------

class ServicioNoDisponibleError(ErrorServicio):

    """
    Error cuando un servicio
    no está disponible.
    """

    def __init__(self):

        super().__init__(
            "El servicio solicitado "
            "no se encuentra disponible."
        )


# ---------------------------------------------------------

class ParametroServicioError(ErrorServicio):

    """
    Error generado por parámetros
    inválidos en un servicio.
    """

    def __init__(self):

        super().__init__(
            "Los parámetros enviados "
            "al servicio son inválidos."
        )


# =========================================================
# EXCEPCIONES RELACIONADAS CON RESERVAS
# =========================================================

class ErrorReserva(SistemaError):

    """
    Maneja errores relacionados
    con las reservas.
    """

    pass


# ---------------------------------------------------------

class DuracionReservaError(ErrorReserva):

    """
    Error cuando la duración
    de la reserva es inválida.
    """

    def __init__(self):

        super().__init__(
            "La duración de la reserva "
            "debe ser mayor a cero."
        )


# ---------------------------------------------------------

class ReservaCanceladaError(ErrorReserva):

    """
    Error cuando se intenta
    procesar una reserva cancelada.
    """

    def __init__(self):

        super().__init__(
            "No es posible procesar "
            "una reserva cancelada."
        )


# ---------------------------------------------------------

class ProcesamientoReservaError(ErrorReserva):

    """
    Error durante el procesamiento
    de una reserva.
    """

    def __init__(self):

        super().__init__(
            "Ocurrió un problema durante "
            "el procesamiento de la reserva."
        )


# =========================================================
# EXCEPCIONES RELACIONADAS CON ARCHIVOS
# =========================================================

class ErrorArchivo(SistemaError):

    """
    Maneja errores relacionados
    con archivos del sistema.
    """

    pass


# ---------------------------------------------------------

class LogError(ErrorArchivo):

    """
    Error al escribir
    en el archivo logs.
    """

    def __init__(self):

        super().__init__(
            "No fue posible registrar "
            "la información en logs.txt"
        )
