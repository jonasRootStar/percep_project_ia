from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSizePolicy, QGroupBox, QComboBox
import pyqtgraph as pg
from PySide6.QtGui import QFont
from PySide6 import QtCore


class VentanaDos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perceptron")
        self.setFixedSize(1200,700)


        label = QLabel("P E R C E P T R O N")
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setFont(QFont('Cascadia Code', 20))
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)


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
        xa_1_input = QLineEdit()
        xa_2 = QLabel("X2")
        xa_2_input = QLineEdit()
        ya_1 = QLabel("Y1")
        ya_1_input = QLineEdit()
        ya_2 = QLabel("Y2")
        ya_2_input = QLineEdit()
        nA = QLabel("Núm. A")
        nA_input = QLineEdit()
        btnA = QPushButton("OK Región A")

        xb_1 = QLabel("X1")
        xb_1_input = QLineEdit()
        xb_2 = QLabel("X2")
        xb_2_input = QLineEdit()
        yb_1 = QLabel("Y1")
        yb_1_input = QLineEdit()
        yb_2 = QLabel("Y2")
        yb_2_input = QLineEdit()
        nB = QLabel("Núm. B")
        nB_input = QLineEdit()
        btnB = QPushButton("OK Región B")

        regInput_layout.addLayout(regA_layout)
        regInput_layout.addLayout(regB_layout)

        regA_layout.addWidget(regA_Group)
        regA_Group.setLayout(gridA_layout)
        regB_layout.addWidget(regB_Group)
        regB_Group.setLayout(gridB_layout)

        gridA_layout.addWidget(xa_1, 0, 0)
        gridA_layout.addWidget(xa_1_input, 0, 1)
        gridA_layout.addWidget(xa_2, 1, 0)
        gridA_layout.addWidget(xa_2_input, 1, 1)
        gridA_layout.addWidget(ya_1, 0, 2)
        gridA_layout.addWidget(ya_1_input, 0, 3)
        gridA_layout.addWidget(ya_2, 1, 2)
        gridA_layout.addWidget(ya_2_input, 1, 3)
        gridA_layout.addWidget(nA, 2, 0)
        gridA_layout.addWidget(nA_input, 2, 1)
        gridA_layout.addWidget(btnA, 3, 0, 1, 4)

        gridB_layout.addWidget(xb_1, 0, 0)
        gridB_layout.addWidget(xb_1_input, 0, 1)
        gridB_layout.addWidget(xb_2, 1, 0)
        gridB_layout.addWidget(xb_2_input, 1, 1)
        gridB_layout.addWidget(yb_1, 0, 2)
        gridB_layout.addWidget(yb_1_input, 0, 3)
        gridB_layout.addWidget(yb_2, 1, 2)
        gridB_layout.addWidget(yb_2_input, 1, 3)
        gridB_layout.addWidget(nB, 2, 0)
        gridB_layout.addWidget(nB_input, 2, 1)
        gridB_layout.addWidget(btnB, 3, 0, 1, 4)


    def entrenamiento_gui(self, entrenaInput_layout):
        combo_box_entrena = QComboBox()
        combo_box_entrena.addItems(("Pintar paso a paso", "Inicio y final"))
        combo_box_entrena.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn_entrenar = QPushButton("Entrenar")
        btn_entrenar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        entrenaInput_layout.addWidget(combo_box_entrena)
        entrenaInput_layout.addWidget(btn_entrenar, 2)


    def reconocimiento_gui(self, recoInput_layout):
        combo_box_reco = QComboBox()
        combo_box_reco.addItems(("Datos aleatorios", "Datos de archivo"))
        combo_box_reco.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn_reco = QPushButton("Reconocimiento")
        btn_reco.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        recoInput_layout.addWidget(combo_box_reco)
        recoInput_layout.addWidget(btn_reco, 2)

    
    def parametros_gui(self, camInput_layou):
        gridcam_layou = QGridLayout()
        param_group = QGroupBox("Parametros")
        param_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        inter_label = QLabel("Intervalos Peso del neurón")
        inter1_input = QLineEdit()
        inter2_input = QLineEdit()
        coef_label = QLabel("Coeficiente de aprendizaje")
        coef_input = QLineEdit()
        btn_cambio = QPushButton("Aplicar")

        gridcam_layou.addWidget(inter_label, 0, 0)
        gridcam_layou.addWidget(inter1_input, 0, 1)
        gridcam_layou.addWidget(inter2_input, 0, 2)
        gridcam_layou.addWidget(coef_label, 1, 0)
        gridcam_layou.addWidget(coef_input, 1, 1)
        gridcam_layou.addWidget(btn_cambio, 2, 0, 1, 2)

        camInput_layou.addWidget(param_group)
        param_group.setLayout(gridcam_layou)




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
        accPor_label = QLabel("_____ %")
        accPor_label.setFont(QFont('Cascadia Code', 12))
        acc_layout = QHBoxLayout()

        graphWidget = pg.PlotWidget()
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        # plot data: x, y values
        graphWidget.plot(hour, temperature)

        vr_layou.addWidget(labelr)
        vr_layou.addWidget(graphWidget)
        vr_layou.addLayout(acc_layout)
        
        acc_layout.addWidget(acc_label)
        acc_layout.addWidget(accPor_label)
