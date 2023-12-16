from window_layout import *
from PIL import Image
from PIL import ImageFilter
from PyQt5.QtGui import QPixmap
import os

workdir = ''


class PhotoEditor:
    def __init__(self):
        self.filename = None
        self.directory = None

    def open(self, filename, directory):
        self.filename = filename
        self.directory = directory


def filterPhotos(name):
    extentions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    for ext in extentions:
        if ext in name:
            return True
        else:
            return False


def fillPhotoList():
    files = filter(filterPhotos, os.listdir(workdir))
    img_list.clear()
    img_list.addItems(files)


def chooseFolder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    image_holder.setText(workdir)
    fillPhotoList()


folder_btn.clicked.connect(chooseFolder)

app.exec_()
