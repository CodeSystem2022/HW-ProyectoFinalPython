class Viaje:
    def __init__(self):
        self.destino = ""
        self.precio = 0

def espacio():
    print("\n\n\n\n\n\n\n\n\n\n")

def definirDestino():
    viaje = Viaje()

    while True:
        print("-----------------------------------------------------------")
        print("                 DESTINOS TURISTICOS SAN RAFAEL            ")
        print("-----------------------------------------------------------")
        print("                       1 - Valle Grande                    ")
        print("                       2 - Los Reyunos                     ")
        print("          3 - El Nihuil y Las Salinas del Diamante         ")
        print("                       4 - El Sosneado                     ")

        num = int(input())

        if num == 1:
            viaje.destino = "Valle Grande"
            viaje.precio = 2800
            print("El destino seleccionado es:", viaje.destino)
            print("Precio = $", viaje.precio)
            espacio()
            #servicioAdicional()
            espacio()
            break
        elif num == 2:
            viaje.destino = "Los Reyunos"
            viaje.precio = 2800
            print("El destino seleccionado es:", viaje.destino)
            print("Precio = $", viaje.precio)
            espacio()
            #servicioAdicional()
            espacio()
            break
        elif num == 3:
            viaje.destino = "El Nihuil y Las Salinas del Diamante"
            viaje.precio = 3500
            print("El destino seleccionado es:", viaje.destino)
            print("Precio = $", viaje.precio)
            espacio()
            #servicioAdicional()
            espacio()
            break
        elif num == 4:
            viaje.destino = "El Sosneado"
            viaje.precio = 4300
            print("El destino seleccionado es:", viaje.destino)
            print("Precio = $", viaje.precio)
            espacio()
            #servicioAdicional()
            espacio()
            break
        else:
            print("Los datos ingresados son incorrectos")
    return viaje
def main():
    definirDestino()
main()





