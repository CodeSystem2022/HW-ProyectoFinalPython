import datetime


def mostrar_numero_dia():
    fecha_actual = datetime.datetime.now()
    numero_dia = fecha_actual.day
    return numero_dia


class MetodoPago:
    def __init__(self, descuento, recargo, recargo2, nombreUsuario=None, numTarjeta=None, codTarjeta=None, precio=None):
        self._descuento = descuento
        self._recargo = recargo
        self._recargo2 = recargo2
        self._nombreUsuario = nombreUsuario
        self._numTarjeta = numTarjeta
        self._codTarjeta = codTarjeta
        self.precio = precio

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


