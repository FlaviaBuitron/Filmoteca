from enum import Enum
class Nacionalidad:
    ESPAÑOLA = 1
    FRANCESA = 2
    INGLESA = 3
    OTRO = 4
class Actor:
    def __init__(self, nombre: str, nacionalidad: Nacionalidad = Nacionalidad.OTRO) -> None:
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        Filmoteca.actores.append(self)
class Pelicula:
    def __init__(self, titulo: str) -> None:
        self.titulo = titulo
        self.reparto: dict[str, Actor] = {}
        Filmoteca.peliculas.append(self)

class Filmoteca():
    actores:list[Actor] = []
    peliculas:list[Pelicula] = []
    def nuevo_actor(self, nombre_actor:str, nacionalidad:Nacionalidad)->None:
        nuevo = Actor(nombre_actor, nacionalidad)
        if nuevo in Filmoteca.actores:
            pass
        else:
            Filmoteca.actores.append(nuevo)
    def nueva_pelicula(self, pelicula:Pelicula)->None:
        if pelicula in Filmoteca.peliculas:
            pass
        else:
            Filmoteca.peliculas.append(pelicula)
    def nuevo_personaje(self, personaje:str, nombre_actor:str, titulo_pelicula:str)->None:
        actor_buscado = None
        for actor in Filmoteca.actores:
            if actor.nombre == nombre_actor:
                actor_buscado = actor
                break
        if actor_buscado is None:
            actor_buscado = Actor(nombre_actor, Nacionalidad.OTRO)
        peli_buscada = None
        for pelicula in Filmoteca.peliculas:
            if titulo_pelicula == pelicula.titulo:
                peli_buscada = pelicula
                break
        if peli_buscada == None:
            peli_buscada = Pelicula(titulo_pelicula)
            Filmoteca.peliculas.append(peli_buscada)
        peli_buscada.reparto[personaje]=actor_buscado
    def donde_aparece(self, busqueda_personaje:str)-> list[tuple[str, str,str]]:
        personajes_encontrados:list[tuple[str,str,str]] = []
        for peli in filmoteca.peliculas: #accedo poco a poco a personaje en pelicula
            for personaje in peli.reparto:
                if busqueda_personaje.lower() in personaje.lower():
                    actor:Actor = peli.reparto.get(personaje)
                    nombre_actor = actor.nombre
                    personajes_encontrados.append([peli.titulo, nombre_actor, personaje])
        return personajes_encontrados
    def filtra_actores(self, nacionalidades:list[Nacionalidad], pelis:list[Pelicula]=[])->list[Actor]:
        actores_enc:list[Actor]=[]
        if pelis == []:
            for peli in filmoteca.peliculas:
                for personaje in peli.reparto:
                    actor:Actor = peli.reparto.get(personaje)
                    if actor.nacionalidad in nacionalidades:
                        actores_enc.append(actor)
        else:
            for peli in filmoteca.peliculas:
                for personaje in peli.reparto:
                    actor:Actor = peli.reparto.get(personaje) 
                    if actor.nacionalidad in nacionalidades:
                        actores_enc.append(actor)
        return actores_enc
    def imprime_actores_sin_peliculas(self)->list[Actor]:
        actores_solos:list[Actor] = []
        for actor in filmoteca.actores:
            actor_encontrado = False
            for peli in filmoteca.peliculas:
                if actor in peli.reparto.values(): #busco los valores
                    actor_encontrado = True
                    break
            if actor_encontrado == False:
                actores_solos.append(actor)
        return actores_solos

                
if __name__ == '__main__':
    filmoteca = Filmoteca()
    filmoteca.nuevo_actor("Tom Hiddelson", Nacionalidad.INGLESA)
    actor1:Actor = Actor(nombre="Robert Downey Jr", nacionalidad=Nacionalidad.OTRO)
    actor2:Actor = Actor(nombre="Scarlett Johansson")
    actor3:Actor = Actor("Margot Robbie", Nacionalidad.OTRO)
    actor4:Actor = Actor("Donald Stutherland", Nacionalidad.INGLESA)
    actor5:Actor = Actor("Kit Harington", Nacionalidad.INGLESA)
    actor6:Actor = Actor("Joseph Gordon")
    actor7:Actor = Actor("George Washington", Nacionalidad.ESPAÑOLA)
    actor8:Actor = Actor("Grace Moretz", Nacionalidad.FRANCESA)
    p = Pelicula("Los Vengadores")
    p.reparto["Tony Stark"]=actor1
    p.reparto["Natasha Romanoff"]= actor2
    b = Pelicula("Barbie")
    b.reparto["Barbara"] = actor3
    p1= Pelicula("Los Juegos del Hambre")
    p1.reparto["Presi Snow"]=actor4
    p2= Pelicula("Cancion de Hielo y Fuego")
    p2.reparto["Jon Snow"]= actor5
    p3= Pelicula("Snowden")
    p3.reparto["Edward Snowden"]= actor6
    
    filmoteca.nueva_pelicula(b)
    filmoteca.nuevo_personaje("Loki", "Tom Hiddelson", "Los Vengadores")

    # for pelicula in filmoteca.peliculas:
    #     print(f"La pelicula:{pelicula.titulo} tiene como reparto:")
    #     for personaje, actor in pelicula.reparto.items():
    #         print(f"Personaje: {personaje}, Actor: {actor.nombre}")    
        
    # for actor in filmoteca.actores:
    #      print(f"Nombre:{actor.nombre}, Nacionalidad: {actor.nacionalidad}")
    # lista_snow = filmoteca.donde_aparece("snow")
    # print(lista_snow)
    actores_ingleses = filmoteca.filtra_actores([Nacionalidad.INGLESA])
    for actor in actores_ingleses:
        print(f"Nombre: {actor.nombre}, Nacionalidad: {actor.nacionalidad}")
    actores_solitos = filmoteca.imprime_actores_sin_peliculas()
    for actor in actores_solitos:
        print(f"Los actores sin pelicula son:{actor.nombre},de nacionalidad: {actor.nacionalidad}")