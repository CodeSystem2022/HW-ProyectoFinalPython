# from typing import List, Tuple, Any
import psycopg2 as bd
import pyfiglet

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

#######################################################################
#######################################################################

class ServicioCombiSeleccion:
    """
    Clase que proporciona servicios relacionados con la selección y ocupación de asientos en combis.

    Atributos:
    - seleccion: Instancia de la clase CombiSeleccion utilizada para almacenar la selección actual.
    """

    seleccion = CombiSeleccion(0,0)

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
        """
        Permite al usuario elegir un asiento disponible en la combi 1.
        """
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

    #Método para la selección de asiento dirigido a la base de datos viajes_db(combi1)
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

#######################################################################
#######################################################################

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
############################################################
############################################################
"""
        Clase que contiene los atributos para poder instanciar un objeto de tipo servicios.
        Atributos:
        - Adicional: se podrá elegir que servicio adicional se desea
        - mostrarresultado: se mostrará el costo total del viaje sumado con el servicio adicional
"""
class Servicios:
    viaje = Viaje('', 0, 0)
    servicioCombi = ServicioCombiSeleccion()

   def nombreEmpresa(self): """Esto muestra Logo del proyecto"""
    print(pyfiglet.figlet_format("Hello World \n TOURS"))

   def espacio(self):  """Genera espacio entre el logo y el siguiente método"""
    print("\n\n\n\n")

  """Se consulta si se desea un Servicio Adicional"""
   def servicioAdicional(self, viaje):
    opcion = 0
    while True:
        print("¿Desea agregar algún servicio adicional?")
        print("                   1-SI                 ")
        print("                   2-NO                 ")
        opcion = int(input()) """El usuario deberá elegir una opción"""
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
