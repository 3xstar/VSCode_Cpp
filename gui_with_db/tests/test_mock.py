import pytest
from unittest.mock import patch, MagicMock
import sys
sys.path.append('c:/VSCODE/gui_with_db')
from services.recipe_service import RecipeService

class TestRecipeGetAll:

    def test_get_all_return_list(self, mock_conn, mock_cursor):
        # Настраиваем поведение mock-объекта
        mock_cursor.fetchall.return_value = [
            (1, "Том Ям", "Суп", "medium", "Основное блюдо"),
            (2, "Пельмени", "Мучное", "enum", "Основное блюдо")
        ]

        # Выполнение тестируемого кода
        with patch('db.db.get_conn', return_value=mock_conn):
            result = RecipeService.get_all()

        # Проверка результата
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0][1] == "Том Ям"

    def test_get_all_calls_corret_query(self, mock_conn, mock_cursor):
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.get_all()

        # Проверка что execute был вызван
        mock_cursor.execute.assert_called_once()

        # Проверка содержимого запроса
        call_args = mock_cursor.execute.call_args[0][0]
        assert 'SELECT' in call_args.upper()
        assert 'recipes.recipes' in call_args

    def test_get_all_handles_db_error(self, mock_conn, mock_cursor):
        # Имитация ошибки
        mock_cursor.execute.side_effect = Exception('DB Error')
        
        with patch('db.db.get_conn', return_value=mock_conn):
            with pytest.raises(Exception):
                RecipeService.get_all()
            
            # Проверяем rollback если он есть
            if hasattr(mock_conn, 'rollback'):
                mock_conn.rollback.assert_called_once()

    # Тест на закрытие соединения
    def test_get_all_closes_resources(self, mock_conn, mock_cursor):
        mock_cursor.fetchall.return_value = []  # Исправлено на return_value
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.get_all()
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


class TestRecipeAddRecipe:
    
    def test_add_recipe_success(self, mock_conn, mock_cursor):
        # Настраиваем поведение mock-объекта
        mock_cursor.lastrowid = 1
        
        # Выполнение тестируемого кода
        with patch('db.db.get_conn', return_value=mock_conn):
            result = RecipeService.add_recipe('Том Ям', 1, 'medium')
        
        # Проверка результата
        assert result == 1
        mock_conn.commit.assert_called_once()
    
    def test_add_recipe_calls_correct_query(self, mock_conn, mock_cursor):
        test_data = {
            'title': 'Пельмени',
            'category_id': 2,
            'difficulty': 'easy'
        }
        
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.add_recipe(test_data['title'], test_data['category_id'], test_data['difficulty'])
        
        # Проверка что execute был вызван
        mock_cursor.execute.assert_called_once()
        
        # Проверка содержимого запроса
        call_args = mock_cursor.execute.call_args[0][0]
        call_params = mock_cursor.execute.call_args[0][1]
        
        assert 'INSERT' in call_args.upper()
        assert 'recipes.recipes' in call_args
        assert call_params == (test_data['title'], test_data['category_id'], test_data['difficulty'])
    
    def test_add_recipe_rollback_on_error(self, mock_conn, mock_cursor):
        # Имитация ошибки при выполнении запроса
        mock_cursor.execute.side_effect = Exception('DB Error')
        
        with patch('db.db.get_conn', return_value=mock_conn):
            with pytest.raises(Exception):
                RecipeService.add_recipe('Рецепт', 1, 'easy')
            
            # Проверяем rollback
            mock_conn.rollback.assert_called_once()
    
    def test_add_recipe_closes_resources(self, mock_conn, mock_cursor):
        mock_cursor.lastrowid = 1
        
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.add_recipe('Рецепт', 1, 'easy')
        
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()
    
    def test_add_recipe_invalid_data(self, mock_conn, mock_cursor):
        # Тест на передачу некорректных данных
        with patch('db.db.get_conn', return_value=mock_conn):
            with pytest.raises(Exception):
                RecipeService.add_recipe('', None, 'invalid')


class TestRecipeGetById:
    
    def test_get_by_id_return_recipe(self, mock_conn, mock_cursor):
        # Настраиваем поведение mock-объекта
        mock_cursor.fetchone.return_value = (1, "Том Ям", "Суп", "medium", "Основное блюдо")
        
        # Выполнение тестируемого кода
        with patch('db.db.get_conn', return_value=mock_conn):
            result = RecipeService.get_by_id(1)
        
        # Проверка результата
        assert result is not None
        assert result[0] == 1
        assert result[1] == "Том Ям"
        assert result[3] == "medium"
    
    def test_get_by_id_return_none_for_invalid_id(self, mock_conn, mock_cursor):
        # Настраиваем поведение - ничего не найдено
        mock_cursor.fetchone.return_value = None
        
        with patch('db.db.get_conn', return_value=mock_conn):
            result = RecipeService.get_by_id(999)
        
        assert result is None
    
    def test_get_by_id_calls_correct_query(self, mock_conn, mock_cursor):
        recipe_id = 5
        
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.get_by_id(recipe_id)
        
        # Проверка что execute был вызван
        mock_cursor.execute.assert_called_once()
        
        # Проверка содержимого запроса
        call_args = mock_cursor.execute.call_args[0][0]
        call_params = mock_cursor.execute.call_args[0][1]
        
        assert 'SELECT' in call_args.upper()
        assert 'recipes.recipes' in call_args
        assert 'WHERE' in call_args.upper()
        assert call_params[0] == recipe_id
    
    def test_get_by_id_handles_db_error(self, mock_conn, mock_cursor):
        # Имитация ошибки базы данных
        mock_cursor.execute.side_effect = Exception('DB Error')
        
        with patch('db.db.get_conn', return_value=mock_conn):
            with pytest.raises(Exception):
                RecipeService.get_by_id(1)
    
    def test_get_by_id_closes_resources(self, mock_conn, mock_cursor):
        mock_cursor.fetchone.return_value = (1, "Рецепт", 1, "easy")
        
        with patch('db.db.get_conn', return_value=mock_conn):
            RecipeService.get_by_id(1)
        
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()
    
    def test_get_by_id_validates_id_type(self, mock_conn, mock_cursor):
        # Проверка работы с разными типами ID
        test_ids = [1, "1"]
        
        for recipe_id in test_ids:
            mock_cursor.reset_mock()
            mock_cursor.fetchone.return_value = (int(str(recipe_id)), "Рецепт", 1, "easy")
            
            with patch('db.db.get_conn', return_value=mock_conn):
                result = RecipeService.get_by_id(recipe_id)
            
            assert result is not None
            assert result[0] == int(str(recipe_id))