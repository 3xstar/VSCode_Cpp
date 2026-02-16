import sys
sys.path.append('c:/VSCODE/postgresql/task_manager/db')
from connection import get_connection
import pandas as pd
from sqlalchemy import text

class TaskRepository:
    def get_all(self):
        engine = get_connection()
        query = "SELECT * FROM app.tasks"
        df = pd.read_sql(query, engine)
        return df
    

    def add(self, title, description, status, priority):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("""INSERT INTO app.tasks (title, description, status, priority)
                              VALUES (:title, :description, :status, :priority)"""),
                         {"title": title, "description": description, "status": status, "priority": priority})
            conn.commit()
        print(f"Задача {title} добавлена\n")
        return self.get_all()


    def get_by_status(self, status):
        engine = get_connection()
        query = "SELECT * FROM app.tasks WHERE status = %s"
        df = pd.read_sql(query, engine, params=(status,))
        print(f"Задачи найденные по статусу - {status}:")
        return df
    

    def update_status(self, task_id, new_status):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("UPDATE app.tasks SET status = :new_status WHERE id = :task_id"),
                         {"new_status": new_status, "task_id": task_id})
            conn.commit()
        print(f"Статус задачи под id - {task_id} обновлен на: {new_status}\n")
        return self.get_all()

    #ФУНКЦИЯ ДЛЯ СБРОСА СЧЕТЧИКА ID ЕСЛИ СПИСОК ЗАДАЧ ПУСТ
    def reset_sequence(self):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(
                text("SELECT setval('app.tasks_id_seq', 1, false)")
            )
            conn.commit()
        print("Счётчик задач сброшен до 1 (таблица пуста)")

    def delete(self, task_id):
        engine = get_connection()
        with engine.connect() as conn:
            conn.execute(text("DELETE FROM app.tasks WHERE id = :task_id"),
                         {"task_id": task_id})
            conn.commit()
            print(f"Задача под id = {task_id} удалена\n")
        
        tasks_count = len(self.get_all())
        if tasks_count == 0:
            self.reset_sequence()

        return self.get_all()