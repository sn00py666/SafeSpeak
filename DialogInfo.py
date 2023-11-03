import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from ceaser_cipher_info import Ui_caesar_cipher_Info
from vigenere_cipher_Info import Ui_vigenere_cipher_Info

# Наследуемся от виджета из PyQt5.QtWidgets и от класса с интерфейсом
class Caesar_cipher_info_diolog(QDialog, Ui_caesar_cipher_Info):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
class Vigenere_cipher_info_diolog(QDialog, Ui_vigenere_cipher_Info):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_caesar_cipher_Info()
    ex.show()
    sys.exit(app.exec_())
