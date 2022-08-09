opcion = ""

while(opcion != "4"):
    
    print("\n***** Bienvenido a la practica #1. *****"+
            "\n\t1. Cargar archivo de entrada"+
            "\n\t2. Gestionar Cursos"+
            "\n\t3. Conteo de Creditos"+
            "\n\t4. Salir\n")     
    opcion = input("Ingrese el numero de opcion que desea: ")

    if opcion == "1":
        print("\nPor favor ingrese la ruta del archivo con extension .csv")
        #Logica de cargar archivo
        
    elif opcion == "2":
        print("\nGracias por seleccionar seleccionar la opcion \"Gestionar Cursos\"")
        #Logica para gestionar cursos

    elif opcion == "3":
        print("\nGracias por elegir la opcion \"Conteo de creditos\" ")
        #Logica para el conteo de creditos

    elif opcion ==  "4":
        print("\nSaliendo del programa..........")
    else:
        print("\nLa opcion elegida es invalida, intente nuevamente")
 