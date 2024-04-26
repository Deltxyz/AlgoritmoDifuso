from funciones_pertenencia import macro_tuneles
from funciones_pertenencia import invernadero
from funciones_pertenencia import agua_sustratos
from mamdani import graficar_func_pertenencia
from mamdani import defusificar_macrotuneles
from mamdani import defusificar_invernadero
from mamdani import defusificar_agua_sustratos


def menu_principal():
    variables = {
        1: 'Modulo Control de Tuneles de Enraizamiento',
        2: 'Modulo Control de Invernadero',
        3: 'Modulo Control de Agua y Sustratos'
    }
    while True:
        print("=== Menú Principal ===")
        for key, value in variables.items():
            print(f"{key}. {value}")
        print('4. Salir')
        modulo = int(input('Ingresar Opcion: '))
        print()

        match modulo:
            case 1:
                submenu_macrotuneles()
            case 2:
                submenu_invernadero()
            case 3:
                submenu_agua_sustratos()
            case 4:
                print('Sesion Finalizada')
                break 
            case _:
                print ('Opcion no valida')


def submenu_macrotuneles():
    variables = {
        1:'Error de humedad',
        2:'Error de temperatura',
        3:'Control de estado de humedad',
        4:'Control de Humedad',
        5:'Ventilacion',
        6:'Sombra'
    }

    while True:
        print("=== Menú Tuneles de Enraizamiento ===")
        print('1. Graficar')
        print('2. Mostrar Resultados')
        print('3. Regresar al Menu Principal')
        opcion = int(input('Ingresar Opcion: '))

        match opcion:
            case 1:
                print("=== Variables ===")
                for key, value in variables.items():
                    print(f"{key}. {value}")
                print('7. Regresar al Menu de macrotuneles')
                variable = int(input('Elegir Variable: '))

                match variable:
                    case range(1,7):
                        graficar_func_pertenencia(macro_tuneles, variables[variable])
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


def submenu_invernadero():
    variables = {
        1: 'Error de humedad',
        2: 'Error de temperatura',
        3: 'Control de estado de humedad',
        4: 'Control de Humedad',
        5: 'Control de Temperatura'
    }

    while True:
        print("=== Menú Invernadero ===")
        print('1. Graficar')
        print('2. Mostrar Resultados')
        print('3. Regresar al Menu Principal')
        opcion = int(input('Ingresar Opcion: '))
        print()

        match opcion:
            case 1:
                print("=== Variables ===")
                for key, value in variables.items():
                    print(f"{key}. {value}")
                print('6. Salir')
                variable = int(input('Elegir Variable: '))
                print()

                match variable:
                    case range(1,6):
                        graficar_func_pertenencia(invernadero, variables[variable])
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


def submenu_agua_sustratos():
    variables = {
        1: 'Error de pH',
        2: 'Error de Conductividad',
        3: 'Control de pH',
        4: 'Control de CE'
    }
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
                for key, value in variables.items():
                    print(f"{key}. {value}")
                print('5. Salir')
                variable = int(input('Elegir Variable: '))
                print()

                match variable:
                    case range(1,5):
                        graficar_func_pertenencia(agua_sustratos, variables[variable])
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


menu_principal()