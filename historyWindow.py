import sqlite3
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
import sys
from PyQt5.QtCore import pyqtSignal

from historyUI import Ui_ManageWindow

class historyWindow(QMainWindow, Ui_ManageWindow):
    switch_to_start = pyqtSignal()
    switch_to_message = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)# Загружаем дизайн

        # Вызываем функцию для заполнения данными из базы данных
        self.populate_table()

        self.openHistoryMoment.clicked.connect(self.openHistoruMomentInMessageWindow)
        self.BackButton.clicked.connect(self.openStartWindow)

    def populate_table(self):
        # Подключаемся к базе данных SQLite
        connection = sqlite3.connect("database/messageDataBase.db")
        cursor = connection.cursor()

        # Выполняем запрос к базе данных
        cursor.execute("SELECT * FROM encryptionData")

        # Получаем результаты запроса
        data = cursor.fetchall()

        # Закрываем соединение с базой данных
        connection.close()

        # Устанавливаем количество строк и столбцов в QTableWidget
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))  # Предполагаем, что все строки имеют одинаковое количество столбцов

        # Заполняем QTableWidget данными из базы данных
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

    def openHistoruMomentInMessageWindow(self):
        selected_items = self.tableWidget.selectedItems()

        if not selected_items:
            print("Ничего не выбрано.")
            return

        selected_data = []

        for item in selected_items:
    
            value = item.text()
            selected_data.append(value)

        # Выводим результаты в консоль (вы можете сохранить их куда-то еще по вашему выбору)
        print("Выбранные элементы:")
        for data in selected_data:
            print(data)

        self.close()  # Закрываем текущее окно
        arguments = {'PlanTextLeft': selected_data[0], 'PlanTextRight': selected_data[1], 'PlanTextKey': selected_data[2], 'lang': selected_data[3], 'cipher': selected_data[4], 'decrypt': selected_data[5],}  # Ваши именованные аргументы
        self.emit_signal_with_arguments(self.switch_to_message, arguments)

    def emit_signal_with_arguments(self, signal, arguments):
        self.switch_to_message.emit(arguments)

    def openStartWindow(self):
        self.close()  # Закрываем текущее окно
        self.switch_to_start.emit()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = historyWindow()
    window.show()
    sys.exit(app.exec_())