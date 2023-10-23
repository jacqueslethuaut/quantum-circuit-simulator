import os
from config import ELEMENT_IMAGES, init_config
from main_window import MainWindow

from quantum_circuit import QuantumCircuit
from drop_area import DropArea

from PyQt5.QtWidgets import QApplication

init_config(os.path.abspath(__file__))

app = QApplication([]) 

quantum_circuit = QuantumCircuit()
drop_area = DropArea(quantum_circuit)

main_window = MainWindow(drop_area)
main_window.showMaximized()

app.exec_()  

