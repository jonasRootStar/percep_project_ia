from PySide6.QtWidgets import QApplication
from ventanav_dos import VentanaDos
import sys
# from ventanav_uno import VentanaUno


app = QApplication(sys.argv)
# ventana = VentanaUno()
# ventana.show()

ventana = VentanaDos()
ventana.show()

app.exec()

