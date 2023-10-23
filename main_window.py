from config import ELEMENT_IMAGES
from draggable_element import DraggableElement
from PyQt5.QtWidgets import QMainWindow, QAction, QToolBar, QVBoxLayout, QWidget, QFrame, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, drop_area, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.triggered.connect(self.zoom_in)

        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.triggered.connect(self.zoom_out)
        
        toolbar = QToolBar("Zoom Toolbar")
        self.addToolBar(toolbar)
        
        toolbar.addAction(zoom_in_action)
        toolbar.addAction(zoom_out_action)

        self.drop_area = drop_area
        
        left_pane = QFrame()
        left_pane.setFrameShape(QFrame.StyledPanel)
        left_pane.setFixedWidth(300)
        left_layout = QVBoxLayout()
        
        gate1 = DraggableElement('Gate 1', ELEMENT_IMAGES.get('Gate 1'), element_id=-1)
        gate2 = DraggableElement('Gate 2', ELEMENT_IMAGES.get('Gate 2'), element_id=-1)
        input_element = DraggableElement('Input', ELEMENT_IMAGES.get('Input'), element_id=-1)
        
        left_layout.addWidget(gate1)
        left_layout.addWidget(gate2)
        left_layout.addWidget(input_element)
        left_pane.setLayout(left_layout)
        
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_pane)
        main_layout.addWidget(self.drop_area)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
    def zoom_in(self):
        self.drop_area.rescale_elements_and_grid(1.1)

    def zoom_out(self):
        self.drop_area.rescale_elements_and_grid(0.9)


