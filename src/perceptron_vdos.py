import numpy as np
# import matplotlib.pyplot as plt


personas = np.array([[0.3, 0.4], [0.4, 0.3],
                     [0.3, 0.2], [0.4, 0.1], 
                     [0.5, 0.2], [0.4, 0.8],
                     [0.6, 0.8], [0.5, 0.6], 
                     [0.7, 0.6], [0.8, 0.5]])


clases = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


# Función de activación para el Perceptron
# Por la teoría sabemos que los pesos se deben de multiplicar
# por sus respectivas entradas de datos a los que pertenecen,
# es decir, tenemos que hacer lo siguiente:
#
# w1*x1 + w2*x2 + ... + wn*xn

def funcion_activacion(pesos, x, umbral):
    operacion_z = pesos * x
    if (operacion_z.sum() + umbral > 0):
        return 1
    else:
        return 0


def entrenamiento(epocas, rango_de_aprendizaje, pesos, umbral):
    for epoca in range(epocas):
        error_total = 0
        for indice in range(len(personas)):
            prediccion = funcion_activacion(pesos, personas[indice], umbral)
            error = clases[indice] - prediccion

            error_total += (error**2)
            pesos[0] += rango_de_aprendizaje * personas[indice][0] * error
            pesos[1] += rango_de_aprendizaje * personas[indice][1] * error
            umbral += rango_de_aprendizaje * error

        print(f'{epoca} -> {error_total}')



pesos = np.random.uniform(-1, 1, size = 2)
umbral = np.random.uniform(-1, 1)
rango_de_aprendizaje = 0.01
epocas = 100


entrenamiento(epocas, rango_de_aprendizaje, pesos, umbral)

print(f'\n\nEl resultado de la funcion es: {funcion_activacion(pesos, [0.5, 0.8], umbral)}')

# print(f'\n\nEl vector de pesos es:  {pesos},\nEl umbral es: {umbral}, \nResultado de función: {funcion_activacion(pesos, [0.5, 0.5], umbral)}\n\n')
