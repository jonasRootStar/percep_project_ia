import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=15):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.umbral = np.random.random()
        self.W = np.random.rand(2,1)  # [[23442], [2342424]]
        self.lineaRecta = []

    def imprime(self):
        print(f'{self.W}')
        print(self.W[2])

    # def set_pesos(self, tam):
    #     for i in range(tam):
    #         self.W = np.random.rand(2,1)


    def entrenamiento(self, X):
        # {llave 1: [5, 2, 1]}  
        # D = obtener la etiqueta o clase

        for _ in range(self.n_iterations):
            for llave in X.keys():
                D = X[llave][2]
                puntos = [X[llave][0], X[llave][1]]
                sum = np.dot(puntos, self.W)                   #Producto punto (o sumatoria entre nuestros pesos y datos entrada)
                funcEsc = sum + self.umbral                        #Operacion dentro de la funcion de activacion

                if funcEsc >= 0:                                   #Funcion de activacion, en este caso la funcion Escalon
                    y_pred = 1
                else:
                    y_pred = -1
                
                #Calculando el delta entre nuestro label y la prediccion de entrenamiento
                funcDelta = D - y_pred  
                                    
                for wi in range(len(self.W)):
                    deltaI = self.learning_rate * funcDelta * X[llave][wi]      #Calculando el delta i que se sumara a nuestro vector de pesos[]
                    self.W[wi] += deltaI

                self.umbral += self.learning_rate * funcDelta      #Modificando el umbral o bias
            m = float(self.W[0]/self.W[1])
            b = float(self.umbral/self.W[1])
            self.lineaRecta.append([m,b])

    def prediccion(self, X):                                   #Funcion que le permitira al Perceptron realizar
        predictions = []                                       #una clasificacion del dataset introducido
        for llave in X.keys():
            puntos = [X[llave][0], X[llave][1]]
            sum = np.dot(puntos, self.W)
            funcEsc = sum - self.umbral                        
            if funcEsc >= 0:                                   
                y_pred = 1
            else:
                y_pred = -1          
            predictions.append(y_pred)
        return predictions

    def calcularAccuracy(self, X, predicciones):                #Funcion que nos permitira saber que predicciones son correctas
        correctas = 0                                           #comparando con nuestra entrada de datos
        i = 0
        for llave in X.keys():
            if X[llave][2] == predicciones[i]:
                correctas+=1
            i+=1
        return float(correctas/len(X)) * 100


    def ecuacionPendiente(self):                            #Funcion que retornara una lista o arreglo donde contendra
        return self.lineaRecta                              #la pendiente m y el termino independiente b para poder graficar
    

prueba = {
    "1": [1,5,1],
    "2": [-2, -4, -1],
    "3": [-8, -10, -1],
    "4": [8, 10, 1],
    "5": [2, 2, 1],
    "6": [-13, -4, -1],
    "7": [-20, -11, -1],
    "8": [9, 9, 1]
}

# percep = Perceptron()
# #percep.imprime()
# percep.entrenamiento(prueba)
# #print(percep.ecuacionPendiente())

prueba2 = {
    "1": [2, 10, 1],
    "2": [-7, -2, -1],
    "3": [-11, -20, 1],
    "4": [5, 5, -1],
    "5": [2, 2, 1],
    "6": [1, 2, -1],
    "7": [-8, -8, -1],
    "8": [-1, -3, -1],
    "9": [6, 12, 1],
    "10": [-5, -2, -1]    
}

# aux = percep.prediccion(prueba2)
# print(aux)
# rel = percep.calcularAccuracy(prueba2, aux)
# print(str(rel))
