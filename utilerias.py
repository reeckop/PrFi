#Lista de pacientes para tener algo con lo que trabajar y no estar metiendo datos a cada rato
lista_de_pacientes=[
        [1, "Juan López", "Colima #4", "M", "1967", "Penicilina"],
        [2, "Ana Juárez", "Del Río #8", "F", "1983", "Ninguna"],
        [3, "María Gómez", "Tímuris #7", "F", "2001", "Polen"],
    ]

#Funcion que imprime con formato, nomas la importan a donde deseen usarla, le pasan el parametro que que deseen imprimir. Aun no se si sirva de algo  pero ahi ta
def formatoImpresion(lista_de_pacientes):
    print("Listado de Pacientes".center(80))
    print("-" * 120)
    print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format("Número", "Nombre", "Dirección", "Sexo", "Año de nacimiento", "Alergias"))
    print("-" * 120)

    for paciente in lista_de_pacientes:
        print("{:<10} {:<30}{:<25} {:<5} {:<20} {:<20}".format(paciente[0], paciente[1], paciente[2], paciente[3], paciente[4], paciente[5]))

    print("-" * 120)
    print(f"Total de Pacientes: {len(lista_de_pacientes)}")
