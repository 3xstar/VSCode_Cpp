# Работа с таблицей "recipes"
import db.db as db

class CategoryService:

    @staticmethod
    def get_all(name, category_id, level, description=None):
        try:
                conn = db.get_conn()
                cursor = conn.cursor()
                cursor.execute('''
                select id, name from recipes.category order by name;
                ''', (name, description, level, category_id))
                result = cursor.fetchall()[0]
                cursor.close()
                conn.close()
        except:
            conn.rollback()
            print("Ошибка в запросе")
        return result
    
    @staticmethod
    def add(name):
        try:
                conn = db.get_conn()
                cursor = conn.cursor()
                cursor.execute('''
                insert into recipes.categories (name) values(%s) returning id;
                ''', (name,))
                result = cursor.fetchall()[0]
                conn.commit()
                cursor.close()
                conn.close()
        except:
            print("Ошибка в запросе")
        return result

    @staticmethod
    def get_by_id(category_id):
        try:
                conn = db.get_conn()
                cursor = conn.cursor()
                cursor.execute('''
                select id, name from recipes.categories where id = %s;
                ''', (category_id,))
                result = cursor.fetchall()[0]
                cursor.close()
                conn.close()
        except:
            print("Ошибка в запросе")
        return result