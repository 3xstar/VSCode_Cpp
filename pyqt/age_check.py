import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class MainWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Проверка возраста') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel()
        self.label.setStyleSheet("""font-size: 24pt;
                                 color: cyan;""")

        self.entry = QLineEdit() # Создаем поле ввода
        self.entry.returnPressed.connect(self.say_hello) # Обрабатываем нажатие
        self.label.setText("Введите ваш возраст в поле")

        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер
        self.setLayout(layout) # Подружаем созданный контейнер

    def say_hello(self):
        try:
            name = self.entry.text() # Считываем текст с поля ввода и заносим его в переменную

            # Мини-проверка на то, что пользователь что-то ввел
            if int(name) < 18:
                self.label.setText("Вы несовершеннолетний")

            if int(name) >= 18:
                self.label.setText("Вы совершеннолетний")

        except ValueError:
            self.label.setText("Вы должны ввести число")


if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = MainWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход
