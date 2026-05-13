# =========================================================
# ARCHIVO PRINCIPAL
# main.py
# Sistema Integral de Gestión - Software FJ
# =========================================================

# =========================================================
# IMPORTACIÓN DE CLASES
# =========================================================

from cliente import Cliente

from servicio import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)

from reserva import Reserva

from logs import (
    iniciar_sistema,
    cerrar_sistema,
    registrar_cliente,
    registrar_servicio,
    registrar_reserva,
    registrar_cancelacion,
    registrar_error,
    registrar_procesamiento
)

# =========================================================
# INICIO DEL SISTEMA
# =========================================================

iniciar_sistema()

print(
    "\n=========================================="
)

print(
    "      SOFTWARE FJ - SISTEMA POO"
)

print(
    "=========================================="
)

# =========================================================
# LISTAS INTERNAS
# =========================================================

clientes_registrados = []

servicios_disponibles = []

reservas_realizadas = []

# =========================================================
# OPERACIÓN 1
# REGISTRO DE CLIENTE VÁLIDO
# =========================================================

try:

    cliente1 = Cliente(
        "Sara Valentina",
        "sara@gmail.com",
        "3204567890"
    )

    clientes_registrados.append(
        cliente1
    )

    registrar_cliente(
        cliente1.obtener_nombre()
    )

    print(
        cliente1.mostrar_cliente()
    )

except Exception as error:

    print(
        "\nERROR AL REGISTRAR CLIENTE:"
    )

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 2
# CLIENTE INVÁLIDO
# =========================================================

try:

    cliente_error = Cliente(
        "",
        "correoincorrecto",
        "abc"
    )

    clientes_registrados.append(
        cliente_error
    )

except Exception as error:

    print(
        "\nCLIENTE INVÁLIDO:"
    )

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 3
# CREACIÓN SERVICIO SALA
# =========================================================

try:

    sala_vip = ReservaSala(
        "Sala Ejecutiva",
        150000,
        4
    )

    servicios_disponibles.append(
        sala_vip
    )

    registrar_servicio(
        sala_vip.nombre_servicio
    )

    print(
        "\nSERVICIO REGISTRADO:"
    )

    print(
        sala_vip.descripcion()
    )

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 4
# SERVICIO ALQUILER
# =========================================================

try:

    alquiler1 = AlquilerEquipos(
        "VideoBeam HD",
        70000,
        2
    )

    servicios_disponibles.append(
        alquiler1
    )

    registrar_servicio(
        alquiler1.nombre_servicio
    )

    print(
        alquiler1.descripcion()
    )

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 5
# SERVICIO ASESORÍA
# =========================================================

try:

    asesoria1 = (
        AsesoriaEspecializada(
            "Consultoría Empresarial",
            300000,
            "Premium"
        )
    )

    servicios_disponibles.append(
        asesoria1
    )

    registrar_servicio(
        asesoria1.nombre_servicio
    )

    print(
        asesoria1.descripcion()
    )

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 6
# SERVICIO INCORRECTO
# =========================================================

try:

    servicio_error = ReservaSala(
        "",
        -500,
        0
    )

except Exception as error:

    print(
        "\nSERVICIO INVÁLIDO:"
    )

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 7
# RESERVA EXITOSA
# =========================================================

try:

    reserva1 = Reserva(
        cliente1,
        sala_vip,
        4
    )

    reservas_realizadas.append(
        reserva1
    )

    registrar_reserva(
        cliente1.obtener_nombre(),
        sala_vip.nombre_servicio
    )

    reserva1.confirmar()

    reserva1.procesar()

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 8
# RESERVA FALLIDA
# =========================================================

try:

    reserva_error = Reserva(
        cliente1,
        alquiler1,
        0
    )

except Exception as error:

    print(
        "\nRESERVA INVÁLIDA:"
    )

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 9
# CANCELACIÓN DE RESERVA
# =========================================================

try:

    reserva2 = Reserva(
        cliente1,
        asesoria1,
        1
    )

    reservas_realizadas.append(
        reserva2
    )

    reserva2.confirmar()

    reserva2.cancelar()

    registrar_cancelacion(
        cliente1.obtener_nombre()
    )

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# OPERACIÓN 10
# CÁLCULO CON DESCUENTO
# =========================================================

try:

    print(
        "\n=========================================="
    )

    print(
        "      CÁLCULO DE DESCUENTO"
    )

    print(
        "=========================================="
    )

    valor_final = (
        sala_vip
        .calcular_costo_descuento(
            50000
        )
    )

    print(
        f"Valor final: "
        f"{valor_final}"
    )

    registrar_procesamiento(
        "Descuento aplicado correctamente."
    )

except Exception as error:

    print(error)

    registrar_error(error)

# =========================================================
# RESUMEN DEL SISTEMA
# =========================================================

print(
    "\n=========================================="
)

print(
    "         RESUMEN GENERAL"
)

print(
    "=========================================="
)

print(
    f"Clientes registrados: "
    f"{len(clientes_registrados)}"
)

print(
    f"Servicios disponibles: "
    f"{len(servicios_disponibles)}"
)

print(
    f"Reservas realizadas: "
    f"{len(reservas_realizadas)}"
)

# =========================================================
# FINALIZACIÓN DEL SISTEMA
# =========================================================

cerrar_sistema()

print(
    "\n=========================================="
)

print(
    "      SISTEMA FINALIZADO"
)

print(
    "==========================================\n"
)
