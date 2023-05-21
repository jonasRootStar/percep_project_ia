import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSizePolicy, QGroupBox, QComboBox, QDialog, QDialogButtonBox, QFileDialog, QMessageBox
from PySide6.QtGui import QFont
from PySide6 import QtCore, QtTest
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from perceptron_cg import Perceptron
from archivo import Archivo


class VentanaEmergente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Cantidad de datos")
        btns = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.btnBox = QDialogButtonBox(btns)
        self.btnBox.accepted.connect(self.accept)
        self.btnBox.rejected.connect(self.reject)

        self.layoutReco = QVBoxLayout()
        self.entrada = QLineEdit()
        msg = QLabel("Introduce la cantidad de datos que se generan de forma aleatoria:")

        self.layoutReco.addWidget(msg)
        self.layoutReco.addWidget(self.entrada)
        self.layoutReco.addWidget(self.btnBox)
        self.setLayout(self.layoutReco)




class VentanaDos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perceptron")
        self.setFixedSize(1200,700)


        label = QLabel("P E R C E P T R O N")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setFont(QFont('Cascadia Code', 20))
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.figuraGrafica = Figure()
        self.graficas = self.figuraGrafica.add_subplot(111)
        self.grafica = FigureCanvas(self.figuraGrafica)

        # aux = [puntox, puntoy, label]
        # self.puntos_regA = dict(aux)
        
        self.puntos_regA = dict(puntosx = [], puntosy = [], region=1)
        self.puntos_regB = dict(puntosx = [], puntosy = [], region=-1)
        self.datosRegiones = pd.DataFrame(columns=['PuntosX', 'PuntosY', 'Region'])
        self.rel = 0
        

        # Layoud principal ---------------------------------------------------
        v_layo = QVBoxLayout()
        # Layoud del titulo --------------------------------------------------
        htitle_layo = QHBoxLayout()
        # Layoud donde se pondran las dos partes izquierda y derecha (datos y grafica)
        h1_layou = QHBoxLayout()
        # Layoud vertical de la parte IZQUIERDA -----------------------------------------
        vl_layou = QVBoxLayout()
        # Layoud vertical de la parte DERECHA -------------------------------------------
        vr_layou = QVBoxLayout()

        # Agregando etiquetas y componentes de los layoud izquierdo y derecho -----------
        htitle_layo.addWidget(label)

        # Componentes de layoud izquierdo -----------------------------------------------
        self.layout_izquierdo_gui(vl_layou)

        # Componentes de layoud derecho -------------------------------------------------
        self.layout_derecho_gui(vr_layou)


        # Agragando LAYOUDS -------------------------
        h1_layou.addLayout(vl_layou)
        h1_layou.addLayout(vr_layou)
        v_layo.addLayout(htitle_layo)
        v_layo.addLayout(h1_layou)

        self.setLayout(v_layo)



    # ---------------------- LAYOUT IZQUIERDO -------------------------
    # Parte de la interfaz donde estaran todas las entradas de datos
    # estos son: los valores para las regiones y la cantidad de puntos,
    # si se generan aleatorios cada vez que sea ejecutado o se leera de
    # un asrchivo hecho previamente con datos aleatorios, si la gráfica
    # sera dibujada por cada etapa del entrenamiento o solo al final
    # y el cambio de parametros (peso y rango de aprendizaje)

    def layout_izquierdo_gui(self, vl_layou):
        regInput_layout = QHBoxLayout() # Layoud para lectura de los datos para regiones A y B
        entrenaInput_layout = QHBoxLayout() # Layoud para el entrenamiento
        recoInput_layout = QHBoxLayout() # Layoud para el reconocimiento
        camInput_layou = QHBoxLayout()

        labell = QLabel("Generación de regiones")
        labell_entrena = QLabel("Entrenamiento")
        labell_reco = QLabel("Reconocimiento")
        labell_cam = QLabel("Cambio de parametros")
        labell.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labell_entrena.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labell_reco.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labell_cam.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labell.setFont(QFont('Cascadia Code', 12))
        labell.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        labell_entrena.setFont(QFont('Cascadia Code', 12))
        labell_entrena.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        labell_reco.setFont(QFont('Cascadia Code', 12))
        labell_reco.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        labell_cam.setFont(QFont('Cascadia Code', 12))
        labell_cam.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        vl_layou.addWidget(labell)
        vl_layou.addLayout(regInput_layout)
        vl_layou.addWidget(labell_entrena)
        vl_layou.addLayout(entrenaInput_layout)
        vl_layou.addWidget(labell_reco)
        vl_layou.addLayout(recoInput_layout)
        vl_layou.addWidget(labell_cam)
        vl_layou.addLayout(camInput_layou)

        # Generacion de regiones ---------------------------
        self.generacion_de_regiones_gui(regInput_layout)

        # Entranamiento --------------------------
        self.entrenamiento_gui(entrenaInput_layout)

        # Reconocimiento --------------------------
        self.reconocimiento_gui(recoInput_layout)

        # Cambio de parametros ---------------------
        self.parametros_gui(camInput_layou)



    def generacion_de_regiones_gui(self, regInput_layout):
        regA_layout = QVBoxLayout()
        regB_layout = QVBoxLayout()
        gridA_layout = QGridLayout()
        gridB_layout = QGridLayout()
        regA_Group = QGroupBox("Región A")
        regA_Group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        regB_Group = QGroupBox("Región B")
        regB_Group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        xa_1 = QLabel("X1")
        self.xa_1_input = QLineEdit()
        xa_2 = QLabel("X2")
        self.xa_2_input = QLineEdit()
        ya_1 = QLabel("Y1")
        self.ya_1_input = QLineEdit()
        ya_2 = QLabel("Y2")
        self.ya_2_input = QLineEdit()
        nA = QLabel("Núm. A")
        self.nA_input = QLineEdit()
        btnA = QPushButton("OK Región A")
        btnA.clicked.connect(self.btnA_clicked)

        xb_1 = QLabel("X1")
        self.xb_1_input = QLineEdit()
        xb_2 = QLabel("X2")
        self.xb_2_input = QLineEdit()
        yb_1 = QLabel("Y1")
        self.yb_1_input = QLineEdit()
        yb_2 = QLabel("Y2")
        self.yb_2_input = QLineEdit()
        nB = QLabel("Núm. B")
        self.nB_input = QLineEdit()
        btnB = QPushButton("OK Región B")
        btnB.clicked.connect(self.btnB_clicked)

        regInput_layout.addLayout(regA_layout)
        regInput_layout.addLayout(regB_layout)

        regA_layout.addWidget(regA_Group)
        regA_Group.setLayout(gridA_layout)
        regB_layout.addWidget(regB_Group)
        regB_Group.setLayout(gridB_layout)

        gridA_layout.addWidget(xa_1, 0, 0)
        gridA_layout.addWidget(self.xa_1_input, 0, 1)
        gridA_layout.addWidget(xa_2, 1, 0)
        gridA_layout.addWidget(self.xa_2_input, 1, 1)
        gridA_layout.addWidget(ya_1, 0, 2)
        gridA_layout.addWidget(self.ya_1_input, 0, 3)
        gridA_layout.addWidget(ya_2, 1, 2)
        gridA_layout.addWidget(self.ya_2_input, 1, 3)
        gridA_layout.addWidget(nA, 2, 0)
        gridA_layout.addWidget(self.nA_input, 2, 1)
        gridA_layout.addWidget(btnA, 3, 0, 1, 4)

        gridB_layout.addWidget(xb_1, 0, 0)
        gridB_layout.addWidget(self.xb_1_input, 0, 1)
        gridB_layout.addWidget(xb_2, 1, 0)
        gridB_layout.addWidget(self.xb_2_input, 1, 1)
        gridB_layout.addWidget(yb_1, 0, 2)
        gridB_layout.addWidget(self.yb_1_input, 0, 3)
        gridB_layout.addWidget(yb_2, 1, 2)
        gridB_layout.addWidget(self.yb_2_input, 1, 3)
        gridB_layout.addWidget(nB, 2, 0)
        gridB_layout.addWidget(self.nB_input, 2, 1)
        gridB_layout.addWidget(btnB, 3, 0, 1, 4)


    def dibujar_scatter(self, puntos_regA, colorA, puntos_regB, colorB):
        self.figuraGrafica.clear()
        self.graficas = self.figuraGrafica.add_subplot(111)

        self.graficas.scatter(puntos_regA["puntosx"], puntos_regA["puntosy"], color=colorA)
        self.graficas.scatter(puntos_regB["puntosx"], puntos_regB["puntosy"], color=colorB)




    def btnA_clicked(self):
        xa1 = float(self.xa_1_input.text())
        ya1 = float(self.ya_1_input.text())
        xa2 = float(self.xa_2_input.text())
        ya2 = float(self.ya_2_input.text())
        numRegA = int(self.nA_input.text())
        puntosX = []
        puntosY = []
        self.puntos_regA = dict(puntosx = puntosX, puntosy = puntosY, region=1)
        # {1: [5, 2, 1]}
        self.figuraGrafica.clear()
        graficaA = self.figuraGrafica.add_subplot(111)


        for punto in range(numRegA):
            # puntosA[punto] = [random.uniform(xa1, xa2)]
            self.puntos_regA["puntosx"].append(random.uniform(xa1,xa2))
            self.puntos_regA["puntosy"].append(random.uniform(ya1,ya2))

        print(f'Region A:{self.puntos_regA}')

        rectA = plt.Rectangle((min(xa2,xa1), min(ya2,ya1)), abs(xa2-xa1), abs(ya2-ya1), facecolor=(0,0,0,0), edgecolor="red")
        graficaA.add_artist(rectA)

        # graficaA.scatter(self.puntos_regA["puntosx"], self.puntos_regA["puntosy"], color="red")
        # graficaA.scatter(self.puntos_regB["puntosx"], self.puntos_regB["puntosy"], color="blue")
        self.dibujar_scatter(self.puntos_regA, "red", self.puntos_regB, "blue")

        self.grafica.draw()

        # dtFrameA = pd.DataFrame.from_dict(self.puntos_regA)
        # dtFrameA.to_csv(r'datosRegA.csv', index=False, header=True)

        print(f'Region A:\nxa1: {xa1}\tya1: {ya1}\nxa2: {xa2}\tya2: {ya2}\nNum: {numRegA}')
        # print(f'\n\nPuntos en X(a) : {self.puntos_regA["puntosx"]}\n\nPuntos en Y(a){self.puntos_regA["puntosy"]}')

    def btnB_clicked(self):
        xb1 = float(self.xb_1_input.text())
        yb1 = float(self.yb_1_input.text())
        xb2 = float(self.xb_2_input.text())
        yb2 = float(self.yb_2_input.text())
        numRegB = int(self.nB_input.text())
        puntosX = []
        puntosY = []
        self.puntos_regB = dict(puntosx = puntosX, puntosy = puntosY, region=-1)

        self.figuraGrafica.clear()
        graficaB = self.figuraGrafica.add_subplot(111)


        for punto in range(numRegB):
            # puntosA[punto] = [random.uniform(xa1, xa2)]
            self.puntos_regB["puntosx"].append(random.uniform(xb1,xb2))
            self.puntos_regB["puntosy"].append(random.uniform(yb1,yb2))

        print(f'\nRegion B{self.puntos_regB}')
        rectB = plt.Rectangle((min(xb2,xb1), min(yb2,yb1)), abs(xb2-xb1), abs(yb2-yb1), facecolor=(0,0,0,0), edgecolor="blue")
        graficaB.add_artist(rectB)

        # graficaB.scatter(self.puntos_regA["puntosx"], self.puntos_regA["puntosy"], color="red")
        # graficaB.scatter(self.puntos_regB["puntosx"], self.puntos_regB["puntosy"], color="blue")
        self.dibujar_scatter(self.puntos_regA, "red", self.puntos_regB, "blue")


        self.grafica.draw()

        print(f'Region B:\nxa1: {xb1}\tya1: {yb1}\nxa2: {xb2}\tya2: {yb2}\nNum: {numRegB}')
        # print(f'\n\nPuntos en X(b) : {self.puntos_regB["puntosx"]}\n\nPuntos en Y(b){self.puntos_regB["puntosy"]}')

    def valores_entrada(self):
        self.xMinima = min(float(self.xa_1_input.text()), float(self.xa_2_input.text()), float(self.xb_1_input.text()), float(self.xb_2_input.text()))
        self.xMax = max(float(self.xa_1_input.text()), float(self.xa_2_input.text()), float(self.xb_1_input.text()), float(self.xb_2_input.text()))
        self.yMinima = min(float(self.ya_1_input.text()), float(self.ya_2_input.text()), float(self.yb_1_input.text()), float(self.yb_2_input.text()))
        self.yMax = max(float(self.ya_1_input.text()), float(self.ya_2_input.text()), float(self.yb_1_input.text()), float(self.yb_2_input.text()))

    def entrenamiento_gui(self, entrenaInput_layout):
        self.combo_box_entrena = QComboBox()
        self.combo_box_entrena.addItems(("Pintar paso a paso", "Inicio y final"))
        self.combo_box_entrena.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_entrenar = QPushButton("Entrenar")
        self.btn_entrenar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        entrenaInput_layout.addWidget(self.combo_box_entrena)
        entrenaInput_layout.addWidget(self.btn_entrenar, 2)
        self.btn_entrenar.clicked.connect(self.btn_entrenar_onClicked)


    def btn_entrenar_onClicked(self):
        dataA = pd.DataFrame.from_dict(self.puntos_regA)
        dataB = pd.DataFrame.from_dict(self.puntos_regB)
        listaFilas = []
        self.percep = Perceptron()

        self.valores_entrada()

        self.datosRegiones = pd.concat([dataA, dataB])
        self.coord = np.array(self.datosRegiones[["puntosx", "puntosy"]].values.tolist())
        self.recta = np.zeros(len(self.coord))
        self.datosRegiones.to_csv(r'datos.csv', index=False, header=True)
        
        for i, fila in self.datosRegiones.iterrows():
            aux = [fila.puntosx, fila.puntosy, fila.region]
            listaFilas.append(aux)

        indices = [i for i in range(len(listaFilas))]
        dicFinal = dict(zip(indices, listaFilas))

        for indice in range(len(dicFinal)):
            print(f'{indice}\t{dicFinal[indice]}')
        
        self.percep.entrenamiento(dicFinal)
        listaPrediccion = self.percep.prediccion(dicFinal)
        print(listaPrediccion)
        self.rel = self.percep.calcularAccuracy(dicFinal, listaPrediccion)
        self.rectaLinea = self.percep.lineaRecta

        print(str(self.rel))
        print(f'{self.percep.n_iterations}')
        self.dibujar_scatter(self.puntos_regA, "red", self.puntos_regB, "blue")


        if (self.combo_box_entrena.currentIndex() == 0):
            print(f'\n\nSe eligió opcion 0 de Entrenamiento')
            for epoca in range(self.percep.n_iterations):
                for x in range(len(dicFinal)):
                    self.recta[x] = -self.rectaLinea[epoca][0] * self.datosRegiones.iloc[x][0] - self.rectaLinea[epoca][1]

                if (epoca == self.percep.n_iterations-1):
                    self.graficas.plot(self.coord[:,0], self.recta, color="yellow", linewidth = "1.0", linestyle = "--")
                else:
                    self.graficas.plot(self.coord[:,0], self.recta, color="gray", linewidth = "1.0", linestyle = "--")


                self.graficas.set_ylim(self.yMinima, self.yMax)
                self.graficas.set_xlim(self.xMinima, self.xMax)

                self.grafica.draw()
                QtTest.QTest.qWait(1000)
                # print(f'Epoca {epoca}:{self.percep.umbral}')
                
        elif (self.combo_box_entrena.currentIndex() == 1):
            print(f'\n\nSe eligió opcion 1 de Entrenamiento')
            for epoca in range(self.percep.n_iterations):
                for x in range(len(dicFinal)):
                    self.recta[x] = -self.rectaLinea[epoca][0] * self.datosRegiones.iloc[x][0] - self.rectaLinea[epoca][1]

                if ((epoca == 0)):
                    self.graficas.plot(self.coord[:,0], self.recta, color="gray", linewidth = "1.0", linestyle = "--")
                elif (epoca == self.percep.n_iterations-1):
                    self.graficas.plot(self.coord[:,0], self.recta, color="yellow", linewidth = "1.0", linestyle = "--")

                self.graficas.set_ylim(self.yMinima, self.yMax)
                self.graficas.set_xlim(self.xMinima, self.xMax)

                self.grafica.draw()
                # QtTest.QTest.qWait(1000)
                print(f'Epoca {epoca}:{self.percep.umbral}')

        self.accPor_label.setText(f'{self.rel}%')
        



    def reconocimiento_gui(self, recoInput_layout):
        self.combo_box_reco = QComboBox()
        self.combo_box_reco.addItems(("Datos aleatorios", "Datos de archivo"))
        self.combo_box_reco.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_reco = QPushButton("Reconocimiento")
        self.btn_reco.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.text_reco = QLineEdit()

        recoInput_layout.addWidget(self.combo_box_reco)
        recoInput_layout.addWidget(self.btn_reco, 2)
        self.btn_reco.clicked.connect(self.btn_reco_onClicked)


    def btn_reco_onClicked(self):
        if (self.combo_box_reco.currentIndex() == 0):
            print(f'\n\nSe eligió opcion 0 de Reconocimiento')
            # ----------------Para datos aleatorios----------------------
            self.datos_reco_aleatorios()
        elif (self.combo_box_reco.currentIndex() == 1):
            print(f'\n\nSe eligió opcion 1 de Reconocimiento')
            self.datos_de_archivo()


    # *************************REVISAR*****************************
    # Revisar la generación de valores aleatorios, además de gráficar la
    # linea recta con base a los nuevos datos.
    def datos_reco_aleatorios(self):
        dlg = VentanaEmergente(self)
        if dlg.exec():
            numAle = int(dlg.entrada.text())
            print(f'Aceptar: {numAle}')
            band = True
        else:
            band = False
            print(f'Cancel')

        if band:
            xb2 = float(self.xb_2_input.text())
            yb2 = float(self.yb_2_input.text())

            xa1 = float(self.xa_1_input.text())
            ya1 = float(self.ya_1_input.text())

            #punto1 = [xa1, yb2]
            #punto2 = [xb2, ya1]
            puntosX = np.random.randint(low=xa1, high=xb2, size=numAle)   #Retorna un arreglo de (n size numeros aleatorios) [2, 3, 4, 5, 8, 1, ...]
            puntosY = np.random.randint(low=ya1, high=yb2, size=numAle)   #low valor minimo inclusivo ;;;;   high valor maximo exclusivo

            datosAleatorios = dict([])
            for i in range(len(puntosX)):
                datosAleatorios[i].append([puntosX[i], puntosY[i], np.random.choice([-1,1])])
            
            resultados = self.percep.prediccion(datosAleatorios)

            score = self.percep.calcularAccuracy(datosAleatorios, resultados)
            self.accPor_label.setText(f'{score}%')



    def datos_de_archivo(self):
        self.valores_entrada()
        archivo = Archivo(self.xMinima, self.xMax, self.yMinima, self.yMax)
        archivo.crear_archivo()
        listaArchivo = []
        archivo_explore = QFileDialog()
        archivo_explore.setFileMode(QFileDialog.ExistingFile)
        if archivo_explore.exec():
            archivo_seleccionado = archivo_explore.selectedFiles()[0]
            self.archivoDataF = pd.read_csv(archivo_seleccionado)

            for i, fila in self.archivoDataF.iterrows():
                aux_archivo = [fila.puntosx, fila.puntosy, fila.region]
                listaArchivo.append(aux_archivo)

            
            datosA = self.archivoDataF[self.archivoDataF['region'] == 1]
            datosB = self.archivoDataF[self.archivoDataF['region'] == -1]
            datosADicc = datosA.to_dict('list')
            datosBDicc = datosB.to_dict('list')

            self.dibujar_scatter(datosADicc, "red", datosBDicc, "blue")
            self.grafica.draw()
            
            indices = [i for i in range(len(listaArchivo))]
            diccArchivo = dict(zip(indices, listaArchivo))

            # ----------------------------------------
            coord = np.array(self.archivoDataF[["puntosx", "puntosy"]].values.tolist())

            rectaArchivo = np.zeros(len(coord))


            resultado = self.percep.prediccion(diccArchivo)
            score = self.percep.calcularAccuracy(diccArchivo, resultado)

            xMinima = min(self.archivoDataF["puntosx"])
            yMinima = min(self.archivoDataF["puntosy"])
            xMax = max(self.archivoDataF["puntosx"])
            yMax = max(self.archivoDataF["puntosy"])

            # *************************REVISAR*****************************
            # Revisar si la gráfica la dibuja adecuadamente respecto al entrenamiento y con los
            # nuevos datos extraidos del archivo
            for epoca in range(self.percep.n_iterations):
                for x in range(len(diccArchivo)):
                    rectaArchivo[x] = -self.rectaLinea[epoca][0] * self.archivoDataF.iloc[x][0] - self.rectaLinea[epoca][1]

                if ((epoca == 0)):
                    self.graficas.plot(coord[:,0], rectaArchivo, color="gray", linewidth = "1.0", linestyle = "--")
                elif (epoca == self.percep.n_iterations-1):
                    self.graficas.plot(coord[:,0], rectaArchivo, color="yellow", linewidth = "1.0", linestyle = "--")

                self.graficas.set_ylim(yMinima, yMax)
                self.graficas.set_xlim(xMinima, xMax)

                self.grafica.draw()

            self.accPor_label.setText(f'{score}%')


            
    
    def parametros_gui(self, camInput_layou):
        gridcam_layou = QGridLayout()
        param_group = QGroupBox("Parametros")
        param_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        inter_label = QLabel("Intervalos Peso del neurón")
        self.inter1_input = QLineEdit()
        self.inter2_input = QLineEdit()
        coef_label = QLabel("Coeficiente de aprendizaje")
        self.coef_input = QLineEdit()
        btn_cambio = QPushButton("Aplicar")
        btn_cambio.clicked.connect(self.btn_cambio_onClicked)

        gridcam_layou.addWidget(inter_label, 0, 0)
        gridcam_layou.addWidget(self.inter1_input, 0, 1)
        gridcam_layou.addWidget(self.inter2_input, 0, 2)
        gridcam_layou.addWidget(coef_label, 1, 0)
        gridcam_layou.addWidget(self.coef_input, 1, 1)
        gridcam_layou.addWidget(btn_cambio, 2, 0, 1, 2)

        camInput_layou.addWidget(param_group)
        param_group.setLayout(gridcam_layou)


    def btn_cambio_onClicked(self):
        try:
            inicio_intervalo = float(self.inter1_input.text())
            fin_intervalo = float(self.inter2_input.text())
            coef_aprendizaje = float(self.coef_input.text())


            if (inicio_intervalo >= 0 and fin_intervalo > inicio_intervalo and coef_aprendizaje > 0 and coef_aprendizaje < 1):
                self.percep.setLearningRate(coef_aprendizaje)
                self.percep.setWeightRange(inicio_intervalo, fin_intervalo)
                QMessageBox.information(self, "Confirmación", "Todos los parámetros modificados")
            elif(coef_aprendizaje > 0 and coef_aprendizaje < 1):
                self.percep.setLearningRate(coef_aprendizaje)
                QMessageBox.information(self, "Confirmación", "Learning rate modificado")
            elif(inicio_intervalo >= 0 and fin_intervalo > inicio_intervalo):
                self.percep.setWeightRange(inicio_intervalo, fin_intervalo)
                QMessageBox.information(self, "Confirmación", "Intervalo modificado")
            else:
                QMessageBox.critical(self, "Error", "Parámetros fuera de los rangos válidos, corrija los parámetros e intente de nuevo.")
        except:
            QMessageBox.critical(self, "Error", "Espacios vacíos, favor de ingresar datos")




    # ---------------------- LAYOUT DERECHO -------------------------
    # Parte de la interfaz donde se encuentra la gráfica y donde
    # se muestra el label para visualizar el porcentaje de ACC.

    def layout_derecho_gui(self, vr_layou):
        labelr = QLabel("Gráfica")
        labelr.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        labelr.setFont(QFont('Cascadia Code', 12))
        labelr.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        acc_label = QLabel("Porcentaje de ACC: ")
        acc_label.setFont(QFont('Cascadia Code', 12))
        self.accPor_label = QLabel("_____ %")
        self.accPor_label.setFont(QFont('Cascadia Code', 12))
        acc_layout = QHBoxLayout()

        # graphWidget = pg.PlotWidget()
        # hour = [1,2,3,4,5,6,7,8,9,10]
        # temperature = [30,32,34,32,33,31,29,32,35,45]
        # plot data: x, y values

        # graphWidget = MainWindow()
        self.figuraGrafica.add_subplot()
        
        # graphWidget.plot(hour, temperature)

        vr_layou.addWidget(labelr)
        # vr_layou.addWidget(graphWidget)
        vr_layou.addWidget(self.grafica)
        vr_layou.addLayout(acc_layout)
        
        self.grafica.draw()
        acc_layout.addWidget(acc_label)
        acc_layout.addWidget(self.accPor_label)
