# from typing import List, Tuple, Any
import psycopg2 as bd


class CombiSeleccion:
    """
        Clase que representa la selección de asientos en una combi.
        Atributos:
        - combi: Número de la combi.
        - asiento: Número del asiento seleccionado.
        - nombre: Nombre del pasajero (opcional).
        - apellido: Apellido del pasajero (opcional).
        - dni: DNI del pasajero (opcional).
        - matriz: Matriz que representa el estado de los asientos en la combi.
        - fila_actual: Lista que representa la fila actual en la construcción de la matriz.
        - contador_columnas: Contador de columnas utilizado en la construcción de la matriz.
        """

    def __init__(self, combi, asiento, nombre=None, apellido=None, dni=None):
        """
        Inicializa una instancia de la clase CombiSeleccion.

        Parámetros:
            - combi: Número de la combi.
            - asiento: Número del asiento seleccionado.
            - nombre: Nombre del pasajero (opcional).
            - apellido: Apellido del pasajero (opcional).
            - dni: DNI del pasajero (opcional).
        """
        self._combi = combi
        self._asiento = asiento
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.matriz = []
        self.fila_actual = []
        self.contador_columnas = 0

    """
    Getter and Setter para el número de la combi.
    """

    @property
    def Combi(self):
        return self._combi

    @Combi.setter
    def Combi(self, combi):
        self._combi = combi

    @property
    def Asiento(self):
        return self._asiento

    @Asiento.setter
    def Asiento(self, asiento):
        self._asiento = asiento


##################################################################################################
##################################################################################################

