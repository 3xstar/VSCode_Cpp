import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QPushButton,
    QMessageBox,
    QInputDialog,
    QFileDialog
)

class MainWindows(QWidget):
        def __init__(self):
                super().__init__()
                layout = QVBoxLayout()
                hlayout = QHBoxLayout()
                label = QLabel("Кароче пофиг")
                label.setStyleSheet('font-size: 24px; margin-bottom: 15px')
                self.pofig = QLineEdit()
                self.pofig.setStyleSheet('font-size: 24px; ')                
                self.btn = QPushButton('Отправить')
                self.btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #323ed7; color: white; border-radius: 15 px;')
                self.rename_btn = QPushButton('Переименовать')
                self.rename_btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #323ed7; color: white; border-radius: 15 px;')
                self.btn.clicked.connect(self.btn_click)
                self.rename_btn.clicked.connect(self.new_name)
                self.file_btn = QPushButton('Загрузить файл')
                self.file_btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #323ed7; color: white; border-radius: 15 px;')
                self.file_btn.clicked.connect(self.load_file)
                layout.addWidget(label)
                layout.addWidget(self.pofig)
                hlayout.addWidget(self.btn)
                hlayout.addWidget(self.rename_btn)
                hlayout.addWidget(self.file_btn)
                layout.addLayout(hlayout)
                self.setLayout(layout)

        def btn_click(self):
                if self.pofig != "":
                      QMessageBox.information(self, "Готово", f'Вы ввели: {self.pofig.text()}')
                else:
                       QMessageBox.warning(self, "Ошибка", "Вы ничего не поняли")

                if self.pofig != "":
                        reply = QMessageBox.information(self, "Подтверждение имени",
                        "Утвердить имя?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                        if reply == QMessageBox.StandardButton.Yes:
                               print("Удалено")
                                         
                else:
                       QMessageBox.warning(self, "Ошибка", "Вы ничего не поняли")

        def new_name(self):
            text, ok = QInputDialog.getText(
                    self, "Новое имя", "Введите название: "
            )
            if ok and text:
                print(text, " ", ok)

        def load_file(self):
              file_path, _ = QFileDialog.getOpenFileName(
                    self,
                    "Открыть файл",
                    "",
                    "Все файлы (*.*)" 
              )
              with open(file_path, "r", encoding = 'UTF-8') as file: 
                        print(file.readlines())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec())
