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

