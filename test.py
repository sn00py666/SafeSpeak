import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QPushButton

SCREEN_SIZE = [400, 400]


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
       
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(100, 50)
        self.btn.move(10, 10)
        self.btn.clicked.connect(self.Setimg)

        ## Изображение
        self.pixmap = QPixmap("pass.png")
        # Если картинки нет, то QPixmap будет пустым, 
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        # Отображаем содержимое QPixmap в объекте QLabel
        # self.image.setPixmap(self.pixmap)
    
    def Setimg(self):
        pass
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.pixmap = QPixmap(fname)
        self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())