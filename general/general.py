# from typing import List, Tuple, Any
import psycopg2 as bd


class CombiSeleccion:
    def __init__(self):
        # self.combi = combi
        self.asiento = 0
        self.nombre = ''
        self.apellido = ''
        self.dni = 0
        self.matriz = []
        self.fila_actual = []
        self.contador_columnas = 0

    def generarMatrizCombi1(self):
        # Establecer la conexión con la base de datos
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
        while True:
            asiento = input("Ingrese el número del asiento que desea ocupar: ")

            # Verificar si el asiento elegido está disponible
            if self.validarAsientoDisponible(asiento):
                print("El asiento está disponible. ¡Puede ocuparlo!")
                self.seleccionarAsiento1BD(asiento)
                break
            else:
                print("El asiento seleccionado no está disponible. Por favor, elija otro asiento.")

    def elegirAsientoDisponible2(self):
        # Pedir al usuario que elija un asiento
        while True:
            asiento = input("Ingrese el número del asiento que desea ocupar: ")

            # Verificar si el asiento elegido está disponible
            if self.validarAsientoDisponible(asiento):
                print("El asiento está disponible. ¡Puede ocuparlo!")
                self.seleccionarAsiento2BD(asiento)
                break
            else:
                print("El asiento seleccionado no está disponible. Por favor, elija otro asiento.")

    def validarAsientoDisponible(self, asiento):
        if asiento == 'x':
            return False

        # Validar si el asiento está disponible en la matriz
        for fila in self.matriz:
            for valor in fila:
                if valor == asiento:
                    return True
        return False

    def seleccionarAsiento1BD(self, asiento):
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
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            sentencia = "UPDATE combi1 SET nombre = %s, apellido = %s, dni = %s, estado = %s WHERE id_asiento = %s "
            valores = (nombre, apellido, dni, 'ocupado', asiento)
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

    def seleccionarAsiento2BD(self, asiento):
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
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            # asiento = input("Ingrese el número de asiento: ")
            sentencia = "UPDATE combi2 SET nombre = %s, apellido = %s, dni = %s, estado = %s WHERE id_asiento = %s "
            valores = (nombre, apellido, dni, 'ocupado', asiento)
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

    def seleccionFinal(self):

        while True:
            self.generarMatrizCombi1()
            self.generarMatrizCombi2()
            combi = input("Ingresa un número (1 o 2): ")

            if combi == '1':
                self.generarMatrizCombi1()
                self.elegirAsientoDisponible1()
                break
            elif combi == '2':
                self.generarMatrizCombi2()
                self.elegirAsientoDisponible2()
                break
            else:
                print('Ingresar un número válido')




#######################################################################
#######################################################################

class Viaje:
    def __init__(self, destino=None, precio=None, adicionales=None):
        self.destino = destino
        self.precio = precio
        self.adicionales = adicionales

    asientoCombi = CombiSeleccion()

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

        if viaje:
            print("Destino seleccionado:", viaje.destino)
            print("Precio del destino: $", viaje.precio)
            print("Servicios adicionales:")
            for adicional in viaje.adicionales:
                print("-", adicional)

            precio_total = calcularPrecioTotal(viaje)
            print("Precio total del viaje:$", precio_total)

    def seleccionarServicioAdicional(self):
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

    def espacio(self):
        print("\n\n\n\n\n\n\n\n")

    def definirDestino(self):
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
            self.seleccionarServicioAdicional()
            self.espacio()
            self.calcularPrecioTotal(viaje)
            self.espacio()
            self.asientoCombi.seleccionFinal()
        elif num == 2:
            destino = "Los Reyunos"
            precio = 20000
            self.espacio()
            self.seleccionarServicioAdicional()
            self.espacio()
            self.calcularPrecioTotal(viaje)
            self.espacio()
            self.asientoCombi.seleccionFinal()
        elif num == 3:
            destino = "El Nihuil y Las Salinas del Diamante"
            precio = 25000
            self.espacio()
            self.seleccionarServicioAdicional()
            self.espacio()
            self.calcularPrecioTotal(viaje)
            self.espacio()
            self.asientoCombi.seleccionFinal()
        elif num == 4:
            destino = "El Sosneado"
            precio = 33000
            self.espacio()
            self.seleccionarServicioAdicional()
            self.espacio()
            self.calcularPrecioTotal()
            self.espacio()
            self.asientoCombi.seleccionFinal()
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
                adicional = self.seleccionarServicioAdicional()
                adicionales.append(adicional)

        return Viaje(destino, precio, adicionales)




########################################################################################
########################################################################################
class Servicios:

    seleccion = CombiSeleccion()



    def servicioAdicional(self):
        opcion = 0
        while True:
            print("¿Desea agregar algún servicio adicional?")
            print("                   1-SI                 ")
            print("                   2-NO                 ")
            opcion = int(input())
            if opcion == 1:
                while True:
                    print("       Seleccione una opción: ")
                    print("1 - Busqueda por alojamiento: $350")
                    print("2 - Vianda en destino: $500")
                    print("3 - Pack Souvenir: $850")
                    print("4 - No deseo ningún adicional.")

                    opcion = int(input())
                    if opcion == 1:
                        viaje.adicional=350
                        break
                    elif opcion == 2:
                        viaje.adicional=500
                        break
                    elif opcion == 3:
                        viaje.adicional=850
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
            # Mostrar pantalla: mostrará los resultados por pantalla

    '''def mostrarResultado(self, viaje):
        suma = precio + adicional
        print("************************************************")
        print("El destino seleccionado es: " + viaje.destino)
        print("************************************************")
        print("El precio es: $" + str(viaje.precio))
        print("************************************************")
        print("El costo adicional seleccionado es: $" + str(viaje.adicional))
        print("************************************************")
        print("El valor total del viaje es: $" + str(suma))'''

    def comprarBoleto(self): #Analizar
        self.espacio()
        print("Bienvenido al sistema de compra de pasajes")
        print(" ")

        opcion = 0
        while opcion != 1 and opcion != 2:
            print("1_ Comprar Boleto")
            print("2_ Volver")
            opcion = int(input())
        if opcion == 1:
            self.seleccion.seleccionFinal()
        else:
            self.definirDestino()

        if self.destinoSeleccionado == 1:
            self.mostrarPantalla(self.viaje, 8, 8, 16, "Mayo", 40)
        elif self.destinoSeleccionado == 2:
            self.mostrarPantalla(self.viaje, 8, 9, 17, "Mayo", 50)
        elif self.destinoSeleccionado == 3:
            self.mostrarPantalla(self.viaje, 8, 10, 18, "Junio", 40)
        elif self.destinoSeleccionado == 4:
            self.mostrarPantalla(self.viaje, 8, 11, 19, "Julio", 40)

    def seleccionarServicioAdicional(self):
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

        if viaje:
            print("Destino seleccionado:", viaje.destino)
            print("Precio del destino: $", viaje.precio)
            print("Servicios adicionales:")
            for adicional in viaje.adicionales:
                print("-", adicional)

            precio_total = calcularPrecioTotal(viaje)
            print("Precio total del viaje:$", precio_total)





    def definirDestino(self):

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
                adicional = self.servicioAdicional()
                adicionales.append(adicional)

        return Viaje(destino, precio, adicionales)






        #self.comprarBoleto()




viaje = Viaje()
viaje.definirDestino()
