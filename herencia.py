class Mascota:#clase padre
    
    def comer(self):
        print('la mascota come')
    
    def dormir(self):
        print('la mascota duerme')


class Perro(Mascota):#Clase hija
    #ACA ESTOY APLICANDO HERENCIA-> PERRO HEREDA A MASCOTA
    pass

class Gato(Mascota):
    pass

duke = Perro()

duke.comer()
duke.dormir()

pandi = Gato()
pandi.comer()
pandi.dormir()
