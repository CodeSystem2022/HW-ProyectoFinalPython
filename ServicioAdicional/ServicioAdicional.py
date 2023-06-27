

def servicioadicional(self):

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

                adicional = int(input())
                if adicional == 1:
                    self.viaje.setAdicional(350)
                    break
                elif adicional == 2:
                    self.viaje.setAdicional(500)
                    break
                elif adicional == 3:
                    self.viaje.setAdicional(850)
                    break
                elif adicional == 4:
                    continue
                else:
                    print("La opción ingresada es incorrecta.")
        elif opcion != 1 and opcion != 2:
            print("Los datos ingresados son incorrectos.")
            print("Por favor, intente nuevamente.")
        else:
            break
    # Mostrar pantalla: mostrará los resultados por pantalla
