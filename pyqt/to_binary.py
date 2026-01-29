import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class ConverterService(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Двоичный код') # Задаем заголовок окну
        self.resize(500, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel()
        self.label.setStyleSheet("""font-size: 20pt;
                                 color: cyan;""")

        self.entry = QLineEdit() # Создаем поле ввода
        self.label.setText("Введите число для перевода: ")

        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер
        self.button = QPushButton("ПЕРЕВЕСТИ") #Создаем кнопку
        self.button.clicked.connect(lambda: self.to_binary(self.entry.text())) #Создаем обработчик событий
        layout.addWidget(self.button)
        self.setLayout(layout) # Подружаем созданный контейнер

    def to_binary(self, number):
        try:
            number = self.entry.text() # Считываем текст с поля ввода и заносим его в переменную

            # Мини-проверка на то, что пользователь что-то ввел
            if int(number):
                binary_form = bin(int(number))
                self.label.setText(f"Ваше число в двоичном коде: {binary_form}")

        except ValueError:
            self.label.setText("Вы должны ввести число")


if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = ConverterService() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход
