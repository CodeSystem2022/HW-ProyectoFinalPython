import random
import datetime
import time
from MetodoPago import MetodoPago


def mostrar_numero_dia():
    fecha_actual = datetime.datetime.now()
    numero_dia = fecha_actual.day
    return numero_dia


class Viaje:
    def __init__(self, destino, precio, adicionales):
        self.destino = destino
        self.precio = precio
        self.adicionales = adicionales


def definirDestino():
    print("-----------------------------------------------------------")
    print("                 DESTINOS TURISTICOS SAN RAFAEL            ")
    print("-----------------------------------------------------------")
    print("                       1 - Valle Grande                    ")
    print("                       2 - Los Reyunos                     ")
    print("          3 - El Nihuil y Las Salinas del Diamante         ")
    print("                       4 - El Sosneado                     ")

    num = int(input("Seleccione el número correspondiente al destino deseado: "))

    if num == 1:
        destino = "Valle Grande"
        precio = 18000
        self.espacio()
        self.servicioAdicional()
        self.espacio()
        self.mostrarResultado(viaje)
    elif num == 2:
        destino = "Los Reyunos"
        precio = 20000
        self.espacio()
        self.servicioAdicional()
        self.espacio()
        self.mostrarResultado(viaje)
    elif num == 3:
        destino = "El Nihuil y Las Salinas del Diamante"
        precio = 25000
        self.espacio()
        self.servicioAdicional()
        self.espacio()
        self.mostrarResultado(viaje)
    elif num == 4:
        destino = "El Sosneado"
        precio = 33000
        self.espacio()
        self.servicioAdicional()
        self.espacio()
        self.mostrarResultado(viaje)
    else:
        print("El número seleccionado es incorrecto.")
        return None

    adicionales = []
    opcion_adicional = "1"

    while opcion_adicional == "1":
        opcion_adicional = input("¿Desea agregar un servicio adicional? (1-Si / 2-No): ")
        while opcion_adicional != "1" and opcion_adicional != "2":
            print("La opción ingresada es incorrecta.")
            opcion_adicional = input("¿Desea agregar un servicio adicional? (1-Si / 2-No): ")

        if opcion_adicional == "1":
            adicional = seleccionarServicioAdicional()
            adicionales.append(adicional)

    return Viaje(destino, precio, adicionales)


def seleccionarServicioAdicional():
    while True:
        print("Seleccione una opción de servicio adicional:")
        print("1 - Búsqueda por alojamiento ($1500)")
        print("2 - Vianda en destino ($1000)")
        print("3 - Guía turística ($2300)")
        print("4 - No deseo ningún adicional")

        opcion = input()

        if opcion == "1":
            return "Búsqueda por alojamiento ($1500)"
        elif opcion == "2":
            return "Vianda en destino ($1000)"
        elif opcion == "3":
            return "Guía turística ($2300)"
        elif opcion == "4":
            return ""
        else:
            print("La opción ingresada es incorrecta.")


def calcularPrecioTotal(viaje):
    precio_total = viaje.precio

    for adicional in viaje.adicionales:
        if adicional == "Búsqueda por alojamiento ($1500)":
            precio_total += 1500
        elif adicional == "Vianda en destino ($1000)":
            precio_total += 1000
        elif adicional == "Guía turística ($2300)":
            precio_total += 2300

    return precio_total


viaje = definirDestino()

if viaje:
    print("Destino seleccionado:", viaje.destino)
    print("Precio del destino: $", viaje.precio)
    print("Servicios adicionales:")
    for adicional in viaje.adicionales:
        print("-", adicional)

    precio_total = calcularPrecioTotal(viaje)
    print("Precio total del viaje:$", precio_total)
####################################################################
numero_aleatorio = random.randint(1000000000000, 9999999999999)
metodoPago = MetodoPago(0.8, 1.15, 1.25)
metodoPago.precio = precio_total

while True:
    print("..:Ingresar medio de pago:..")
    time.sleep(0.5)
    print("1. Pago contado (20% de descuento)")
    time.sleep(0.5)
    print("2. Tarjeta en 12 cuotas (15% de recargo)")
    time.sleep(0.5)
    print("3. Financiado en 6 cuotas (25% recargo)")
    time.sleep(0.5)
    Opcion = int(input("Digite una opción entre 1 y 3: "))

    if Opcion == 1:
        print(f"El precio total de contado es de: {metodoPago.precio_descuento():.2f} pesos")
        print("Generando código de pago")
        time.sleep(3)
        print(f"Su código de pago es: {numero_aleatorio}, por favor diríjase a su RapiPago más cercano para "
              f"concretar la compra")
        break
    elif Opcion == 2:
        print(f"El precio total con tarjeta es de: {metodoPago.precio_tarjeta_total():.2f} pesos")
        print(f"En doce cuotas de: {metodoPago.precio_tarjeta_cuota():.2f} pesos")
        metodoPago.nombreUsuario = input("Ingrese el nombre del titular de la tarjeta: ")
        metodoPago.numTarjeta = int(input("Digite el número de la tarjeta: "))
        metodoPago.codTarjeta = int(input("Digite el código de la tarjeta: "))
        print(f"Usted ingresó los siguientes datos: {metodoPago.__str__()}")
        while True:
            print("Desea confirmar la compra?")
            time.sleep(0.5)
            print("1.Si")
            print("2.No, salir")
            time.sleep(0.5)
            opcion2 = int(input("Ingrese una opción entre 1 y 2: "))
            if opcion2 == 1:
                print("Generando código de pago")
                time.sleep(3)
                print(f"Su código de pago es: {numero_aleatorio}")
                time.sleep(1)
                print(f"La cuota mensual será descontada el día {mostrar_numero_dia()} de cada mes")
                break
            elif opcion2 == 2:
                break
            else:
                print("Usted ingresó una opción inválida")
                print("Por favor ingrese una opción entre 1 y 2")
        break
    elif Opcion == 3:
        print(f"El precio total con el financiado de la casa es de: {metodoPago.precio_financiado_total():.2f} pesos")
        print(f"En seis cuotas de: {metodoPago.precio_financiado_cuota():.2f} pesos")
        time.sleep(0.5)
        print("Generando código de pago")
        time.sleep(3)
        print(f"Su código de pago es: {numero_aleatorio}, por favor diríjase a su RapiPago más cercano para "
              f"concretar el pago de la primera cuota")
        time.sleep(1)
        print(f"Si usted efectúa el pago hoy antes de las 20hs la cuota mensual será descontada el día "
              f"{mostrar_numero_dia()} de cada mes")
        break
    else:
        print("Usted ingresó una opción incorrecta")
        time.sleep(0.5)
        print("Por favor ingrese una opción entre 1 y 2")
