import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Save Text to File")
        
        # Создаем PlainTextEdit для ввода текста
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setGeometry(10, 10, 280, 200)
        
        # Создаем кнопку для сохранения текста
        save_button = QPushButton("Save", self)
        save_button.setGeometry(10, 220, 80, 30)
        save_button.clicked.connect(self.save_text_to_file)
        
    def save_text_to_file(self):
        # Открываем диалоговое окно для выбора имени и пути сохранения файла
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            
            # Получаем текст из PlainTextEdit
            text = self.text_edit.toPlainText()
            
            # Сохраняем текст в файл
            with open(file_path, 'w') as file:
                file.write(text)
                
            print("File saved successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 300, 260)
    window.show()
    sys.exit(app.exec_())