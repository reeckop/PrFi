from lista_de_pacientess import mostrar_lista_pacientes

from utilerias import lista_de_pacientes
def actualizaPaciente(lista_de_pacientes): 
    mostrar_lista_pacientes(lista_de_pacientes)  #mostrar lista de pacientes 
    Num_paciente_a_actualizar=int(input("Ingrese el número del paciente: ")) #Numero de paciente que se desea modificar


    if Num_paciente_a_actualizar in lista_de_pacientes: #si el paciente si existe en la lista entonces modifica
        print(Num_paciente_a_actualizar) #lista de paciente a actulizar 
    else: #si no existe, entonces marca error y 
        print(">"*10,'Error',"<"*10)
        print("Número de paciente [no registrado], porfavor introduzca un número registrado.")
        actualizaPaciente(lista_de_pacientes)

        


