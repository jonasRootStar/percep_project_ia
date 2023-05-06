import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        
    def fit(self, X, y):
        n_samples, n_features = X.shape
        
        self.weights = np.zeros(n_features + 1)
        
        for _ in range(self.n_iterations):
            for i in range(n_samples):
                x = np.insert(X[i], 0, 1)
                y_pred = np.dot(x, self.weights)
                
                if y[i] * y_pred <= 0:
                    self.weights += self.learning_rate * y[i] * x
                    
    def predict(self, X):
        n_samples, n_features = X.shape
        predictions = []
        
        for i in range(n_samples):
            x = np.insert(X[i], 0, 1)
            y_pred = np.dot(x, self.weights)
            predictions.append(np.sign(y_pred))
            
        return predictions
