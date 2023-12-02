from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
width = 800
height = 600

window = QWidget()
window.resize(width, height)
window.setWindowTitle('Eas Editor')

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
m_layout = QHBoxLayout()

folder_btn = QPushButton('Папка')
img_list = QListWidget()

image_holder = QLabel('Photo')
left_btn = QPushButton('Повернути вліво')
right_btn = QPushButton('Повернути вправо')
mirror_btn = QPushButton('Віддзеркалити')
blur_btn = QPushButton('Розмити')
chb_btn = QPushButton('Ч / Б')

v1.addWidget(folder_btn)
v1.addWidget(img_list)

h1.addWidget(left_btn)
h1.addWidget(right_btn)
h1.addWidget(mirror_btn)
h1.addWidget(blur_btn)
h1.addWidget(chb_btn)

v2.addWidget(image_holder)
v2.addLayout(h1)

m_layout.addLayout(v1, stretch=1)
m_layout.addLayout(v2, stretch=2)

window.setLayout(m_layout)

window.show()
app.exec_()

