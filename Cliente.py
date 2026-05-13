# ======================================================
# ARCHIVO: cliente.py
# Sistema de Gestión - Software FJ
# ======================================================

# ======================================================
# EXCEPCIÓN PERSONALIZADA
# ======================================================

class ErrorCliente(Exception):

    """
    Clase para controlar errores relacionados
    con los clientes del sistema.
    """

    pass


# ======================================================
# CLASE CLIENTE
# ======================================================

class Cliente:

    """
    Clase encargada de almacenar y validar
    la información de los clientes.
    """

    # --------------------------------------------------
    # MÉTODO CONSTRUCTOR
    # --------------------------------------------------

    def __init__(
        self,
        nombre_completo,
        correo,
        telefono
    ):

        # VALIDAR NOMBRE

        if len(nombre_completo.strip()) < 3:

            raise ErrorCliente(
                "El nombre debe tener mínimo 3 caracteres."
            )

        # VALIDAR CORREO

        if "@" not in correo or "." not in correo:

            raise ErrorCliente(
                "Debe ingresar un correo válido."
            )

        # VALIDAR TELÉFONO

        if not telefono.isnumeric():

            raise ErrorCliente(
                "El teléfono solo debe contener números."
            )

        if len(telefono) != 10:

            raise ErrorCliente(
                "El teléfono debe tener 10 dígitos."
            )

        # ATRIBUTOS PRIVADOS

        self.__nombre_completo = nombre_completo
        self.__correo = correo
        self.__telefono = telefono

    # --------------------------------------------------
    # OBTENER NOMBRE
    # --------------------------------------------------

    def obtener_nombre(self):

        return self.__nombre_completo

    # --------------------------------------------------
    # OBTENER CORREO
    # --------------------------------------------------

    def obtener_correo(self):

        return self.__correo

    # --------------------------------------------------
    # OBTENER TELÉFONO
    # --------------------------------------------------

    def obtener_telefono(self):

        return self.__telefono

    # --------------------------------------------------
    # ACTUALIZAR TELÉFONO
    # --------------------------------------------------

    def actualizar_telefono(
        self,
        nuevo_telefono
    ):

        if not nuevo_telefono.isnumeric():

            raise ErrorCliente(
                "El nuevo teléfono es inválido."
            )

        self.__telefono = nuevo_telefono

    # --------------------------------------------------
    # MOSTRAR INFORMACIÓN
    # --------------------------------------------------

    def mostrar_informacion(self):

        return (

            f"\nCLIENTE REGISTRADO\n"
            f"Nombre: {self.__nombre_completo}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"

        )
