def saludar(username):
    mensaje = f'hola {username}' #variable local

    def mostrar_mensaje():#anidada
        print(mensaje)

    return mostrar_mensaje


username = 'cody'
respuesta = saludar(username)

username = 'no cody'
#aunque modifique username, sigue usando el anterior siendo variable global
respuesta()
