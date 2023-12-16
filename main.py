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
        self.path = None
        self.photo = None
        self.editedDir = "Edited Photos"

    def showPhoto(self):
        pixmap = QPixmap(self.path)
        width, height = image_holder.width(), image_holder.height()
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        image_holder.setPixmap(pixmap)

    def savePhoto(self):
        path = os.path.join(self.directory, self.editedDir)
        if not os.path.exists(path) or os.path.isdir(path):
            os.makedirs(path, exist_ok=True)
        self.photo.save(os.path.join(path, self.filename))

    def open(self, filename, directory):
        self.filename = filename
        self.directory = directory

        self.path = os.path.join(self.directory, self.filename)
        try:
            self.photo = Image.open(self.path)
        except:
            QMessageBox.warning(window, "Error", "File not found =(")


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


def displayPhoto():
    filename = img_list.selectedItems()[0].text()
    photo.open(filename, workdir)
    photo.showPhoto()


photo = PhotoEditor()
folder_btn.clicked.connect(chooseFolder)
img_list.itemClicked.connect(displayPhoto)

app.exec_()
