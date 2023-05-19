def saludar():

    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de python')
    
    return mostrar_mensaje

respuesta = saludar()
#almacenamos la funcion en una variable

respuesta()
#para que podamos llamar la funcion atraves de la variable, colocamos variable+()
