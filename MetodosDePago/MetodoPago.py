import random
import time
import datetime
import DestinosMasAdicionales


def mostrar_numero_dia():
    fecha_actual = datetime.datetime.now()
    numero_dia = fecha_actual.day
    return numero_dia


class MetodoPago:
    def __init__(self, descuento, recargo, recargo2, nombreUsuario=None, numTarjeta=None, codTarjeta=None):
        self._descuento = descuento
        self._recargo = recargo
        self._recargo2 = recargo2
        self._nombreUsuario = nombreUsuario
        self._numTarjeta = numTarjeta
        self._codTarjeta = codTarjeta

    precio = DestinosMasAdicionales.calcularPrecioTotal(DestinosMasAdicionales.viaje)

    def __str__(self):
        return f'''
                    Nombre del titular: {self._nombreUsuario},
                    Número de la tarjeta: {self._numTarjeta},
                    Código de la tarjeta: {self._codTarjeta}
                '''

    def precio_descuento(self):
        return self.precio * self._descuento

    def precio_tarjeta_total(self):
        return self.precio * self._recargo

    def precio_tarjeta_cuota(self):
        return self.precio * self._recargo / 12

    def precio_financiado_cuota(self):
        return self.precio * self._recargo2 / 6

    def precio_financiado_total(self):
        return self.precio * self._recargo2

    @property
    def descuento(self):
        return self._descuento

    @property
    def recargo(self):
        return self._recargo

    @property
    def recargo2(self):
        return self._recargo2

    @property
    def nombreUsuario(self):
        return self._nombreUsuario

    @nombreUsuario.setter
    def nombreUsuario(self, nombreUsuario):
        self._nombreUsuario = nombreUsuario

    @property
    def numTarjeta(self):
        return self._numTarjeta

    @numTarjeta.setter
    def numTarjeta(self, numTarjeta):
        self._numTarjeta = numTarjeta

    @property
    def codTarjeta(self):
        return self._codTarjeta

    @codTarjeta.setter
    def codTarjeta(self, codTarjeta):
        self._codTarjeta = codTarjeta


metodoPago = MetodoPago(0.8, 1.15, 1.25)
numero_aleatorio = random.randint(1000000000000, 9999999999999)
while True:
    time.sleep(2)
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
        print(f"Su código de pago es: {numero_aleatorio}, por favor diríjase a su   RapiPago más cercano para "
              f"concretar la compra")
        break
    elif Opcion == 2:
        time.sleep(1.5)
        print(f"El precio total con tarjeta es de: {metodoPago.precio_tarjeta_total():.2f} pesos")
        print(f"En doce cuotas de: {metodoPago.precio_tarjeta_cuota():.2f} pesos")
        metodoPago.nombreUsuario = input("Digite nombre y apellido del titular de la tarjeta: ")
        metodoPago.numTarjeta = int(input("Digite el número de la tarjeta: "))
        metodoPago.codTarjeta = int(input("Digite el código de la tarjeta: "))
        time.sleep(1)
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
