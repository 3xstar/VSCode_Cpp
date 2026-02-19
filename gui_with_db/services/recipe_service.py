# Работа с таблицей "recipes"
import db.db as db

class RecipeService:
    @staticmethod
    def get_all():
        conn = db.get_conn()
        cursor = conn.cursor()
        try:
            cursor.execute('''
            select r.id, r.name, r.description, r.level, c.name from 
            recipes.recipes r join recipes.category c on r.category_id = 
            c.id;''')
            result = cursor.fetchall()
            cursor.close()
            conn.close()
        except:
            print("Ошибка")
        return result

    @staticmethod
    def get_by_id(recipe_id):
        try:
            conn = db.get_conn()
            cursor = conn.cursor()
            cursor.execute('''
            select r.id, r.name, r.description, r.level, c.name from 
            recipes.recipes r join recipes.category c on r.category_id = c.
            id WHERE id = %s;
            ''', (recipe_id, ))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
        except:
            print("Ошибка в запросе")
        return result

    def add_recipe(name, category_id, level, description=None):
        try:
                conn = db.get_conn()
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO recipes.resipes (name, description, level, 
                category_id) VALUES(%s, %s, %s, %s) RETURNING id
                ''', (name, description, level, category_id))
                result = cursor.fetchall()[0]
                cursor.close()
                conn.close()
        except:
            conn.rollback()
            print("Ошибка в запросе")
        return result
