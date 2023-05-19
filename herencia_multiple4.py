class Animal():#Clase Padre del padre, Abuelo

    def comer(self):#hice la prueba y sin poner self igual funka
        print('El animal come')
    
    def dormir(self):
        print('El animal duerme')#hice la prueba y sin poner self igual funka, no se porque?!


class Mascota(Animal):#clase padre
    
    def comer(self):
        print('La mascota come')


class Felino:

    def cazar(self):
        print('El felino caza')


class Gato(Mascota,Felino):#Clase hija
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        super().comer()#ACA ESTOY LLAMANDO A METODO DE CLASE PADRE
        print(f'{self.nombre} come')
    

tutuca = Gato('Tutuca')
tutuca.comer()
tutuca.dormir()