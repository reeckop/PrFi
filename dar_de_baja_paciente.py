from utilerias import lista_de_pacientes

def darDeBajaPaciente(lista_de_pacientes):
    print("                         Listado de Pacientes")
    print("-----------------------------------------------------------------------------")
    print("Número   Nombre       Dirección      Sexo        Año Nacimiento      Alergias")
    print("-----------------------------------------------------------------------------")
    
    for paciente in lista_de_pacientes:
        print(f"  {paciente[0]}    {paciente[1]}    {paciente[2]} {paciente[3]} {paciente[4]}                {paciente[5]}")

    print("-----------------------------------------------------------------------------")
    print(f"Total, de Pacientes: {len(lista_de_pacientes)}")

    