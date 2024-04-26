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
                variables_submenu(macro_tuneles)
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
    while True:
        print("=== Menú Invernadero ===")
        print('1. Graficar')
        print('2. Mostrar Resultados')
        print('3. Regresar al Menu Principal')
        opcion = int(input('Ingresar Opcion: '))
        print()

        match opcion:
            case 1:
                variables_submenu(invernadero)
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
    while True:
        print("=== Menú Agua Sustratos ===")
        print('1. Graficar')
        print('2. Mostrar Resultados')
        print('3. Salir')
        opcion = int(input('Ingresar Opcion: '))
        print()

        match opcion:
            case 1:
                variables_submenu(agua_sustratos)
            case 2:
                ph = float(input('Ingrese pH: '))
                ce = float(input('Ingrese Error Conductividad: '))
                defusificar_agua_sustratos(ph, ce)
            case 3:
                break
            case _:
                print('Opcion no valida')


def variables_submenu(modulo):
    variables = list(modulo['func_membresia'].keys())
    print("=== Variables ===")
    for index, value in enumerate(variables):
        print(f'{index+1}. {value}')
    variable = int(input('Elegir Variable: '))
    print()

    match variable:
        case val if val in range(1, len(variables)+1):
            graficar_func_pertenencia(modulo, variables[variable-1])
        case _:
            print('Opción no válida')

menu_principal()