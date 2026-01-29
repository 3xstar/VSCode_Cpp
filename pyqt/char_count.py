import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout


#Создаем окно
class MainWindow(QWidget):
    #Базовая настройка окна
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Подсчет') #Задаем заголовок окну
        self.resize(300,200) #Выставляем размеры
        self.setup_ui() #Загружаем интерфейс

    def setup_ui(self):
        layout = QVBoxLayout() #Создаем контейнер
        self.label = QLabel("Тут будет количество символов") #Создаем текстовую метку
        self.label.setStyleSheet("""font-size: 17pt;
                                 color: cyan;""")
        layout.addWidget(self.label) #Добавляем текстовую метку на созданный контейнер

        self.entry = QLineEdit() #Создаем поле ввода
        self.entry.textChanged.connect(self.on_text_changed) #Обрабатываем изменение текста
        layout.addWidget(self.entry) #Добавляем поле ввода на контейнер

        self.setLayout(layout) #Подгружаем созданный контейнер

    def on_text_changed(self, text):
        self.label.setStyleSheet("""font-size: 17pt;
                                 color: cyan;""")
        self.label.setText(f"Количество символов: {len(text)}")

    #Создаем слот(метод, который обрабатывает действия при нажатии на кнопку)
    def say_hello(self):
        name = self.entry.text() #Заносим в переменную значение, введенное в LiteEdit
        self.label.setText(f'Привет, {name}') #Выводим результат в консоль

if __name__ == "__main__":
    app = QApplication(sys.argv) #Создаем приложение и цикл событий
    window = MainWindow() #Создаем окно на базе созданного класса
    window.show() #Открываем/показываем окно
    sys.exit(app.exec()) #Корректный выход