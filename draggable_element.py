from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap, QDrag

class DraggableElement(QLabel):
    
    def __init__(self, element_type, image_path, element_id, *args, **kwargs):
        super(DraggableElement, self).__init__(*args, **kwargs)
        self.element_type = element_type
        self.setText(self.element_type)
        self.setFixedSize(112, 62)
        self.original_pixmap = QPixmap(image_path)
        self.scale = 1.0
        self.original_width = 112
        self.original_height = 62
        self.setScaledPixmap()
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
        
    def setScaledPixmap(self):
        scaled_pixmap = self.original_pixmap.scaled(
            int(self.original_pixmap.width() * self.scale),
            int(self.original_pixmap.height() * self.scale),
            Qt.KeepAspectRatio
        )
        self.setPixmap(scaled_pixmap)

    def rescale(self, scale_factor):
        self.scale = scale_factor
        new_width = int(self.original_width * self.scale)
        new_height = int(self.original_height * self.scale)
        self.setFixedSize(new_width, new_height)
        self.setScaledPixmap()