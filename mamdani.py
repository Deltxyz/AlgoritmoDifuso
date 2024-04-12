import numpy as np #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib
import skfuzzy as fuzz # pip install scikit-fuzzy
from funciones_pertenencia import macro_tuneles
from funciones_pertenencia import invernadero
from funciones_pertenencia import agua_sustratos
import reglas

def calcular_universo_discurso(func_pertenencia):
    valores = [valor for lista_valores in func_pertenencia.values() for valor in lista_valores]
    return [min(valores), max(valores)]

# variables -> diccionario que tiene como keys los nombres de las variables
# n_variable -> nombre de la variable a usar
def graficar_func_pertenencia(variables, n_variable):
    rangos = variables['parametros'][n_variable]

    # Definir el rango de valores para el eje x
    univ = calcular_universo_discurso(rangos)
    
    x = np.linspace(univ[0], univ[1], 1000)

    plt.figure(figsize=(8, 5),num = n_variable.upper())

    for rango in rangos:
        if(len(rangos[rango]) == 3):
            variable = fuzz.trimf(x, rangos[rango])
        else:
            variable = fuzz.trapmf(x, rangos[rango])

        plt.plot(x, variable, label = variables['func_membresia'][n_variable][rango])

    plt.title(f'Funcion de Pertenencia de {n_variable}')
    plt.xlabel(n_variable)
    plt.ylabel('Pertenencia')
    plt.legend()
    plt.grid(True,linewidth=0.5, alpha=0.9)
    plt.show()


# Funciones de membresía (triangulares)
def triangular(x, rango):

    if x < rango[0]:
        return 0.0
    # rango[a] - rango[b] != 0 -> evita divisiones por 0
    if x <= rango[1] and (rango[1] - rango[0]) != 0:
        return (x - rango[0]) / (rango[1] - rango[0])

    if x <= rango[2] and (rango[2] - rango[1]) != 0:
        return (rango[2] - x) / (rango[2] - rango[1])

    return 0.0


# Funciones de membresía (trapezoidales)
def trapezoidal(x, rango):
    if x < rango[0]:
        return 0.0
    if x <= rango[1]:
        return (x - rango[0]) / (rango[1] - rango[0])
    elif x <= rango[2]:
        return 1
    elif x <= rango[3]:
        return (rango[3] - x) / (rango[3]-rango[2])
    else:
        return 0.0


def funcion_pertenencia(x, rango):
    if len(rango) ==3:
        return triangular(x, rango)
    else:
        return trapezoidal(x, rango)


#valores_entrada -> key con nombre de la variable de entrada en funciones_pertenecia
def valores_membresia(valores_entrada, valor_variable):
    valores = {}
    for key in valores_entrada:
        valores[key] = funcion_pertenencia(valor_variable, valores_entrada[key])

    return valores


def fusificar_reglas_doble(reglas, var1, var2, value1, value2):
    membresia_var1 = valores_membresia(var1, value1)
    membresia_var2 = valores_membresia(var2, value2)
    membresia_salida = {}
    
    for key1 in var1:
        for key2 in var2:

            pert_regla = min(membresia_var1[key1],membresia_var2[key2])
            if pert_regla != 0:
                membresia_salida[reglas[key1][key2]] = pert_regla
    
    return membresia_salida


def fusificar_reglas_simple(reglas, var1, value1):
    membresia_salida = {}
    membresia_var1 = valores_membresia(var1, value1)

    for key in var1:
        membresia_salida[reglas[key]] = membresia_var1[key]
    
    return membresia_salida


def calcular_centroide(pertenencia, rangos):
    total_peso = 0
    suma_centroides = 0
    
    for etiqueta, grado_pertenencia in pertenencia.items():
        rango = rangos[etiqueta]
        centro = sum(rango) / len(rango)
        
        total_peso += grado_pertenencia
        suma_centroides += centro * grado_pertenencia
    
    try:
        centroide = suma_centroides / total_peso
    except:
        return 0

    return centroide


def salida_cualitativa(func_membresia):
    print("func membresia" , func_membresia)
    max_value = max(list(func_membresia.values()))
    for clave, valor in func_membresia.items():

        if valor == max_value:
            return clave        


def defusificar_macrotuneles(humedad, temperatura, estado_control_humedad):
    control_humedad = fusificar_reglas_simple(reglas.error_humedad, macro_tuneles["parametros"]["Error de humedad"], humedad )

    estado_humedad = macro_tuneles["func_membresia"]["Control de Humedad"][salida_cualitativa(control_humedad)]
    
    print(f'Control de Humedificacion: {estado_humedad}')
    
    reglas_ventilacion = fusificar_reglas_doble(reglas.error_temperatura_ventilacion, macro_tuneles['parametros']['Control de estado de humedad'], macro_tuneles['parametros']['Error de temperatura'],estado_control_humedad,temperatura)
    reglas_sombra = fusificar_reglas_doble(reglas.error_temperatura_sombra, macro_tuneles['parametros']['Control de estado de humedad'], macro_tuneles['parametros']['Error de temperatura'],estado_control_humedad,temperatura)

    estado_ventilacion = calcular_centroide(reglas_ventilacion,macro_tuneles['parametros']['Ventilacion'])

    estado_sombra = salida_cualitativa(reglas_sombra)
    print(f'Estado Sombra: {estado_sombra}')
    print(f'Ventilacion: {round(estado_ventilacion,2)}')


def defusificar_invernadero(humedad, temperatura, estado_control_humedad):
    control_humedad = fusificar_reglas_simple(reglas.error_humedad1, invernadero["parametros"]["Error de humedad"], humedad )
    estado_humedad = calcular_centroide(control_humedad, invernadero['parametros']['Control de Humedad'])
    
    print(f'Control de Humedad: {round(estado_humedad,2)}%')
    
    reglas_temperatura = fusificar_reglas_doble(reglas.error_temperatura1, invernadero['parametros']['Control de estado de humedad'], invernadero['parametros']['Error de temperatura'],estado_control_humedad,temperatura)
    estado_temperatura = calcular_centroide(reglas_temperatura,invernadero['parametros']['Control de Temperatura'])

    print(f'Salida Temperatura: {round(estado_temperatura,2)}%')


def defusificar_agua_sustratos(error_ph, error_ce):
    control_ph = fusificar_reglas_simple(reglas.error_ph, agua_sustratos["parametros"]["Error de pH"], error_ph )
    estado_ph = calcular_centroide(control_ph, agua_sustratos['parametros']['Control de pH'])
    print(f'Control de pH: {round(estado_ph,2)}%')

    control_ce = fusificar_reglas_simple(reglas.error_ce, agua_sustratos["parametros"]["Error de Conductividad"], error_ce )
    estado_ce = calcular_centroide(control_ce, agua_sustratos['parametros']['Control de CE'])
    print(f'Control de CE: {round(estado_ce,2)}%')
