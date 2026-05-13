# =========================================================
# ARCHIVO: logs.py
# Sistema Integral de Gestión - Software FJ
# Registro de eventos y errores del sistema
# =========================================================

# =========================================================
# IMPORTACIÓN DE LIBRERÍAS
# =========================================================

from datetime import datetime

# =========================================================
# FUNCIÓN PRINCIPAL DE LOGS
# =========================================================

def registrar_evento(tipo, mensaje):

    """
    Registra eventos y errores
    en el archivo logs.txt
    """

    try:

        # FECHA Y HORA ACTUAL

        fecha_actual = datetime.now()

        # FORMATO DEL REGISTRO

        registro = (
            f"[{fecha_actual}] "
            f"[{tipo}] "
            f"{mensaje}\n"
        )

        # APERTURA DEL ARCHIVO

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(registro)

    except Exception as error:

        print(
            "Error al escribir "
            "en el archivo logs:"
        )

        print(error)

# =========================================================
# REGISTRO DE CLIENTES
# =========================================================

def registrar_cliente(nombre_cliente):

    """
    Registra clientes creados
    correctamente.
    """

    registrar_evento(
        "CLIENTE",
        f"Cliente registrado: "
        f"{nombre_cliente}"
    )

# =========================================================
# REGISTRO DE SERVICIOS
# =========================================================

def registrar_servicio(nombre_servicio):

    """
    Guarda servicios creados
    en el sistema.
    """

    registrar_evento(
        "SERVICIO",
        f"Servicio agregado: "
        f"{nombre_servicio}"
    )

# =========================================================
# REGISTRO DE RESERVAS
# =========================================================

def registrar_reserva(cliente, servicio):

    """
    Guarda reservas realizadas.
    """

    registrar_evento(
        "RESERVA",
        f"Reserva realizada por "
        f"{cliente} para "
        f"{servicio}"
    )

# =========================================================
# REGISTRO DE CANCELACIONES
# =========================================================

def registrar_cancelacion(cliente):

    """
    Guarda cancelaciones
    de reservas.
    """

    registrar_evento(
        "CANCELACIÓN",
        f"Reserva cancelada por "
        f"{cliente}"
    )

# =========================================================
# REGISTRO DE ERRORES
# =========================================================

def registrar_error(error):

    """
    Guarda errores generados
    durante la ejecución.
    """

    registrar_evento(
        "ERROR",
        str(error)
    )

# =========================================================
# REGISTRO DE INICIO DEL SISTEMA
# =========================================================

def iniciar_sistema():

    """
    Registra el inicio del sistema.
    """

    registrar_evento(
        "SISTEMA",
        "Inicio del sistema Software FJ"
    )

# =========================================================
# REGISTRO DE CIERRE DEL SISTEMA
# =========================================================

def cerrar_sistema():

    """
    Registra el cierre del sistema.
    """

    registrar_evento(
        "SISTEMA",
        "Cierre del sistema Software FJ"
    )

# =========================================================
# REGISTRO DE VALIDACIONES
# =========================================================

def registrar_validacion(mensaje):

    """
    Guarda validaciones exitosas.
    """

    registrar_evento(
        "VALIDACIÓN",
        mensaje
    )

# =========================================================
# REGISTRO DE PROCESAMIENTO
# =========================================================

def registrar_procesamiento(mensaje):

    """
    Guarda procesos importantes.
    """

    registrar_evento(
        "PROCESO",
        mensaje
    )

# =========================================================
# MENSAJE DE PRUEBA
# =========================================================

if __name__ == "__main__":

    iniciar_sistema()

    registrar_cliente(
        "Sara Valentina"
    )

    registrar_servicio(
        "Sala VIP"
    )

    registrar_reserva(
        "Sara Valentina",
        "Sala VIP"
    )

    registrar_validacion(
        "Datos verificados correctamente"
    )

    registrar_procesamiento(
        "Reserva procesada con éxito"
    )

    registrar_cancelacion(
        "Sara Valentina"
    )

    registrar_error(
        "Correo inválido detectado"
    )

    cerrar_sistema()

    print(
        "Archivo logs.txt "
        "actualizado correctamente."
    )
