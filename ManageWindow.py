import sys
import os
from PyQt5.QtWidgets import QApplication
from startWindow import StartWindow
from MessageWindow import MessageWindow
from FilesWindow import FilesWindow
from historyWindow import historyWindow

# os.system("pip install -r requirements.txt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    start_window = StartWindow()
    message_window = MessageWindow()
    files_window = FilesWindow()
    history_window = historyWindow()

    start_window.switch_to_message.connect(message_window.show)
    start_window.switch_to_files.connect(files_window.show)
    start_window.switch_to_history.connect(history_window.show)

    message_window.switch_to_start.connect(start_window.show)
    files_window.switch_to_start.connect(start_window.show)
    history_window.switch_to_start.connect(start_window.show)

    history_window.switch_to_message.connect(message_window.show_with_arguments)

    

    start_window.show()
    
    sys.exit(app.exec_())
