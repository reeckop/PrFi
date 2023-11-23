from utilerias import formatoImpresion
from utilerias import lista_de_pacientes

def agregarPaciente(lista_de_pacientes):
    
    respuesta="s"
    while respuesta.lower()=="s": #convierte en minuscula la respuesta para que no haya problema al validar
        num_paciente=int(input('\n Ingrese el número de paciente =>')) #pedimos que se ingrese el numero de paciente para darlo de alta
        
        #Aqui se recorre la lista de pacientes existentes para verificar que el numero de paciente que se quiere agregar no existe
        #En caso de que SI existe se arroja un mensaje y se vuelve a pedir el numero de paciente
        #En caso de que NO existe, se permite dar registro al paciente
        while any(num_paciente==paciente[0] in paciente for paciente in lista_de_pacientes):
            print("Este paciente ya existe")
            num_paciente=int(input('\n Ingrese el número de paciente =>'))

        print("-"*15 + 'Datos Descriptivos Paciente' +"-"*15 )
        nombre_paciente=input("Nombre: ") #Se pide el nombre del paciente
        direccion_paciente=input("Dirección: ")#Se pide la direccion
        sexo_paciente=input("Sexo: ") #Se pide el sexo
        año_nacimiento=input("Año de nacimiento: ") #se pide el año de nacimiento
        alergias_paciente=input("Alergias: ") #Se piden las alergias del paciente
        #Aqui abajo se crea una lista llamada paciente a la cual se le añaden las respuestas anteriores
        paciente=[num_paciente,nombre_paciente,direccion_paciente,sexo_paciente,año_nacimiento,alergias_paciente] 
        
        confirmacion = input("¿Confirmar el registro? (S/N)").lower()
        
        if confirmacion == "s":
            #Aqui abajo se agrega la lista del paciente a la lista de todos los demas pacientes y luego se imprime
            lista_de_pacientes.append(paciente)
            formatoImpresion(lista_de_pacientes)
            respuesta=input("\n¿Desea registrar otro paciente? => ")   
        elif confirmacion == "n":
            respuesta=input("\n¿Desea registrar otro paciente? => ")   
        else:
            #Aqui es para regresar al menu principal
            return
        
            
            