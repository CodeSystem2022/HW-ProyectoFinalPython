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
    elif num == 2:
        destino = "Los Reyunos"
        precio = 20000
    elif num == 3:
        destino = "El Nihuil y Las Salinas del Diamante"
        precio = 25000
    elif num == 4:
        destino = "El Sosneado"
        precio = 33000
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