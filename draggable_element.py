from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDrag

class DraggableElement(QLabel):
    
    def __init__(self, element_type, image_path, element_id, *args, **kwargs):
        super(DraggableElement, self).__init__(*args, **kwargs)
        self.element_type = element_type
        self.setText(self.element_type)
        self.setFixedSize(112, 62)
        print(image_path)
        pixmap = QPixmap(image_path)
        self.setPixmap(pixmap)  
        self.setStyleSheet("border: 1px solid black; padding: 1px;")
        self.from_left_panel = True
        self.element_id = element_id
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        drag = QDrag(self)
        mimeData = QMimeData()
        mimeData.setText(self.element_type)

        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())
        drag.setPixmap(self.pixmap()) 
        
        dropAction = drag.exec_(Qt.MoveAction)
        
    