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
    QMessageBox
)

class MainWindows(QWidget):
        def __init__(self):
                super().__init__()
                layout = QVBoxLayout()
                label = QLabel("Кароче пофиг")
                label.setStyleSheet('font-size: 24px; margin-bottom: 15px')
                pofig = QLineEdit()
                pofig.setStyleSheet('font-size: 24px; ')                
                btn = QPushButton('Отправить')
                btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #323ed7;')
                layout.addWidget(label)
                layout.addWidget(btn)
                self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec())