class ServicioCombiSeleccion:
    """
    Clase que proporciona servicios relacionados con la selección y ocupación de asientos en combis.

    Atributos:
    - seleccion: Instancia de la clase CombiSeleccion utilizada para almacenar la selección actual.
    """

    seleccion = CombiSeleccion(0, 0)

    def generarMatrizCombi1(self):
        """
       Se Establece la conexión con la base de datos
       El código utiliza la biblioteca psycopg2 para establecer la conexión con una base de datos PostgreSQL
       y ejecutar consultas SQL para obtener el estado de los asientos en las combis.
        """
        conexion = bd.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='viajes_bd'
        )
        try:
            conexion.autocommit = False
            cursor = conexion.cursor()
            sentencia = "SELECT estado, id_asiento FROM combi1 ORDER BY id_asiento ASC;"
            cursor.execute(sentencia)
            resultados = cursor.fetchall()

            # Generar la matriz según los valores de la columna "estado"
            matriz = []
            fila_actual = []
            contador_columnas = 0

            for fila in resultados:
                estado = fila[0]
                id_asiento = int(fila[1])  # Convertir a entero

                if estado == "ocupado":
                    fila_actual.append("x")
                elif estado == "desocupado":
                    fila_actual.append(str(id_asiento))

                contador_columnas += 1

                if contador_columnas == 3:
                    matriz.append(fila_actual)
                    fila_actual = []
                    contador_columnas = 0

            # Imprimir la matriz
            print("Combi 1:")
            for fila in matriz:
                print(fila)
            self.matriz = matriz

            conexion.commit()  # Hacemos el commit manualmente
            print('------------------')
        except Exception as e:
            conexion.rollback()
            print(f'Ocurrio un error, se hizo un rollback: {e}')
        finally:
            conexion.close()

    def generarMatrizCombi2(self):
        # Establecer la conexión con la base de datos
        """
        Genera y muestra la matriz de asientos para la combi 1 a partir de los datos en la base de datos.
        """
        conexion = bd.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='viajes_bd'
        )
        try:
            conexion.autocommit = False
            cursor = conexion.cursor()
            sentencia = "SELECT estado, id_asiento FROM combi2 ORDER BY id_asiento ASC;"
            cursor.execute(sentencia)
            resultados = cursor.fetchall()

            # Generar la matriz según los valores de la columna "estado"
            matriz = []
            fila_actual = []
            contador_columnas = 0

            for fila in resultados:
                estado = fila[0]
                id_asiento = int(fila[1])  # Convertir a entero

                if estado == "ocupado":
                    fila_actual.append("x")
                elif estado == "desocupado":
                    fila_actual.append(str(id_asiento))

                contador_columnas += 1

                if contador_columnas == 3:
                    matriz.append(fila_actual)
                    fila_actual = []
                    contador_columnas = 0

            # Imprimir la matriz
            print("Combi 2:")
            for fila in matriz:
                print(fila)
            self.matriz = matriz

            conexion.commit()  # Hacemos el commit manualmente
            print('------------------')
        except Exception as e:
            conexion.rollback()
            print(f'Ocurrio un error, se hizo un rollback: {e}')
        finally:
            conexion.close()

    def elegirAsientoDisponible1(self):
        # Pedir al usuario que elija un asiento

        """Permite al usuario elegir un asiento disponible en la combi 1."""

        while True:
            self.seleccion.Asiento = input("Ingrese el número del asiento que desea ocupar: ")

            # Verificar si el asiento elegido está disponible
            if self.validarAsientoDisponible(self.seleccion.Asiento):
                print("El asiento está disponible. ¡Puede ocuparlo!")
                self.seleccionarAsiento1BD(self.seleccion.Asiento)
                break
            else:
                print("El asiento seleccionado no está disponible. Por favor, elija otro asiento.")

    def elegirAsientoDisponible2(self):
        # Pedir al usuario que elija un asiento
        while True:
            self.seleccion.Asiento = input("Ingrese el número del asiento que desea ocupar: ")

            # Verificar si el asiento elegido está disponible
            if self.validarAsientoDisponible(self.seleccion.Asiento):
                print("El asiento está disponible. ¡Puede ocuparlo!")
                self.seleccionarAsiento2BD(self.seleccion.Asiento)
                break
            else:
                print("El asiento seleccionado no está disponible. Por favor, elija otro asiento.")

    # Método para verificar que el asiento seleccionado
    # se encuentre disponible.
    def validarAsientoDisponible(self, seleccion):
        if self.seleccion.Asiento == 'x':
            return False

        # Verificar si el asiento está disponible en la matriz
        for fila in self.matriz:
            for valor in fila:
                if valor == self.seleccion.Asiento:
                    return True
        return False

    # Método para la selección de asiento dirigido a la base de datos viajes_db(combi1)
    def seleccionarAsiento1BD(self, seleccion):
        conexion = bd.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='viajes_bd'
        )
        # Inicia la conexión y envia una sentencia que guarda los datos del usuario.
        try:
            conexion.autocommit = False
            cursor = conexion.cursor()
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            sentencia = "UPDATE combi1 SET nombre = %s, apellido = %s, dni = %s, estado = %s WHERE id_asiento = %s "
            valores = (nombre, apellido, dni, 'ocupado', self.seleccion.Asiento)
            cursor.execute(sentencia, valores)
            conexion.commit()  # Hacemos el commit manualmente
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
            print('Termina la transacción')
        except Exception as e:
            conexion.rollback()
            print(f'Ocurrio un error, se hizo un rollback: {e}')
        finally:
            conexion.close()

    # Método para la selección de asiento dirigido a la base de datos viajes_db(combi2)
    def seleccionarAsiento2BD(self, seleccion):
        conexion = bd.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
            database='viajes_bd'
        )
        # Inicia la conexión y envia una sentencia que guarda los datos del usuario.
        try:
            conexion.autocommit = False
            cursor = conexion.cursor()
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            sentencia = "UPDATE combi2 SET nombre = %s, apellido = %s, dni = %s, estado = %s WHERE id_asiento = %s "
            valores = (nombre, apellido, dni, 'ocupado', self.seleccion.Asiento)
            cursor.execute(sentencia, valores)
            conexion.commit()  # Hacemos el commit manualmente
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')
            print('Termina la transacción')
        except Exception as e:
            conexion.rollback()
            print(f'Ocurrio un error, se hizo un rollback: {e}')
        finally:
            conexion.close()

    # Selecciona los métodos a utilizar según la combi seleccionada por el usuario.
    def seleccionFinal(self):

        while True:
            self.generarMatrizCombi1()
            self.generarMatrizCombi2()
            combi = input("Ingresa un número (1 o 2): ")

            if combi == '1':
                self.seleccion.Combi = 1
                self.generarMatrizCombi1()
                self.elegirAsientoDisponible1()
                break
            elif combi == '2':
                self.seleccion.Combi = 2
                self.generarMatrizCombi2()
                self.elegirAsientoDisponible2()
                break
            else:
                print('Ingresar un número válido')

    # retornarAsiento y retornarCombi solo retornarán los valores
    # contenidos en las propiedades asiento y combi.
    def retornaAsiento(self):
        return self.seleccion.Asiento

    def retornaCombi(self):
        return self.seleccion.Combi


##################################################################################################
##################################################################################################

"""
        Clase que contiene los atributos para poder instanciar un objeto de tipo Viaje.
        Atributos:
        - destino: se ingresará el valor del destino seleccionado.
        - precio: se ingresará el valor del  precio según el destino.
        - adicional: se ingresará el valor del los adicionales que se agreguen al viaje.
        """


