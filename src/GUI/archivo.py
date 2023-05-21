import csv
import random

class Archivo:
    def __init__(self, xMin, xMax, yMin, yMax) -> None:
        self.xMin = xMin
        self.yMin = yMin
        self.xMax = xMax
        self.yMax = yMax
        # self.archivo = open("archivo_de_prueba.csv", "w")

    def crear_archivo(self):
        encabezado = ["puntosx", "puntosy", "region"]
    
        with open('datos_de_prueba.csv', 'w', newline='') as archivo:
            archivo_a_escribir = csv.writer(archivo)
            filtros = ["puntosx", "puntosy", "region"]

            archivo_a_escribir.writerow(filtros)
            for i in range(0,100):
                archivo_a_escribir.writerow([random.uniform(self.xMin, self.xMax), random.uniform(self.yMin, self.yMax), random.choice([1,-1])])



        