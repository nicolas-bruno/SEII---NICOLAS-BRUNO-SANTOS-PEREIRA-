#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLabel, QShortcut, QFileDialog, QMessageBox, QMenuBar
from PyQt5.QtGui import QKeySequence
from PyQt5 import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.file_path = None
        

        self.open_new_file_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.open_new_file_shortcut.activated.connect(self.open_new_file)

        self.save_current_file_shortcut = QShortcut(QKeySequence('Ctrl+S'), self)
        self.save_current_file_shortcut.activated.connect(self.save_current_file)

        vbox = QVBoxLayout()
        text = "New Archive"
        self.title = QLabel(text)
        self.title.setWordWrap(True)
        self.title.setAlignment(Qt.Qt.AlignCenter)
        vbox.addWidget(self.title)
        self.setLayout(vbox)
        
     

        self.scrollable_text_area = QTextEdit()
        vbox.addWidget(self.scrollable_text_area)
        
    

    def open_new_file(self):
        self.file_path, filter_type = QFileDialog.getOpenFileName(self, "Abrir novo arquivo", 
                                                                  "", "Todos os arquivos (*)")
        if self.file_path:
            with open(self.file_path, "r") as f:
                file_contents = f.read()
                self.title.setText(self.file_path)
                self.scrollable_text_area.setText(file_contents)
        else:
            self.invalid_path_alert_message()

    def save_current_file(self):
        if not self.file_path:
            new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Salvar arquivo em...", 
                                                                     "", "Todos os arquivos (*)")
            if new_file_path:
                self.file_path = new_file_path
            else:
                self.invalid_path_alert_message()
                return False
        file_contents = self.scrollable_text_area.toPlainText()
        with open(self.file_path, "w") as f:
            f.write(file_contents)
        self.title.setText(self.file_path)

    def closeEvent(self, event):
        messageBox = QMessageBox()
        title = "Fechar Aplicação?"
        message = "Salvar antes de sair?"
       
        reply = messageBox.question(self, title, message, messageBox.Yes | messageBox.No |
                messageBox.Cancel, messageBox.Cancel)
        if reply == messageBox.Yes:
            return_value = self.save_current_file()
            if return_value == False:
                event.ignore()
        elif reply == messageBox.No:
            event.accept()
        else:
            event.ignore()

    def invalid_path_alert_message(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Invalid file")
        messageBox.setText("Arquivo invalido ")
        messageBox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.showMaximized()
    sys.exit(app.exec_())