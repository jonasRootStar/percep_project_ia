# pagina donde podemos encontrar un nuevo codigo
# https://towardsdatascience.com/perceptron-algorithm-in-python-f3ac89d2e537
# https://vitalflux.com/perceptron-explained-using-python-example/


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from perceptronTest import Perceptron

def accuracy(y_true, y_pred):
    acc_porcentaje = np.sum(y_true == y_pred) / len(y_true)
    return acc_porcentaje



X, y = datasets.make_blobs(n_samples=150, n_features=2, centers=2, cluster_std=1.05, random_state=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

percep = Perceptron(learning_rate=0.01, n_iters=1000)
percep.fit(X_train, y_train)
predicciones = percep.predict(X_test)

print(f'\n\nPorcentaje de ACC del Perceptron {accuracy(y_test, predicciones)}\n\n')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(X_train[:,0], X_train[:,1], marker='o', c=y_train)

x0_1 = np.amin(X_train[:,0])
x0_2 = np.amax(X_train[:,0])

x1_1 = (-percep.weights[0] * x0_1 - percep.bias / percep.weights[1])
x1_2 = (-percep.weights[0] * x0_2 - percep.bias / percep.weights[1])

ax.plot([x0_1, x0_2], [x1_1, x1_2], 'k')

ymin = np.amin(X_train[:,1])
ymax = np.amax(X_train[:,1])
ax.set_ylim([ymin-3, ymax+3])

plt.show()