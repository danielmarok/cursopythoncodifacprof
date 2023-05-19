class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls,radio):
        return cls.pi * (radio ** 2)


resultado = Circulo.area(14)
#no necesitamos instanciar un objeto, directamente lo llamamos.
print(resultado)

