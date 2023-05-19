def operacion(cantidad,balance,tipo='deposito'):

    def deposito(cantidad,balance):
        return cantidad + balance
    
    def retiro(cantidad,balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    

    #aca estoy en el alcance/SCOPE de operacion
    if tipo =='deposito':
        return deposito(cantidad,balance)
    
    elif tipo =='retiro':
        return retiro(cantidad,balance)


resultado = operacion(10,30)
# resultado = operacion(10,30,'retiro')  # devuelve 20
# resultado = operacion(40,30,'retiro') #devuelve None
print('Usted deposito: ',resultado)
