import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog , QDialog

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os

from PyQt5.QtCore import pyqtSignal

from fileUI import Ui_MainWindow

class FilesWindow(QMainWindow, Ui_MainWindow):
    switch_to_start = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Загружаем дизайн

        self._cryptionMode = "Шифрование"
        self.fname = None
        self.EncriptionMode.clicked.connect(self.setEncryptionMode)
        self.DecriptionMode.clicked.connect(self.setDecryptionMode)

        self.DownloadFile.clicked.connect(self.downloadFile)
        self.EncriptionGO.clicked.connect(self.encriptionGO_en_de)
        
        self.SaveFile.clicked.connect(self.saveFile)

        self.plainTextEdit_Key.textChanged.connect(self.duplicateText)

        self.copyKey.clicked.connect(self.CopyButtons)
        self.copyKey_2.clicked.connect(self.CopyButtons)

        self.BackButton.clicked.connect(self.openStartWindow)
        
    def setEncryptionMode(self):
        self.EncriptionMode.setStyleSheet('background-color: rgba(72, 199, 166, 1); color: white; border-radius: 5px;')
        self.DecriptionMode.setStyleSheet('background-color: rgba(126, 126, 126, 1); color: white; border-radius: 5px;')
        self._cryptionMode = "Шифрование"
        self.EncriptionGO.setText("Шифровать")
        self.label_5.setText("Cохраните зашифрованный файл")
        self.label_saveKey.setVisible(True)
        self.KeyDublicate.setVisible(True)
        self.copyKey_2.setVisible(True)
        self.DownloadFile.setText("Выбрать файл...                                ")
        self.fname == None
        
    def setDecryptionMode(self):
        self.EncriptionMode.setStyleSheet('background-color: rgba(126, 126, 126, 1); color: white; border-radius: 5px;')
        self.DecriptionMode.setStyleSheet('background-color: rgba(72, 199, 166, 1); color: white; border-radius: 5px;')
        self._cryptionMode = "Расшифровка"
        self.EncriptionGO.setText("Расшифровать")
        self.label_5.setText("Cохраните расшифрованный файл")
        self.label_saveKey.setVisible(False)
        self.KeyDublicate.setVisible(False)
        self.copyKey_2.setVisible(False)
        self.DownloadFile.setText("Выбрать файл...                                ")
        self.fname == None

    def downloadFile(self):
        
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выберете файл')[0]
        
        self.DownloadFile.setText(self.fname.split("/")[-1])
            
    def encriptionGO_en_de(self):
        self.password = self.plainTextEdit_Key.toPlainText()
        
        if self._cryptionMode == "Шифрование" and self.fname != None:
            self.encrypt_file(self.fname, self.password)
        elif self._cryptionMode == "Расшифровка" and self.fname != None:
            self.decrypt_file(self.fname, self.password)

    def encrypt_file(self, file_path, password):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        iv = os.urandom(16)

        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, 'rb') as file:
            plaintext = file.read()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        self.plaintext = salt + iv + ciphertext
        if self.EncriptionGO.text()[-1] != "✅":
            self.EncriptionGO.setText(self.EncriptionGO.text() + "✅")
        # Запись зашифрованных данных в новый файл

    def decrypt_file(self, encrypted_file_path, password):
        with open(encrypted_file_path, 'rb') as file:
            # Считывание соли, вектора инициализации и зашифрованных данных
            salt = file.read(16)
            iv = file.read(16)
            ciphertext = file.read()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())

        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Дешифрование данных
        self.plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        if self.EncriptionGO.text()[-1] != "✅":
            self.EncriptionGO.setText(self.EncriptionGO.text() + "✅")
        
    def saveFile(self):
        output_file_path = QFileDialog.getSaveFileName(self, "Сохранить файл")[0]
        with open(output_file_path, 'wb') as decrypted_file:
             decrypted_file.write(self.plaintext)

    def duplicateText(self):
        text = self.plainTextEdit_Key.toPlainText()
        self.KeyDublicate.setPlainText(text)

    def CopyButtons(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plainTextEdit_Key.toPlainText())
        
    def openStartWindow(self):
        self.close()
        self.switch_to_start.emit()

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FilesWindow()
    ex.show()
    sys.exit(app.exec_())