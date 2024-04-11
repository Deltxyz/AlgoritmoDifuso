from funciones_pertenencia import macro_tuneles
from funciones_pertenencia import invernadero
from funciones_pertenencia import agua_sustratos
from mamdani import graficar_func_pertenencia
from mamdani import defusificar_macrotuneles
from mamdani import defusificar_invernadero
from mamdani import defusificar_agua_sustratos


def menu_principal():
    while True:
        print("=== Menú Principal ===")
        print('1. Modulo Control de Tuneles de Enraizamiento')
        print('2. Modulo Control de Invernadero')
        print('3. Modulo Control de Agua y Sustratos')
        print('4. Salir')
        modulo = int(input('Ingresar Opcion: '))
        print()
        match modulo:
            case 1:
                while True:
                    print("=== Menú Tuneles de Enraizamiento ===")
                    print('1. Graficar')
                    print('2. Mostrar Resultados')
                    print('3. Salir')
                    opcion = int(input('Ingresar Opcion: '))

                    match opcion:
                        case 1:
                            print("=== Variables ===")
                            print('1. Error de humedad')
                            print('2. Error de temperatura')
                            print('3. Control de estado de humedad')
                            print('4. Control de Humedad')
                            print('5. Ventilacion')
                            print('6. Sombra')
                            print('7. Salir')
                            variable = int(input('Elegir Variable: '))

                            match variable:
                                case 1:
                                    graficar_func_pertenencia(macro_tuneles, 'Error de humedad')
                                case 2:
                                    graficar_func_pertenencia(macro_tuneles, 'Error de temperatura')
                                case 3:
                                    graficar_func_pertenencia(macro_tuneles, 'Control de estado de humedad')
                                case 4:
                                    graficar_func_pertenencia(macro_tuneles, 'Control de Humedad')
                                case 5:
                                    graficar_func_pertenencia(macro_tuneles, 'Ventilacion')
                                case 6:
                                    graficar_func_pertenencia(macro_tuneles, 'Sombra')
                                case 7:
                                    break
                                case _:
                                    print('Opcion no valida')
                        case 2:
                            humedad = float(input('Ingrese Humedad: '))
                            temperatura = float(input('Ingrese Temperatura: '))
                            control_estado_humedad = float(input('Ingrese control estado humedad: '))
                            defusificar_macrotuneles(humedad, temperatura, control_estado_humedad)
                        case 3:
                            break
                        case _:
                            print('Opcion no valida')      
            
            case 2:

                while True:
                    print("=== Menú Invernadero ===")
                    print('1. Graficar')
                    print('2. Mostrar Resultados')
                    print('3. Salir')
                    opcion = int(input('Ingresar Opcion: '))
                    print()

                    match opcion:
                        case 1:
                            print("=== Variables ===")
                            print('1. Error de humedad')
                            print('2. Error de temperatura')
                            print('3. Control de estado de humedad')
                            print('4. Control de Humedad')
                            print('5. Control de Temperatura')
                            print('6. Salir')
                            variable = int(input('Elegir Variable: '))
                            print()

                            match variable:
                                case 1:
                                    graficar_func_pertenencia(invernadero, 'Error de humedad')
                                case 2:
                                    graficar_func_pertenencia(invernadero, 'Error de temperatura')
                                case 3:
                                    graficar_func_pertenencia(invernadero, 'Control de estado de humedad')
                                case 4:
                                    graficar_func_pertenencia(invernadero, 'Control de Humedad')
                                case 5:
                                    graficar_func_pertenencia(invernadero, 'Control de Temperatura')
                                case 6:
                                    break
                                case _:
                                    print('Opcion no valida')
                        case 2:
                            humedad = float(input('Ingrese Humedad: '))
                            temperatura = float(input('Ingrese Temperatura: '))
                            control_estado_humedad = float(input('Ingrese control estado humedad: '))
                            defusificar_invernadero(humedad, temperatura, control_estado_humedad)
                        case 3:
                            break
                        case _:
                            print('Opcion no valida')      

            case 3:

                while True:
                    print("=== Menú Agua Sustratos ===")
                    print('1. Graficar')
                    print('2. Mostrar Resultados')
                    print('3. Salir')
                    opcion = int(input('Ingresar Opcion: '))
                    print()

                    match opcion:
                        case 1:
                            print("=== Variables ===")
                            print('1. Error de pH')
                            print('2. Error de Conductividad')
                            print('3. Control de pH')
                            print('4. Control de CE')
                            print('5. Salir')
                            variable = int(input('Elegir Variable: '))
                            print()

                            match variable:
                                case 1:
                                    graficar_func_pertenencia(agua_sustratos, 'Error de pH')
                                case 2:
                                    graficar_func_pertenencia(agua_sustratos, 'Error de Conductividad')
                                case 3:
                                    graficar_func_pertenencia(agua_sustratos, 'Control de pH')
                                case 4:
                                    graficar_func_pertenencia(agua_sustratos, 'Control de CE')
                                case 5:
                                    break
                                case _:
                                    print('Opcion no valida')
                        case 2:
                            ph = float(input('Ingrese pH: '))
                            ce = float(input('Ingrese Error Conductividad: '))
                            defusificar_agua_sustratos(ph, ce)
                        case 3:
                            break
                        case _:
                            print('Opcion no valida')     
            case 4:
                print('Sesion Finalizada')
                break 

            #case _:
                #print ('Opcion no valida')


menu_principal()