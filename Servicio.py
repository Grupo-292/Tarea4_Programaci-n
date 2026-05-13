# =========================================================
# ARCHIVO: servicio.py
# =========================================================

from abc import ABC, abstractmethod

# =========================================================
# EXCEPCIÓN PERSONALIZADA
# =========================================================

class ErrorServicio(Exception):

    pass

# =========================================================
# CLASE ABSTRACTA
# =========================================================

class Servicio(ABC):

    def __init__(
        self,
        nombre_servicio,
        costo_base
    ):

        if not nombre_servicio.strip():

            raise ErrorServicio(
                "El nombre del servicio es obligatorio."
            )

        if costo_base <= 0:

            raise ErrorServicio(
                "El costo debe ser mayor a cero."
            )

        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    # =====================================================

    @abstractmethod
    def calcular_costo(self):
        pass

    # =====================================================

    @abstractmethod
    def descripcion(self):
        pass

# =========================================================
# CLASE RESERVA SALA
# =========================================================

class ReservaSala(Servicio):

    def __init__(
        self,
        nombre_servicio,
        costo_base,
        horas
    ):

        super().__init__(
            nombre_servicio,
            costo_base
        )

        if horas <= 0:

            raise ErrorServicio(
                "Las horas deben ser válidas."
            )

        self.horas = horas

    # =====================================================

    def calcular_costo(self):

        return (
            self.costo_base *
            self.horas
        )

    # =====================================================

    def calcular_costo_descuento(
        self,
        descuento=0
    ):

        return (
            self.calcular_costo() -
            descuento
        )

    # =====================================================

    def descripcion(self):

        return (
            f"Reserva de sala por "
            f"{self.horas} horas."
        )

# =========================================================
# CLASE ALQUILER EQUIPOS
# =========================================================

class AlquilerEquipos(Servicio):

    def __init__(
        self,
        nombre_servicio,
        costo_base,
        dias
    ):

        super().__init__(
            nombre_servicio,
            costo_base
        )

        if dias <= 0:

            raise ErrorServicio(
                "Los días deben ser válidos."
            )

        self.dias = dias

    # =====================================================

    def calcular_costo(self):

        return (
            self.costo_base *
            self.dias
        )

    # =====================================================

    def descripcion(self):

        return (
            f"Alquiler de equipos "
            f"por {self.dias} días."
        )

# =========================================================
# CLASE ASESORÍA ESPECIALIZADA
# =========================================================

class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre_servicio,
        costo_base,
        nivel
    ):

        super().__init__(
            nombre_servicio,
            costo_base
        )

        self.nivel = nivel

    # =====================================================

    def calcular_costo(self):

        if self.nivel.lower() == "premium":

            return (
                self.costo_base * 2
            )

        return self.costo_base

    # =====================================================

    def descripcion(self):

        return (
            f"Asesoría especializada "
            f"nivel {self.nivel}."
        )
