import sys
import os
sys.path.append('c:/VSCODE/postgresql/dao')
from ui.db import get_conn
from sqlalchemy import text  # Добавляем импорт text

class RecipeService:
    # Получение всех рецептов
    def get_all(self):
        engine = get_conn()  # Получаем Engine
        with engine.connect() as conn:  # Создаем соединение
            result = conn.execute(text('SELECT * FROM recipes.recipes'))
            rows = result.fetchall()
        return rows
    
    # Добавление нового рецепта
    def add(self, name, category, level, description):
        engine = get_conn()
        with engine.connect() as conn:
            try:
                # Получаем category_id
                result = conn.execute(
                    text('SELECT category_id FROM categories WHERE id = :category'),
                    {'category': category}
                )
                category_id = result.fetchone()[0]
                
                # Вставляем рецепт
                conn.execute(
                    text('''
                        INSERT INTO recipes.recipes (name, category_id, level, description) 
                        VALUES (:name, :category_id, :level, :description)
                    '''),
                    {'name': name, 'category_id': category_id, 'level': level, 'description': description}
                )
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"Ошибка: {e}")
                raise
    
    # Редактирование рецепта по id
    def edit(self, id, name, category, level, description):
        engine = get_conn()
        with engine.connect() as conn:
            try:
                result = conn.execute(
                    text('SELECT category_id FROM categories WHERE id = :category'),
                    {'category': category}
                )
                category_id = result.fetchone()[0]
                
                conn.execute(
                    text('''
                        UPDATE recipes.recipes 
                        SET name = :name, category_id = :category_id, level = :level, description = :description 
                        WHERE id = :id
                    '''),
                    {'name': name, 'category_id': category_id, 'level': level, 
                     'description': description, 'id': id}
                )
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"Ошибка: {e}")
                raise

    # Удаление рецепта
    def drop(self, id):
        engine = get_conn()
        with engine.connect() as conn:
            try:
                conn.execute(
                    text('DELETE FROM recipes.recipes WHERE id = :id'),
                    {'id': id}
                )
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"Ошибка: {e}")
                raise

    # Получение рецепта по категории
    def get_by_category(self, category):
        engine = get_conn()
        with engine.connect() as conn:
            result = conn.execute(
                text('''
                    SELECT * FROM recipes.recipes 
                    WHERE category_id = (SELECT category_id FROM categories WHERE name = :category)
                '''),
                {'category': category}
            )
            rows = result.fetchall()
            return rows