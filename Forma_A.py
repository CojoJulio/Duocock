print('Serviexpress')

vehiculos_reg = []

while True: # Bucle Menu

    print('Menu\n')
    print('1. Registrar automovil')
    print('2. Registro Mantenimiento')
    print('3. Consultar automovil')
    print('4. Salir')

    try:
        opcion = int(input('Ingrese su opcion:'))

        if opcion == 1: # Registrar Automovil
            vehiculo_actual = []

            while True: # Patente
                patente = str(input('Ingrese la patente del vehiculo (AA1000/BBBB10): '))

                if len(patente) == 6: #Arreglar.
                    vehiculo_actual.append(patente)
                    break
                else:
                    print('Patente Invalida, intentelo denuevo.')

            while True: # Marca
                marca = str(input('Ingrese la marca del vehiculo: '))

                if len(marca) > 1:
                    vehiculo_actual.append(marca)
                    break
                else:
                    print('No puede dejar este campo vacio')

            while True: # Modelo
                modelo = str(input('Ingrese el modelo del Vehiculo: '))

                if len(modelo) > 1:
                    vehiculo_actual.append(modelo)
                    break
                else:
                    print('No puede dejar este campo vacio.')

            while True:
                try: # anno de fabricacion
                    anno = int(input('Ingrese el anno del vehiculo: '))

                    if anno in range(1900, 2022):
                        vehiculo_actual.append(anno)
                        break
                    else:
                        print('El anno ingresado es invalido, porfavor ingrese un anno entre 1900 y 2021')
                except ValueError:
                    print('El anno ingresado es invalido, porfavor ingrese un anno entre 1900 y 2021')

            while True:
                try: # tipo de vehiculo
                    print('Tipos de Vehiculos: Bencina, Diesel, Electrico, Hibrido')
                    tipo = str(input('\nIngrese el Tipo de vehiculo (b, d, e, h): '))
                    tipo = tipo.lower()
                    if tipo == 'b':
                        vehiculo_actual.append('Bencina')
                        break
                    elif tipo == 'd':
                        vehiculo_actual.append('Diesel')
                        break
                    elif tipo == 'e':
                        vehiculo_actual.append('Electrico')
                        break
                    elif tipo == 'h':
                        vehiculo_actual.append('Hibrido')
                        break
                except ValueError:
                    print('Tipo de vehiculo Invalido, Intentelo nuevamente')

            vehiculos_reg.append(vehiculo_actual)

        if opcion == 2: # Registro Mantenimiento
            while True:
                ver_patente = str(input('Ingrese la patente del vehiculo (*salir* para MENU): '))
                ver_patente = ver_patente.lower()

                if ver_patente == 'salir':
                    break
                elif len(ver_patente) == 6:

                    for auto in vehiculos_reg:
                        if ver_patente in auto:
                            print(auto)
                            mant = []
                            fech = str(input('Ingrese la fecha del mantenimiento: '))
                            obser = str(input('Ingrese las observaciones del vehiculo: '))
                            mant.append(fech)
                            mant.append(obser)
                            auto.append(mant)
                            break
                else:
                    print('Patente Incorrecta o no esta en el sistema')

        if opcion == 3: # Consultar Vehiculo
            while True:
                ver_patente = str(input('Ingrese la patente del vehiculo (*salir* para MENU): '))
                ver_patente = ver_patente.lower()

                if ver_patente == 'salir':
                    break
                elif len(ver_patente) == 6:

                    for auto in vehiculos_reg:
                        if ver_patente in auto:
                            for dato in auto:
                                print(dato)
                            input('*Enter* para continuar')

        if opcion == 4: # Salir
            print('Cerrando Sesion')
            break

        if opcion == 99: # Debug
            print(vehiculo_actual)
            print(vehiculos_reg)
            print('')

            for a in vehiculos_reg:
                print(a)

    except ValueError:
        print('Porfavor Ingrese un valor valido')

    if(opcion>4):
        print("Opcion elegida debe ser de 1 a 4")