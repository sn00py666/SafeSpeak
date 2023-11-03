import sys

from functools import partial
import win32clipboard #pip install pywin32

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog , QDialog
from DialogInfo import Caesar_cipher_info_diolog, Vigenere_cipher_info_diolog

class MyWidget(QMainWindow):
    def __init__(self, PlanTextLeft="", PlanTextRight="", PlanTextKey="", lang="ML", cipher="Шифр Цезаря", decrypt="Зашифровать"):
        super().__init__()
        uic.loadUi('message.ui', self)  # Загружаем дизайн

        self.Encription.clicked.connect(self.run)
        self.change.clicked.connect(self.changeCryptoMode)
        self.DownloadTxt.clicked.connect(self.DownloadText)

        self.copyLeftPlainText.clicked.connect(self.copyTextLeftPlanText)
        self.copyRightPlainText.clicked.connect(self.copyTextRightPlanText)
        self.copyKey.clicked.connect(self.copyTextKey)

        self.SaveMenu.clicked.connect(self.Visible_unvisble_Buttons)
        self.SaveRight.setVisible(False)
        self.SaveRightWichKey.setVisible(False)
        self.SaveRight.setEnabled(False)
        self.SaveRightWichKey.setEnabled(False)

        self.SaveRight.clicked.connect(self.save_text_to_file)
        self.SaveRightWichKey.clicked.connect(self.save_text_to_file_wichKey)

        self.InfoButton.clicked.connect(self.OpenInfo)
        

        # Наполнение инфой окно в начале
        self.plainTextEdit_Left.appendPlainText(PlanTextLeft)
        self.plainTextEdit_Left.appendPlainText(PlanTextRight)
        self.plainTextEdit_Left.appendPlainText(PlanTextKey)
        self.language.setCurrentIndex(self.language.findText(lang))
        self.Encription.setText(decrypt)
        self.code.setCurrentIndex(self.code.findText(cipher))


    def run(self):
        self.plainTextEdit_Right.clear()
        if self.code.currentText() == "Шифр Цезаря":
            if self.label_3.text() == "Сообщение:":
                self.plainTextEdit_Right.appendPlainText(self.caesar_cipher(self.plainTextEdit_Left.toPlainText(), self.plainTextEdit_Key.toPlainText(), self.language.currentText(), decrypt=False))
            else:
                self.plainTextEdit_Right.appendPlainText(self.caesar_cipher(self.plainTextEdit_Left.toPlainText(), self.plainTextEdit_Key.toPlainText(), self.language.currentText(), decrypt=True))   
        else:
            if self.label_3.text() == "Сообщение:":
                self.plainTextEdit_Right.appendPlainText(self.vigenere_cipher(self.plainTextEdit_Left.toPlainText(), self.plainTextEdit_Key.toPlainText(), self.language.currentText(), decrypt=False))
            else:
                self.plainTextEdit_Right.appendPlainText(self.vigenere_cipher(self.plainTextEdit_Left.toPlainText(), self.plainTextEdit_Key.toPlainText(), self.language.currentText(), decrypt=True))
        
        # Имя элемента совпадает с objectName в QTDesigner

    # Функция для шифрования с помощью шифра Цезаря    
    def caesar_cipher(self, message, key, language, decrypt=False):
        # если ничего не ввели в качестве ключа
        if key:
            key = int(key)
        else:
            key = 0

        alphabet = ""
        if language == "RU":
            alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        elif language == "ML":
            alphabet = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя"
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        encrypted_message = ""
        for char in message:
            if char.lower() in alphabet:
                index = alphabet.index(char.lower())
                if decrypt:
                    # Если decrypt=True, выполняется расшифровка
                    encrypted_index = (index - key) % len(alphabet)
                    if char.isupper():
                        encrypted_message += alphabet[encrypted_index].upper()
                    else:
                        encrypted_message += alphabet[encrypted_index]
                else:
                    # Если decrypt=False (по умолчанию), выполняется шифрование
                    encrypted_index = (index + key) % len(alphabet)
                    if char.isupper():
                        encrypted_message += alphabet[encrypted_index].upper()
                    else:
                        encrypted_message += alphabet[encrypted_index]
            else:
                # Если символ не находится в алфавите, оставляем его без изменений
                encrypted_message += char
        
        return encrypted_message
    
    # Функция для шифрования с помощью шифра Виженера
    def vigenere_cipher(self, message, key, language, decrypt=False):
        # Определение алфавита на основе указанного языка
        if language == "RU":
            alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        elif language == "ML":
            alphabet = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя"
        else:
            alphabet = "abcdefghijklmnopqrstuvwxyz"

        key = key.lower()
        key_length = len(key)
        result_message = ""

        for i, char in enumerate(message):
            if char.lower() in alphabet:
                index = alphabet.index(char.lower())
                key_char = key[i % key_length]
                key_index = alphabet.index(key_char)
                if decrypt:
                    # Если decrypt=True, выполняется расшифровка
                    decrypted_index = (index - key_index) % len(alphabet)
                    if char.isupper():
                        result_message += alphabet[decrypted_index].upper()
                    else:
                        result_message += alphabet[decrypted_index]
                else:
                    # Если decrypt=False (по умолчанию), выполняется шифрование
                    encrypted_index = (index + key_index) % len(alphabet)
                    if char.isupper():
                        result_message += alphabet[encrypted_index].upper()
                    else:
                        result_message += alphabet[encrypted_index]
            else:
                # Если символ не находится в алфавите, оставляем его без изменений
                result_message += char

        return result_message
    
    def changeCryptoMode(self):
        txt1 = self.label_3.text()
        txt2 = self.label_4.text()
        self.label_3.setText(txt2)
        self.label_4.setText(txt1)

        if self.Encription.text() == "Зашифровать":
            self.Encription.setText("Расшифровать")
        else:
            self.Encription.setText("Зашифровать")

    def DownloadText(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выберете файл txt', '',
            'Документ (*.txt)')[0]
        with open(fname, encoding='utf-8') as f:
            content = f.read()
        self.plainTextEdit_Left.clear()
        self.plainTextEdit_Left.appendPlainText(content)
            
    def send_to_clipboard(data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

    def copyTextLeftPlanText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plainTextEdit_Left.toPlainText())

    def copyTextKey(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plainTextEdit_Key.toPlainText())
    
    def copyTextRightPlanText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plainTextEdit_Right.toPlainText())
    
    def save_text_to_file(self):
        # Открываем диалоговое окно для выбора имени и пути сохранения файла
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            
            # Получаем текст из PlainTextEdit
            text = self.plainTextEdit_Right.toPlainText()
            
            # Сохраняем текст в файл
            with open(file_path, 'w') as file:
                file.write(text)
                
            print("File saved successfully!")

    def save_text_to_file_wichKey(self):
        # Открываем диалоговое окно для выбора имени и пути сохранения файла
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            
            # Получаем текст из PlainTextEdit
            text = self.plainTextEdit_Right.toPlainText()
            key = self.plainTextEdit_Key.toPlainText()
            
            # Сохраняем текст в файл
            with open(file_path, 'w') as file:
                file.write(text)
                file.write(f"\n\nКлюч для расшифровки: {key}")
                
            # print("File saved successfully!")

    def Visible_unvisble_Buttons(self):
        if self.SaveRight.isEnabled():
            self.SaveRight.setVisible(False)
            self.SaveRightWichKey.setVisible(False)
            self.SaveRight.setEnabled(False)
            self.SaveRightWichKey.setEnabled(False)
        else:
            self.SaveRight.setVisible(True)
            self.SaveRightWichKey.setVisible(True)
            self.SaveRight.setEnabled(True)
            self.SaveRightWichKey.setEnabled(True)

    def OpenInfo(self):
        if self.code.currentText() == "Шифр Цезаря":
            Ui_caesar_cipher_Info_inst = Caesar_cipher_info_diolog()
            Ui_caesar_cipher_Info_inst.show()
            Ui_caesar_cipher_Info_inst.exec()
        else:
            Ui_caesar_cipher_Info_inst = Vigenere_cipher_info_diolog()
            Ui_caesar_cipher_Info_inst.show()
            Ui_caesar_cipher_Info_inst.exec()


    # send_to_clipboard(win32clipboard.CF_DIB, data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())