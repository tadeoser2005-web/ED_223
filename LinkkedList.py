class Cancion:
    def __init__(self,titulo):
        self.titulo = titulo
        self.siguiente = None

cancion1 = Cancion("Suave - Luis Miguel")
cancion2 = Cancion("Quiero ver - Cafe Tacvba")
cancion3 = Cancion("Disfraces - Luis Miguel")
cancion4 = Cancion("Azul - Zoe")
cancion5 = Cancion("Crimen - Gustavo Cerati")


cancion1.siguiente = cancion2
cancion2.siguiente = cancion3
cancion3.siguiente = cancion4
cancion4.siguiente = cancion5

print("Iniciando reproductor de musica.....\n")

cancion_actual = cancion1

while cancion_actual != None:
    print("Reproduciendo: ", cancion_actual.titulo)
    cancion_actual = cancion_actual.siguiente
    

print("\n Fin de la playlist")