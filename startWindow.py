import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal

from mainUI import Ui_ManageWindow

class StartWindow(QMainWindow, Ui_ManageWindow):
    switch_to_message = pyqtSignal()
    switch_to_files = pyqtSignal() 
    switch_to_history = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)# Загружаем дизайн
        
        # Подключаем сигнал нажатия кнопки к методу OpenMessageWindow
        self.OpenMessageEncription.clicked.connect(self.openMessageWindow)
        self.OpenFilesEncription.clicked.connect(self.openFilesWindow)
        self.OpenHistoryEncription.clicked.connect(self.openHistoryWindow)
    
    def openMessageWindow(self):
        self.close()
        self.switch_to_message.emit()
    
    def openFilesWindow(self):
        self.close()
        self.switch_to_files.emit()
    
    def openHistoryWindow(self):
        self.close()
        self.switch_to_history.emit()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())

    