class Viaje:
    def __init__(self, destino, precio, adicionales):
        self._destino = destino
        self._precio = precio
        self._adicionales = adicionales

    """
       Getter and Setter
    """

    @property
    def Destino(self):
        return self._destino

    @Destino.setter
    def Destino(self, destino):
        self._destino = destino

    @property
    def Precio(self):
        return self._precio

    @Precio.setter
    def Precio(self, precio):
        self._precio = precio

    @property
    def Adicionales(self):
        return self._adicionales

    @Adicionales.setter
    def Adicionales(self, adicionales):
        self._adicionales = adicionales

    def __str__(self):
        return (self._precio + self._adicionales)


##################################################################################################
##################################################################################################
"""
        Clase que contiene los atributos para poder instanciar un objeto de tipo servicios.
        Atributos:
        - Adicional: se podrá elegir que servicio adicional se desea
        - mostrarresultado: se mostrará el costo total del viaje sumado con el servicio adicional
"""


class Servicios:
    viaje = Viaje('', 0, 0)
    servicioCombi = ServicioCombiSeleccion()

    def nombreEmpresa(self):
        print(
            " ----    ----    --------    ----        ----          --------         -----    -----    -----     --------     ---------     ----       ----- ")
        print(
            " ----    ----    --------    ----        ----         ----------         -----   -----   -----     ----------    ----------    ----       --------")
        print(
            " ----    ----    --------    ----        ----         ----------          -----  -----  -----      ----------    ----  ----    ----       ---------")
        print(
            " ----    ----    ----        ----        ----         ----------           ----- ----- -----       ----------    ---    ---    ----       ----------")
        print(
            " ------------    ----        ----        ----         ---    ---            ---------------        ---    ---    ---    ---    ----       ---    ---")
        print(
            " ------------    --------    ----        ----         ---    ---             -------------         ---    ---    ----  ---     ----       ---    ---")
        print(
            " ------------    --------    ----        ----         ---    ---              -----------          ---    ---    --------      ----       ---    ---")
        print(
            " ------------    --------    ----        ----         ---    ---               ---------           ---    ---    ---------     ----       ---    ---")
        print(
            " ------------    ----        ----        ----         ---    ---                -------            ---    ---    ---  -----    ----       ---    ---")
        print(
            " ----    ----    ----        ----        ----         ----------                 -----             ----------    ---   ----    ----       ----------")
        print(
            " ----    ----    --------    --------    --------     ----------                  ---              ----------    ---   ----    --------   ---------")
        print(
            " ----    ----    --------    --------    --------     ----------                   -               ----------    ---   ----    --------   --------")
        print(
            " ----    ----    --------    --------    --------      --------                    -                --------     ---   ----    --------   -----")
        print("\n")
        print("\n")
        print("\n")
        print(
            "                                                **********   **********   ***    ***   **********   **********   ")
        print(
            "                                                **********   **********   ***    ***   ****  ****   ****         ")
        print(
            "                                                   ****      ***    ***   ***    ***   ****  ****   **********   ")
        print(
            "                                                   ****      ***    ***   ***    ***   **********   **********   ")
        print(
            "                                                   ****      **********   **********   ***  *****         ****   ")
        print(
            "                                                   ****      **********   **********   ***  *****   **********   ")



    def espacio(self):  """Genera espacio entre el logo y el siguiente método"""


    print("\n\n\n\n")

    """Se consulta si se desea un Servicio Adicional"""


    def servicioAdicional(self, viaje):
        opcion = 0
        while True:
            print("¿Desea agregar algún servicio adicional?")
            print("                   1-SI                 ")
            print("                   2-NO                 ")
            opcion = int(input())
            """El usuario deberá elegir una opción"""
            if opcion == 1:
                while True:
                    print("       Seleccione una opción: ")
                    print("1 - Búsqueda por alojamiento: $350")
                    print("2 - Vianda en destino: $500")
                    print("3 - Pack Souvenir: $850")
                    print("4 - No deseo ningún adicional.")

                    opcion = int(input())
                    if opcion == 1:
                        self.viaje.Adicionales = self.viaje.Adicionales + 350
                        break
                    elif opcion == 2:
                        self.viaje.Adicionales = self.viaje.Adicionales + 500
                        break
                    elif opcion == 3:
                        self.viaje.Adicionales = self.viaje.Adicionales + 850
                        break
                    elif opcion == 4:
                        continue
                    else:
                        print("La opción ingresada es incorrecta.")
            elif opcion != 1 and opcion != 2:
                print("Los datos ingresados son incorrectos.")
                print("Por favor, intente nuevamente.")
            else:
                break

        """ Mostrar pantalla: mostrará los resultados por pantalla"""

    def mostrarResultado(self, viaje):
        suma = self.viaje.Precio + self.viaje.Adicionales
        print("************************************************")
        print("El destino seleccionado es: " + self.viaje.Destino)
        print("************************************************")
        print("El precio es: $" + str(self.viaje.Precio))
        print("************************************************")
        print("El costo adicional seleccionado es: $" + str(self.viaje.Adicionales))
        print("************************************************")
        print(f"El valor total del viaje es: $" + str(suma))

    '''Damos inicio a la confirmación de compra del pasaje por porte del usuario o la opcion de volver atras, con el método comprarBoleto'''

    def comprarBoleto(self, viaje):
        self.espacio()
        print("Bienvenido al sistema de compra de pasajes")
        print(" ")
        # Usuario define si compra boleto o no
        opcion = 0
        while opcion != 1 and opcion != 2:
            print("1_ Comprar Boleto")
            print("2_ Volver")
            opcion = int(input())
        # En caso de confirmar la compra
        if opcion == 1:
            self.servicioCombi.seleccionFinal()
        else:
            self.definirDestino()

        if self.viaje.Destino == "Valle Grande":
            self.mostrarPantalla(self.viaje.Destino, 8, 8, 16, "Julio", 40, self.servicioCombi.retornaAsiento())
        elif self.viaje.Destino == "Los Reyunos":
            self.mostrarPantalla(self.viaje.Destino, 8, 9, 17, "Julio", 50, self.servicioCombi.retornaAsiento())
        elif self.viaje.Destino == "El Nihuil y Las Salinas del Diamante":
            self.mostrarPantalla(self.viaje.Destino, 8, 10, 18, "Julio", 40, self.servicioCombi.retornaAsiento())
        elif self.viaje.Destino == "El Sosneado":
            self.mostrarPantalla(self.viaje.Destino, 8, 11, 19, "Julio", 40, self.servicioCombi.retornaAsiento())  ####

    # Imprime por pantalla los datos que contiene el boleto de compra
    def mostrarPantalla(self, viaje, horarioSalida, horarioLlegada, dia, mes, duracion, serrvicioCombi):
        print("")
        print("")
        print("\t\t\t\t\t\tOpción: ")
        print("\t\t\t\t\t\t" + self.viaje.Destino + " ")
        print("\t\t\t\t\tINFORMACION DEL TUR: ")
        print("\t\t\t--------------------------------------------------")
        print("\t\t\t\t\tDestino:   " + self.viaje.Destino + " ")
        print("\t\t\t\t\tCombi: Combi Nº" + str(self.servicioCombi.retornaCombi()) + " ")
        print("\t\t\t\t\tAsiento:    " + str(self.servicioCombi.retornaAsiento()) + " ")
        print("\t\t\t---------------------------------------------------")
        print("\t\t\t   --------------------     -------------------- ")
        print("\t\t\t\t  SALIDA                   LLEGADA")
        print("\t\t\t  Lunes " + str(dia) + " de " + mes + "             Lunes " + str(dia) + " de " + mes + " ")
        print("\t\t\t\t" + str(horarioSalida) + ":00    hs               " + str(horarioLlegada) + ":" + str(
            duracion) + "   hs ")
        print("\t\t\t   --------------------     -------------------- ")
        print("\t\t\t\t   [Duración Viaje:" + str(duracion) + " min.] ")
        print("\t\t\t\t     Precio: $ " + str(self.viaje.Precio + self.viaje.Adicionales))
        print("")

    def metodoDePago(self):
        opcionDePago = 0

        while opcionDePago not in [1, 2, 3]:  # Ciclo While. Muestra el menú hasta que se coloque una opción correcta
            print("..:Ingresar medio de pago:..")
            print("1. Pago contado (20% de descuento)")
            print("2. Tarjeta en 12 cuotas (15% de recargo)")
            print("3. Financiado en 6 cuotas (25% recargo)")
            opcionDePago = int(input("Digite una opción entre 1 y 3: "))
            # Cálculo de precio total con descuento del 20%
            if opcionDePago == 1:
                print("El precio total de contado es:", (self.viaje.Precio + self.viaje.Adicionales) * 0.8,
                      "pesos")
            # Cálculo de precio total con recargo del 15%
            elif opcionDePago == 2:
                precioTotal = (self.viaje.Precio + self.viaje.Adicionales) * 1.15
                print(f"El precio total con tarjeta es: {precioTotal:.2f} pesos")
                print(f"Seis cuotas de {precioTotal / 6:.2f} pesos")
                self.espacio()
                self.opcionTarjeta()
            # Cálculo de precio total con financiado de la casa con recargo del 25%
            elif opcionDePago == 3:
                precioTotal = (self.viaje.Precio + self.viaje.Adicionales) * 1.25
                print(f"El precio total con financiado de la casa es: {precioTotal:.2f} pesos")
                print(f"Doce cuotas de {precioTotal / 12:.2f} pesos")
            # Mensaje en caso de que la opcion ingresada no sea 1, 2 o 3
            else:
                print("|---------------------|")
                print("|Número fuera de rango|")
                print("|---------------------|")

        self.espacio()
        self.compraExitosa()

    def opcionTarjeta(self):  # Método para que el usuario ingrese los datos de su tarjeta para realizar el pago
        titular = ""

        # Se solicitan los datos
        print("Ingrese el nombre completo del titular de la tarjeta: ")
        while len(titular) < 3:
            titular = input()

        print("Ingrese el número de la tarjeta: ")
        numeroTarjeta = input()

        print("Ingrese el CV de la tarjeta: ")
        numeroCV = int(input())
        # Se muestran los datos ingresados en pantalla
        print("Sus datos son: Titular:", titular + ", Número de tarjeta:", numeroTarjeta + ", CV de la tarjeta:",
              numeroCV)

    def compraExitosa(self):  # Mensaje de confirmación de compra
        print("Tú compra fue un éxito.")
        print("Esperamos disfrutes tú viaje.")

    ###########
    # Este metodo permite al usuario seleccionar un destino turistico
    # Metodo dentro de la clase Servicios
    def definirDestino(self):
        # Se utiliza un bucle While True para mantener al usuario en el menù
        # hasta que ingrese una opcion valida
        while True:
            print("-----------------------------------------------------------")
            print("|              DESTINOS TURISTICOS SAN RAFAEL              |")
            print("-----------------------------------------------------------")
            print("|   Opción   |           Destino             |   Precio    |")
            print("-----------------------------------------------------------")
            print("|     1      |         Valle Grande          |    2800     |")
            print("|     2      |         Los Reyunos           |    3200     |")
            print("|     3      |  El Nihuil y Las Salinas del  |    3500     |")
            print("|            |          Diamante             |             |")
            print("|     4      |         El Sosneado           |    4300     |")
            print("-----------------------------------------------------------")
            # menù de Destinos turisticos
            num = int(input("Seleccione el número correspondiente al destino deseado: "))
            # seleccion de el número que elige el usuario.
            if num == 1:
                self.viaje.Destino = "Valle Grande"
                self.viaje.Precio = 2800
                print("El destino seleccionado es:", self.viaje.Destino)
                print("Precio = $", self.viaje.Precio)
                self.espacio()
                self.servicioAdicional(self.viaje)
                self.espacio()
                self.mostrarResultado(self.viaje)
                break
            elif num == 2:
                self.viaje.Destino = "Los Reyunos"
                self.viaje.Precio = 3200
                print("El destino seleccionado es:", self.viaje.Destino)
                print("Precio = $", self.viaje.Precio)
                self.espacio()
                self.servicioAdicional(self.viaje)
                self.espacio()
                self.mostrarResultado(self.viaje)
                break
            elif num == 3:
                self.viaje.Destino = "El Nuhuil y Las Salinas del Diamante"
                self.viaje.Precio = 3500
                print("El destino seleccionado es:", self.viaje.Destino)
                print("Precio = $", self.viaje.Precio)
                self.espacio()
                self.servicioAdicional(self.viaje)
                self.espacio()
                self.mostrarResultado(self.viaje)
                break
            elif num == 4:
                self.viaje.Destino = "El Sosneado"
                self.viaje.Precio = 4300
                print("El destino seleccionado es:", self.viaje.Destino)
                print("Precio = $", self.viaje.Precio)
                self.espacio()
                self.servicioAdicional(self.viaje)
                self.espacio()
                self.mostrarResultado(self.viaje)
                # caso que elija una de las 4 opciones mostrara el resultado
                # del destino seleccionado y el precio.
                break
            else:
                print("Los datos ingresados son incorrectos")
            # Fin de la Estructura Condicional
        # return viaje
        self.comprarBoleto(self.viaje)
        self.espacio()
        self.metodoDePago()



eleccion = Servicios()
eleccion.nombreEmpresa()
eleccion.espacio()
eleccion.definirDestino()
