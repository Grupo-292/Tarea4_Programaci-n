# ======================================================
# ARCHIVO: servicio.py
# Sistema de Gestión - Software FJ
# ======================================================

from abc import ABC, abstractmethod

# ======================================================
# EXCEPCIÓN PERSONALIZADA
# ======================================================

class ErrorServicio(Exception):

    """
    Controla errores relacionados
    con los servicios.
    """

    pass


# ======================================================
# CLASE ABSTRACTA SERVICIO
# ======================================================

class Servicio(ABC):

    """
    Clase abstracta base para todos
    los servicios del sistema.
    """

    def __init__(
        self,
        nombre_servicio,
        tarifa_base
    ):

        if tarifa_base <= 0:

            raise ErrorServicio(
                "La tarifa debe ser mayor a cero."
            )

        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base

    # ----------------------------------------------

    @abstractmethod
    def calcular_valor(self):
        pass

    # ----------------------------------------------

    @abstractmethod
    def detalle_servicio(self):
        pass


# ======================================================
# SERVICIO: RESERVA DE SALAS
# ======================================================

class SalaReuniones(Servicio):

    def __init__(
        self,
        nombre_servicio,
        tarifa_base,
        cantidad_horas
    ):

        super().__init__(
            nombre_servicio,
            tarifa_base
        )

        if cantidad_horas <= 0:

            raise ErrorServicio(
                "Las horas deben ser válidas."
            )

        self.cantidad_horas = cantidad_horas

    # ----------------------------------------------

    def calcular_valor(self):

        return (
            self.tarifa_base *
            self.cantidad_horas
        )

    # ----------------------------------------------
    # MÉTODO SOBRECARGADO
    # ----------------------------------------------

    def calcular_valor_descuento(
        self,
        descuento=0
    ):

        return (
            self.calcular_valor() -
            descuento
        )

    # ----------------------------------------------

    def detalle_servicio(self):

        return (
            f"Sala reservada por "
            f"{self.cantidad_horas} horas."
        )


# ======================================================
# SERVICIO: ALQUILER DE EQUIPOS
# ======================================================

class EquiposTecnologia(Servicio):

    def __init__(
        self,
        nombre_servicio,
        tarifa_base,
        dias_alquiler
    ):

        super().__init__(
            nombre_servicio,
            tarifa_base
        )

        if dias_alquiler <= 0:

            raise ErrorServicio(
                "Los días son inválidos."
            )

        self.dias_alquiler = dias_alquiler

    # ----------------------------------------------

    def calcular_valor(self):

        return (
            self.tarifa_base *
            self.dias_alquiler
        )

    # ----------------------------------------------

    def detalle_servicio(self):

        return (
            f"Equipo alquilado por "
            f"{self.dias_alquiler} días."
        )


# ======================================================
# SERVICIO: ASESORÍAS
# ======================================================

class Consultoria(Servicio):

    def __init__(
        self,
        nombre_servicio,
        tarifa_base,
        categoria
    ):

        super().__init__(
            nombre_servicio,
            tarifa_base
        )

        self.categoria = categoria

    # ----------------------------------------------

    def calcular_valor(self):

        if self.categoria.lower() == "vip":

            return self.tarifa_base * 2

        return self.tarifa_base

    # ----------------------------------------------

    def detalle_servicio(self):

        return (
            f"Asesoría tipo "
            f"{self.categoria}"
        )
