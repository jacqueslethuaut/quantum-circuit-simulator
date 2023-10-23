from config import ELEMENT_IMAGES

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget
from quantum_circuit import QuantumCircuit
from draggable_element import DraggableElement

class DropArea(QWidget):
    
    def __init__(self, quantum_circuit, *args, **kwargs):
        super(DropArea, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setStyleSheet("border: 1px")
        self.quantum_circuit = quantum_circuit
        self.draggable_elements = {}

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        print("Drop event triggered.")  # Debugging line
        position = event.pos()
        element_type = event.mimeData().text()
        image_path = ELEMENT_IMAGES.get(element_type)
        existing_element = self.quantum_circuit.find_element(element_type)
        
        grid_step = 20  
        new_x = round(position.x() / grid_step) * grid_step
        new_y = round(position.y() / grid_step) * grid_step

        is_from_left_panel = event.source().from_left_panel if event.source() else False
  
        if is_from_left_panel:
            image_path = ELEMENT_IMAGES.get(element_type)  
            new_element_data = self.quantum_circuit.add_element(element_type, (new_x, new_y))
            new_gui_element = DraggableElement(new_element_data['type'], image_path, new_element_data['id'])
            new_gui_element.move(position)
            new_gui_element.setParent(self)
            new_gui_element.show()
            new_gui_element.from_left_panel = False 

            self.draggable_elements[new_element_data['id']] = new_gui_element
            
        else:
            existing_element = self.quantum_circuit.find_element_by_id(event.source().element_id)
            if existing_element is not None:
                existing_element['position'] = (new_x, new_y)
                event.source().move(new_x, new_y)
            else:
                print(f"Element with ID {event.source().element_id} not found.")
            
 
    def paintEvent(self, event):
        super(DropArea, self).paintEvent(event)
        
        qp = QPainter()
        qp.begin(self)
        self.drawGrid(qp)
        qp.end()

    def drawGrid(self, qp):
        pen = QPen(Qt.gray, 0.5, Qt.DashLine)
        qp.setPen(pen)

        grid_step = 20  

        # Draw vertical lines
        x = 0
        while x < self.width():
            qp.drawLine(x, 0, x, self.height())
            x += grid_step

        # Draw horizontal lines
        y = 0
        while y < self.height():
            qp.drawLine(0, y, self.width(), y)
            y += grid_step