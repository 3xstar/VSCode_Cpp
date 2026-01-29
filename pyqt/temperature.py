import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# Создаем окно
class MainWindow(QWidget):
    # Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Перевод градусов') # Задаем заголовок окну
        self.resize(400, 300) # Выставляем размеры
        self.setup_ui() # Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() # Создаем контейнер
        self.label = QLabel()
        self.label.setStyleSheet("""font-size: 17pt;
                                 color: cyan;""")

        self.entry = QLineEdit() # Создаем поле ввода
        self.label.setText("Введите градусы Цельсия снизу в поле")

        layout.addWidget(self.label) # Добавляем текстовую метку, на созданный контейнер
        layout.addWidget(self.entry) # Добавляем поле ввода на контейнер
        self.button = QPushButton("ПЕРЕВЕСТИ") #Создаем кнопку
        self.button.clicked.connect(self.transform) #Создаем обработчик событий
        layout.addWidget(self.button)
        self.setLayout(layout) # Подружаем созданный контейнер

    def transform(self):
        try:
            celsiya = self.entry.text() # Считываем текст с поля ввода и заносим его в переменную

            # Мини-проверка на то, что пользователь что-то ввел
            if int(celsiya):
                farengeita = (int(celsiya) * 1.8) + 32
                self.label.setText(f"Количество градусов Фаренгеита: {farengeita}")

        except ValueError:
            self.label.setText("Вы должны ввести число")


if __name__ == "__main__":
    app = QApplication(sys.argv) # Создаем приложение и цикл событий 
    window = MainWindow() # Создаем окно на базе созданного класса
    window.show() # Открываем/показывае окно
    sys.exit(app.exec()) # Корректный выход
