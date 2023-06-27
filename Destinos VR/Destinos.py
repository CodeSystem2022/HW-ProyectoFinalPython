class Viaje:
    def __init__(self, destino, precio, adicional):
        self.destino = destino
        self.precio = precio
        self.adicional = adicional

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
    elif num == 2:
        destino = "Los Reyunos"
        precio = 2000
    elif num == 3:
        destino = "El Nihuil y Las Salinas del Diamante"
        precio = 2500
    elif num == 4:
        destino = "El Sosneado"
        precio = 3300
    else:
        print("El número seleccionado es incorrecto.")
        return None

    return Viaje(destino, precio, "")

viaje = definirDestino()

if viaje:
    print("Destino seleccionado:", viaje.destino)
    print("Precio:", viaje.precio)


