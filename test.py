import os
from config import ELEMENT_IMAGES, init_config
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys


init_config(os.path.abspath(__file__))

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout()

label = QLabel("Image should appear below:")
layout.addWidget(label)

image_path = ELEMENT_IMAGES.get('Gate 1')
print("File exists:", os.path.exists(image_path))
pixmap = QPixmap(image_path)

if pixmap.isNull():
    print("Failed to load image!")
else:
    image_label = QLabel()
    image_label.setPixmap(pixmap)
    layout.addWidget(image_label)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
